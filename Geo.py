class Geo:
    def __init__(self, lat, lng):
        self._lat = lat
        self._lng = lng

    @property
    def lat(self):
        return self._lat

    @property
    def lng(self):
        return self._lng

    @lat.setter
    def lat(self, lat):
        self._lat = lat

    @lng.setter
    def lng(self, lng):
        self._lng = lng
