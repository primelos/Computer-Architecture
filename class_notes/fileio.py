
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

# self.ram = [None] * 256
# address = 0

try: 
    with open(sys.argv[1]) as file:
        for line in file:
            comment_split = line.split('#')
            possible_num = comment_split[0]

            if possible_num == '':
                continue

            if possible_num[0] == '1' or possible_num[0] == '0':
                num = possible_num[:8]
                print(f'{num}: {int(num,2)}')

                # self.ram[address] = int(num, 2)
                # address += 1

except FileNotFoundError:
    print(f'{sys.argv[0]}: {sys.argv[1]} not found')




# python fileio.py ../ls8/examples/print8.l