from urllib import response
import requests
import json





print(len(tml_stat))

#line = str(input("Enter Line: "))
#station = str(input("Enter Station: "))

for i in tml_stat:

    payload = {"line": "TML", "sta": i}

    r = requests.get(
    "https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php?", params=payload)

    tmt_stat_obj = json.dumps(r.json(), indent=4)

    print(tmt_stat_obj)

    with open("tml_stat.json", "w") as file:
        file.write(tmt_stat_obj)


# file.write(data)
