import requests

from entity.person import Person
from entity.planet import Planet
from entity.ship import Ship


class StarWarsApi:
    def __init__(self):
        self.base_url = 'https://swapi.dev/'

    def get_entity(self, entity, entity_id):
        url = f"{self.base_url}api/{entity}/{entity_id}/"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        else:
            raise ValueError(f'Неможливо отримати дані для сутності {entity} з індетифікатором {entity_id}')

    def get_person(self, person_id):
        return Person(self.get_entity('people', person_id))

    def get_planets(self, planet, planet_id):
        url = f"{self.base_url}api/{planet}/{planet_id}/"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f'Неможливо отримати дані для сутності {planet} з індетифікатором {planet_id}')
    def get_planet(self, planet_id):
        return Planet(self.get_entity('planets', planet_id))

    def get_ships(self, ship, ship_id):
        url = f"{self.base_url}api/{ship}/{ship_id}/"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f'Неможливо отримати дані для сутності {planet} з індетифікатором {planet_id}')

    def get_ship(self, ship_id):
        return Ship(self.get_entity('starships', ship_id))



