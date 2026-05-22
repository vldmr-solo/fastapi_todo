from data import users

def find_user(user_id: int):
    for user in users:
        if user.get("id") == user_id:
            return user
    
    return None