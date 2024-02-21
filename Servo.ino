#include <ros.h>
#include <std_msgs/Int16.h>
#include <std_msgs/Bool.h>
#include <Servo.h>



bool Mode = true; //bool
int gui_potentiometer;
int gui_encoder; 
int potPin = A0;
int potValue;  // Declare potValue as a global variable
volatile unsigned int temp, counter = 0; 
Servo servoEncoder;
Servo servoPot;

void encoderMessageCallback(const std_msgs::Int16& msg) {
   gui_encoder = msg.data;
  //servoEncoder.write(gui_encoder);
  
}

void potMessageCallback(const std_msgs::Int16& msg) {
  gui_potentiometer = msg.data;
 //servoPot.write(gui_potentiometer);
  
}

void switchMessageCallback(const std_msgs::Bool& msg) {
  Mode = msg.data;
  if(Mode){
    digitalWrite(LED_BUILTIN, HIGH);
  }
  else{
    digitalWrite(LED_BUILTIN, LOW);
  }
  
}

ros::NodeHandle nh;

// Define ROS publishers
std_msgs::Int16 encoderPos_msg;
ros::Publisher encoderPosPub("encoder", &encoderPos_msg);
ros::Subscriber<std_msgs::Int16> encoderSub("gui_encoder", &encoderMessageCallback);

std_msgs::Int16 potValue_msg;
ros::Publisher potValuePub("potentiometer", &potValue_msg);
ros::Subscriber<std_msgs::Int16> potSub("gui_potentiometer", &potMessageCallback);

ros::Subscriber<std_msgs::Bool> switchSub("Switch_Mode", &switchMessageCallback);


void setup() {
  //Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(potPin, INPUT);
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  attachInterrupt(0, ai0, RISING);
  attachInterrupt(1, ai1, RISING);
  servoPot.attach(9);
  servoEncoder.attach(10);
  
  nh.initNode();
  nh.advertise(encoderPosPub);
  nh.advertise(potValuePub);
  nh.subscribe(switchSub);
  nh.subscribe(encoderSub);
  nh.subscribe(potSub);
}

void loop() {
  
  potValue = analogRead(potPin);  // Update potValue
  //Serial.println("hi");
  if (counter != temp) {
    counter = constrain(counter, 0, 180);
    temp = counter;
    if (counter > 180) {
      counter = 180;
    }
    if (counter < 1) {
      counter = 1;
    }
  }
    //////////////////////////////////////////////////////////////////////
     int potentiometerServoAngle = map(potValue, 0, 1023, 0, 180);
    if (!Mode){
      servoEncoder.write(counter);
      servoPot.write(potentiometerServoAngle);
    }
    else{
       servoEncoder.write(gui_encoder);
       servoPot.write(gui_potentiometer);

    }
    
  encoderPos_msg.data =  counter;
  encoderPosPub.publish(&encoderPos_msg);
  potValue_msg.data  = potentiometerServoAngle ;
  potValuePub.publish(&potValue_msg);
  nh.spinOnce();  
  }
  
void ai0() {
  if (digitalRead(3) == LOW) {
    counter++;
    if (counter > 180) {
      counter = 180;
    }
  }
}

void ai1() {
  if (digitalRead(2) == LOW) {
    counter--;
    if (counter < 1) {
      counter = 1;
    }
  }
}
