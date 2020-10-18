# deprecated

import urllib.request
import json
import random
import datetime
import locale

# set locale to czech to get the name of months right
locale.setlocale(locale.LC_TIME, "czech")

# parts for the final article
article_part_1 = ["Koronavirová situace je taková, že ke dni {}",
                  "Ke dni {}"]
article_part_2 = ["bylo provedeno {} testů.",
                  "otestováno {} lidí na koronavirus."]
article_part_3 = ["Aktuálně je aktivních {} případů.",
                  "V současné době je {} aktivních případů nemoci."]
article_part_4 = ["Zatím se vyléčilo {} nemocných.",
                  "Aktuálně je {} nemocných."]
article_part_5 = ["Do dnešního dne na koronavirus zemřelo {} nemocných.",
                  "Koronavirová epidemie si do dnešního dne vyžádala {} obětí."]
article_part_6 = ["Aktuálně je kvůli covid-19 hospitalizováno {} pacientů.",
                  "Hospitalizovaných kvůli koronaviru je aktuálně {} pacientů."]
article_part_7 = ["Včera bylo provedeno {} testů.",
                  "Zdravotníci včera provedli {} testů."]
article_part_8 = ["Během včerejšího dne se potvrdilo {} nových případů nákazy.",
                  "Odborníci zaregistrovali {} nových potvrzených případů nemoci."]
article_part_9 = ["Dnes se nakazilo {} lidí koronavirovou infekcí.",
                  "Během dnešního dne je {} nových nakažených nemocí covid-19"]

# random parts of article templates selection
article_part_1_selected = random.sample(article_part_1, 1)[0]
article_part_2_selected = random.sample(article_part_2, 1)[0]
article_part_3_selected = random.sample(article_part_3, 1)[0]
article_part_4_selected = random.sample(article_part_4, 1)[0]
article_part_5_selected = random.sample(article_part_5, 1)[0]
article_part_6_selected = random.sample(article_part_6, 1)[0]
article_part_7_selected = random.sample(article_part_7, 1)[0]
article_part_8_selected = random.sample(article_part_8, 1)[0]
article_part_9_selected = random.sample(article_part_9, 1)[0]

# download file, process and print
with urllib.request.urlopen("https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/zakladni-prehled.json") as dataset:
    covid_data = json.loads(dataset.read())

    covid_data_processed = covid_data["data"][0]
    data_aquisition_date = covid_data_processed.get("datum")
    datetime_aquistition = datetime.datetime.strptime(data_aquisition_date, "%Y-%m-%d").date()
    datetime_stamp = datetime_aquistition.strftime("%d. %b %Y")
    tests_done_total = covid_data_processed.get("provedene_testy_celkem")
    active_cases = covid_data_processed.get("aktivni_pripady")
    cured_total = covid_data_processed.get("vyleceni")
    deaths_total = covid_data_processed.get("umrti")
    hospitalized = covid_data_processed.get("aktualne_hospitalizovani")
    tests_done_yesterday = covid_data_processed.get("provedene_testy_vcerejsi_den")
    confirmed_cases_yesterday = covid_data_processed.get("potvrzene_pripady_vcerejsi_den")
    confirmed_cases_today = covid_data_processed.get("potvrzene_pripady_dnesni_den")

    print(article_part_1_selected.format(datetime_stamp),
          article_part_2_selected.format(tests_done_total),
          article_part_3_selected.format(active_cases),
          article_part_4_selected.format(cured_total),
          article_part_5_selected.format(deaths_total),
          article_part_6_selected.format(hospitalized),
          article_part_7_selected.format(tests_done_yesterday),
          article_part_8_selected.format(confirmed_cases_today),
          article_part_9_selected.format(confirmed_cases_today))
