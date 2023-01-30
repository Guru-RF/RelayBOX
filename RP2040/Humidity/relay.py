import board
import digitalio
import analogio

one = digitalio.DigitalInOut(board.GP19)
one.direction = digitalio.Direction.OUTPUT
one.value = False

