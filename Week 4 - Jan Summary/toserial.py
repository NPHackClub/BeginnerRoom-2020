# import libraries
import serial
import  time

#open file
with open('data.txt', 'r') as file:
    data = file.read().replace('\n', ' ')
nums = data.split( )
ser = serial.Serial('COM5')

# give time to flash serial port
time.sleep(2)

# while player plays, push data continously to arduino
while(nums[4]=="T"):
    with open('data.txt', 'r') as file:
        data = file.read().replace('\n', ' ')
    nums = data.split( )
    ser.write(nums[0].encode())
    time.sleep(0.3)
    ser.write(nums[1].encode())
    time.sleep(0.1)
    ser.write(nums[2].encode())
    time.sleep(0.1)
    ser.write(nums[3].encode())
    time.sleep(0.7)

# close serial port
ser.close()