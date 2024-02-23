# Rock, Paper, Scissors Game with Computer Vision

This Python script allows you to play the classic game of Rock, Paper, Scissors against a computer using your webcam. The computer makes its choices based on hand gestures detected through computer vision techniques.

## How it Works

The script captures video frames from your webcam, processes them to detect hand gestures, and compares your choice with the computer's choice to determine the winner of each round. The game continues until one player wins three rounds.

## Prerequisites

- Python 3.x
- OpenCV (cv2)
- Keras
- NumPy

## Setup and Installation

1. Clone this repository to your local machine:
    git clone https://github.com/EmiltonGH/rock-paper-scissors.git

2. Navigate to the project directory:
    cd rock-paper-scissors

3. Install dependencies:
    pip install -r requirements.txt
    

## Usage

1. Ensure your webcam is connected to your computer.

2. Run the script:
    python rock_paper_scissors.py

3. A window will open displaying the webcam feed. To start playing, press the 'p' key. Press 'q' to quit the game.

4. Follow the on-screen instructions to make your choice for each round.

## Troubleshooting

- If the webcam feed is not displaying correctly, ensure that your webcam is connected and recognized by your operating system.
- If you encounter errors related to missing dependencies, make sure you have installed all required libraries by running `pip install -r requirements.txt`.


