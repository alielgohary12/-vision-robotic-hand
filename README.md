# Vision-Controlled Robotic Hand

A 3D-printed robotic hand that mirrors the user's finger movements in real time.
A webcam tracks the hand with **MediaPipe**, a Python script detects which fingers are open or closed, and sends the result to an **Arduino Nano** that drives five **SG90 servo motors**.

**Demo video:** [paste your YouTube / LinkedIn link here]

![Robotic hand](photo1.png)

## How it works

1. **OpenCV** captures live video from the webcam.
2. **MediaPipe Hands** detects 21 hand landmarks in every frame.
3. The script compares each fingertip landmark with the joint below it to decide whether the finger is open (1) or closed (0).
4. The five values `[thumb, index, middle, ring, pinky]` are sent over **USB Serial** to the Arduino Nano using **cvzone**.
5. The Arduino sets a target angle for each finger (180° open, 0° closed) and moves the servos toward it in small steps (1° every 5 ms), which gives smooth, non-jerky finger motion.

## Hardware

| Component | Quantity |
|---|---|
| Arduino Nano | 1 |
| SG90 servo motor | 5 |
| External power supply for the servos | 1 |
| 3D-printed robotic hand | 1 |
| Webcam / laptop camera | 1 |

## Wiring

| Finger | Arduino Nano pin |
|---|---|
| Little (pinky) | D3 |
| Ring | D5 |
| Middle | D6 |
| Index | D9 |
| Thumb | D10 |

The servos are powered from the external supply, and its ground is shared with the Arduino ground.

## Software

- Python 3 with `opencv-python`, `mediapipe`, `cvzone`
- Arduino IDE with the `Servo` and `cvzone` libraries

## Files

| File | Description |
|---|---|
| `handRobotV2.py` | Hand tracking and finger detection (PC side) |
| `handRobotV3.ino` | Servo control firmware (Arduino Nano) |
| `photo1.png`, `photo2.png` | Project photos |
| `demo.mp4` | Demo video |

## How to run

1. Upload `handRobotV3.ino` to the Arduino Nano.
2. Install the Python libraries:
```
   pip install opencv-python mediapipe cvzone
```
3. In `handRobotV2.py`, change `COM15` to your Arduino's port.
4. Run the script:
```
   python handRobotV2.py
```
5. Show your hand to the camera. Press **q** to quit.

## Notes

- Finger detection is binary (open / closed), and the thumb check is tuned for one hand orientation.
- Possible improvements: proportional servo angles for each finger and support for both hands.

## Author

Ali El-Gohary - Mechatronics Engineering Student, Zagazig National University
