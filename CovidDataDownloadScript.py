from CovidDataGetter import GetCovidData

url = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/zakladni-prehled.json"
output = "zakladni-prehled.json"

GetCovidData(url, output)