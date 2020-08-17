"""CPU functionality."""

import sys

HLT  = 0b00000001 #1
LDI  = 0b10000010 #130
PRN  = 0b01000111 #71
MUL  = 0b10100010 #162
PUSH = 0b01000101
POP  = 0b01000110
RET  = 0b00010001
CALL = 0b01010000
ST   = 0b10000100
# print(sys.argv[1])

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.PC = 0
        self.reg = [0] * 8
        self.ram = [0] * 256
        self.running = True
        # reserve sp points to F4
        self.reg[7] = 0xF4    # -> reg 244

    def ram_read(self, MAR):
        return self.ram[MAR]
        
    
    def ram_write(self, MDR, MAR):
        self.ram[MAR] = MDR
        

    def load(self, filename):
        """Load a program into memory."""

        address = 0
        try:
            with open (sys.argv[1]) as files:
                # for a in files:
                #     print(a)
                for i in files:
                    # print('i', i)
                    comment = i.strip().split('#')
                    # print('comment',comment)
                    result = comment[0].strip()
                    # print('result', result)
                    if result == '':
                        continue
                    instruction = int(result, 2)
                    self.ram[address] = instruction
                    # print('self.ram[address]',self.ram[address])
                    address += 1
        except FileExistsError:
            print('missing')
            sys.exit(1)

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        elif op == MUL:
            self.reg[reg_a] *= self.reg[reg_b]
        elif op == 'CMP':
            if self.reg[reg_a] == self.reg[reg_b]:
                self.equal = True
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.PC,
            #self.fl,
            #self.ie,
            self.ram_read(self.PC),
            self.ram_read(self.PC + 1),
            self.ram_read(self.PC + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while self.running:
            IR = self.ram_read(self.PC)
            operand_a = self.ram_read(self.PC + 1)
            operand_b = self.ram_read(self.PC + 2)
            
            # print('operand_a', operand_a)
            # print('operand_b',operand_b)
            num_operands = IR >> 6
            # self.PC += 1 + (IR >> 6)

            if IR == LDI:
                self.reg[operand_a] = operand_b
            
            elif IR == PRN:
                print(self.reg[operand_a])

            elif IR == MUL:
                self.alu(IR, operand_a, operand_b)

            elif IR == HLT:
                self.running = False
            
            elif IR == PUSH:
                self.reg[7] -= 1
                reg_num = self.ram_read(self.PC + 1)
                value = self.reg[reg_num]
                SP = self.reg[7]
                self.ram_write(value, SP)
                

            elif IR == POP:
                reg_num = self.ram_read(self.PC + 1)
                SP = self.reg[7]
                self.reg[reg_num] = self.ram_read(SP)
                self.reg[7] += 1

            else:
                print(f'not working')
                sys.exit(1)

            command_sets_pc_directly = ((IR >> 4) & 0b0001) == 1
    
            if not command_sets_pc_directly:
                self.PC += num_operands + 1