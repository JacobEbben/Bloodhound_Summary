def get_highvalue_groups(bloodhound_data):
    found_groups = []
    for group in bloodhound_data.groups:
        if group.highvalue:
            found_groups.append(group)
    return found_groups

def get_interesting_groups(bloodhound_data, filter_rids):
    found_groups = []
    for user in bloodhound_data.users:
        for ace in user.Aces:
            principal_rid = ace["PrincipalSID"].split('-')[-1]
            if ace["PrincipalType"] == "Group" and principal_rid not in filter_rids:
                group = bloodhound_data.get_object_by_sid(ace["PrincipalSID"])
                if group:
                    found_groups.append(group)
                    found_groups.extend(get_group_members_inside_group(bloodhound_data, group, filter_rids))
    for computer in bloodhound_data.computers:
        for ace in computer.Aces:
            principal_rid = ace["PrincipalSID"].split('-')[-1]
            if ace["PrincipalType"] == "Group" and principal_rid not in filter_rids:
                group = bloodhound_data.get_object_by_sid(ace["PrincipalSID"])
                if group:
                    found_groups.append(group)
                    found_groups.extend(get_group_members_inside_group(bloodhound_data, group, filter_rids))
    for domain in bloodhound_data.domains:
        for ace in domain.Aces:
            principal_rid = ace["PrincipalSID"].split('-')[-1]
            if ace["PrincipalType"] == "Group" and principal_rid not in filter_rids:
                group = bloodhound_data.get_object_by_sid(ace["PrincipalSID"])
                if group:
                    found_groups.append(group)
                    found_groups.extend(get_group_members_inside_group(bloodhound_data, group, filter_rids))
    return found_groups

def get_group_members_inside_group(bloodhound_data, group, filter_rids):
    found_groups = []
    for member in group.Members:
        if member["ObjectType"] == "Group" and member["ObjectIdentifier"].split('-')[-1] not in filter_rids:
            group = bloodhound_data.SID_MAP[member["ObjectIdentifier"]]
            found_groups.append(group)
            get_group_members_inside_group(bloodhound_data, group, filter_rids)
    return found_groups
            

def get_group_descriptions(bloodhound_data):
    found_groups = []
    for group in bloodhound_data.groups:
        if group.description:
            found_groups.append(group)
    return found_groups
