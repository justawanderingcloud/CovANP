from CovidDataLocal import covid_general_article_build
from CovidRegionDataLocal import covid_region_article_build

general_article = covid_general_article_build("zakladni-prehled.json")
regional_article = covid_region_article_build("kraj-okres-nakazeni-vyleceni-umrti.csv")

print(general_article)
print(regional_article)