session_store = {}

def set_user_session(session_id, username):
    session_store[session_id] = username

def get_user_from_session(session_id):
    return session_store.get(session_id)

def clear_session(session_id):
    if session_id in session_store:
        del session_store[session_id]
