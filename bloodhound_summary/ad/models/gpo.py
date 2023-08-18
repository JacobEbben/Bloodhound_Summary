import datetime

class BloodHoundGpo(object):

    def __init__(self, object):
        self.ObjectIdentifier = object["ObjectIdentifier"]
        self.Aces = object["Aces"]

        if 'name' in object["Properties"].keys():
            self.name = object["Properties"]["name"]
        else:
            self.name = None

        if 'domain' in object["Properties"].keys():
            self.domain = object["Properties"]["domain"]
        else:
            self.domain = None

        if 'domainsid' in object["Properties"].keys():
            self.domainsid = object["Properties"]["domainsid"]
        else:
            self.domainsid = None

        if 'distinguishedname' in object["Properties"].keys():
            self.distinguishedname = object["Properties"]["distinguishedname"]
        else:
            self.distinguishedname = None

        if 'gpcpath' in object["Properties"].keys():
            self.gpcpath = object["Properties"]["gpcpath"]
        else:
            self.gpcpath = None

        if 'description' in object["Properties"].keys():
            self.description = object["Properties"]["description"]
        else:
            self.description = None

        if 'whencreated' in object["Properties"].keys() and object["Properties"]["whencreated"] != 0:
            self.whencreated = datetime.datetime.fromtimestamp( object["Properties"]["whencreated"] )
        else:
            self.whencreated = ""

        if 'highvalue' in object["Properties"].keys():
            self.highvalue = object["Properties"]["highvalue"]
        else:
            self.highvalue = None