from pprint import pprint

from backend.graph.graph_builder import graph

from backend.services.session_manager import SessionManager

session = SessionManager()

while True:

    query = input("\nYou : ")

    if query.lower() == "exit":
        break

    session.set_query(query)

    result = graph.invoke(

        session.get_state()

    )

    session.update_state(result)

    print()

    pprint(

        result["final_response"]

    )