#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16,Float64,Bool
import tkinter as tk
from tkinter import Scale
from sensor_msgs.msg import JointState
class GuiApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Arduino GUI")
		self.mode_msg = Bool()
		self.encoderguivalue = Int16()
		self.potguivalue = Int16()
		
		
		self.pubjoint1 = rospy.Publisher('joint_states', JointState, queue_size=10)
		self.joint_state = JointState()
		
		self.joint_state.name = ['joint1','joint2']
		self.joint_state.position=[0,0]
		
		
		self.encoder_label = tk.Label(root, text="Encoder:")
		self.encoder_label.pack()
		
		self.potentiometer_label = tk.Label(root, text="Potentiometer:")
		self.potentiometer_label.pack()

		self.scalePot_label = tk.Label(root, text="Potentiometer Value:")
		self.scalePot_label.pack()

		self.scale_varpot = tk.DoubleVar()
		self.scale_pot = Scale(root, from_=0, to=180, variable=self.scale_varpot, orient=tk.HORIZONTAL)
		self.scale_pot.pack()
		
		self.scaleEncoder_label = tk.Label(root, text="Encoder Value:")
		self.scaleEncoder_label.pack()

		self.scale_varencoder = tk.DoubleVar()
		self.scale_encoder = Scale(root, from_=0, to=180, variable=self.scale_varencoder, orient=tk.HORIZONTAL)
		self.scale_encoder.pack()
		
		self.encoder_var = tk.StringVar()
		self.encoder_value = tk.Label(root, textvariable=self.encoder_var)
		self.encoder_value.pack()

		self.potentiometer_var = tk.StringVar()
		self.potentiometer_value = tk.Label(root, textvariable=self.potentiometer_var)
		self.potentiometer_value.pack()

		self.mode_label = tk.Label(root, text="Mode 1")
		self.mode_label.pack()
        
		self.gui_mode = True
		self.mode_button = tk.Button(root, text="Switch Mode", command= self.gui_mode_command)
		self.mode_button.pack()
		
		self.set_button = tk.Button(root, text="Set Mode", command= self.set_command)
		self.set_button.pack()
 			
		rospy.init_node('gui_node', anonymous=True)
		self.pubencoder = rospy.Publisher('gui_encoder', Int16, queue_size = 10)	#gui
		self.pubpot = rospy.Publisher('gui_potentiometer', Int16, queue_size =10)	#gui
		
		self.pubswitch = rospy.Publisher('Switch_Mode', Bool, queue_size = 10)

		self.subencoder = rospy.Subscriber('encoder', Int16, self.encoder_callback)	
		self.subpot = rospy.Subscriber('potentiometer', Int16, self.potentiometer_callback)

	def encoder_callback(self, data):
		if not self.gui_mode:
			self.encoder_var.set(str(data.data))

	def potentiometer_callback(self, data):
		if not self.gui_mode:
			self.potentiometer_var.set(str(data.data))
		
	
	def set_command(self): #sent value to arduino
		if self.gui_mode :
			
			self.encoderguivalue.data = int (self.scale_varencoder.get())
			self.pubencoder.publish(self.encoderguivalue)
			
			self.potguivalue.data = int (self.scale_varpot.get())
			self.pubpot.publish(self.potguivalue)
			
			joint1_position = self.scale_varpot.get()
			joint2_position = self.scale_varencoder.get()
			
			self.joint_state.header.stamp = rospy.Time.now()
			self.joint_state.position = [joint1_position/(180)*(3.14)/18,joint2_position/(180)*(3.14)/(2)]
			self.pubjoint1.publish(self.joint_state)
	
	def gui_mode_command(self):
		self.gui_mode = not self.gui_mode
		if self.gui_mode:
			self.mode_label.config(text = "Mode 1")
		else :
			self.mode_label.config(text = "Mode 2")
		self.mode_msg.data = self.gui_mode
		self.pubswitch.publish(self.mode_msg)
		


if __name__ == '__main__':
    root = tk.Tk()
    app = GuiApp(root)
    root.geometry("600x300")
    root.mainloop()	

