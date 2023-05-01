import cv2
import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf
import os
from tensorflow import keras
from keras import layers
from keras.models import Sequential
import os
from pathlib import Path

def predict(image):
    img_path = image
    img = tf.keras.utils.load_img(
      img_path, target_size=(img_height, img_width)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    
    predictions = newmodel.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    n = class_names[np.argmax(score)]
    con = 100 * np.max(score)
    if con < 50:
      msg = "The confidence is lower than 50 so please try again"
      n = "the face is not recognized"
      print(msg)
      return (n,con,msg)
    else:
      msg="This image most likely belongs to {} with a {:.2f} percent confidence.".format(class_names[np.argmax(score)], 100 * np.max(score))
      print(msg)
      return (n,con,msg)
def saveImage(image,crop):
    
    # Save the images inside the previously created folder
    x,y,w,h = crop
    imgcrop = image[y:h,x:w]
    imgcrop = cv2.resize(imgcrop,(224,224))
    cv2.imwrite("input.jpg", imgcrop)
    
def facerecg():
    
    global img_height
    global img_width
    global newmodel
    global class_names
    img_height=224
    img_width=224
    newmodel =keras.models.load_model("Facedetetion.h5")
    train_ds = tf.keras.utils.image_dataset_from_directory("dataset")
    class_names = train_ds.class_names
    font = cv2.FONT_HERSHEY_COMPLEX
    # Initialize the classifier
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # Start the video camera
    vc = cv2.VideoCapture(0)

    while True:
        # Capture the frame/image
        _, img = vc.read()

        # assign the image to a variable called original_img to later save it
        original_img = img.copy()

        # Get the gray version of our image
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Get the coordinates of the location of the face in the picture
        
        faces = faceCascade.detectMultiScale(gray_img,
                                            scaleFactor=1.2,
                                            minNeighbors=5,
                                            minSize=(50, 50))

        # Draw a rectangle at the location of the coordinates
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Show the image
        cv2.imshow("Identified Face", img)

        
        c=0
        # Wait for user keypress
        key = cv2.waitKey(1) & 0xFF
        if key == ord('p'):
            saveImage(original_img,(x,y,x+w,y+w))
            name,confident,msg=predict("input.jpg")  
            c=1
            
            
        if key == ord('q') or c==1:
            break

        
    # Stop the video camera
    vc.release()
    # Close all Windows
    cv2.destroyAllWindows()
    return(name,confident,msg)
    