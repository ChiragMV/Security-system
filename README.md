# Security-system
This project is based on laser securit system, along with face recognition.
# Installation `#f03c15`
You need to have processing, arduino and Python installed in your PC.
#Components required
# Usage
Refer to the circuit diagram, which gives a detailed description on how the components must be connected.
Once this is done, 
1. Run the python file Create.py to create a model. Note that you need to make your your webcam is accessible in order to create the model.
3. Once the model is created, you can see a file named "chirag.yml". You can change the name of the model in the python files Create.py and Ardpy.py.
4. Then, run the python file Ardpy.py.
5. Upload the pyfirmata code to port 8:File -> Examples -> Firmata -> Standard Firmata
6. Simultaneously, run the processing code processing_code.pde to port 6(present in Security_system/Radar and photosensor/Processing code.
7. Make sure there are no obstacles around you when you start the processing code.
# Testing
You can test the project by blocking the light incoming on the photosensor. Then, if the webcam(that is running due to Ardpy.py) does not detect the user, then the buzzer will be activated and the servo motor starts to rotate. Since it has the ultrasonic sensor attached to it, even that will rotate and this can be seen on the Processing app as a radar.
You can test the radar feature by keeping an obstacle at some position in the range of the ultrasonic sensor-servo motor combination. Once it detects the obstacle, it shows red lines on the Processing app, which represents the obstacle.
Note that if the webcam detects the user, there is a 14-second duration for the user to move away from the light source (and let the light fall on the photosensor), beyond which the buzzer activates if the light source is blocked. In both cases, when user is detected by webcam or not, the ultrasonic sensor-servo motor combination activates since it is better for the user to see the radar for multiple obstacle.
