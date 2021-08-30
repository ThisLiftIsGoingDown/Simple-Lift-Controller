from interface import pin, motor
from call import callcr, switch

print("Welcome to the Simple lift controller by ThisLiftIsGoingDown!")
print("Finding Car Position...")

while not pin.state(1):
    motor.down()

level = 0
call = -1
print("Car position Found!, Car is at level 0")

while True:
    while call == -1:
        call = callcr.get()
    while level != call:
        if level > call:
            motor.down()
        elif level < call:
            motor.up()
        level = switch.checkPos()
    motor.stop()