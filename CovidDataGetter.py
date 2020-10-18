# there needs to be some sort of exception handling
# also check if filename exists, if yes, then rename into backuped-datetime and then download

from requests import get


def GetCovidData(url, output):
    with open(output, "wb") as file:
        response = get(url)
        file.write(response.content)
