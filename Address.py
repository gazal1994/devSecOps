class Address:
    def __init__(self, street, suite, city, zipcode, geo):
        self._street = street
        self._suite = suite
        self._city = city
        self._zipcode = zipcode
        self._geo = geo

    @property
    def street(self):
        return self._street

    @property
    def suite(self):
        return self._suite

    @property
    def city(self):
        return self._city

    @property
    def zipcode(self):
        return self._zipcode

    @property
    def geo(self):
        return self._geo

    @street.setter
    def street(self, street):
        self._street = street

    @geo.setter
    def geo(self, geo):
        self._geo = geo

    @zipcode.setter
    def zipcode(self, zipcode):
        self._zipcode = zipcode

    @city.setter
    def city(self, city):
        self._city = city

    @suite.setter
    def suite(self, suite):
        self.suite = suite
