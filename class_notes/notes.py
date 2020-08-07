print_tim = 0b00000001
halt      = 0b00000010
print_num = 0b00000011   #3
save      = 0b00000100
print_register = 0b00000101
add       = 0b00000110  #6

memory_arr = [ #this represents our memory
    print_tim,  #<--- PC
    print_tim,
    print_num, #3
    99,
    save,
    42,  # number to save
    2,   # number to register
    save,
    42,
    3,
    add,
    2,
    3,
    print_register,
    2,
    halt,

        ]

running = True
pc = 0

registers = [None] * 8

while running:
    command = memory_arr[pc]

    if command == print_tim:
        print('print_tim', print_tim)
        pc += 1

    if command == print_num:
        # print('co_num',command)
        # print('pc_num',pc)
        number_to_print = memory_arr[pc + 1]
        # print('print_num',number_to_print, 'command', command)
        pc += 2

    if command == save:
        print('command_save', command)  #cmd 4
        print('pc_save', pc)
        num = memory_arr[pc +1]
        print('num',num)
        index = memory_arr[pc + 2]
        print('i',index)
        registers[index] = num
        print(registers)
        pc += 3
        print('pc_save', pc)

    if command == print_register:   # cmd 5
        print('com_reg', command)
        print('pc_reg', pc)
        reg_idx = memory_arr[pc + 1]
        print('reg_idx',reg_idx)
        print(registers[reg_idx])
        pc += 2 
    
    if command == add:
        first_reg_idx = memory_arr[pc + 1]
        second_reg_idx = memory_arr[pc + 2]

        
    
    if command == halt:
        running = False

    # print('command', command)
# print('pc',pc)

print(memory_arr)