
# try:
#     file = open('examples/print8.ls8', 'r')
#     lines = file.read()
#     print(lines)
#     raise Exception('hi')
#     file.close()
# except Exception:
#     print(file.closed

import sys
print(sys.argv)


# try:
#     with open ('examples/print8.ls8.ls8') as file:
#         for line in file:
#             print(line)
#             raise Exception('hi')
# except Exception:
    # print(file.closed)

if len(sys.argv) < 2:
    print('did you forget the file to open')
    print('usage: filename file_to_open')
    sys.exit()

try: 
    with open (sys.argv[0]) as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print(f'{sys.argv[0]}: {sys.argv[1]} not found')

    