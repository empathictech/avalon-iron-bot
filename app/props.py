class Property:
  
  def __init__(self, name):
    self.name = name
    self.price = "No price found"
    self.address = "No address found"
    self.commute_info = "Commute: info not requested"
    self.availability = "No move in/out info found"
    self.link = "URL not found"

  def get_info(self):
    return f"""
Posting name: {self.name}
Rent: {self.price}
Property address: {self.address}
{self.commute_info}
Availability: {self.availability}
Link to page: {self.link}
"""