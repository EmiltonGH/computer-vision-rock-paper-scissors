import cv2
from keras.models import load_model
import numpy as np
import random
import time

def get_prediction(frame):
    model = load_model('keras_model.h5')
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1  # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)[0]  # Selecting the first prediction result
    print("Model Prediction:", prediction)
    # Finding the index with the highest probability
    predicted_class_index = np.argmax(prediction)
    # Returning the predicted class
    return predicted_class_index

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return None  # It's a tie
    elif ((computer_choice == 0 and user_choice == 2) or
          (computer_choice == 2 and user_choice == 1) or
          (computer_choice == 1 and user_choice == 0)):
        return 'computer'  # Computer wins
    else:
        return 'user'  # User wins

def play_round():
    computer_choice = get_computer_choice()
    user_choice = get_prediction(frame)
    print("Computer chose:", computer_choice)
    return get_winner(computer_choice, user_choice)

def play_game():
    computer_wins = 0
    user_wins = 0
    while computer_wins < 3 and user_wins < 3:
        winner = play_round()
        if winner == 'computer':
            computer_wins += 1
            print("Computer wins this round!")
        elif winner == 'user':
            user_wins += 1
            print("You win this round!")
        else:
            print("It's a tie!")
        print("Computer: ", computer_wins, " - User: ", user_wins)

    if computer_wins == 3:
        print("Computer wins the game!")
    else:
        print("You win the game!")

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('p'):  # Press 'p' to play the game
        play_game()
    elif cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
