class MyUser:
    def __init__(self, id, email, username, name):
        self._id = id
        self._email = email
        self._username = username
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    def __str__(self):
        return "id: " + str(self.id) + " name: " + self.name + " email: " + self.email + " username: " + self.username
