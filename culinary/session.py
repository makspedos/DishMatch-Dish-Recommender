from flask import session
from uuid import uuid4

def initialize_session():
    if 'session_id' not in session:
        session['session_id'] = str(uuid4())