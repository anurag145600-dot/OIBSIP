import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

CONFIG_PATH = os.path.join(
    BASE_DIR,
    "config",
    "commands.json"
)

with open(CONFIG_PATH, "r") as file:
    CONFIG = json.load(file)