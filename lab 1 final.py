from engi1020.arduino.api import *

rot_val = analog_read(0)

y = 300/1023*(rot_val - 0) + 300

buzzer_frequency(5, int(y))
