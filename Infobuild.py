from CovidDataLocal import covid_general_article_build
from CovidRegionDataLocal import covid_region_article_build

print(covid_general_article_build("zakladni-prehled.json"))
covid_region_article_build("kraj-okres-nakazeni-vyleceni-umrti.csv")