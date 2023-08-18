import datetime

class BloodHoundUser(object):

    def __init__(self, object=None):
        self.ObjectIdentifier = object["ObjectIdentifier"]
        self.PrimaryGroupSID = object["PrimaryGroupSID"]
        self.AllowedToDelegate = object["AllowedToDelegate"]
        self.Aces = object["Aces"]
        self.SPNTargets = object["SPNTargets"]


        if 'name' in object["Properties"].keys():
            self.name = object["Properties"]["name"]
        else:
            self.name = None

        if 'domain' in object["Properties"].keys():
            self.domain = object["Properties"]["domain"]
        else:
            self.domainsid = None

        if 'domainsid' in object["Properties"].keys():
            self.domainsid = object["Properties"]["domainsid"]
        else:
            self.domainsid = None

        if 'distinguishedname' in object["Properties"].keys():
            self.distinguishedname = object["Properties"]["distinguishedname"]
        else:
            self.distinguishedname = None

        if 'unconstraineddelegation' in object["Properties"].keys():
            self.unconstraineddelegation = object["Properties"]["unconstraineddelegation"]
        else:
            self.unconstraineddelegation = None

        if 'trustedtoauth' in object["Properties"].keys():
            self.trustedtoauth = object["Properties"]["trustedtoauth"]
        else:
            self.trustedtoauth = None

        if 'passwordnotreqd' in object["Properties"].keys():
            self.passwordnotreqd = object["Properties"]["passwordnotreqd"]
        else:
            self.passwordnotreqd = None

        if 'enabled' in object["Properties"].keys():
            self.enabled = object["Properties"]["enabled"]
        else:
            self.enabled = None

        if 'lastlogon' in object["Properties"].keys() and object["Properties"]["lastlogon"] != 0:
            self.lastlogon = datetime.datetime.fromtimestamp( object["Properties"]["lastlogon"] )
        else:
            self.lastlogon = ""

        if 'pwdlastset' in object["Properties"].keys() and object["Properties"]["pwdlastset"] != 0:
            self.pwdlastset = datetime.datetime.fromtimestamp( object["Properties"]["pwdlastset"] )
        else:
            self.pwdlastset = ""

        if 'dontreqpreauth' in object["Properties"].keys():
            self.dontreqpreauth = object["Properties"]["dontreqpreauth"]
        else:
            self.dontreqpreauth = None

        if 'hasspn' in object["Properties"].keys():
            self.hasspn = object["Properties"]["hasspn"]
        else:
            self.hasspn = None
        
        if 'serviceprincipalnames' in object["Properties"].keys():
            self.serviceprincipalnames = object["Properties"]["serviceprincipalnames"]
        else:
            self.serviceprincipalnames = None


        if 'displayname' in object["Properties"].keys():
            self.displayname = object["Properties"]["displayname"]
        else:
            self.displayname = None

        if 'email' in object["Properties"].keys():
            self.email = object["Properties"]["email"]
        else:
            self.email = None

        if 'title' in object["Properties"].keys():
            self.title = object["Properties"]["title"]
        else:
            self.title = None

        if 'description' in object["Properties"].keys():
            self.description = object["Properties"]["description"]
        else:
            self.description = None

        if 'admincount' in object["Properties"].keys():
            self.admincount = object["Properties"]["admincount"]
        else:
            self.admincount = None

        if 'whencreated' in object["Properties"].keys() and object["Properties"]["whencreated"] != 0:
            self.whencreated = datetime.datetime.fromtimestamp( object["Properties"]["whencreated"] )
        else:
            self.whencreated = ""

        if 'samaccountname' in object["Properties"].keys():
            self.samaccountname = object["Properties"]["samaccountname"]
        else:
            self.samaccountname = None

        if 'userpassword' in object["Properties"].keys():
            self.userpassword = object["Properties"]["userpassword"]
        else:
            self.userpassword = None

        if 'unixpassword' in object["Properties"].keys():
            self.unixpassword = object["Properties"]["unixpassword"]
        else:
            self.unixpassword = None

        if 'unicodepassword' in object["Properties"].keys():
            self.unicodepassword = object["Properties"]["unicodepassword"]
        else:
            self.unicodepassword = None

        if 'sfupassword' in object["Properties"].keys():
            self.sfupassword = object["Properties"]["sfupassword"]
        else:
            self.sfupassword = None

        if 'highvalue' in object["Properties"].keys():
            self.highvalue = object["Properties"]["highvalue"]
        else:
            self.highvalue = None
