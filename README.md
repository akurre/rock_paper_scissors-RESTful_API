# Rock Paper Scissors RESTful API
A turn-based game of "Rock, Paper, Scissors" that takes user input via REST API, plays for the computer, and then 
declares the winner. Computer moves are chosen randomly.

To access the API, run the python script 'RESTapi_RockPaperScissors.py' to initialize then use curl via terminal, or 
use the browser. The port is specified under the Global Variables section in the python script.

This project was created on Mac OS.

## Rules of the Game

The game "Rock, Paper, Scissors" is played by two players, where both players choose between Rock, Paper, or Scissors.
The winner is determined by the following rules:

* Paper beats rock, 

* Rock beats scissors,

* Scissors beats paper.

* Two of the same answer results in a draw.

In person, each player's choice is supposed to be made simultaneously so as to avoid cheating, but this API returns a
random response once it receives a request, keeping the game fair despite the lack of simultaneous choosing.

## API Usage

### General Info

All responses that the API will give, provided correct user input, will have the form
```json
{
    "result": "STATUS", 
    "computer_hand": "OPPONENT"
}
``` 

After the user has sent the API their choice of either ROCK, PAPER, or SCISSORS, the computer will randomly generate 
its own choice. This choice, "OPPONENT", or the value of key "computer_hand", will be one of the following: ROCK, PAPER, 
SCISSORS. "STATUS, or the value of key "result", is determined according to the rules of the game, listed above.

If the user enters anything besides these three options, the API will give the response:

```json
{
    "result": "UNKNOWN"
}
``` 

### How to Obtain README.md in Browser / Terminal

**Method/Endpoint**

`GET /`


**Command Example**

```curl localhost:4567/``` or
```curl localhost:4567``` for terminal, 

or

`localhost:4567` or `localhost:4567/` in browser


**Response**

- '200 OK' on success
- will print this readme, markdown compatible on browser


**Header Content Type**

'text/html'


### How to Begin to Play

**Method/Endpoint**

`POST /game`


**Command Example**

```curl -X POST localhost:4567/game -d '{"hand": "PAPER"}'```


**Arguments** 

- '"hand":string' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; string = 'ROCK', 'PAPER', or 'SCISSORS'


**Response**

- '200 OK' on success
- example response payload below:

```json
{
    "result": "WON", 
    "computer_hand": "ROCK"
}
```

**Header Content Type**

'application/json'



### To See Your Score

**Method/Endpoint**

`GET /score`


**Command Example**

```curl localhost:4567/score```


**Arguments** 

- '"PLAYER":int'  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  int = number of points for that player


**Response**

- `200 OK` on success
- example response payload below:

```json
{
    "User": 10, 
    "Computer": 9 
}
```

**Header Content Type**

'application/json'
