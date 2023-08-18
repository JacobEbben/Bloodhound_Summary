from bloodhound_summary.printers.commons import print_topic


def print_domain_info(bloodhound_data):
    _print_domains(bloodhound_data)
    _print_domain_aces(bloodhound_data)
    

def _print_domains(bloodhound_data):
    content = []
    for domain in bloodhound_data.domains:
        content.append([domain.name, domain.domainsid, domain.description, domain.functionallevel, domain.whencreated])
    table_title = "DOMAINS"
    table_info = "Domains and basic information"
    table_headers = ["Name", "Domain SID", "Description", "Functional Level", "Creation Date"]
    print_topic(table_title, table_info, table_headers, content)


def _print_domain_aces(bloodhound_data):
    for domain in bloodhound_data.domains:
        content = []
        name = domain.name
        table_title = f"DOMAIN ACCESS CONTROL ENTRIES: {name}"
        table_info = "Access control information that define how privileged users and groups can interact with the domain."
        for ace in domain.Aces:
            PrincipalName = bloodhound_data.get_object_by_sid(ace["PrincipalSID"]).name
            content.append([ace["RightName"], PrincipalName, ace["PrincipalType"]])
        table_headers = ["Right", "Name", "Type"]
        print_topic(table_title, table_info, table_headers, content)