#!/usr/bin/python3
########################################################################
#                          Action Dino                                 #
########################################################################
# Description:                                                         #
# This program contols a toy dinosaur. A button is pressed to make     #
# the Pteranodon move and squawk.                                      #
#                                                                      #
# This program is also a demonstration of controlling a motor using    #
# the gpiozero module.                                                 #
# This program is also an example of adding color to text displayed to #
# the screen.                                                          #
#                                                                      #
#                                                                      #
# Author: Paul Ryan                                                    #
#                                                                      #
########################################################################

########################################################################
#                          Import files                                #
########################################################################

from gpiozero import Motor, Button, OutputDevice
from time import sleep
from signal import pause
import pygame
import random
import os, sys

########################################################################
#                           Variables                                  #
########################################################################

pteranodon_motor = Motor(23, 24, True)
pteranodon_motor_enable = OutputDevice(25)
yellow_button = Button(17)
red_button = Button(9) 

########################################################################
#                           Initialize                                 #
########################################################################

pygame.mixer.init()

########################################################################
#                            Functions                                 #
########################################################################
'''
The file_check function checks to see if the necessary files exist.
If they all exist, the program will continue.
If a file is missing, the program will print a message and exit.
'''
def file_check():
	
	dinosaur_facts_flag = 0
	pteranodon1_flag = 0
	pteranodon2_flag = 0
	pteranodon3_flag = 0
	pteranodon4_flag = 0
	
	print("Checking for necessary files:")
	# Check to see if dinosaur_facts.txt file exists
	print("Looking for dinosaur_facts.txt...", end="")
	if os.path.isfile('Files/dinosaur_facts.txt'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		dinosaur_facts_flag = 1
	# Check to see if pteranodon1.mp3 file exists
	print("Looking for pteranodon1.mp3...", end="")
	if os.path.isfile('Sounds/pteranodon1.mp3'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		pteranodon1_flag = 1
	# Check to see if pteranodon2.mp3 file exists
	print("Looking for pteranodon2.mp3...", end="")
	if os.path.isfile('Sounds/pteranodon2.mp3'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		pteranodon2_flag = 1	
	# Check to see if pteranodon3.mp3 file exists
	print("Looking for pteranodon3.mp3...", end="")
	if os.path.isfile('Sounds/pteranodon3.mp3'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		pteranodon3_flag = 1
	# Check to see if pteranodon4.mp3 file exists
	print("Looking for pteranodon4.mp3...", end="")
	if os.path.isfile('Sounds/pteranodon4.mp3'):
		print("\033[1;32;40mfound\033[1;37;40m!")
	else:
		print("\033[1;31;40mnot found\033[1;37;40m!")
		pteranodon4_flag = 1
		
	# If there are no missing files, return to the main function,
	# otherwise print out messages and exit the program
	if dinosaur_facts_flag == 0  and pteranodon1_flag == 0 and pteranodon2_flag == 0 and pteranodon3_flag == 0 and pteranodon4_flag == 0:
		return
	else:
		if dinosaur_facts_flag == 1:
			print("\033[1;31;40mCheck to make sure that the dinosaur_facts.txt file exists in the 'Files' folder.")
		if pteranodon1_flag == 1: 	
			print("\033[1;31;40mCheck to make sure that the pteranodon1.mp3 file exists in the 'Sounds' folder.")
		if pteranodon2_flag == 1:
			print("\033[1;31;40mCheck to make sure that the pteranodon2.mp3 file exists in the 'Sounds' folder.") 
		if pteranodon3_flag == 1:
			print("\033[1;31;40mCheck to make sure that the pteranodon3.mp3 file exists in the 'Sounds' folder.")
		if pteranodon4_flag == 1:
			print("\033[1;31;40mCheck to make sure that the pteranodon4.mp3 file exists in the 'Sounds' folder.")
		print("\033[1;37;40mExiting program.\n")
		release_gpio_pins()
		exit()

'''
The access_file_check function checks to see if the user has permission
to read the necessary files. If so, the program will continue. If not, 
messages are printed out to the screen and the program will exit.
'''
def access_file_check():
	
	dinosaur_facts_flag = 0
	pteranodon1_flag = 0
	pteranodon2_flag = 0
	pteranodon3_flag = 0
	pteranodon4_flag = 0
	
	print("Checking to see if user has permission to read the necessary files:")
	# Check to see if user has read access to dinosaur_facts.txt
	print("Does user have read permissions for dinosaur_facts.txt?...", end="")
	if os.access('Files/dinosaur_facts.txt', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		dinosaur_facts_flag = 1
	# Check to see if user has read access to pteranodon1.mp3
	print("Does user have read permissions for pteranodon1.mp3?...", end="")
	if os.access('Sounds/pteranodon1.mp3', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		pteranodon1_flag = 1
	# Check to see if user has read access to pteranodon2.mp3
	print("Does user have read permissions for pteranodon2.mp3?...", end="")
	if os.access('Sounds/pteranodon2.mp3', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		pteranodon2_flag = 1
	# Check to see if user has read access to  pteranodon3.mp3
	print("Does user have read permissions for pteranodon3.mp3?...", end="")
	if os.access('Sounds/pteranodon3.mp3', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		pteranodon3_flag = 1
	# Check to see if user has read access to  pteranodon4.mp3
	print("Does user have read permissions for pteranodon4.mp3?...", end="")
	if os.access('Sounds/pteranodon4.mp3', os.R_OK):
		print("\033[1;32;40mYes\033[1;37;40m!")
	else:
		print("\033[1;31;40mNo\033[1;37;40m!")
		pteranodon4_flag = 1
	
	
	if dinosaur_facts_flag == 0  and pteranodon1_flag == 0 and pteranodon2_flag == 0 and pteranodon3_flag == 0 and pteranodon4_flag == 0:
		return
	else:
		if dinosaur_facts_flag == 1:
			print("\033[1;31;40mMake sure that the user has read access to the 'Files' folder and the dinosaur_facts.txt file.")
		if pteranodon1_flag == 1: 	
			print("\033[1;31;40mMake sure that the user has read access to the 'Sounds' folder and the 'pteranodon1.mp3' file.")
		if pteranodon2_flag == 1:
			print("\033[1;31;40mMake sure that the user has read access to the 'Sounds' folder and the 'pteranodon2.mp3' file.") 
		if pteranodon3_flag == 1:
			print("\033[1;31;40mMake sure that the user has read access to the 'Sounds' folder and the 'pteranodon3.mp3' file.")
		if pteranodon4_flag == 1:
			print("\033[1;31;40mMake sure that the user has read access to the 'Sounds' folder and the 'pteranodon4.mp3' file.")
		print("\033[1;37;40mExiting program.\n")
		release_gpio_pins()
		exit()
'''
The read_file function will read the dinosaur facts file and each 
line of the file will be an element in the fun_facts list. It will then
return the dino_facts list to the main function.
If the program is unable to read the file, it will display an error
message and then exit the program.
If the dino_facts file is empty, an error message will be displayed 
and the program will exit.
'''
def read_file(file_name):
	print("\033[1;37;40mReading the dinosaur_facts.txt file...", end="")
	f = open(file_name, "r")     # open the file as read-only
	dino_facts = f.readlines()
	f.close()
	print("\033[1;32;40mdone\033[1;37;40m!")

	return dino_facts
	
'''
This empty_file_check function checks to see if the file is empty. If it
is, the program will print a message to the screen. If not, the program
will continue.
'''
def empty_file_check(file_name):		
	print("\033[1;37;40mIs the dinosaur_facts.txt file empty?...", end="")
	if file_name == []:
		print("\033[1;31;40mYes\033[1;37;40m!")
		print("\033[1;31;40mThe dinosaur.txt file is empty. The program won't work.")
		release_gpio_pins()
		exit()
	else:
		print("\033[1;32;40mNo\033[1;37;40m!")
		
'''
The print_header function will print out the program header to the 
screen.
'''
def print_header():
	print("\033[1;33;40m===========================================================================")
	print("\033[1;33;40m   _  _   ____     ____  _                                 _               ")
	print("\033[1;33;40m  | || | |  _ \   |  _ \| |_ ___ _ __ __ _ _ __   ___   __| | ___  _ __    ")
	print("\033[1;33;40m  | || |_| | | |  | |_) | __/ _ \ '__/ _` | '_ \ / _ \ / _` |/ _ \| '_ \   ")
	print("\033[1;33;40m  |__   _| |_| |  |  __/| ||  __/ | | (_| | | | | (_) | (_| | (_) | | | |  ")
	print("\033[1;33;40m     |_| |____/   |_|    \__\___|_|  \__,_|_| |_|\___/ \__,_|\___/|_| |_|  ")
	print("\033[1;33;40m                                                                           ")
	print("\033[1;33;40m===========================================================================\n")
                                                      

'''
The get_squawk function will randomly select one of the Pteranodon 
squawk sound files and return it and its file length to the main 
function.
'''
def get_squawk():
	
	squawk1 = "Sounds/pteranodon1.mp3"
	squawk2 = "Sounds/pteranodon2.mp3"
	squawk3 = "Sounds/pteranodon3.mp3"
	squawk4 = "Sounds/pteranodon4.mp3"

	squawk1_length = 6.5     # lenth of file in seconds
	squawk2_length = 6.5     # lenth of file in seconds
	squawk3_length = 6       # lenth of file in seconds
	squawk4_length = 6       # lenth of file in seconds
	
	squawks = [squawk1, squawk2, squawk3, squawk4]
	
	squawk = random.choice(squawks)   # Selects random sound file
	
	if squawk == squawk1:
		return squawk, squawk1_length
	elif squawk == squawk2:
		return squawk, squawk2_length
	elif squawk == squawk3:
		return squawk, squawk3_length
	else:
		return squawk, squawk4_length

'''
The activate_pteranodon funciton takes 2 inputs: squawk and squawk_length. 
This function will play the sound file and then activate the motor for 
the duration of the sound file. 
'''

def activate_pteranodon(squawk, squawk_length):
	try:
		pteranodon_motor.value = 0.6       # Controls the motor speed
	except ValueError:
		print("\033[1;31;40mBad value specified for pteranodon_motor. Enter a value between 0 and 1.\n")
		release_gpio_pins()
		exit()
	pygame.mixer.music.load(squawk)        # Loads the sound file
	pteranodon_motor_enable.on()           # Starts the motor
	pygame.mixer.music.play()              # Plays the sound file
	sleep(squawk_length)                   # Length of sound file in seconds
	pteranodon_motor_enable.off()          # Stops the motor

'''
The prompt_user_for_input function prompts a user to push a button.
'''
def prompt_user_for_input():
	print("\033[1;37;40mPush the \033[1;33;40myellow button \033[1;37;40mto activate the \033[1;33;40mPteranodon\033[1;37;40m.")
	print("\033[1;37;40mPush the \033[1;31;40mred button \033[1;37;40mor press Ctrl-C to \033[1;31;40mstop \033[1;37;40mthe program.\n")

'''
This function realeases the gpio pins.
'''
def release_gpio_pins():
	pteranodon_motor.close()
	pteranodon_motor_enable.close()
	red_button.close()
	yellow_button.close()
	
'''
This is the main fucntion. It will wait until one of two buttons is 
pressed. One button will start the program and the other button will
stop the program. Pressing Ctrl-C will also stop the program.
'''
def main():
	try:
		# Check to see that the necessary files exist
		file_check()
		# Check to see if files are accessible
		access_file_check()
		# Read the dinosaur_facts.txt file to populate the dino_facts list.
		dino_facts = read_file("Files/dinosaur_facts.txt")
		# Check to see if the file is empty
		empty_file_check(dino_facts)
		# Acknowledge that prelimiary checks are complete
		print("\033[1;37;40mPrelimiary checks are complete. Starting program...\n")
		# Display program header
		print_header()
		# Pre-load the first sound file
		squawk, squawk_length = get_squawk()
		# Prompt the user to press a button
		prompt_user_for_input()
		
		while True:
			
			if yellow_button.is_pressed:
				# Print out a random dinosaur fun fact
				print("\033[1;34;40mDINOSAUR FUN FACT:")
				print(random.choice(dino_facts))
				# Move the T. rex for the duration of the sound file
				activate_pteranodon(squawk, squawk_length)
				# Prompt the user to press a button
				prompt_user_for_input()
				# Load the next sound file
				squawk, squawk_length = get_squawk()
				
			if red_button.is_pressed:
				print("Exiting program.\n")
				release_gpio_pins()
				exit()
				
	except KeyboardInterrupt:
		release_gpio_pins()
		print("\nExiting program.\n")
		
if __name__ == '__main__':
	main()
