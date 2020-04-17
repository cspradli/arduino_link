# ros_simuino
ROS - SIMUINO linkup

## Download and Install

In catkin ws:
 ```
 cd src
 git clone https://github.com/cspradli/arduino_link.git
 cd arduino_link/src
 git clone https://github.com/cspradli/simuino.git 
 ```
 Note: If no src folder in arduino link, run this inside the arduino_link folder:
 ```
 mkdir src
 ```
 
 Once cloned:
 ```
 cd ../../
 catkin_make
 ```
