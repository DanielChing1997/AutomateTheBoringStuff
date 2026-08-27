import time, sys

# indent = 0
# indent_increasing = True

# try:
#     while True:
#         print(' ' * indent, end = '')
#         print('********')
#         time.sleep(0.1)

#         if indent_increasing:
#             indent = indent + 1
#             if indent == 20:
#                 indent_increasing = False

#         else:
#             indent = indent - 1
#             if indent == 0:
#                 indent_increasing = True

# except KeyboardInterrupt:
#     sys.exit()

try:
    while True:
        for i in range(1,9):
            print('-' * (i * i))
            time.sleep(0.1)

        for i in range(7,1,-1):
            print('0'*(i*i))
            time.sleep(0.1)

except KeyboardInterrupt:
    sys.exit()

