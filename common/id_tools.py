import random

UUID_PREFIX_CHAT = 'chat'

UUID_MAC_LENGTH = 25

def get_uuid(prefix, width=UUID_MAC_LENGTH):
    count = width - len(prefix) - 1
    uuid = prefix + '-'
    while count > 0:
        uuid += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012356789')
        count = count - 1
    return uuid
def get_chat_uuid():
    return get_uuid(prefix=UUID_PREFIX_CHAT)