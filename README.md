# ROBOT_PR

### STEP 1 Installation Ubuntu 20.04
```bash
https://www.youtube.com/watch?v=C5deqtXrpgk
```
### STEP 2 Installation ROS
```bash
https://www.youtube.com/watch?v=92Zz5nnd41c&list=PLk51HrKSBQ8-jTgD0qgRp1vmQeVSJ5SQC&index=2
```
### STEP 3 Installation Python in ROS
```bash
https://www.youtube.com/watch?v=w7v4CZt1po8
```
## Software
* Ubuntu
* ROS
* Python

## Hardware
* Breadboard
* Potentiometer
* Encoder
* Servo MG90s 2 
* Arduino UNO R3
* Jump wire

### CONSTRUCT ROS WORKSPACE
Now, we are going to construct the folder “catkin_ws” in the folder home. By using the following command
```bash
mkdir catkin_ws
```
Go to the “catkin_ws” folder
```bash
cd catkin_ws
```
Use the following command to create the folder name “src”.
```bash
mkdir src
```
Use the following command to construct files and folders that are the base construction in “catkin”
```bash
catkin_make
```
Go back to workspace with this command
```bash
cd 
cd catkin_ws
catkin_make
```
Clone my Robot_PR with this command
```bash
git clone https://github.com/liza10263/project_PR.git
```
Go back to workspace again with this command
```bash
#to go catkin_ws
cd .. 

catkin_make
```
Go to file project_PR package : 
```bash
cd src/project_PR/src
```
Add permissions to execute GUI Python file
```bash
chmod +x projectgui.py
```
Launch a launch.file of akarapon64
```bash
roslaunch akarapon64 projectgui.launch model:=' $(find robot_description)/urdf/robot.urdf '
```


### Circuit
![Screenshot 2024-02-21 214815](https://github.com/liza10263/project_PR/assets/129593656/e2a4327b-fd09-4d0e-8325-83bb84385c57)

### Assembly

![Screenshot 2024-02-22 100707](https://github.com/liza10263/project_PR/assets/129593656/8f34ec49-8982-4203-89fe-42b504c36b83)

### GUI display


