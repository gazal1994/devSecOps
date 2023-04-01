import json

import requests
from Address import Address
from Geo import Geo
from MyUser import MyUser
from SpeedUser import SpeedUser


class UserService:
    users_list = {}
    speed_user_list = {}
    data_json = []

    def init_data_from_json(self, url):
        response = requests.get(url)
        try:
            self.data_json = response.json()
        except json.decoder.JSONDecodeError:
            print("Failed to parse JSON data from URL.")
            return None

    def get_random_name(self, url, num):
        for n in range(num):
            response = requests.get(url)
            try:
                print("the name is : " + response.json()["results"][0]["name"]["first"])
            except json.decoder.JSONDecodeError:
                print("Failed to parse JSON data from URL.")
                return None

    def init_users_by_name(self):
        for user in self.data_json:
            self.users_list[user["name"]] = MyUser(user["id"],
                                                   user["email"],
                                                   user["username"],
                                                   user["name"])

    def init_SpeedUser_by_id(self):
        for user in self.data_json:
            geo = Geo(user["address"]["geo"]["lat"], user["address"]["geo"]["lng"])
            address = Address(user["address"]["street"], user["address"]["suite"], user["address"]["city"],
                              user["address"]["zipcode"], geo)
            self.speed_user_list[user["id"]] = SpeedUser(user["id"],
                                                         user["email"],
                                                         user["username"],
                                                         user["name"],
                                                         address)

    def get_closer_latitude(self, lat):
        closer = 100000000
        speed_user_id = None
        for value in self.speed_user_list:
            speed_user = self.speed_user_list[value]
            if abs(lat - float(speed_user.address.geo.lat)) < closer:
                closer = abs(lat - float(speed_user.address.geo.lat))
                speed_user_id = speed_user.id

        return self.speed_user_list[speed_user_id]

    def get_user_by_name(self, name):
        return self.users_list[name] if name in self.users_list else "user not found"


if __name__ == "__main__":
    u = UserService()
    u.init_data_from_json('https://jsonplaceholder.typicode.com/users')
    u.init_users_by_name()
    u.init_SpeedUser_by_id()
    print(u.get_user_by_name("Ervin Howell").__str__())
    lat = float(input("Enter a latitude-point : "))
    print(u.get_closer_latitude(lat).__str__())
    number = int(input("Enter a number less than 100: "))
    while number > 100:
        number = int(input("Enter a number less than 100: "))
    u.get_random_name("https://randomuser.me/api/", number)
