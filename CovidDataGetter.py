# there needs to be some sort of exception handling
# also check if filename exists, if yes, then rename into backuped-datetime and then download

import requests
import urllib.request


def get_covid_data_json(url, output):
    try:
        resp = requests.get(url)
        with open(output, "w") as output:
            output.write(resp.text)
    except ConnectionError as e:
        print(e)


def get_covid_data_csv(url, output):
    try:
        urllib.request.urlretrieve(url, output)
    except ConnectionError as e:
        print(e)
