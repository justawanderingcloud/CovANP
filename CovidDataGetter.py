from requests import get


def GetCovidData(url, output):
    with open(output, "wb") as file:
        response = get(url)
        file.write(response.content)
