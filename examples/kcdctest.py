from pyrolab.drivers.motion.z825b  import Z825B

from ctypes import (
    c_short,
    c_int,
    c_char_p,
    byref,
)

motorX = 27504851
motorY = 27003497
motorR = 27003366

x = Z825B(motorX)
y = Z825B(motorY)
r = Z825B(motorR)

print(x.position)
print(y.position)
print(r.position)

# realX = x._real_value_from_du(x.position, 0)

# print(realX)

# maxPos = x._real_value_from_du(x._max_pos, 0)
# minPos = x._real_value_from_du(x._min_pos, 0)

# print(maxPos)
# print(minPos)

# x.move_to(1200)
# y.move_to(0)

# x.move("forward")
# y.move("backward")

# x.move_by(1200)
# y.move_by(1200)
# r.move_by(100)



# x.jog()
# y.jog()

# x.stop
