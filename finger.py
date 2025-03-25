import cv2
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)

canvas = np.zeros((480, 640, 3), dtype=np.uint8)

cap = cv2.VideoCapture(0)

prev_x, prev_y = None, None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            if lm_list:
                index_finger_tip = lm_list[8]
                middle_finger_tip = lm_list[12]

        
                if lm_list[8][1] < lm_list[6][1] and lm_list[12][1] > lm_list[10][1]:  
                    x, y = index_finger_tip

                    if prev_x is None or prev_y is None:
                        prev_x, prev_y = x, y

                    cv2.line(canvas, (prev_x, prev_y), (x, y), (255, 255, 255), 5)
                    prev_x, prev_y = x, y
                else:
                    prev_x, prev_y = None, None

                if all(lm_list[i][1] < lm_list[i-2][1] for i in [8, 12, 16, 20]):
                    canvas = np.zeros((480, 640, 3), dtype=np.uint8)

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    frame = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)

    cv2.imshow("Virtual Painter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
