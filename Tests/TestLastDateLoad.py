import pandas as pd

region_source = "kraj-okres-nakazeni-vyleceni-umrti.csv"

data = pd.read_csv(region_source)

last_date2 = data["datum"].iloc[-1]

print(last_date2)