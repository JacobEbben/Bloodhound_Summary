import datetime

class BloodHoundDomain(object):

    def __init__(self, object):
        self.ObjectIdentifier = object["ObjectIdentifier"]
        self.Trusts = object["Trusts"]
        self.Aces = object["Aces"]
        self.GPOChanges = object["GPOChanges"]


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

        if 'description' in object["Properties"].keys():
            self.description = object["Properties"]["description"]
        else:
            self.description = None

        if 'functionallevel' in object["Properties"].keys():
            self.functionallevel = object["Properties"]["functionallevel"]
        else:
            self.functionallevel = None

        if 'whencreated' in object["Properties"].keys() and object["Properties"]["whencreated"] != 0:
            self.whencreated = datetime.datetime.fromtimestamp( object["Properties"]["whencreated"] )
        else:
            self.whencreated = ""
        
        if 'highvalue' in object["Properties"].keys():
            self.highvalue = object["Properties"]["highvalue"]
        else:
            self.highvalue = None
