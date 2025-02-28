from materials import Material
from random import choice, randint, randrange
from datetime import datetime

import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

TOKEN = os.environ.get("INFLUXDB_TOKEN")
INFLUX_HOST = os.environ.get("INFLUX_HOST", "localhost")
INFLUX_PORT = os.environ.get("INFLUX_PORT", 8086)
ORG = "docs"
URL = f"http://{INFLUX_HOST}:{INFLUX_PORT}"

client = influxdb_client.InfluxDBClient(url=URL, token=TOKEN, org=ORG)
bucket = "dev-material-transactions"
write_api = client.write_api(write_options=SYNCHRONOUS)


class Agent:

    def consume(self, material: Material):
        amount = randrange(50, 30_000)
        if material.total_quantity > amount:
            material.total_quantity -= amount
        return amount

    def produce(self, material: Material):
        amount = randrange(500, 15_000)
        material.total_quantity += amount
        return amount

    def decide(self, articles):
        selected_material = choice(articles)
        action = randint(0, 1)

        if action == 1:
            amount_produced = self.produce(selected_material)
            print(datetime.now(), "Producing:", selected_material.article_number, amount_produced,
                  selected_material.total_quantity)
            p = influxdb_client.Point("Transactions") \
                .time(datetime.utcnow()) \
                .tag("action", "producing") \
                .tag("article_number", selected_material.article_number) \
                .field("amount", amount_produced) \
                .field("total_quantity", selected_material.total_quantity)
            write_api.write(bucket=bucket, org=ORG, record=p)

        if action == 0:

            previous_amount = selected_material.total_quantity
            amount_consumed = self.consume(selected_material)

            if previous_amount > amount_consumed:
                print(datetime.now(), "Consuming:", selected_material.article_number, amount_consumed,
                      selected_material.total_quantity)
                p = influxdb_client.Point("Transactions") \
                    .time(datetime.utcnow()) \
                    .tag("action", "consuming") \
                    .tag("article_number", selected_material.article_number) \
                    .field("amount", amount_consumed) \
                    .field("total_quantity", selected_material.total_quantity)
                write_api.write(bucket=bucket, org=org, record=p)