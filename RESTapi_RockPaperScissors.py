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


# =====================================================================================================================
# ================================================= USER CONTROLS =====================================================
control = True


# =====================================================================================================================
# ================================================ GLOBAL VARIABLES ===================================================
port_chosen = 8000


# =====================================================================================================================
# =================================================== FUNCTIONS =======================================================
def main():
    do = 'something'
    return do


# =====================================================================================================================
# ==================================================== CLASSES ========================================================



# =====================================================================================================================
# ==================================================== RUN CODE =======================================================
if __name__ == "__main__":
    main()
