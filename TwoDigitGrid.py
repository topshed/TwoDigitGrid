''' TowDigitGrid.py
This module contains a single function which creates and 64 element list
designed to be used as an image for the Astro-PI HAT LED numToMatrix
'''


#f = [255, 255, 255]
#b = [0, 0, 0]

def numToMatrix(num,back_colour=[255,255,255],text_colour=[0,0,0]):

	if len(str(num)) != 2:
		print("Warning: Number with more than 2 digits - using first 2 digits from left only")

	b = back_colour
	f = text_colour

	space = [
	b,b,b,b,b,b,b,b,
	b,b,b,b,b,b,b,b
	]
# define 1x8 columns that make  single digits when combined


	num_1_2 = [b,b,f,b,b,b,f,b]
	num_1_1 = [b,f,f,f,f,f,f,b]
	num_1_0 = [b,b,b,b,b,b,f,b]

	num_2_2 = [b,f,b,b,b,f,f,b]
	num_2_1 = [b,f,b,b,f,b,f,b]
	num_2_0 = [b,f,f,f,b,b,f,b]

	num_3_2 = [b,f,b,b,f,b,f,b]
	num_3_1 = [b,f,b,b,f,b,f,b]
	num_3_0 = [b,f,f,f,f,f,f,b]

	num_4_2 = [b,f,f,f,f,b,b,b]
	num_4_1 = [b,b,b,b,f,b,b,b]
	num_4_0 = [b,f,f,f,f,f,f,b]

	num_5_2 = [b,f,f,f,f,b,f,b]
	num_5_1 = [b,f,b,b,f,b,f,b]
	num_5_0 = [b,f,b,b,f,f,b,b]

	num_6_2 = [b,f,f,f,f,f,f,b]
	num_6_1 = [b,f,b,b,f,b,f,b]
	num_6_0 = [b,f,b,b,f,f,f,b]

	num_7_2 = [b,f,b,b,b,b,b,b]
	num_7_1 = [b,f,b,b,b,b,b,b]
	num_7_0 = [b,f,f,f,f,f,f,b]

	num_8_2 = [b,f,f,f,f,f,f,b]
	num_8_1 = [b,f,b,b,f,b,f,b]
	num_8_0 = [b,f,f,f,f,f,f,b]

	num_9_2 = [b,f,f,f,f,b,f,b]
	num_9_1 = [b,f,b,b,f,b,f,b]
	num_9_0 = [b,f,f,f,f,f,f,b]

	num_0_2 = [b,f,f,f,f,f,f,b]
	num_0_1 = [b,f,b,b,b,b,f,b]
	num_0_0 = [b,f,f,f,f,f,f,b]

# combine columns to make digits

	sing_0 = num_0_0 + num_0_1 + num_0_2
	sing_1 = num_1_0 + num_1_1 + num_1_2
	sing_2 = num_2_0 + num_2_1 + num_2_2
	sing_3 = num_3_0 + num_3_1 + num_3_2
	sing_4 = num_4_0 + num_4_1 + num_4_2
	sing_5 = num_5_0 + num_5_1 + num_5_2
	sing_6 = num_6_0 + num_6_1 + num_6_2
	sing_7 = num_7_0 + num_7_1 + num_7_2
	sing_8 = num_8_0 + num_8_1 + num_8_2
	sing_9 = num_9_0 + num_9_1 + num_9_2

# map digits onto appropriate strings


	def digitConvert(digit):
		if digit == '1':
			return sing_1
		if digit == '2':
			return sing_2
		if digit == '3':
			return sing_3
		if digit== '4':
			return sing_4
		if digit == '5':
			return sing_5
		if digit == '6':
			return sing_6
		if digit == '7':
			return sing_7
		if digit == '8':
			return sing_8
		if digit == '9':
			return sing_9
		if digit == '0':
			return sing_0


	image = digitConvert(str(num)[1]) + space + digitConvert(str(num)[0]) # build image from two digits plus spacer
	return image


