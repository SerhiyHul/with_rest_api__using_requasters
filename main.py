from star_wars_api import StarWarsApi

api_client = StarWarsApi()
person = api_client.get_person(1)
print("Name: " + person.name)
print("Skin color: " + person.skin_color)

planet = api_client.get_planet(2)
print("Name planet " + planet.name)

ship = api_client.get_ship(9)
print("Name: " + ship.name)