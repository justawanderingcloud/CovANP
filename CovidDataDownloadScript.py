from CovidDataGetter import GetCovidData

url = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/zakladni-prehled.json"
output = "zakladni-prehled.json"

url2 = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/kraj-okres-nakazeni-vyleceni-umrti.csv"
output2 = "kraj-okres-nakazeni-vyleceni-umrti.csv"

GetCovidData(url, output)
GetCovidData(url2, output2)