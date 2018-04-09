import requests
from configparser import ConfigParser
import pprint

config = ConfigParser()
config.read("config.ini")

pprint.pprint("No tests fount")