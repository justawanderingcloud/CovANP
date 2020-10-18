# there needs to be some sort of exception handling
# also check if filename exists, if yes, then rename into backuped-datetime and then download
# with csv downloads entire page for some reason

import requests

def GetCovidData(url, output):
    resp = requests.get(url)
    with open(output, "w") as output:
        output.write(resp.text)
