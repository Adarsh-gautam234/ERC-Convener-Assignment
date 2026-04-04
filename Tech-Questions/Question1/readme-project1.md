Multiplayer Reaction Duel (4-Player System with False Start Detection)

[FOR BETTER FORMATTED DOCUMENT - https://docs.google.com/document/d/1UUea0EBpKUPDQ3-WqR-KouqoKG1FEKmRsSgLIeXUXXM/edit?usp=sharing ]
Introduction
This project is a simple and interactive multiplayer game built using an Arduino. It is designed to be completed within a weekend and is suitable for beginners who are new to electronics and programming.
The system allows four players to compete in a reaction-based game where they must press a button as quickly as possible after a signal is given. The system detects the fastest player and provides visual and sound feedback.
To make the game fair and more engaging, a false start detection feature is included.
Objective
The aim of this project is to:
Build an interactive and fun electronic system
Encourage competition and engagement among students
Introduce beginners to Arduino and basic circuit design
Demonstrate real-time input-output systems
Components Required

Component
Quantity
Approx Cost (₹)
Arduino Uno (or compatible)
 
1
 
250–300
Push Buttons

4

40
LEDs (Player Indicators)

4

40
Signal LED

1

10
Buzzer

1

30
Resistors (220Ω)

5- 6

20
Breadboard

1

100
Jumper Wires

~20

100

Total estimated cost: ₹550–650
System Design
The system consists of:
4 input buttons (one for each player)
5 LEDs (4 player LEDs + 1 signal LED)
1 buzzer for feedback
Arduino Uno as the controller
Each player has:
One button (input)
One LED (output indicator)
A central LED acts as the signal for starting the game.
Circuit Description
Power Connections
Arduino 5V → Breadboard positive rail
Arduino GND → Breadboard ground rail
All components share this common ground.
Buttons (Inputs)
Each button is connected as follows:
One side → GND rail
Other side → Arduino digital pin
Player
Pin
Player 1
D2
Player 2
D3
Player 3
D4
Player 4
D5

Internal pull-up resistors are used in code, so no external resistors are required.
LEDs (Outputs)
Each LED is connected in series with a resistor:
LED
Pin
Player 1 LED
D6
Player 2 LED
D7
Player 3 LED
D8
Player 4 LED
D9
Signal LED
D11

Connection:
LED positive (long leg) → Arduino pin
LED negative (short leg) → resistor → GND
Buzzer
Positive → D10
Negative → GND
Working Principle
Step 1: Initial State
All LEDs are OFF. The system is waiting.
Step 2: Random Delay
The Arduino waits for a random time between 2–5 seconds.
Step 3: False Start Detection
If any player presses their button during the delay:
That player is penalized
Their LED blinks
Buzzer gives an error sound
Game resets
Step 4: Signal Activation
The signal LED turns ON, indicating players can respond.
Step 5: Player Reaction
Players press their buttons as quickly as possible.
Step 6: Winner Detection
The Arduino detects the first button press and declares that player as the winner.
Step 7: System Lock
After detecting the winner:
Other inputs are ignored
Only one winner is allowed
Step 8: Output
Winner’s LED blinks
Buzzer produces a sound
Step 9: Reset
System resets for the next round.
Arduino Code
int buttons[] = {2, 3, 4, 5};
int leds[] = {6, 7, 8, 9};

int signalLED = 11;
int buzzer = 10;

bool gameStarted = false;
bool winnerFound = false;

void setup() {
  for (int i = 0; i < 4; i++) {
    pinMode(buttons[i], INPUT_PULLUP);
    pinMode(leds[i], OUTPUT);
  }
  pinMode(signalLED, OUTPUT);
  pinMode(buzzer, OUTPUT);
  randomSeed(analogRead(0));
}

void loop() {
  resetGame();
  gameStarted = false;
  winnerFound = false;

  unsigned long startTime = millis();
  int waitTime = random(2000, 5000);

  while (millis() - startTime < waitTime) {
    checkFalseStart();
  }

  digitalWrite(signalLED, HIGH);
  gameStarted = true;

  while (!winnerFound) {
    for (int i = 0; i < 4; i++) {
      if (digitalRead(buttons[i]) == LOW) {
        declareWinner(i);
        winnerFound = true;
        break;
      }
    }
  }

  delay(3000);
}

void checkFalseStart() {
  for (int i = 0; i < 4; i++) {
    if (digitalRead(buttons[i]) == LOW) {
      falseStart(i);
      delay(2000);
      resetGame();
      return;
    }
  }
}

void falseStart(int player) {
  for (int i = 0; i < 5; i++) {
    digitalWrite(leds[player], HIGH);
    delay(100);
    digitalWrite(leds[player], LOW);
    delay(100);
  }
  tone(buzzer, 300, 500);
}

void declareWinner(int player) {
  digitalWrite(signalLED, LOW);
  for (int i = 0; i < 3; i++) {
    digitalWrite(leds[player], HIGH);
    delay(300);
    digitalWrite(leds[player], LOW);
    delay(300);
  }
  tone(buzzer, 1000, 500);
}

void resetGame() {
  for (int i = 0; i < 4; i++) {
    digitalWrite(leds[i], LOW);
  }
  digitalWrite(signalLED, LOW);
}

Learning Outcomes
Participants will learn:
Basic Arduino programming
Digital input and output handling
Breadboard circuit design
Debugging and testing hardware
Real-time system behavior
Conclusion
The Multiplayer Reaction Duel is a simple yet engaging project that combines electronics and gameplay. It is easy to build, cost-effective, and highly interactive, making it ideal for ERC weekend workshops. The addition of false start detection ensures fairness and enhances user experience.

 Made this circuit on tinkerscad (good platform to make circuit and test running it can upload code to arduino as well on their platform)




