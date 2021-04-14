import enum

class Material(enum.Enum):
    cardboard = 0 
    glass = 1
    metal = 2
    paper = 3
    plastic = 4
    trash = 5
    
class SensorPrediction:
  def __init__(self, metal, plastic, glass):
    self.metal = metal
    self.plastic = plastic
    self.glass = glass
  
  def __str__(self):
    return "Metal: %s, Plastic: %s, Glass: %s" % (self.metal, self.plastic, self.glass)

class ImagePrediction:
  def __init__(self, material, confidence):
    self.material = material 
    self.confidence = confidence 

  def __str__(self):
    return "%s: %s" % (self.material, self.confidence)
  





