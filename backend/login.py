from backend.models import User
from backend.session import session


def login_user(pseudo, passwd):
    user = session.query(User).filter_by(personal_id=pseudo).first()
    if user == None or user.password != passwd:
        return None
    return user
