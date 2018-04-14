#!/usr/bin/python3
########################################################################
#                          4D Pteranodon                               #
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
import os, sys, logging

########################################################################
#                           Variables                                  #
########################################################################

pteranodon_motor = Motor(2, 3, True)			# forward, backward, pwm
pteranodon_motor_enable = OutputDevice(4)
yellow_button = Button(17)
red_button = Button(9) 

########################################################################
#                           Initialize                                 #
########################################################################

pygame.mixer.init()

logging.basicConfig(filename='Files/Pteranodon.log', filemode='w',
	level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', 
	datefmt='%m/%d/%y %I:%M:%S %p:')

########################################################################
#                            Functions                                 #
########################################################################
'''
This is the main function. It will wait until one of two buttons is 
pressed. One button will start the program and the other button will
stop the program. Pressing Ctrl-C will also stop the program.
'''
def main():
	try:
		logging.info("START")
		# Check to see that the necessary files exist
		file_check()
		# Check to see if files are accessible
		permission_check()
		# Read the dinosaur_facts.txt file to populate the dino_facts list.
		dino_facts = read_file("Files/dinosaur_facts.txt")
		# Check to see if the file is empty
		empty_file_check(dino_facts)
		# Acknowledge that prelimiary checks are complete
		logging.info("Prelimiary checks are complete. Starting program...")
		# Display program header
		print_header()
		# Pre-load the first sound file
		squawk, squawk_length = get_squawk()
		# Prompt the user to press a button
		prompt_user_for_input()
		
		while True:
			
			if yellow_button.is_pressed:
				# Print out a random dinosaur fun fact
				print_dinosaur_fact(dino_facts)
				# Move the Pteranodon for the duration of the sound file
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
		stop_the_program()

'''
The file_check function checks to see if the necessary files exist.
If they all exist, the program will continue.
If a file is missing, the program will print a message and exit.
'''
def file_check():
	
	file_missing_flag = 0
	
	logging.info("FILE CHECK")
	# Check to see if dinosaur_facts.txt file exists
	if os.path.isfile('Files/dinosaur_facts.txt'):
		logging.info("dinosaur_facts.txt file was found!")
	else:
		detail_log.error("dinosaur_facts.txt file was not found! Make sure that the dinosaur_facts.txt file exists in the Files folder.")
		file_missing_flag = 1
	# Check to see if pteranodon1.mp3 file exists
	if os.path.isfile('Sounds/pteranodon1.mp3'):
		logging.info("pteranodon1.mp3 file was found!")
	else:
		logging.error("pteranodon1.mp3 file was not found! Make sure that the pteranodon1.mp3 file exists in the 'Sounds' folder.")
		file_missing_flag = 1
	# Check to see if pteranodon2.mp3 file exists
	if os.path.isfile('Sounds/pteranodon2.mp3'):
		logging.info("pteranodon2.mp3 file was found!")
	else:
		logging.error("pteranodon2.mp3 file was not found! Make sure that the pteranodon2.mp3 file exists in the 'Sounds' folder.")
		file_missing_flag = 1
	# Check to see if pteranodon3.mp3 file exists
	if os.path.isfile('Sounds/pteranodon3.mp3'):
		logging.info("pteranodon3.mp3 file was found!")
	else:
		logging.error("pteranodon3.mp3 file was not found! Make sure that the pteranodon3.mp3 file exists in the 'Sounds' folder.")
		file_missing_flag = 1
	# Check to see if pteranodon4.mp3 file exists
	if os.path.isfile('Sounds/pteranodon4.mp3'):
		logging.info("pteranodon4.mp3 file was found!")
	else:
		logging.error("pteranodon4.mp3 file was not found! Make sure that the pteranodon4.mp3 file exists in the 'Sounds' folder.")
		file_missing_flag = 1
		
	# If there are no missing files, return to the main function
	# Otherwise print out message and exit the program
	if file_missing_flag == 0:  
		return
	else:
		print("\033[1;31;40m\nCould not run the program. Some files are missing. Check the DinoDen_log.txt file in the 'Files' folder for more information.")
		stop_the_program()

'''
The permission_check function checks to see if the user has permission
to read the necessary files. If so, the program will continue. If not, 
messages are printed out to the screen and the program will exit.
'''
def permission_check():
	
	permission_flag = 0
	
	logging.info("PERMISSION CHECK")
	# Check to see if user has read access to dinosaur_facts.txt
	if os.access('Files/dinosaur_facts.txt', os.R_OK):
		logging.info("User has permission to read the dinosaur_facts.txt file.")
	else:
		logging.error("User does not have permission to read the dinosaur_facts.txt file.")
		permission_flag = 1
	# Check to see if user has read access to pteranodon1.mp3
	if os.access('Sounds/pteranodon1.mp3', os.R_OK):
		logging.info("User has permission to read the pteranodon1.mp3 file.")
	else:
		logging.error("User does not have permission to read the pteranodon1.mp3 file.")
		permission_flag = 1
	# Check to see if user has read access to pteranodon2.mp3
	if os.access('Sounds/pteranodon2.mp3', os.R_OK):
		logging.info("User has permission to read the pteranodon2.mp3 file.")
	else:
		logging.error("User does not have permission to read the pteranodon2.mp3 file.")
		permission_flag = 1
	# Check to see if user has read access to  pteranodon3.mp3
	if os.access('Sounds/pteranodon3.mp3', os.R_OK):
		logging.info("User has permission to read the pteranodon3.mp3 file.")
	else:
		logging.error("User does not have permission to read the pteranodon3.mp3 file.")
		permission_flag = 1
	# Check to see if user has read access to  pteranodon4.mp3
	if os.access('Sounds/pteranodon4.mp3', os.R_OK):
		logging.info("User has permission to read the pteranodon4.mp3 file.")
	else:
		logging.error("User does not have permission to read the pteranodon4.mp3 file.")
		permission_flag = 1
	
	
	if permission_flag == 0:  
		return
	else:
		print("\033[1;31;40m\nCould not run the program. Check the DinoDen_log.txt file in the 'Files' folder for more information.")
		stop_the_program()

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
	logging.info("READING DINOSAUR_FACTS.TXT")
	with open(file_name, "r") as f:   # open the file as read-only
		dino_facts = f.readlines()

	return dino_facts
	
'''
This empty_file_check function checks to see if the file is empty. If it
is, the program will print a message to the screen. If not, the program
will continue.
'''
def empty_file_check(file_name):
	logging.info("EMPTY FILE CHECK")
	if file_name == []:
		logging.error("The dinosaur.txt file is empty. The program won't work.")
		print("\033[1;31;40mErrors were encountered. Check the log in the 'Files' folder for more details.\033[1;31;40m")
		stop_the_program()
	else:
		logging.info("The dinosaur.txt file is not empty.(This is good. We don't want an empty file.)")
		
'''
The print_header function will print out the program header to the 
screen.
'''
def print_header():
	print("\n")
	print("\033[1;33;40m===========================================================================")
	print("\033[1;33;40m   _  _   ____     ____  _                                 _               ")
	print("\033[1;33;40m  | || | |  _ \   |  _ \| |_ ___ _ __ __ _ _ __   ___   __| | ___  _ __    ")
	print("\033[1;33;40m  | || |_| | | |  | |_) | __/ _ \ '__/ _` | '_ \ / _ \ / _` |/ _ \| '_ \   ")
	print("\033[1;33;40m  |__   _| |_| |  |  __/| ||  __/ | | (_| | | | | (_) | (_| | (_) | | | |  ")
	print("\033[1;33;40m     |_| |____/   |_|    \__\___|_|  \__,_|_| |_|\___/ \__,_|\___/|_| |_|  ")
	print("\033[1;33;40m                                                                           ")
	print("\033[1;33;40m===========================================================================")
	print("\n")
                                                      
'''
The print_dinosaur_fact function prints out a random fact about 
dinosaurs. The dino_facts file needs to be sent to this function.
'''
def print_dinosaur_fact(dino_facts):
	print("\033[1;34;40mDINOSAUR FUN FACT:")
	print(random.choice(dino_facts))

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
		logging.error("A bad value was specified for pteranodon_motor. The value should be between 0 and 1.")
		print("\033[1;31;40mAn error was encountered. Check the detail log for more information.\n")
		stop_the_program()
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

def stop_the_program():
	release_gpio_pins()
	print("\033[1;37;40mExiting program.\n")
	logging.info("END")
	exit()
	
if __name__ == '__main__':
	main()
