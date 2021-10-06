# Engineering_4_Notebook
Dylan Hensley's Engineering 4 Notebook

## Table of Contents
* [Basics](#Basics)
* [Python_Dice_Roller](#PythonDiceRoller)
* [Python_Calculator](#Python_Calculator)
---

## Basics
You can delete this section from your own personal readme. 

### Assignment Description

Write your assignment description here. It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here.  You need to communicate what your thing does. For code only assignments like the Python calculator, include a screenshot of the output of the code.

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here.

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

<img src="Screenshot%20(3).png?raw=true" width="400">
 
<details><summary>Robotic Arm Code</summary>
 
``` arduino
#include <Servo.h> // HEY!!!... here's a servo

Servo servo1; // Labeling Micro Servo #1
Servo servo2; // Labeling Micro Servo #2
Servo servo3; // Labeling Micro Servo #3
Servo servo4; // Labeling Micro Servo #4
Servo servo5; // Labeling Micro Servo #5

int flex1 = A0; // Pin set up for Flex Sensor #1
int flex2 = A1; // Pin set up for Flex Sensor #2
int flex3 = A2; // Pin set up for Flex Sensor #3
int flex4 = A3; // Pin set up for Flex Sensor #4
int flex5 = A4; // Pin set up for Flex Sensor #5

void setup()
{
  Serial.begin(9600);
  
  servo1.attach(8); // Pin set up for Micro Servo #1
  servo2.attach(9); // Pin set up for Micro Servo #2
  servo3.attach(10); // Pin set up for Micro Servo #3
  servo4.attach(11); // Pin set up for Micro Servo #4
  servo5.attach(12); // Pin set up for Micro Servo #5
}

void loop()
{
  int flexValue1; // For calibrating Flex Sensor #1
  int flexValue2; // For calibrating Flex Sensor #2
  int flexValue3; // For calibrating Flex Sensor #3
  int flexValue4; // For calibrating Flex Sensor #4
  int flexValue5; // For calibrating Flex Sensor #5
  int servoPosition1; // For Synchronizing the angles of the Flex Sencor #1 to Micro Servo #1
  int servoPosition2; // For Synchronizing the angles of the Flex Sencor #2 to Micro Servo #2
  int servoPosition3; // For Synchronizing the angles of the Flex Sencor #3 to Micro Servo #3
  int servoPosition4; // For Synchronizing the angles of the Flex Sencor #4 to Micro Servo #4
  int servoPosition5; // For Synchronizing the angles of the Flex Sencor #5 to Micro Servo #5

  flexValue1 = analogRead(flex1); // Renaming analogRead for #1
  flexValue2 = analogRead(flex2); // Renaming analogRead for #2
  flexValue3 = analogRead(flex3); // Renaming analogRead for #3
  flexValue4 = analogRead(flex4); // Renaming analogRead for #4
  flexValue5 = analogRead(flex5); // Renaming analogRead for #5

  servoPosition1 = map(flexValue1, 600, 800, 0, 180); // when flex sensor #1 is bend, micro servo #1 will make the angle...
  servoPosition1 = constrain(servoPosition1, 0, 180); // .. but will not go passed 0 or 180
  servoPosition2 = map(flexValue2, 600, 800, 0, 180); // when flex sensor #2 is bend, micro servo #2 will make the angle...
  servoPosition2 = constrain(servoPosition2, 0, 180); // .. but will not go passed 0 or 180
  servoPosition3 = map(flexValue3, 600, 800, 0, 180); // when flex sensor #3 is bend, micro servo #3 will make the angle...
  servoPosition3 = constrain(servoPosition3, 0, 180); // .. but will not go passed 0 or 180
  servoPosition4 = map(flexValue4, 600, 800, 0, 180); // when flex sensor #4 is bend, micro servo #4 will make the angle...
  servoPosition4 = constrain(servoPosition4, 0, 180); // .. but will not go passed 0 or 180
  servoPosition5 = map(flexValue5, 600, 800, 0, 180); // when flex sensor #5 is bend, micro servo #5 will make the angle...
  servoPosition5 = constrain(servoPosition5, 0, 180); // .. but will not go passed 0 or 180

  servo1.write(servoPosition1);
  servo2.write(servoPosition2);
  servo3.write(servoPosition3);
  servo4.write(servoPosition4);
  servo5.write(servoPosition5);

  delay(100); // reaction time for Micro Servo
  }
```
</details>
 https://www.online-python.com/
