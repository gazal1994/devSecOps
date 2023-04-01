from MyUser import MyUser


class SpeedUser(MyUser):

    def __init__(self, id, email, username, name, address):
        super().__init__(id, email, username, name)
        self._address = address

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    def __str__(self):
        return "id: " + str(self.id) \
            + " name: " + self.name \
            + " email: " + self.email \
            + " username: " + self.username \
            + " address: [ " \
            "street: " + self.address.street + ", " \
            "suite: " + self.address.suite + ", " \
            "city: " + self.address.city + ", " \
            "zipcode: " + self.address.zipcode + ", " \
            "geo: { " \
            "lat: " + str(self.address.geo.lat) + ", " \
            "lng: " + str(self.address.geo.lng) + " } ]"
