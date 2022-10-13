from os import stat
from urllib import response
import requests
import json

line = str(input("Enter Line: "))
station = str(input("Enter Station: "))

payload = {"line": line, "sta": station}

r = requests.get(
    "https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php?", params=payload)

mtr_obj = json.dumps(r.json())

with open("mtr.json", "w") as file:
    file.write(mtr_obj)


# file.write(data)
