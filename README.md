# ros_simuino
ROS - SIMUINO linkup

## Download and Install

In catkin ws:
 ```
 cd src
 git clone https://github.com/cspradli/arduino_link.git
 cd arduino_link
 mkdir src
 cd src
 git clone https://github.com/cspradli/simuino.git 
 ```
 Once cloned:
 ```
 cd ../../
 catkin_make
 ```
## To run
1) Open another terminal and run:
```
roscore
```
2) From catkin workspace directory:
```
cd src/arduino_link/src/simuino/
rosrun arduino_link simuino
```
