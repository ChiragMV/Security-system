# Security-system
This project is based on laser security system, along with face recognition.
# Installation
You need to have Processing, Arduino and Python installed on your PC.
# Components required
1. Arduino Uno (X2)
2. Resistors (X2)
3. Light-dependent resistor (LDR)
4. Buzzer
5. AND gate
6. NOT gate
7. Servo motor
8. Ultrasonic sensor
9. USB 2.0 Cable Type A/B (to connect Arduino Uno to PC)
10. Light source (Laser, torch, etc.) 
# Usage
Refer to the circuit diagram, which gives a detailed description of how the components must be connected.
Once this is done, 
1. Upload the PyFirmata code to Arduino Uno connected to port 8: File -> Examples -> Firmata -> Standard Firmata.
2. Run the python file Create.py to create a model. Note that you need to make your your webcam is accessible in order to create the model.
3. Once the model is created, you can see a file named "chirag.yml". You can change the name of the model in the python files Create.py and Ardpy.py.
4. Then, run the python file Ardpy.py.
5. Simultaneously, upload the arduino code and run the processing code processing_code.pde to port 6(present in Security_system/Radar and photosensor/Processing code.
6. Make sure there are no obstacles around you when you start the processing code.
# Testing
1. Test the project by blocking the incoming light on the photosensor.
2. Then, if the webcam(that is running due to Ardpy.py) does not detect the user, then the buzzer will be activated and the servo motor starts to rotate. Since it has the ultrasonic sensor attached to it, even that will rotate and this can be seen on the Processing app as a radar.
3. You can test the radar feature by keeping an obstacle at some position in the range of the ultrasonic sensor-servo motor combination. Once it detects the obstacle, it shows red lines on the Processing app, which represents the obstacle.
4. Note that if the webcam detects the user, there is a 14-second duration for the user to move away from the light source (and let the light fall on the photosensor), beyond which the buzzer activates if the light source is blocked.
5. In both cases, when user is detected by webcam or not, the ultrasonic sensor-servo motor combination activates since it is better for the user to see the radar for multiple obstacles.
# Contributing:
Your willingness to contribute and enhance the project is highly valued and greatly appreciated. You could also modify and add additional features to this project (like using switches to introduce a lock pattern and so on).
# References:
Online research papers.
