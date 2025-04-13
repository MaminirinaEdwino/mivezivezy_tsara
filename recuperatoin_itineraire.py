import json
from geopy.geocoders import Nominatim
from routingpy import ORS
from math import atan2, radians, degrees, cos, sin

def get_bearing(start, end):
    lat1, lon1 = map(radians, start)
    lat2, lon2 = map(radians, end)

    delta_lon = lon2 - lon1
    x = sin(delta_lon) * cos(lat2)
    y = cos(lat1)*sin(lat2) - sin(lat1)*cos(lat2)*cos(delta_lon)
    bearing = atan2(x, y)
    return (degrees(bearing) + 360) % 360

locator = Nominatim(user_agent="myGeocoder")
# location = locator.geocode("tombotsoa antsirabe")

# location2 = locator.geocode("asja antsirabe")
# print(location2.address)
# print(location.address)
start = [47.508249, -18.920810]
end = [47.512011, -18.914724]
def recup_trajet(start, end): 
    ors_client = ORS(
        api_key="5b3ce3597851110001cf6248a2395e98d9a34e8cab30870bdfb638f4",
    )
    route = ors_client.directions(locations=[start, end], profile="driving-car")
    # print("route \n", route)
    # print(route.distance/1000, "Km")
    # print(route.duration/60, "minutes")
    # print(route.geometry)
    # print(f"direction {get_bearing(start, end)}°")
    # with open(nom_fichier, "w") as file:
    #     json.dump({
    #     "distance": route.distance/1000,
    #     "duration": route.duration/60,
    #     "geometry": route.geometry,
    #     "bearing": get_bearing(start, end)
    # }, file)
    return {
        "distance": route.distance/1000,
        "duration": route.duration/60,
        "geometry": route.geometry,
        "bearing": get_bearing(start, end)
    }
        
# recup_trajet([47.508474, -18.916382],[47.508791, -18.916387], "trajet1.json")
# recup_trajet([ 47.508614,-18.916259], [47.508584, -18.916578], "trajet2.json")
# recup_trajet([47.508750, -18.916244], [47.508499, -18.916506], "trajet3.json")
# recup_trajet([47.508771, -18.916254], [47.508514, -18.916059], "trajet4.json")
# recup_trajet([47.508803, -18.916269], [ 47.508519, -18.916061], "trajet5.json")
# recup_trajet([ 47.508615, -18.916477], [ 47.508782, -18.916381], "trajet6.json")
    
