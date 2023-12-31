from hashmoves import HashMoves
from hashfacialexp import HashFacialExp
from machine import I2C, Pin,UART
from time import sleep

uart= UART(1,9600)


sda = Pin(0)
scl = Pin(1)
id = 0
i2c = I2C(0, sda=sda, scl=scl)

hf=HashFacialExp()  
hm=HashMoves()

hf.initialize(i2c)
hm.initialize(i2c)
hf.default_face()
sleep(2)

while True:
    if uart.any(): #Checking if data available
        data=uart.read() #Getting data
        data=str(data) #Converting bytes to str type
        #print(data)
        
        if('A01' in data):
            hf.default_face()
        if('A02' in data):
            hf.happy_face()
        if('A03' in data):
            hf.sad_face()
        if('A04' in data):
            hf.eyeclose_face()
        if('A05' in data):
            hf.blink(3)
        if('A06' in data):
            hf.sleep_face(3)
        if('A07' in data):
            hf.wink_face()
        if('A08' in data):
            hf.hardcry_face(3)
        if('A09' in data):
            hf.love_face()
        if('A10' in data):
            hf.angry_face()
        if('A11' in data):
            hf.shock_face()
        if('A12' in data):
            hf.default_face()
        if('B01' in data):
            hm.move_forward(500,5)
        if('B02' in data):
            hm.turn_left(500,5)
        if('B03' in data):
            hm.initial_position()
        if('B04' in data):
            hm.turn_right(500,5)
        if('B05' in data):
            hm.move_backward(500,5)
        if('B06' in data):
            hm.say_hi(2000,2)
        if('B07' in data):
            hm.hands_up(2000,1)
        if('B08' in data):
            hm.hands_down(2000,1)
        if('B09' in data):
            hm.side_move_left(500,5)
        if('B10' in data):
            hm.flying_move(1000,3)
        if('B11' in data):
            hm.side_move_right(500,5)
        if('B12' in data):
            hm.left_slide_wave(2000,3)
        if('B13' in data):
            hm.leg_head_shake(1000,3)
        if('B14' in data):
            hm.right_slide_wave(2000,3)
        if('B15' in data):
            hm.leg_shake(1000,3)
        if('B16' in data):
            hm.hand_straight_shake(1000,3)
        if('B17' in data):
            hm.jump(1000,3)
        if('B18' in data):
            hm.left_hand_balance(2000,3)
        if('B19' in data):
            hm.side_shake(1000,2)
        if('B20' in data):
            hm.right_hand_balance(2000,3)
            
            

# hm.say_hi(2000,2)
# hm.hands_up(2000,1)
# hm.hands_down(2000,1)
# hm.move_forward(500,5)
# hm.move_backward(500,5)
# hm.turn_left(500,5)
# hm.turn_right(500,5)
# hm.side_move_right(500,5)
# hm.side_move_left(500,5)
# hm.flying_move(1000,3)
# hm.leg_shake(1000,3)
# hm.hand_straight_shake(1000,3)
# hm.leg_head_shake(1000,3)
# hm.jump(1000,3)
# hm.right_slide_wave(2000,3)
# hm.left_slide_wave(2000,3)
# hm.right_hand_balance(2000,3)
# hm.left_hand_balance(2000,3)
# hm.side_shake(1000,2)

# hf.happy_face()
# hf.sad_face()
# hf.eyeclose_face()
# hf.blink(5)
# hf.sleep_face(5)
# hf.wink_face()
# hf.hardcry_face(3)
# hf.love_face()
# hf.angry_face()
# hf.shock_face()
# hf.default_face()



