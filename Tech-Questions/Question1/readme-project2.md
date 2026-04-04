ERC Weekend Project Proposal

[FOR BETTER FORMATTED DOCUMENT - https://docs.google.com/document/d/1UUea0EBpKUPDQ3-WqR-KouqoKG1FEKmRsSgLIeXUXXM/edit?usp=sharing ]
Introduction
While designing these projects, I wanted to create an experience that appeals to different kinds of students. Some people naturally enjoy competition and fast-paced challenges, while others are more inclined towards social interaction and fun activities. Keeping this in mind, I designed two projects—one that focuses on competitive gameplay through a reaction-based buzzer system, and another that encourages interaction through a light-hearted compatibility tester. The idea was to ensure that whether someone wants to compete or simply engage with others, there is something that immediately captures their interest and participation.
Compatibility Tester (Detailed Build and Explanation)

11. Introduction
After designing the reaction-based multiplayer game, I wanted to build something completely different in nature. While the first project focuses on competition, this one focuses on interaction and fun.
The idea was to create a system that people would casually use, especially in a college environment. Something that naturally brings people together, creates curiosity, and adds humor to the experience.
This led to the design of a Compatibility Tester, where two users interact with the system and receive a compatibility score along with humorous feedback.

12. Components Required
Component
Quantity
Arduino Uno
1
Push Buttons
2
LEDs (Red, Yellow, Green)
3
Resistors (220Ω)
3
Piezo Buzzer
1
16x2 LCD Display
1
Breadboard
1
Jumper Wires
As required


12.1 Cost Estimation
While designing this project, I made sure that the total cost remains within the given budget of ₹1000 per kit. All components used are easily available and commonly used in beginner electronics kits, which also makes the project scalable for workshops.
Component
Quantity
Approx Cost (₹)
Arduino Uno (compatible)
1
250–300
Push Buttons
2
20
LEDs (Red, Yellow, Green)
3
30
Resistors (220Ω)
3
10
Piezo Buzzer
1
30
16x2 LCD Display
1
120–150
Breadboard
1
100
Jumper Wires
—
100

Total Estimated Cost: ₹650–750
This keeps the project well within budget while still allowing multiple features such as display, sound effects, and interactive feedback. The cost-to-experience ratio is high, making it suitable for ERC activities where both learning and engagement are important.

13. Circuit Design and Connections
The circuit is designed in a structured way so that each component has a clear role.

13.1 Power Connections
Arduino 5V → Breadboard positive rail
Arduino GND → Breadboard ground rail
All components share a common ground through the rail.

13.2 Button Connections (Input)
Two buttons are used for user interaction.
Button
Arduino Pin
Button A
D2
Button B
D3

Each button is connected as:
One side → GND
Other side → Arduino pin
The code uses INPUT_PULLUP, so no external resistor is required.

13.3 LED Connections (Output)
Three LEDs are used to represent different outcomes.
LED
Arduino Pin
Red LED
D6
Yellow LED
D7
Green LED
D8

Each LED is connected in series:
Long leg → Arduino pin
Short leg → Resistor → GND

13.4 Buzzer Connection
Positive terminal → D10
Negative terminal → GND
The buzzer is used to create different sound patterns.

13.5 LCD Connections (Parallel Mode)
LCD Pin
Arduino
RS
D12
E
D11
D4
D5
D5
D4
D6
D9
D7
D13
VCC
5V
GND
GND
RW
GND
VO
GND

The LCD is used to display the score and messages.

14. Working of the System
The system works in multiple stages, creating an interactive flow.

Step 1: Initial State
The LCD displays:
“Press Buttons”
The system waits for both users to press their respective buttons.

Step 2: Input Detection
When one button is pressed, its state is stored.
Only when both buttons are pressed, the system proceeds further.

Step 3: Countdown Phase
A countdown (3…2…1…) is displayed on the LCD.
At the same time, short buzzer sounds are generated to build anticipation.

Step 4: Processing Phase
After the countdown:
LCD displays “Checking…”
Buzzer produces ticking sounds
The system then generates a random number between 0 and 100, representing compatibility.

Step 5: Score Animation
Instead of directly showing the result, the score is animated from 0 up to the final value.
This creates a sense of suspense and improves user experience.

Step 6: Result Output
Based on the generated score:
Low Compatibility (0–40)
Red LED glows
Sad sound pattern
Funny message like “Stay friends”
Medium Compatibility (40–70)
Yellow LED glows
Neutral sound
Message like “Maybe…”
High Compatibility (70–100)
Green LED glows
Happy sound pattern
Message like “Perfect Match!”
Additional animation effect

Step 7: Reset
After displaying the result for a few seconds:
LEDs turn OFF
LCD resets to initial message
System becomes ready for next interaction

15. Arduino Code
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 9, 13);

int buttonA = 2;
int buttonB = 3;

int redLED = 6;
int yellowLED = 7;
int greenLED = 8;

int buzzer = 10;

bool aPressed = false;
bool bPressed = false;

// Sound functions
void suspenseSound() {
  for (int i = 0; i < 5; i++) {
    tone(buzzer, 400, 100);
    delay(200);
  }
}

void sadSound() {
  tone(buzzer, 300, 300);
  delay(350);
  tone(buzzer, 200, 400);
}

void neutralSound() {
  tone(buzzer, 600, 200);
  delay(250);
  tone(buzzer, 700, 200);
}

void happySound() {
  tone(buzzer, 1000, 150);
  delay(200);
  tone(buzzer, 1200, 150);
  delay(200);
  tone(buzzer, 1500, 300);
}

void countdown() {
  lcd.clear();
  for (int i = 3; i >= 1; i--) {
    lcd.setCursor(0, 0);
    lcd.print("Starting in:");
    lcd.setCursor(0, 1);
    lcd.print(i);
    tone(buzzer, 500, 200);
    delay(800);
  }
}

void animateScore(int finalScore) {
  for (int i = 0; i <= finalScore; i += 5) {
    lcd.setCursor(0, 0);
    lcd.print("Score: ");
    lcd.print(i);
    lcd.print("   ");
    delay(50);
  }
}

String goodMsgs[] = {"Perfect match!", "Shaadi pakki", "Love detected", "Couple goals"};
String midMsgs[] = {"Maybe maybe", "50-50 chance", "Loading...", "Try again"};
String badMsgs[] = {"Stay friends", "Rejected bro", "Mission failed", "No vibes"};

void setup() {
  pinMode(buttonA, INPUT_PULLUP);
  pinMode(buttonB, INPUT_PULLUP);

  pinMode(redLED, OUTPUT);
  pinMode(yellowLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(buzzer, OUTPUT);

  lcd.begin(16, 2);
  lcd.print("Press Buttons");

  randomSeed(analogRead(0));
}

void loop() {

  if (digitalRead(buttonA) == LOW) aPressed = true;
  if (digitalRead(buttonB) == LOW) bPressed = true;

  if (aPressed && bPressed) {

    countdown();

    lcd.clear();
    lcd.print("Checking...");
    suspenseSound();

    int score = random(0, 101);

    lcd.clear();
    animateScore(score);

    if (score < 40) {
      lcd.setCursor(0, 1);
      lcd.print(badMsgs[random(0,4)]);
      digitalWrite(redLED, HIGH);
      sadSound();
    } 
    else if (score < 70) {
      lcd.setCursor(0, 1);
      lcd.print(midMsgs[random(0,4)]);
      digitalWrite(yellowLED, HIGH);
      neutralSound();
    } 
    else {
      lcd.setCursor(0, 1);
      lcd.print(goodMsgs[random(0,4)]);
      digitalWrite(greenLED, HIGH);
      happySound();
    }

    delay(3000);

    digitalWrite(redLED, LOW);
    digitalWrite(yellowLED, LOW);
    digitalWrite(greenLED, LOW);

    lcd.clear();
    lcd.print("Press Again");

    aPressed = false;
    bPressed = false;
  }
}


16. Learning Outcomes
Through this project, participants understand:
How to integrate multiple outputs (LCD, LED, buzzer)
How to create user interaction systems
How to use randomness in embedded logic
How to enhance projects using animations and feedback

17. Transition Between Projects
While the first project focuses on competition and fast response, this second project shifts towards interaction and user experience.
Together, these two systems demonstrate how microcontroller-based projects can be designed not just for functionality, but also for engagement and creativity.

