from bloodhound_summary.printers.commons import print_topic, label_if_disabled, label_if_admincount, highlight, highlight_if_enabled, highlight_if_enabled_admincount

from bloodhound_summary.parsers.user import get_users_with_descriptions, get_users_with_stored_passwords, get_users_with_passwordnotreqd, get_users_with_spns, \
                                            get_users_with_dontreqpreauth, get_users_with_unconstrained_delegation, get_users_with_constrained_delegation

KNOWN_DEFAULT_USER_RIDS_WITH_DESCRIPTIONS = ["500", "501", "502"]
KNOWN_DEFAULT_HIGH_PRIVILEGE_RIDS = ["512", "519", "526", "527", "544","548"]

def print_user_info(bloodhound_data):
    _print_users(bloodhound_data)
    _print_user_descriptions(bloodhound_data, KNOWN_DEFAULT_USER_RIDS_WITH_DESCRIPTIONS)
    _print_user_passwords(bloodhound_data)
    _print_user_aces(bloodhound_data, KNOWN_DEFAULT_HIGH_PRIVILEGE_RIDS)
    _print_passwordnotreqd_users(bloodhound_data)
    _print_users_with_spns(bloodhound_data)
    _print_users_with_noreqpreauth(bloodhound_data)
    _print_users_with_unconstrained_delegation(bloodhound_data)
    _print_users_with_constrained_delegation(bloodhound_data)
    

def _print_users(bloodhound_data):
    content = []
    users = bloodhound_data.users
    users = sorted(users, key=lambda user: (int(not user.admincount), int(not user.enabled), int(user.ObjectIdentifier.split('-')[-1])))
    for user in users:
        user_name = user.name
        user_name = highlight_if_enabled_admincount(user_name, user)
        user_name = label_if_admincount(user_name, user)
        user_name = label_if_disabled(user_name, user)
        content.append([user_name, user.displayname, user.title, user.lastlogon, user.pwdlastset, user.whencreated])
    table_title = "USERS"
    table_info = "User accounts and basic information."
    table_headers = ["Name", "Display Name", "Title", "Last logon", "Password last set", "Creation date"]
    print_topic(table_title, table_info, table_headers, content)

def _print_user_descriptions(bloodhound_data, filter_rids):
    content = []
    for user in get_users_with_descriptions(bloodhound_data):
        user_name = highlight_if_enabled(user.name, user)
        user_name = label_if_admincount(user_name, user)
        user_name = label_if_disabled(user_name, user)
        description = user.description
        if len(description) > 100:
            description = description[0:100] + "..."
        description = highlight(description)
        if user.ObjectIdentifier.split('-')[-1] not in filter_rids:
            content.append([user_name, description])
    table_title = "USER DESCRIPTIONS"
    table_info = "User accounts with filled in description attributes."
    table_headers = ["Name", "Description"]
    print_topic(table_title, table_info, table_headers, content)

def _print_user_passwords(bloodhound_data):
    content = []
    for user in get_users_with_stored_passwords(bloodhound_data):
        user_name = highlight(user.name)
        user_name = label_if_admincount(user_name, user)
        user_name = label_if_disabled(user_name, user)
        content.append([user_name, user.userpassword, user.unixpassword, user.unicodepassword, user.sfupassword])
    table_title = "USER PASSWORDS"
    table_info = "User accounts that might have passwords stored in user properties. Note that this can only parse through the fields that the bloodhound ingestor scans for. Manual parsing of LDAP is required for certainty."
    table_headers = ["Name", "userpassword", "unixpassword", "unicodepassword", "sfupassword"]
    print_topic(table_title, table_info, table_headers, content)

def _print_user_aces(bloodhound_data, filter_rids):
    content = []
    for user in bloodhound_data.users:
        for ace in user.Aces:
            subject = bloodhound_data.get_object_by_sid(ace["PrincipalSID"])
            if subject:
                subject_name = highlight_if_enabled(subject.name, subject)
                subject_name = label_if_admincount(subject_name, subject)
                subject_name = label_if_disabled(subject_name, subject)
                object_name = highlight_if_enabled(user.name, user)
                object_name = label_if_admincount(object_name, user)
                object_name = label_if_disabled(object_name, user)
                if ace["PrincipalSID"].split('-')[-1] not in filter_rids:
                    content.append([subject_name, ace["PrincipalType"], ace["RightName"], object_name])
    table_title = "INTERESTING USER ACCESS CONTROL ENTRIES"
    table_info = "Access control information that defines how users and groups can interact with the other user accounts. Filtered to remove default privileged groups."
    table_headers = ["Subject", "Type", "Right", "Privileges on"]
    print_topic(table_title, table_info, table_headers, content)

def _print_passwordnotreqd_users(bloodhound_data):
    content = []
    for user in get_users_with_passwordnotreqd(bloodhound_data):
        user_name = highlight_if_enabled(user.name, user)
        user_name = label_if_admincount(user_name, user)
        user_name = label_if_disabled(user_name, user)         
        content.append([user_name])
    table_title = "USERS WITH NO PASSWORD REQUIRED"
    table_info = "Accounts that override the password policy of the domain. These accounts could have passwords that violate the password policy, or even blank passwords."
    table_headers = ["Name"]
    print_topic(table_title, table_info, table_headers, content)

def _print_users_with_spns(bloodhound_data):
    content = []
    for user in get_users_with_spns(bloodhound_data):
        user_name = highlight_if_enabled(user.name, user)
        user_name = label_if_admincount(user_name, user)
        user_name = label_if_disabled(user_name, user)     
        content.append([user_name, user.serviceprincipalnames])
    table_title = "SERVICE ACCOUNTS (Kerberoast)"
    table_info = "Accounts with registered Service Principal Names (SPN). Allowing an attacker to request a Service Ticket (ST). An attacker can attempt to crack the service account password from this ST."
    table_headers = ["Name","Service Principal Names"]
    print_topic(table_title, table_info, table_headers, content)

def _print_users_with_noreqpreauth(bloodhound_data):
    content = []
    for user in get_users_with_dontreqpreauth(bloodhound_data):
        user_name = highlight(user.name)
        user_name = label_if_admincount(user_name, user)
        user_name = label_if_disabled(user_name, user)     
        content.append([user_name])
    table_title = "NO PREAUTHENTICATION REQUIRED (ASREProast)"
    table_info = "Accounts that can request an encrypted Ticket Granting Ticket (TGT) without pre-authentication. An attacker can attempt to crack the account password from this TGT."
    table_headers = ["Name"]
    print_topic(table_title, table_info, table_headers, content)

def _print_users_with_unconstrained_delegation(bloodhound_data):
    content = []
    for user in get_users_with_unconstrained_delegation(bloodhound_data):
        user_name = highlight(user.name)
        user_name = label_if_admincount(user_name, user)
        user_name = label_if_disabled(user_name, user)     
        content.append([user_name])
    table_title = "UNCONSTRAINED DELEGATION (Users)"
    table_info = "Accounts that can authenticate users on behalf of any service account."
    table_headers = ["Name"]
    print_topic(table_title, table_info, table_headers, content)

def _print_users_with_constrained_delegation(bloodhound_data):
    content = []
    for user in get_users_with_constrained_delegation(bloodhound_data):
        user_name = highlight(user.name)
        user_name = label_if_admincount(user_name, user)
        user_name = label_if_disabled(user_name, user)     
        allowed_to_delegate = []
        for sid in user.AllowedToDelegate:
            object = bloodhound_data.get_object_by_sid(sid)
            if object:
                object_name = object.name
                object_name = label_if_admincount(object_name, object)
                object_name = label_if_disabled(object_name, object) 
                allowed_to_delegate.append(object_name)
        content.append([user_name, allowed_to_delegate])
    table_title = "CONSTRAINED DELEGATION (Users)"
    table_info = "Accounts that can authenticate users on behalf of a specific service account."
    table_headers = ["Name", "Trusted to auth for"]
    print_topic(table_title, table_info, table_headers, content)