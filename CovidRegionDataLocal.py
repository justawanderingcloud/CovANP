# exception handling for NameError
# parametrize for input region

import pandas as pd
import random
import datetime

# pd.set_option("display.max_rows", None, "display.max_columns", None)


def covid_region_article_build(region_source):
    data = pd.read_csv(region_source)

    stredocesky_kraj = "CZ020"

    last_date = data[data["datum"] == data["datum"].iloc[-1]]

    # stredocesky kraj
    str_cz = last_date[last_date["kraj_nuts_kod"] == stredocesky_kraj]

    str_cz_processed = str_cz.replace(["CZ020", "CZ0201", "CZ0202", "CZ0203", "CZ0204", "CZ0205", "CZ0206", "CZ0207",
                                       "CZ0208", "CZ0209", "CZ020A", "CZ020B", "CZ020C"],
                                      ["Stredocesky kraj", "Benešov", "Beroun", "Kladno",
                                       "Kolín", "Kutná Hora", "Mělník", "Mladá Boleslav",
                                       "Nymburk", "Praha-východ", "Praha-západ", "Příbram",
                                       "Rakovník"])

    str_cz_processed.to_csv(r"output.csv", index=False)

    str_cz_sorted_total_infected = str_cz_processed["kumulativni_pocet_nakazenych"].sum()
    str_cz_sorted_total_cured = str_cz_processed["kumulativni_pocet_vylecenych"].sum()
    str_cz_sorted_total_dead = str_cz_processed["kumulativni_pocet_umrti"].sum()

    str_cz_sorted_infected = str_cz_processed.sort_values(["kumulativni_pocet_nakazenych"], ascending=False)
    str_cz_sorted_cured = str_cz_processed.sort_values(["kumulativni_pocet_vylecenych"], ascending=False)
    str_cz_sorted_dead = str_cz_processed.sort_values(["kumulativni_pocet_umrti"], ascending=False)

    str_cz_sorted_most_infected = str_cz_sorted_infected.iloc[[0], [2, 3]]
    str_cz_sorted_least_infected = str_cz_sorted_infected.iloc[[-1], [2, 3]]

    str_cz_sorted_most_cured = str_cz_sorted_cured.iloc[[0], [2, 4]]
    str_cz_sorted_least_cured = str_cz_sorted_cured.iloc[[-1], [2, 4]]

    str_cz_sorted_most_dead = str_cz_sorted_dead.iloc[[0], [2, 5]]
    str_cz_sorted_least_dead = str_cz_sorted_dead.iloc[[-1], [2, 5]]

    str_cz_sorted_most_infected_list = str_cz_sorted_most_infected.values.tolist()[0]
    str_cz_sorted_least_infected_list = str_cz_sorted_least_infected.values.tolist()[0]

    str_cz_sorted_most_cured_list = str_cz_sorted_most_cured.values.tolist()[0]
    str_cz_sorted_least_cured_list = str_cz_sorted_least_cured.values.tolist()[0]

    str_cz_sorted_most_dead_list = str_cz_sorted_most_dead.values.tolist()[0]
    str_cz_sorted_least_dead_list = str_cz_sorted_least_dead.values.tolist()[0]

    template_most_infected = ["Nejhůře na tom je okres {} s {} nemocnými covid-19. ",
                              "Situace je z kraje nejlepší v okrese {}, kde je v současné době {} nemocných. "]
    template_least_infected = ["Nejlépe na tom je okres {} s {} nemocnými. ",
                               "Naopak nejlépe se daří okresu {}, kde je pouze {} nemocných. "]
    template_most_cured = ["V okrese {} se z nemoci covid-19 vyléčilo nejvíce pacientů z kraje, a sice  {} lidí. ",
                           "Nejvíce vyléčených zaznameni hygienici v okrese {}, kde je takových pacientů {} ."]
    template_least_cured = ["Dosud se nejméně pacientů vyléčilo na okrese {}, nemoci se zbavilo pouze {} nemocných. ",
                            "Okres {} má v tuto chvíli nejméně vyléčených, a sice {} pacientů. "]
    template_most_dead = ["Na nemoc covid-19 v okrese {} zemřelo nejvíce lidí: {} nemocných. ",
                          "Nemoci covid-19 podlehlo z kraje nejvíce lidí v okrese {}: a sice {} obětí. "]
    template_least_dead = ["Nejméně lidí podlehlo koronaviru v okrese {}. Jedná se o {} nemocných, kteří zemřeli. ",
                           "V okrese {} zemřelo na koronavirus {} lidí, což je nejméně z kraje. "]

    template_most_infected_selected = random.sample(template_most_infected, 1)[0]
    template_least_infected_selected = random.sample(template_least_infected, 1)[0]
    template_most_cured_selected = random.sample(template_most_cured, 1)[0]
    template_least_cured_selected = random.sample(template_least_cured, 1)[0]
    template_most_dead_selected = random.sample(template_most_dead, 1)[0]
    template_least_dead_selected = random.sample(template_least_dead, 1)[0]

    newest_date = data["datum"].iloc[-1]
    newest_date_processed = datetime.datetime.strptime(newest_date, "%Y-%m-%d").date()
    newest_date_str = newest_date_processed.strftime("%d. %b %Y")
    epilogue = "Nejnovější data hygieniků k " + str(newest_date_str) + " hovoří o následujícím: "
    stc_cz_total_infected_article = "Ve Středočeském kraji je v současné době " + str(str_cz_sorted_total_infected) + " nakažených lidí nemocí covid-19. "
    stc_cz_total_cured_article = "Dosud se vyléčilo " + str(str_cz_sorted_total_cured) + " pacientů. "
    stc_cz_total_dead_article = "Celkový počet obětí nemoci covid-19 je " + str(str_cz_sorted_total_dead) + " pacientů. "

    stc_cz_most_infected_article = template_most_infected_selected.format(*str_cz_sorted_most_infected_list)
    stc_cz_least_infected_article = template_least_infected_selected.format(*str_cz_sorted_least_infected_list)
    stc_cz_most_cured_article = template_most_cured_selected.format(*str_cz_sorted_most_cured_list)
    stc_cz_least_cured_article = template_least_cured_selected.format(*str_cz_sorted_least_cured_list)
    stc_cz_most_dead_article = template_most_dead_selected.format(*str_cz_sorted_most_dead_list)
    stc_cz_least_dead_article = template_least_dead_selected.format(*str_cz_sorted_least_dead_list)

    stc_covid_regional_article_parts = [epilogue, stc_cz_total_infected_article, stc_cz_total_cured_article,
                                        stc_cz_total_dead_article, stc_cz_most_infected_article,
                                        stc_cz_least_infected_article, stc_cz_most_cured_article,
                                        stc_cz_least_cured_article, stc_cz_most_dead_article,
                                        stc_cz_least_dead_article]

    stc_covid_regional_article = "".join(stc_covid_regional_article_parts)
    return stc_covid_regional_article
