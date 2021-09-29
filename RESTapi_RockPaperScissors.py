"""
======PROJECT======
Rock-Paper-Scissors Web Version

======DESCRIPTION======
Design a turn-based game of rock-paper-scissors that takes user input via REST API, plays for the computer, and then
declares the winner. Computer moves are chosen randomly.

======VERSION CHANGES======
This is the first version.

======BUGS / ISSUES TO RESOLVE======
TODO:

======INPUT DATA FORM======
Request Payload Format:
    {'hand': '...'}

======OUTPUT DATA FORM======
Response Payload Format:
    {'result': 'LOST', 'computer_hand': '...'}

======EXAMPLE======
curl -X POST localhost:4567/game -d '{"hand": "PAPER"}'
{"result": "WON", "computer_hand": "ROCK"}

curl -X POST localhost:4567/game -d '{"hand": "PAPER"}'
{"result": "DRAW", "computer_hand": "PAPER"}

curl -X POST localhost:4567/game -d '{"hand": "PAPER"}'
{"result": "LOST", "computer_hand": "SCISSORS"}

curl -X POST localhost:4567/game -d '{"hand": "KICK"}'
{"result": "UNKNOWN"}

======CODE PREREQUISITES======
python3

======OTHER NOTES======
Create public/private github repository
Push all code to master branch
Documentation

======AUTHOR CONTACT & DATE======
Ashlen Kurre - a.l.kurre@gmail.com
28 September 2021
"""


# =====================================================================================================================
# =============================================== IMPORT STATEMENTS====================================================
from http.server import HTTPServer, BaseHTTPRequestHandler
import random
import markdown
import json


# =====================================================================================================================
# ================================================ GLOBAL VARIABLES ===================================================
PORT = 4567     # choice of port

possible_responses = ['ROCK', 'PAPER', 'SCISSORS']
won_response = "WON"
lost_response = "LOST"
draw_response = "DRAW"
other_response = "UNKNOWN"
response_payload = {"result": "",
                    "computer_hand": ""}      # to be populated later
winner_dict = {'SCISSORS': 'ROCK',
               'PAPER': 'SCISSORS',
               'ROCK': 'PAPER'}     # in this dict, the value beats the key, meaning whoever chose the value wins


# =====================================================================================================================
# =================================================== FUNCTIONS =======================================================
def get_random_response(responses):
    random_response = random.sample(responses, 1)      # chooses one item from the list 'responses'
    return random_response[0]       # get string out of list


def process_winner(user_pick, computer_pick):
    if user_pick == winner_dict[computer_pick]:     # if the user_pick is the value of the computer_pick key
        return won_response     # value beats key, user wins
    elif computer_pick == winner_dict[user_pick]:
        return lost_response
    elif computer_pick == user_pick:
        return draw_response
    else:
        return other_response


def game_play(request_json):
    user_choice = request_json["hand"]
    computer_choice = get_random_response(responses=possible_responses)
    score_indicator = process_winner(user_pick=user_choice, computer_pick=computer_choice)
    response_payload["result"] = score_indicator
    response_payload["computer_hand"] = computer_choice
    return response_payload


def main():
    server = HTTPServer(('', PORT), myRequestHandler)  # first thing is instance of the server class (first is
    # tuple host name, blank because we're serving on local host. Second is port number). Then it is the request handler

    print(f'Server running on port {PORT}')
    server.serve_forever()  # this method starts a server and runs until it is stopped with ctrl+c in terminal


# =====================================================================================================================
# ==================================================== CLASSES ========================================================
class myRequestHandler(BaseHTTPRequestHandler):  # takes the web address path and displays it in the browser

    def set_headers(self, content_type):
        """ headers represent the metadata associated with the API request and response """
        self.send_response(200)     # send back a response (200=success)
        self.send_header('Content-type', content_type)      # details content type which the web page will display
        self.end_headers()      # must close headers once all are listed

    def do_GET(self):
        """ the GET method is used to request data from a specified resource """
        self.set_headers(content_type='text/html')
        with open('README.md', 'r') as markdown_file:
            read_me = markdown_file.read()      # read in the file; returns the specified number of bytes from the file
            markdown_read_me = markdown.markdown(read_me)   # converts the markdown text into HTML equivalent
            self.wfile.write(markdown_read_me.encode())     #

    def do_POST(self):
        """ the POST method is used to send data to a server to create/update a resource """
        if self.path == '/game':
            """ the /game endpoint is used to actually play the game """
            self.set_headers(content_type='application/json')
            request_payload = int(self.headers.get('content-length', 0))    # content-length header specifies number of bytes in HTTP POST
            request_payload = self.rfile.read(request_payload)      # specify number of bytes read, must be int type
            request_payload = json.loads(request_payload.decode('utf-8'))   # json.loads parses string to python dict
            response = game_play(request_json=request_payload)      # uses dict as input, returns dict
            response = json.dumps(response)     # parses python dict type into json string
            self.wfile.write(response.encode())     # encodes json string to set of bytes

        if self.path == '/score':
            """ the /score endpoint is used to display the score """
            self.set_headers(content_type='text/html')
            response = ''
            self.wfile.write(response.encode())


# =====================================================================================================================
# ==================================================== RUN CODE =======================================================
if __name__ == "__main__":      # if this python file is being run directly, not an imported module
    main()
