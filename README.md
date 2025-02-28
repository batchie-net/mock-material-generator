# Mock data generator
An internal agent we are using within Batchie.net for generating random mock data for our AI training.

What does it contain?

- Agent that decides on action taken
- Randomized pick method for purchase and consumption
- Delivery of data to InfluxDB
- State management with a transient JSON file to track state between sessions.

## InfluxDB
You can also find a setup for a InfluxDB DEV instance in this repo.

You need to set up environment variables as mentioned in the official documentation.

Link: https://docs.influxdata.com/influxdb/v2/install/use-docker-compose/

## Installation
Right now this is prepared to run within a VENV. You can always initiailize a virtual environment
and run the requirements.txt to get all dependencies.

Soon, a Dockerfile and a Docker Compose-file will be added to the project.

## Coming features
We might flesh this out with a bit more internal processes regarding picking of material based on orders
instead of materials directly. We are also preparing to implement a function for picking-bias.