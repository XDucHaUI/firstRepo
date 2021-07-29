from phonenumbers import phonenumber, geocoder
from urllib import response
from urllib.request import urlopen
import json
import numpy as np
import cv2 as cv

from phonenumbers import data
import phonenumbers

phonenumbers00=phonenumbers.parse("+84989630379");
print(geocoder.description_for_number(phonenumbers00,'en'))

url='http://ipinfo.io/'
response=urlopen(url)

data = json.load(response)
print(data)