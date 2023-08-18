from bloodhound_summary.printers.commons import print_topic, label_if_admincount, label_if_disabled, highlight

from bloodhound_summary.parsers.group import get_highvalue_groups, get_interesting_groups, get_group_descriptions


KNOWN_DEFAULT_HIGH_PRIVILEGE_RIDS = ["500","512", "519", "526", "527", "544","548"]

KNOWN_DEFAULT_GROUP_RIDS_WITH_DESCRIPTIONS = ['498', '512', '513', '514', '515', '516', '517', '518', '519', '520', '521', '522', '525', \
                                      '526', '527', '544', '545', '546', '548', '549', '550', '551', '552', '553', '554', '555', \
                                      '556', '557', '558', '559', '560', '561', '562', '568', '569', '571', '572', '573', '574', \
                                      '575', '576', '577', '578', '579', '580', '582', '1101', '1102', '1117', '1118', '1119']


def print_group_info(bloodhound_data):
    _print_highvalue_group_members(bloodhound_data, KNOWN_DEFAULT_HIGH_PRIVILEGE_RIDS)
    _print_interesting_group_members(bloodhound_data, KNOWN_DEFAULT_HIGH_PRIVILEGE_RIDS)
    _print_group_descriptions(bloodhound_data, KNOWN_DEFAULT_GROUP_RIDS_WITH_DESCRIPTIONS)
    _print_groups(bloodhound_data)

def _print_groups(bloodhound_data):
    content = []
    for group in bloodhound_data.groups:
        content.append([group.name, group.whencreated])

    table_title = "GROUPS"
    table_info = "All collected groups"
    table_headers = ["Group Name", "Creation Date"]
    print_topic(table_title, table_info, table_headers, content)

def _print_highvalue_group_members(bloodhound_data, filter_rids):
    content = []
    for group in get_highvalue_groups(bloodhound_data):
        group_name = group.name
        for member in group.Members:
            object = bloodhound_data.get_object_by_sid(member["ObjectIdentifier"])
            if object:
                member_name = object.name
                if object.ObjectIdentifier.split('-')[-1] not in filter_rids:
                    member_name = highlight(member_name)
                member_name = label_if_admincount(member_name, object)
                member_name = label_if_disabled(member_name, object)    
                content.append([group_name, member["ObjectType"], member_name])
    table_title = "HIGH VALUE GROUP MEMBERSHIP"
    table_info = "Groups marked as high value by BloodHound and their membership."
    table_headers = ["Group Name", "Member Type", "Member Name"]
    print_topic(table_title, table_info, table_headers, content)

def _print_interesting_group_members(bloodhound_data, filter_rids):
    content = []
    for group in get_interesting_groups(bloodhound_data, filter_rids):
        group_name = highlight(group.name)
        for member in group.Members:
            user = bloodhound_data.get_object_by_sid(member["ObjectIdentifier"])
            if user:
                member_name = user.name
                if user.ObjectIdentifier.split('-')[-1] not in filter_rids:
                    member_name = highlight(member_name)
                member_name = label_if_admincount(member_name, user)
                member_name = label_if_disabled(member_name, user)    
                content.append([group_name, member["ObjectType"], member_name])
    table_title = "INTERESTING GROUP MEMBERSHIP"
    table_info = "Groups that Bloodhound_Summary detected as interesting and their membership."
    table_headers = ["Group Name", "Member Type", "Member Name"]
    print_topic(table_title, table_info, table_headers, content)

def _print_group_descriptions(bloodhound_data, filter_rids):
    content = []
    for group in get_group_descriptions(bloodhound_data):
        if group.ObjectIdentifier.split('-')[-1] not in filter_rids:
            name = highlight(group.name)
            description = group.description
            if len(description) > 100:
                description = description[0:100] + "..."
            description = highlight(description)
            content.append([name, description])
    table_title = "GROUP DESCRIPTIONS"
    table_info = "Groups with filled in description attributes."
    table_headers = ["Group Name", "Description"]
    print_topic(table_title, table_info, table_headers, content)