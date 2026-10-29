USERS = {}

def add_user(username, password_hash, role):
    USERS[username] = {"password_hash": password_hash, "role": role}

def get_user(username):
    return USERS.get(username)
