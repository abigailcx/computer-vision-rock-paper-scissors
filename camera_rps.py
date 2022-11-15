import random
import time
import csv
import cv2
from keras.models import load_model
import numpy as np


# WORK IN PROGRESS
# functional programming paradigm for RPS game using only the camera

print("about to load model")
model = load_model('keras_model.h5') #load model ready to make prediction
print("load model complete")
cap = cv2.VideoCapture(0) # Open a camera for video capturing. To open default camera using default backend just pass 0.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) # construct a numpy array
label_file = 'labels.txt'


with open(label_file) as f:
        reader = csv.reader(f, delimiter=' ')
        label_dict = dict(reader)
        print(label_dict)

def get_normalized_image():
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image

    return frame, data

def get_prediction():
    frame, data = get_normalized_image()
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    prediction_index = np.argmax(prediction)
    print(prediction_index)
    
    return prediction_index

def get_user_choice():
    prediction_index = get_prediction()
    moves = []
    for k, v in label_dict.items():
        moves.append(v)
    user_choice = moves[prediction_index]
    print(user_choice)
    
    return user_choice


def get_winner(prediction):
    pass
    # take predicted player move 
    # take computer move
    # compute & return winner 

#def get_countdown():
    # pass
    
while True:
    start = time.time()
    get_user_choice()
    end = time.time()
    time_elapsed = end - start
    if time_elapsed >= 3:
        print(f"you chose {user_choice}!")
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()


