# pip install geopy
from geopy.geocoders import Nominatim

a=Nominatim(user_agent="My_App")
print(a.geocode("ISBM , india"))

"""
from geopy.geocoders import Nominatim

geo = Nominatim(user_agent="My_App")
print(geo.geocode("Pune, India"))
"""
