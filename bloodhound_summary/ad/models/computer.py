import datetime

class BloodHoundComputer(object):

    def __init__(self, object):
        self.ObjectIdentifier = object["ObjectIdentifier"]
        self.PrimaryGroupSID = object["PrimaryGroupSID"]
        self.AllowedToAct = object["AllowedToAct"]
        self.AllowedToDelegate = object["AllowedToDelegate"]
        self.Aces = object["Aces"]

        if object["LocalAdmins"]["Collected"]:
            self.LocalAdmins = object["LocalAdmins"]["Results"]
        else:
            self.LocalAdmins = []
        
        if object["PSRemoteUsers"]["Collected"]:
            self.PSRemoteUsers = object["PSRemoteUsers"]["Results"]
        else:
            self.PSRemoteUsers = []

        if object["RemoteDesktopUsers"]["Collected"]:
            self.RemoteDesktopUsers = object["RemoteDesktopUsers"]["Results"]
        else:
            self.RemoteDesktopUsers = []

        if object["DcomUsers"]["Collected"]:
            self.DcomUsers = object["DcomUsers"]["Results"]
        else:
            self.DcomUsers = []

        if object["Sessions"]["Collected"]:
            self.Sessions = object["Sessions"]["Results"]
        else:
            self.Sessions = []

        if object["PrivilegedSessions"]["Collected"]:
            self.PrivilegedSessions = object["PrivilegedSessions"]["Results"]
        else:
            self.PrivilegedSessions = []

        if object["RegistrySessions"]["Collected"]:
            self.RegistrySessions = object["RegistrySessions"]["Results"]
        else:
            self.RegistrySessions = []

        if 'name' in object["Properties"].keys():
            self.name = object["Properties"]["name"]
        else:
            self.name = None
        
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

        if 'enabled' in object["Properties"].keys():
            self.enabled = object["Properties"]["enabled"]
        else:
            self.enabled = None

        if 'trustedtoauth' in object["Properties"].keys():
            self.trustedtoauth = object["Properties"]["trustedtoauth"]
        else:
            self.trustedtoauth = None
    
        if 'samaccountname' in object["Properties"].keys():
            self.samaccountname = object["Properties"]["samaccountname"]
        else:
            self.samaccountname = None

        if 'haslaps' in object["Properties"].keys():
            self.haslaps = object["Properties"]["haslaps"]
        else:
            self.haslaps = None

        if 'lastlogon' in object["Properties"].keys() and object["Properties"]["lastlogon"] != 0:
            self.lastlogon = datetime.datetime.fromtimestamp( object["Properties"]["lastlogon"] )
        else:
            self.lastlogon = ""
    
        if 'whencreated' in object["Properties"].keys() and object["Properties"]["whencreated"] != 0:
            self.whencreated = datetime.datetime.fromtimestamp( object["Properties"]["whencreated"] )
        else:
            self.whencreated = ""

        if 'serviceprincipalnames' in object["Properties"].keys():
            self.serviceprincipalnames = object["Properties"]["serviceprincipalnames"]
        else:
            self.serviceprincipalnames = None

        if 'description' in object["Properties"].keys():
            self.description = object["Properties"]["description"]
        else:
            self.description = None

        if 'operatingsystem' in object["Properties"].keys():
            self.operatingsystem = object["Properties"]["operatingsystem"]
        else:
            self.operatingsystem = None
