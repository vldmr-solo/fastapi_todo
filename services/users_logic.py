def get_user(users, user_id: int):
    for user in users:
        if user.get("id") == user_id:
            return user
    
    return None