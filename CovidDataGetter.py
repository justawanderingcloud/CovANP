# there needs to be some sort of exception handling
# also check if filename exists, if yes, then rename into backuped-datetime and then download
# with csv downloads entire page for some reason

import requests
import urllib.request


def get_covid_data_json(url, output):
    resp = requests.get(url)
    with open(output, "w") as output:
        output.write(resp.text)

def get_covid_data_csv(url, output):
    urllib.request.urlretrieve(url, output)
