import requests
from configparser import ConfigParser
from pprint import pprint

config = ConfigParser()
config.read("config.ini")

pprint("No tests fount")