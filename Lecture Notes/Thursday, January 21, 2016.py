"""
Protocol
-------
Polling server: already written
Polling client: We'll write this together

Polling Protocol
----------------
" request/reply protocol" : A protocol where clients make requests and servers send replies as a result.


* Client connects to Polling Server
* Server accepts the connections
* Client sends "POLLING_HELLO username"
                 - If the server recognizes the username, server responds with "Hello"
                 - If not, server responds with "No_USER username"
* Once the user is logged in, then there are five(?) requests that can be sent

(1) Client sends "POLLING_QUESTIONS"
    Server responds with
    "QUESTION_COUNT number_of_questions
    "QUESTION question_id question_text"

(2) Client sends "POLLING_CHOICES question_id:

"""

