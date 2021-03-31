import enum

class Material(enum.Enum):
    paper = 1
    cardboard = 2 
    plastic = 3
    metal = 4
    glass = 5
    trash = 6
    
class Prediction:
  def __init__(self, metal, plastic):
    self.metal = metal
    self.plastic = plastic
  
  def __str__(self):
      return "Metal: %s, Plastic: %s" % (self.metal, self.plastic)

