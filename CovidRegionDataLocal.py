# exception handling for NameError
# parametrize for input region

import pandas as pd

# pd.set_option("display.max_rows", None, "display.max_columns", None)


def covid_region_article_build(region_source):
    data = pd.read_csv(region_source)

    stredocesky_kraj = "CZ020"

    last_date = data[data["datum"] == data["datum"].iloc[-1]]

    # stredocesky kraj
    str_cz = last_date[last_date["kraj_nuts_kod"] == stredocesky_kraj]

    str_cz_processed = str_cz.replace(["CZ020", "CZ0201", "CZ0202", "CZ0203", "CZ0204", "CZ0205", "CZ0206", "CZ0207",
                                       "CZ0208", "CZ0209", "CZ020A", "CZ020B", "CZ020C"],
                                      ["Stredocesky kraj", "Okres Benešov", "Okres Beroun", "Okres Kladno",
                                       "Okres Kolín", "Okres Kutná Hora", "Okres Mělník", "Okres Mladá Boleslav",
                                       "Okres Nymburk", "Okres Praha-východ", "Okres Praha-západ", "Okres Příbram",
                                       "Okres Rakovník"])

    # str_cz_processed.to_csv(r"output.csv", index=False)

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

    template1_1 = "Nejhůře na tom je {} s {} nemocnými."
    template1_2 = "Nejlépe na tom je {} s {} nemocnými."
    template2_1 = "V okrese {} se z covidu vylecilo nejvice pacientu z kraje: {} lidi."
    template2_2 = "Naopak v okrese {} se vylecilo nejmene pacientu, tedy {}."

    print("Celkovy pocet nakazenych v STC kraji je", str_cz_sorted_total_infected)
    print("Celkovy pocet vylecenych v STC kraji je", str_cz_sorted_total_cured)
    print("Celkovy pocet zemrelych v STC kraji je", str_cz_sorted_total_dead)

    print(template1_1.format(*str_cz_sorted_most_infected_list))
    print(template1_2.format(*str_cz_sorted_least_infected_list))
    print(template2_1.format(*str_cz_sorted_most_cured_list))
    print(template2_2.format(*str_cz_sorted_least_cured_list))
