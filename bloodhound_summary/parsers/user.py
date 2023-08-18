def get_users_with_descriptions(bloodhound_data):
    found_users = []
    for user in bloodhound_data.users:
        if user.description:
            found_users.append(user)
    return found_users

def get_users_with_stored_passwords(bloodhound_data):
    found_users = []
    for user in bloodhound_data.users:
        if user.userpassword or user.unixpassword or user.unicodepassword or user.sfupassword:
            found_users.append(user)
    return found_users

def get_users_with_passwordnotreqd(bloodhound_data):
    found_users = []
    for user in bloodhound_data.users:
        if user.passwordnotreqd:
            found_users.append(user)
    return found_users

def get_users_with_spns(bloodhound_data):
    found_users = []
    for user in bloodhound_data.users:
        if user.hasspn:
            found_users.append(user)
    return found_users

def get_users_with_dontreqpreauth(bloodhound_data):
    found_users = []
    for user in bloodhound_data.users:
        if user.dontreqpreauth:
            found_users.append(user)
    return found_users

def get_users_with_unconstrained_delegation(bloodhound_data):
    found_users = []
    for user in bloodhound_data.users:
        if user.unconstraineddelegation:
            found_users.append(user)
    return found_users

def get_users_with_constrained_delegation(bloodhound_data):
    found_users = []
    for user in bloodhound_data.users:
        if user.trustedtoauth:
            found_users.append(user)
    return found_users