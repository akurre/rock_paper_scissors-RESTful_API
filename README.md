# Rock Paper Scissors RESTful API
A turn-based game of "Rock, Paper, Scissors" that takes user input via REST API, plays for the computer, and then declares the winner. Computer moves are chosen randomly.

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


