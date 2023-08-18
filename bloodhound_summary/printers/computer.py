from bloodhound_summary.printers.commons import print_topic, label_if_disabled, highlight_if_enabled, highlight

from bloodhound_summary.parsers.computer import get_computers_with_unconstrained_delegation, get_computers_with_constrained_delegation

KNOWN_DEFAULT_HIGH_PRIVILEGE_RIDS = ["500","512", "519", "526", "527", "544","548"]

def print_computer_info(bloodhound_data):
    _print_computers(bloodhound_data)
    _print_computer_aces(bloodhound_data, KNOWN_DEFAULT_HIGH_PRIVILEGE_RIDS)
    _print_computers_with_unconstrained_delegation(bloodhound_data)
    _print_computers_with_constrained_delegation(bloodhound_data)
    #_print_local_admins_of_computers(bloodhound_data)
    #_print_psremote_users_of_computers(bloodhound_data)
    #_print_remotedesktop_users_of_computers(bloodhound_data)
    #_print_dcom_users_of_computers(bloodhound_data)
    #_print_privileged_sessions_computers(bloodhound_data)
    #_print_registry_sessions_computers(bloodhound_data)
    #_print_computer_spns(bloodhound_data)

def _print_computers(bloodhound_data):
    content = []
    for computer in bloodhound_data.computers:
        computer_name = computer.name
        computer_name = label_if_disabled(computer_name, computer)
        content.append([computer.name, computer.operatingsystem, computer.lastlogon, computer.whencreated])
    table_title = "COMPUTERS"
    table_info = "User accounts and basic information."
    table_headers = ["Computer Name", "Operating System", "Last logon", "Creation date"]
    print_topic(table_title, table_info, table_headers, content)

def _print_computer_aces(bloodhound_data, filter_rids):
    content = []
    for computer in bloodhound_data.computers:
        for ace in computer.Aces:
            subject = bloodhound_data.get_object_by_sid(ace["PrincipalSID"])
            if subject:
                subject_name = highlight_if_enabled(subject.name, subject)
                subject_name = label_if_disabled(subject_name, subject)
                object_name = highlight_if_enabled(computer.name, computer)
                object_name = label_if_disabled(object_name, computer)
                if subject.ObjectIdentifier.split('-')[-1] not in filter_rids:
                    content.append([subject_name, ace["PrincipalType"], ace["RightName"], object_name])
    table_title = "INTERESTING COMPUTER ACCESS CONTROL ENTRIES"
    table_info = "Access control information that defines how users and groups can interact with the other computer accounts. Filtered to remove default privileged groups."
    table_headers = ["Subject", "Type", "Right", "Privileges on"]
    print_topic(table_title, table_info, table_headers, content)

def _print_computers_with_unconstrained_delegation(bloodhound_data):
    content = []
    for computer in get_computers_with_unconstrained_delegation(bloodhound_data):
        computer_name = highlight(computer.name)
        computer_name = label_if_disabled(computer_name, computer)     
        content.append([computer_name])
    table_title = "UNCONSTRAINED DELEGATION (Computers)"
    table_info = "Computers that hold onto Kerberos Ticket Granting Tickets (TGT) for use in Kerberos Delegation."
    table_headers = ["Name"]
    print_topic(table_title, table_info, table_headers, content)

def _print_computers_with_constrained_delegation(bloodhound_data):
    content = []
    for computer in get_computers_with_constrained_delegation(bloodhound_data):
        computer_name = highlight(computer.name)
        computer_name = label_if_disabled(computer_name, computer)     
        allowed_to_delegate = []
        for sid in computer.AllowedToDelegate:
            object = bloodhound_data.get_object_by_sid(sid)
            if object:
                object_name = object.name
                object_name = label_if_disabled(object_name, object) 
                allowed_to_delegate.append(object_name)
        content.append([computer_name, allowed_to_delegate])
    table_title = "CONSTRAINED DELEGATION (Computers)"
    table_info = "Computers that can authenticate users on behalf of a specific service account."
    table_headers = ["Name", "Trusted to auth for"]
    print_topic(table_title, table_info, table_headers, content)