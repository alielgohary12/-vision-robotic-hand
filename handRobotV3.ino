#include <Servo.h>
#include <cvzone.h>


SerialData serialData(5, 1);
int valsRec[5];

Servo Little, Ring, Middle, Index, Thumb;

int angleUp = 180;   
int angleDown = 0; 


int currentAngles[5] = {0, 0, 0, 0, 0};
int targetAngles[5]  = {0, 0, 0, 0, 0};


unsigned long previousMillis = 0;

const long servoSpeed = 5; 

void setup() {
  serialData.begin();

  Little.attach(3);
  Ring.attach(5);
  Middle.attach(6);
  Index.attach(9);
  Thumb.attach(10);


  for(int i=0; i<5; i++){
     currentAngles[i] = angleUp;
     targetAngles[i]  = angleUp;
  }

  Thumb.write(currentAngles[0]);
  Index.write(currentAngles[1]);
  Middle.write(currentAngles[2]);
  Ring.write(currentAngles[3]);
  Little.write(currentAngles[4]);
}

void loop() {

  serialData.Get(valsRec);

  if(valsRec[0] == 1) targetAngles[0] = angleUp; else targetAngles[0] = angleDown;
  if(valsRec[1] == 1) targetAngles[1] = angleUp; else targetAngles[1] = angleDown;
  if(valsRec[2] == 1) targetAngles[2] = angleUp; else targetAngles[2] = angleDown;
  if(valsRec[3] == 1) targetAngles[3] = angleUp; else targetAngles[3] = angleDown;
  if(valsRec[4] == 1) targetAngles[4] = angleUp; else targetAngles[4] = angleDown;


  unsigned long currentMillis = millis();
  
  if (currentMillis - previousMillis >= servoSpeed) {
    previousMillis = currentMillis;


    for(int i=0; i<5; i++) {
      if (currentAngles[i] < targetAngles[i]) {
        currentAngles[i]++; 
      } else if (currentAngles[i] > targetAngles[i]) {
        currentAngles[i]--; 
      }
    }


    Thumb.write(currentAngles[0]);
    Index.write(currentAngles[1]);
    Middle.write(currentAngles[2]);
    Ring.write(currentAngles[3]);
    Little.write(currentAngles[4]);
  }
}
