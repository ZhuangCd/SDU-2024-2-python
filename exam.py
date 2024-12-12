import pandas as pd
from urllib.request import Request, urlopen

url = "https://en.wikipedia.org/wiki/List_of_continents_and_continental_subregions_by_population"


tables = pd.read_html(url, header=0)
print(f"TYPE: {type(tables)}, SIZE: {len(tables)}")


print(tables)
