import cv2
import mediapipe as mp
import Pyfirmata_and_Arduino as ar
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    image_height, image_width, _ = image.shape

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    count = 0
    diff = 255
    diff_pre = 255
          
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
          #print('hand_landmarks:', hand_landmarks)

          
          
          pi_d_l = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x * image_height
          th_d = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x * image_height

          if(th_d>pi_d_l):
            
            in_u = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height
            in_d = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y * image_height
            
            mid_u = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height
            mid_d = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * image_height
            
            ri_u = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height
            ri_d = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y * image_height
            
            pi_u = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * image_height
            pi_d = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y * image_height

            pi_u_l = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * image_height
            pi_d_l = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x * image_height

            th_u_h = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_height
            th_d_h = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y * image_height
            
            th_u = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image_height
            th_d = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x * image_height

            if(in_u<in_d):
                count+=1
                
            if(mid_u<mid_d):
                count+=1
                
            if(ri_u<ri_d):
                count+=1
                
            if(pi_u<pi_d):
                count+=1
                
            if(th_u>th_d):
                count+=1

            print(count)

          if(th_d<pi_d_l):
            th_u_hleft = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_height
            in_u_left = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height
            th_d_hleft = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image_height
            in_d_left = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_height

            
            diff = (th_u_hleft - in_u_left)*1.75

            if(abs(diff-diff_pre)<5):
                diff = diff_pre

            diff_pre = (th_u_hleft - in_u_left)*1.75

            if(diff>255):
                diff = 255
            if(diff<4):
                diff = 0

            print(diff)

          ar.k3(count,diff)
            

          mp_drawing.draw_landmarks(
              image,
              hand_landmarks,
              mp_hands.HAND_CONNECTIONS,
              mp_drawing_styles.get_default_hand_landmarks_style(),
              mp_drawing_styles.get_default_hand_connections_style())
        #print(hand_landmarks)
        
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(1) == 13 :
      break
cap.release()
cv2.destroyAllWindows()
