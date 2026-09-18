import cv2
import mediapipe as mp
from cvzone.SerialModule import SerialObject

# تأكد من رقم البورت الخاص بك
arduino = SerialObject('COM15')
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands 
hands = mpHands.Hands() 
mpDraw = mp.solutions.drawing_utils 
tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    results = hands.process(imgRGB) 
    
    lmList = []
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) 
    
    if len(lmList) != 0:
        # مصفوفة لتخزين حالة الـ 5 أصابع (0 مغلق، 1 مفتوح)
        fingers_data = [0, 0, 0, 0, 0] 

        # الإبهام (Thumb)
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            print("thumb up")
            fingers_data[0] = 1
        else:
            print("thumb down")
            fingers_data[0] = 0
        
        # السبابة (Index)
        if lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2]:
            print("index up")
            fingers_data[1] = 1
        else:
            print("index down")
            fingers_data[1] = 0

        # الوسطى (Middle)
        if lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2]:
            print("middle up")
            fingers_data[2] = 1
        else:
            print("middle down")
            fingers_data[2] = 0
        
        # البنصر (Ring)
        if lmList[tipIds[3]][2] < lmList[tipIds[3] - 2][2]:
            print("ring up")
            fingers_data[3] = 1
        else:
            print("ring down")
            fingers_data[3] = 0

        # الخنصر (Pinky)
        if lmList[tipIds[4]][2] < lmList[tipIds[4] - 2][2]:
            print("pinky up")
            fingers_data[4] = 1
        else:
            print("pinky down")
            fingers_data[4] = 0

        # إرسال البيانات مرة واحدة فقط للـ 5 أصابع معاً للأردوينو
        arduino.sendData(fingers_data)

    cv2.imshow("robot hand", img)
    
    # الخروج من البرنامج عند الضغط على حرف q
    if cv2.waitKey(1) == ord('q'):
        break

# إغلاق الكاميرا والنوافذ بشكل نظيف بعد الخروج
cap.release()
cv2.destroyAllWindows()