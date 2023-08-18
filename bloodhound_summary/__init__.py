import sys
import zipfile
import json
from termcolor import colored

from bloodhound_summary.ad.bloodhound import BloodHoundData

from bloodhound_summary.printers.domain import print_domain_info
from bloodhound_summary.printers.user import print_user_info
from bloodhound_summary.printers.group import print_group_info
from bloodhound_summary.printers.computer import print_computer_info


def print_header():
    print(colored("  ____  _                 _ _                           _   ____                                             ", 'yellow', attrs=["bold"]))
    print(colored(" | __ )| | ___   ___   __| | |__   ___  _   _ _ __   __| | / ___| _   _ _ __ ___  _ __ ___   __ _ _ __ _   _ ", 'yellow', attrs=["bold"]))
    print(colored(" |  _ \| |/ _ \ / _ \ / _` | '_ \ / _ \| | | | '_ \ / _` | \___ \| | | | '_ ` _ \| '_ ` _ \ / _` | '__| | | |", 'yellow', attrs=["bold"]))
    print(colored(" | |_) | | (_) | (_) | (_| | | | | (_) | |_| | | | | (_| |  ___) | |_| | | | | | | | | | | | (_| | |  | |_| |", 'yellow', attrs=["bold"]))
    print(colored(" |____/|_|\___/ \___/ \__,_|_| |_|\___/ \__,_|_| |_|\__,_| |____/ \__,_|_| |_| |_|_| |_| |_|\__,_|_|   \__, |", 'yellow', attrs=["bold"]))
    print(colored("                                                                                                       |___/ ", 'yellow', attrs=["bold"]))
    print()
    print(colored("Developed by @JacobEbben on Github", 'cyan', attrs=["bold"]))
    print()

def open_json_from_zip(filename):
    zip_content = []
    with zipfile.ZipFile(filename, 'r') as bloodhound_zip:
        for json_filename in bloodhound_zip.namelist():
            data_raw = bloodhound_zip.open(json_filename, mode='r').read()
            data = json.loads(data_raw.decode('utf-8-sig'))
            zip_content.append(data)
    return zip_content

def main():
    print_header()

    bloodhound_data = BloodHoundData()

    bloodhound_files = open_json_from_zip(sys.argv[1])

    for data_type_file in bloodhound_files:
        bloodhound_data.import_ingestor_file(data_type_file)
    
    print_domain_info(bloodhound_data)
    print_user_info(bloodhound_data)
    print_group_info(bloodhound_data)
    print_computer_info(bloodhound_data)


if __name__ == '__main__':
    main()