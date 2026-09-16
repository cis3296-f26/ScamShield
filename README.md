# ScamShield

ScamShield is a web application that identifies common warning signs in suspicious emails, text messages, and job offers.

## Features

- Allows users to paste a suspicious message
- Detects common scam phrases and warning signs
- Detects links in messages
- Gives a LOW, MEDIUM, or HIGH risk level
- Explains why parts of the message may be suspicious

## Technologies Used

- Python
- Flask
- HTML
- CSS

## System Information

- Operating System: macOS 26.6.2
- Build Version: 25G83
- Python Version: 3.11.5

## How to Run ScamShield

1. Clone the repository:

   git clone https://github.com/cis3296-f26/ScamShield.git

2. Enter the project folder:

   cd ScamShield

3. Create a virtual environment:

   python3 -m venv venv

4. Activate the virtual environment:

   source venv/bin/activate

5. Install the required packages:

   pip install -r requirements.txt

6. Start the application:

   flask --app app run --port 5001

7. Open the following address in a web browser:

   http://127.0.0.1:5001


## How It Works

The user pastes a suspicious message into the website and clicks "Analyze Message." ScamShield checks the message for common warning signs, such as urgent language, suspicious links, requests for personal information, and unusual payment requests.

Based on the warning signs detected, the application returns a LOW, MEDIUM, or HIGH risk level and explains what made the message suspicious.

## Proof of Concept

The current version of ScamShield uses rule-based detection to identify common scam patterns in messages. It shows that the main features of the project can work together in a simple web application. More warning signs and advanced detection methods can be added as the project develops.
