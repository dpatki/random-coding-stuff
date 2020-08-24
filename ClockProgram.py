import time
def clock(input_hour, input_minute, input_second):
	if input_hour == 12:
		hour_angle = (30 * input_hour + 0.5 * input_minute + (1 / 120) * input_second) - 360
	else:
		hour_angle = 30 * input_hour + 0.5 * input_minute + (1 / 120) * input_second
	minute_angle = 6 * input_minute + 0.1 * input_second
	second_angle = 6 * input_second
	if input_hour > 12 or input_hour < 1:
		print("Not a valid hour, please provide a valid input")
	elif input_minute > 59 or input_minute < 0:
		print("Not a valid minute, please provide a valid input")
	elif input_second > 59 or input_second < 0:
		print("Not a valid second, please provide a valid second")
	else:
		print(hour_angle)
		print(minute_angle)
		print(second_angle)
	
def between_hands(input_hour, input_minute, input_second):
	if input_hour == 12:
		hour_angle = (30 * input_hour + 0.5 * input_minute + (1 / 120) * input_second) - 360
	else:
		hour_angle = 30 * input_hour + 0.5 * input_minute + (1 / 120) * input_second
	minute_angle = 6 * input_minute + 0.1 * input_second
	second_angle = 6 * input_second
	diff_hour_minute = abs(hour_angle - minute_angle)
	diff_hour_second = abs(hour_angle - second_angle)
	diff_minute_second = abs(minute_angle - second_angle)
	if input_hour > 12 or input_hour < 1:
		print("Not a valid hour, please provide a valid input")
	elif input_minute > 59 or input_minute < 0:
		print("Not a valid minute, please provide a valid input")
	elif input_second > 59 or input_second < 0:
		print("Not a valid second, please provide a valid second")
	else:
		print("Difference between hour and minute angles: " + str(diff_hour_minute))
		print("Difference between hour and second angles: " + str(diff_hour_second))
		print("Difference between minute and second angles: " + str(diff_minute_second))
		
		
new_random_thingy = input(" NOTE: All measurements are in degress. \n Inputs that are not integers WILL crash this program. \n If you want measurements in radians, go somewhere else. \n Would you like the angle differences between the hands? \n If so, type 'yes'. If not, press enter. ")

new_hour = int(input("Add hour here: "))
new_minute = int(input("Add minute here: "))
new_second = int(input("Add second here: "))

if new_random_thingy == "yes":
	between_hands(new_hour, new_minute, new_second)
else:
	clock(new_hour, new_minute, new_second)
time.sleep(10.0)	

