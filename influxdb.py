import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


class Influx:

    token = os.environ.get("INFLUXDB_TOKEN")
    org = "docs"
    url = "http://localhost:8086"

    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org, )
    bucket = "dev-material-transactions"
    write_api = client.write_api(write_options=SYNCHRONOUS)

