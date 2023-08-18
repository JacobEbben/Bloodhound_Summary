from bloodhound_summary.ad.models.user import BloodHoundUser
from bloodhound_summary.ad.models.domain import BloodHoundDomain
from bloodhound_summary.ad.models.computer import BloodHoundComputer
from bloodhound_summary.ad.models.group import BloodHoundGroup
from bloodhound_summary.ad.models.container import BloodHoundContainer
from bloodhound_summary.ad.models.gpo import BloodHoundGpo
from bloodhound_summary.ad.models.ou import BloodHoundOu
from bloodhound_summary.ad.models.object import BloodHoundObject

class BloodHoundData():

    def __init__(self):
        self.SUPPORTED_TYPES = ["users", "domains", "computers", "groups", "containers", "gpos", "ous"]
        self.SUPPORTED_VERSIONS = [5]

        self.loaded_files = []
        self.SID_MAP = {} 
        self.domains = []
        self.users = []
        self.computers = []
        self.groups = []
        self.containers = []
        self.gpos = []
        self.ous = []
        self.objects = []


    def import_ingestor_file(self, bloodhound_file):

        metadata = bloodhound_file["meta"]

        self.loaded_files.append(metadata)

        if metadata["type"] not in self.SUPPORTED_TYPES:
            print(f'{metadata["type"].upper()} BloodHound data is not supported by this tool ...')
            return None

        if metadata["version"] not in self.SUPPORTED_VERSIONS:
            print(f'Unsupported ingestor version: {metadata["version"]} ...')
            print("Exiting ...")
            exit()

        for bloodhound_object in bloodhound_file["data"]:

            sid = bloodhound_object["ObjectIdentifier"]

            if metadata["type"] == "users":
                new_object = BloodHoundUser(bloodhound_object)
                self.users.append(new_object)
            elif metadata["type"] == "domains":
                new_object = BloodHoundDomain(bloodhound_object)
                self.domains.append(new_object)
            elif metadata["type"] == "computers":
                new_object = BloodHoundComputer(bloodhound_object)
                self.computers.append(new_object)
            elif metadata["type"] == "groups":
                new_object = BloodHoundGroup(bloodhound_object)
                self.groups.append(new_object)
            elif metadata["type"] == "containers":
                new_object = BloodHoundContainer(bloodhound_object)
                self.containers.append(new_object)
            elif metadata["type"] == "gpos":
                new_object = BloodHoundGpo(bloodhound_object)
                self.gpos.append(new_object)
            elif metadata["type"] == "ous":
                new_object = BloodHoundOu(bloodhound_object)
                self.ous.append(new_object)
            else:
                new_object = BloodHoundObject(bloodhound_object)
                self.objects.append(new_object)
        
            self.SID_MAP[sid] = new_object
    
    def get_object_by_sid(self, sid):
        try:
            return self.SID_MAP[sid]
        except KeyError:
            return None
