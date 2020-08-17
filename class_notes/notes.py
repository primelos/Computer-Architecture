
print_tim =      0b00000001
halt      =      0b00000010
print_num =      0b01000011   # command 3
save      =      0b10000100
print_register = 0b01000101
add       =      0b10000110  # command 6
push      =      0b01000111  # 1 operand command 7  
pop       =      0b01001000  # 1 operand command 8
call      =      0b01011001
ret       =      0b00011010

import sys

# moved over to our_program.ls8 in binary 
# memory_arr = [
#     print_tim,  #<--- PC
#     print_tim,
#     print_num, # 3
#     99,
#     save,
#     40,  # number to save
#     2,   # number to register
#     save,
#     42,
#     3,
#     add,
#     2,
#     3,
#     print_register,
#     2,
#     halt,
# ]

memory_arr = [None] * 256  #this represents our memory

running = True
pc = 0

def load_program():
    address = 0
    try: 
        with open(sys.argv[1]) as file:
            for line in file:
                comment_split = line.split('#')
                possible_num = comment_split[0]

                if possible_num == '':
                    continue

                if possible_num[0] == '1' or possible_num[0] == '0':
                    num = possible_num[:8]
                    # print(f'{num}: {int(num,2)}')

                    memory_arr[address] = int(num, 2)
                    address += 1

    except FileNotFoundError:
        print(f'{sys.argv[0]}: {sys.argv[1]} not found')

load_program()

registers = [None] * 8
registers[7] = 0xF4 
print(registers[7])

while running:
    command = memory_arr[pc]

    num_operands = command >> 6
    # print('num_operands',num_operands)

    if command == print_tim:
        print('print_tim', print_tim)

    elif command == print_num:
        number_to_print = memory_arr[pc + 1]
        print(number_to_print)

    elif command == save:
        # print('command_save', command)  #cmd 4
        # print('pc_save', pc)
        num = memory_arr[pc +1]
        # print('num',num)
        index = memory_arr[pc + 2]
        # print('i',index)
        registers[index] = num
        # print(registers)
        # print('pc_save', pc)
    # print(registers)

    elif command == print_register:   # cmd 5
        # print('com_reg', command)
        # print('pc_reg', pc)
        reg_idx = memory_arr[pc + 1]
        # print('reg_idx',reg_idx)
        print('registers[reg_idx]',registers[reg_idx])
    
    elif command == add:
        first_reg_idx = memory_arr[pc + 1]
        second_reg_idx = memory_arr[pc + 2]

        registers[first_reg_idx] += registers[second_reg_idx]

    elif command == push:
        registers[7] -= 1
        register_num = memory_arr[pc + 1]
        number_to_push = registers[register_num]
        sp = registers[7]
        memory_arr[sp] = number_to_push

    elif command == pop:
        sp = registers[7]
        popped_value = memory_arr[sp]
        register_num = memory_arr[pc + 1]
        registers[register_num] = popped_value
        registers[7] += 1

    elif command == halt:
        running = False

    elif command == call:
        next_instruction_address = pc + 2
        registers[7] -= 1
        sp = registers[7]
        memory_arr[sp] = next_instruction_address
        reg_address = memory_arr[pc + 1]
        address_to_jump_to = registers[reg_address]
        pc = address_to_jump_to
    
    elif command == ret:
        sp = registers[7]
        return_address = memory_arr[sp]
        registers[7] += 1
        pc = return_address

    command_sets_pc_directly = ((command >> 4) & 0b0001) == 1
    
    if not command_sets_pc_directly:
        pc += num_operands + 1



    # else:
    #     'error in program'

    # pc += num_operands + 1
    # print('command', command)
    # print('pc',pc)

print(registers)
