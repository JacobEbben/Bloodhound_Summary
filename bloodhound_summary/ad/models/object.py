class BloodHoundObject(object):

    def __init__(self, object):
        self.ObjectIdentifier = object["ObjectIdentifier"]
        self.Aces = object["Aces"]

        if 'name' in object["Properties"].keys():
            self.name = object["Properties"]["name"]
        else:
            self.name = None