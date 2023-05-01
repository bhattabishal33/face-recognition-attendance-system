def createdataset(r, n):
    import cv2
    import os
    from pathlib import Path

    # Initialize the classifier
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # Start the video camera
    vc = cv2.VideoCapture(0)

    # Get the userId and userName
    # print("Enter the id and name of the person: ")
    userId = r
    userName = n

    # Initially Count is = 1
    count = 1

    # Function to save the image
    def saveImage(image, userName, userId, crop):
        # Create a folder with the name as userName
        Path("dataset/{}".format(userName)).mkdir(parents=True, exist_ok=True)
        # Save the images inside the previously created folder
        x, y, w, h = crop
        imgcrop = image[y:h, x:w]
        imgcrop = cv2.resize(imgcrop, (224, 224))
        lst = os.listdir("dataset/"+userName)
        numlst = len(lst)  # count number of files
        cv2.imwrite("dataset/{}/{}_{}.jpg".format(userName,
                    userId, numlst), imgcrop)
        print("[INFO] Image  has been saved in folder : {}".format(userName))

    print("[INFO] Video Capture is now starting please stay still")

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
        i = 0
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            i = i+1
            """cv2.putText(img, "Press s to predict and q to quit", (x-50, y-100),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 0.2)"""
            if (i == 1):
                status = 0
            else:
                status = 1
        # Show the image1
        cv2.imshow("Press s to predict and q to quit", img)

        # Wait for user keypress
        key = cv2.waitKey(1) & 0xFF

        # Check if the pressed key is 'k' or 'q'
        if key == ord('s'):
            if status == 0:
                # If count is less than 5 then save the image
                if count <= 300:
                    saveImage(original_img, userName, userId, (x, y, x+w, y+w))
                    count += 1
                else:
                    break
            else:
                cv2.putText(img, "multi face detected", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
        # If q is pressed break out of the loop
        elif key == ord('q'):
            break

    print("[INFO] Dataset has been created for {}".format(userName))

    # Stop the video camera
    vc.release()
    # Close all Windows
    cv2.destroyAllWindows()
