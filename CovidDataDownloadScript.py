from CovidDataGetter import get_covid_data_json, get_covid_data_csv

url = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/zakladni-prehled.json"
output = "zakladni-prehled.json"

url2 = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/kraj-okres-nakazeni-vyleceni-umrti.csv"
output2 = "kraj-okres-nakazeni-vyleceni-umrti.csv"

get_covid_data_json(url, output)
get_covid_data_csv(url2, output2)
