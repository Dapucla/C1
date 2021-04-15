class Guest:
    def __init__(self, name, location, status):
        self.name = name
        self.location = location
        self.status = status


class GuestData(Guest):
    def get_guest(self):
        return str(self.name) + "," + str(self.location) + "," + "cтатус " + '"' + str(self.status) + '"'