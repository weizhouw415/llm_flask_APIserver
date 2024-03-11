import random

UUID_PREFIX_HOST = 'host'
UUID_PREFIX_APP = 'app'

UUID_MAC_LENGTH = 25

def get_uuid(prefix, width=UUID_MAC_LENGTH):
    count = width - len(prefix) - 1
    uuid = prefix + '-'
    while count > 0:
        uuid += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012356789')
        count = count - 1
    return uuid

def get_host_uuid():
    return get_uuid(UUID_PREFIX_HOST)

def get_app_uuid():
    return get_uuid(UUID_PREFIX_APP)