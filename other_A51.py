# A5/1 Cipher
# Author: Abraham Kong
# Class: CS 166
# Professor Fabio Di Troia

import re
import collections

'''
# Get input
key = input("Please enter a random number: ")
type(key)

print("The number will be used to generate the 64-bit keystream")

# Convert to Binary
key = format(key, '#064b')
# key = bin(key)
print("This is your number in binary: " + key)
'''

key = '0101001000011010110001110001100100101001000000110111111010110111'
# Create X, Y, and Z registers
key_x = key[2:21]
key_y = key[21:43]
key_z = key[-23:]

# Print out to confirm the 3 registers
print("X: " + key_x)
print("Y: " + key_y)
print("Z: " + key_z)

# Find out Clocking bits
x = key_x[7] # Get the 8th bit
y = key_y[9] # Get the 10th bit
z = key_z[9] # Get the 10th bit

# majority function
c = collections.Counter(x = x, y = y, z = z)
vote = max(c[0], c[1]) # Return the majority vote

# Shift
if x == vote : step_x()
if y == vote : step_y()
if z == vote : step_z() 

print("new X: " + key_x)
print("new Y: " + key_y)
print("new Z: " + key_z)
print("new keystream: " + key_x + key_y + key_z)

def step_x():
	# 4 bits used to compute the new first bit
	x1 = key_x[13]
	x2 = key_x[16]
	x3 = key_x[17]
	x4 = key_x[18]
	x_new_first_bit = int(x1) ^ int(x2) ^ int(x3) ^ int(x4) #XOR all bits to compute new first bit
	key_x = str(x_new_first_bit) + key_x[:18] # new register = new first bit and the original shifting right


def step_y():
	# 2 bits used to compute the new first bit
	y1 = key_y[20]
	y2 = key_y[21]
	y_new_first_bit = int(y1) ^ int(y2) #XOR all bits to compute new first bit
	key_y = str(y_new_first_bit) + key_y[:21] # new register = new first bit and the original shifting right
	print 



def step_z():
	# 4 bits used to compute the new first bit
	z1 = key_z[7]
	z2 = key_z[20]
	z3 = key_z[21]
	z4 = key_z[22]
	z_new_first_bit = int(z1) ^ int(z2) ^ int(z3) ^ int(z4) #XOR all bits to compute new first bit
	key_z = str(z_new_first_bit) + key_z[:22] # new register = new first bit and the original shifting right

def new_bit():
	# Get the last bit of each register
	x_last = key_x[18]
	y_last = key_y[21]
	z_last = key_z[22]
	new_bit = int(x) ^ int(y) ^ int(z)
	print("new bit: " + str(new_bit))
	return new_bit

new_bit()

