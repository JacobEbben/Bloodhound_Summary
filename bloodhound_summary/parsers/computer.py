def get_computers_with_unconstrained_delegation(bloodhound_data):
    found_computers = []
    for computer in bloodhound_data.computers:
        if computer.unconstraineddelegation:
            found_computers.append(computer)
    return found_computers

def get_computers_with_constrained_delegation(bloodhound_data):
    found_computers = []
    for computer in bloodhound_data.computers:
        if computer.trustedtoauth:
            found_computers.append(computer)
    return found_computers