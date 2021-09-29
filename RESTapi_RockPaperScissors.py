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

score = {'computer': 0,
         'user': 0}     # starting score


# =====================================================================================================================
# =================================================== FUNCTIONS =======================================================
def get_random_response(responses):
    """ this function generates a random response for the computer, between options in the possible_responses list """
    random_response = random.sample(responses, 1)      # chooses one item from the list 'responses'
    return random_response[0]       # get string out of list


def process_winner(user_pick, computer_pick):
    """ this function determines which player wins according to the winner_dict """
    if user_pick == winner_dict[computer_pick]:     # if the user_pick is the value of the computer_pick key
        return won_response     # value beats key, user wins
    elif computer_pick == winner_dict[user_pick]:   # if the computer_pick is the value of the user_pick key
        return lost_response    # value beats key, computer wins
    elif computer_pick == user_pick:    # if the two players' choices match
        return draw_response    # give a draw
    else:   # if the user's response is not one of the options required
        return other_response   # give unknown


def game_play(request_json):
    """ this function gets the user's input, generates a random choice for the computer's play, and gives a winner"""
    user_choice = request_json["hand"].upper()     # gets the value of the user's input (string, uppercase to fit dict)
    computer_choice = get_random_response(responses=possible_responses)     # picks random choice for computer
    score_indicator = process_winner(user_pick=user_choice, computer_pick=computer_choice)  # determines a winner
    response_payload["result"] = score_indicator    # gives the string of the result, ie 'win', 'lose', etc
    response_payload["computer_hand"] = computer_choice     # gives string of what the computer chose
    return response_payload


def determine_score(game_result_dict):
    """ updates the score dictionary to reflect the current score. If a draw, both players get a point """
    if game_result_dict['result'] == won_response:    # if the result is "WON", user gets a point
        score['user'] = (score['user'] + 1)
    if game_result_dict['result'] == lost_response:    # if the result is "LOST", computer gets a point
        score['computer'] = (score['computer'] + 1)
    if game_result_dict['result'] == draw_response:    # if the result is "DRAW", both players get a point
        score['user'] = (score['user'] + 1)
        score['computer'] = (score['computer'] + 1)


def main():
    """ establishes and serves the server until stopped """
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
        if self.path == '/':
            self.set_headers(content_type='text/html')
            with open('README.md', 'r') as markdown_file:
                read_me = markdown_file.read()   # read in the file; returns the specified number of bytes from the file
                markdown_read_me = markdown.markdown(read_me)   # converts the markdown text into HTML equivalent
                self.wfile.write(markdown_read_me.encode())     # encodes HTML into set of bytes

        if self.path == '/score':
            """ the /score endpoint is used to display the score """
            self.set_headers(content_type='application/json')
            response = json.dumps(score)    # parses python dict type into json string
            print(f'Current score: \n User: {score["user"]}, Computer: {score["computer"]} ')    # print in console
            self.wfile.write(response.encode())     # encodes json string to set of bytes

    def do_POST(self):
        """ the POST method is used to send data to a server to create/update a resource """
        if self.path == '/game':
            """ the /game endpoint is used to actually play the game """
            self.set_headers(content_type='application/json')
            request_payload = int(self.headers.get('content-length', 0))    # content-length header specifies number of bytes in HTTP POST
            request_payload = self.rfile.read(request_payload)      # specify number of bytes read, must be int type
            request_payload = json.loads(request_payload.decode('utf-8'))   # json.loads parses string to python dict
            response = game_play(request_json=request_payload)      # uses dict as input, returns dict
            determine_score(game_result_dict=response)      # retrieves and updates the score
            print(f"Result: you {response['result']}! \n {score} ")
            response = json.dumps(response)     # parses python dict type into json string
            self.wfile.write(response.encode())     # encodes json string to set of bytes


# =====================================================================================================================
# ==================================================== RUN CODE =======================================================
if __name__ == "__main__":      # if this python file is being run directly, not an imported module
    main()
