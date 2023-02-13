import pyfirmata

comport = "COM3"

board = pyfirmata.Arduino(comport)


led1 = board.get_pin("d:5:p")
led2 = board.get_pin("d:6:p")
led3 = board.get_pin("d:9:p")
led4 = board.get_pin("d:10:p")
led5 = board.get_pin("d:11:p")


'''led2.write(0.2)'''

'''def led(led_a):
    if led == 1:
        led.Write(1)
    else:
        led_Write(0)'''

def k3(count,diff):
    if(count == 0):
        led1.write(0)
        led2.write(0)
        led3.write(0)
        led4.write(0)
        led5.write(0)
        
    if(count == 1):
        led1.write(diff/255)
        led2.write(0)
        led3.write(0)
        led4.write(0)
        led5.write(0)
        
    if(count == 2):
        led1.write(diff/255)
        led2.write(diff/255)
        led3.write(0)
        led4.write(0)
        led5.write(0)

    if(count == 3):
        led1.write(diff/255)
        led2.write(diff/255)
        led3.write(diff/255)
        led4.write(0)
        led5.write(0)

    if(count == 4):
        led1.write(diff/255)
        led2.write(diff/255)
        led3.write(diff/255)
        led4.write(diff/255)
        led5.write(0)

    if(count == 5):
        led1.write(diff/255)
        led2.write(diff/255)
        led3.write(diff/255)
        led4.write(diff/255)
        led5.write(diff/255)
    

    
