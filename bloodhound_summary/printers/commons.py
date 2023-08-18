from tabulate import tabulate
from termcolor import colored

from bloodhound_summary.ad.models.group import BloodHoundGroup
from bloodhound_summary.ad.models.computer import BloodHoundComputer

MAX_TABLE_SIZE = 1000

def label_if_disabled(message, object):
    if isinstance(object, BloodHoundGroup):
        return message
    if not object.enabled:
        return message + colored(" (disabled)", 'red')
    return message

def label_if_admincount(message, object):
    if isinstance(object, BloodHoundGroup) or isinstance(object, BloodHoundComputer):
        return message
    if object.admincount:
        return message + colored(" (admincount)", 'cyan')
    return message

def highlight(message):
    return colored(message, 'yellow')

def highlight_if_enabled_admincount(message, object):
    if isinstance(object, BloodHoundGroup) or isinstance(object, BloodHoundComputer):
        return highlight(message)
    if object.enabled and object.admincount:
        return highlight(message)
    return message

def highlight_if_enabled(message, object):
    if isinstance(object, BloodHoundGroup):
        return highlight(message)
    if object.enabled:
        return highlight(message)
    return message

def print_topic(header_text, info_text, table_headers, content):
    _print_topic_header(header_text)
    _print_info(info_text)
    if len(content) != 0:
        _print_table(table_headers, content)
    else:
        print("Nothing found ... \n")

def _print_topic_header(header_text):
    topic_header = colored(header_text, "green", attrs=["bold"])
    print(topic_header)

def _print_info(info_text):
    info_text = colored(info_text, "blue", attrs=["dark"])
    print(info_text)

def _print_table(headers, content):
    if len(content) > MAX_TABLE_SIZE:
        print(colored(f"Content exceeds maximum size! Truncated to only {MAX_TABLE_SIZE} records.", "red"))
        content = content[:MAX_TABLE_SIZE]
    table = tabulate(content, headers=headers, numalign="left")
    print(table + "\n")
