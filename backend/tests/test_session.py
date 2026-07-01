from pprint import pprint

from backend.services.session_manager import SessionManager

session = SessionManager()

session.set_query("I ate milk")

print()

pprint(session.get_state())

session.reset()

print()

pprint(session.get_state())