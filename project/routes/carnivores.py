from app import app
from project.functions.dinosaurs import getCarnivores

import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.nhm.ac.uk/discover/dino-directory/nemegtosaurus.html')
soup = BeautifulSoup(r.text, 'lxml')



@app.route('/')
def routeGetCarnivores():
  # return getCarnivores()
  # div_dinosaur = soup.find('div',class_='dinosaur--comparison-dino')
  dino_container = soup.find('div',class_='dinosaur--description-container')
  div_human      = dino_container.find_all('div',class_='dinosaur--comparison-human')
  # div_dinosaur.img['src'] = "https://www.nhm.ac.uk" + div_dinosaur.img['src']1
  # div_human.img['src'] = "https://www.nhm.ac.uk" + div_dinosaur.img['src']
  print( str(div_human))
  return str(div_human)
