from backend.models import Request
from backend.session import session


def get_requests():
    requests = session.query(Request).join(Request.supplier).all()
    return requests
