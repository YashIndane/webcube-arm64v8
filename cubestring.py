import cv2
import numpy as np
import joblib
from subprocess import getstatusoutput as gso

def get_cubestring():

  s_scalar = joblib.load("Scalar1")
  model = joblib.load("model_0.04")
  
  cubestring = ""
  colours = ["orange", "red", "green", "blue", "yellow", "white"]
  
  colour_mappings = {

    "red": "F",
    "green": "R",
    "blue": "L",
    "yellow": "U",
    "white": "D",
    "orange": "B"
 
  }

  coordinates = [

    [22,35], [22,74], [22,113],
    [72,35], [72,74], [72,113],
    [122,35], [122,74], [122,113]

  ]
  
  for i in range(6) :
    face = cv2.imread(f"face_{i}.png")
    for x in range(9) :
      n , m = coordinates[x]
      pixel_array = []
      for p in face[n][m] :
        pixel_array.append(p)

      n_array = np.array([pixel_array])
      arr = s_scalar.transform([pixel_array])
      value = model.predict(arr)

      index = value[0] - 1
      cubestring += colour_mappings[colours[index]]

    gso(f"echo 'y' | rm face_{i}.png")
      
  return cubestring
