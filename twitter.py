import requests
from bs4 import BeautifulSoup
import json
import time


while 1:
    page = requests.get("https://www.worldometers.info/coronavirus/country/brazil/")
    soup = BeautifulSoup(page.text, 'html.parser')

    container = soup.findAll("div", {"class": "maincounter-number"})
    cases = container[0].text.strip()
    deaths = container[1].text.strip()
    recovered = container[2].text.strip()

    brasil = ("🇧🇷 Total de casos no Brasil: \n"+ \
          "Casos confirmadoss: " + cases + "\n" + \
          "Óbitos: " + deaths + "\n" + \
          "Recuperações: " + recovered + "\n\n") 

    page = requests.get("https://www.worldometers.info/coronavirus/")
    soup = BeautifulSoup(page.text, 'html.parser')  
    container = soup.findAll("div", {"class": "maincounter-number"})
    cases = container[0].text.strip()
    deaths = container[1].text.strip()
    recovered = container[2].text.strip()

    mundo = ("🌎 Total de casos no Mundo: \n"+ \
          "Casos confirmados: " + cases + "\n" + \
          "Óbitos: " + deaths + "\n" + \
          "Recuperações: " + recovered + "\n\n") 

    print(brasil)
    print(mundo)

    url = "https://hooks.zapier.com/hooks/catch/7498357/oreb9s1"
    data = {'value1:': brasil , 'value2': mundo}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)

    print(r.text)
    time.sleep(3600)