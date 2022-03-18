from project.classes.dinosaur import Dinosaur
from flask import jsonify

def getCarnivores():
  data = []
  dino_list = ['t-rex','megalodon']
  for dino in dino_list:
    dinosaur = Dinosaur(dino).toDict()
    data.append(dinosaur)
  return jsonify(data)