class pin:

    def high(pinNr):
        print(f"Pin {pinNr} High")
        return True
    
    def low(pinNr):
        print(f"Pin {pinNr} Low")
        return True

    def state(pinNr):
        t = input(f"pin {pinNr} 1 or 0? ")
        if t == "0":
            return False
        else:
            return True

class motor:

    def down():
        print("down")
        return True
    
    def up():
        print("up")
        return True
    
    def stop():
        print("stop")
        return True