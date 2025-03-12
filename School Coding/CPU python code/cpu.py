class machine:#
    def __init__(self):
        self.pc = 0
        self.mar = 0
        self.mdr = 0
        self.cir = 0
        self.acc = 0
        self.ram = [["LOAD 000", "ADD 001", "STA 100", "INP 000", "ADD 100", "OUT 000", "HALT 000"],[0 for i in range(999)]]
        self.ram[1][0] = 5
        self.ram[1][1] = 3
        self.end = False #value to end program.
        self.tempLoc = None #To store PC state for JUMP instruction
        self.SR = [0,0] # [Zero flag, Negative flag]
        self.jumped = False

    def stripInstruction(self,string):
        words = string.split()
        instructions = words[0]
        operand = words[1]
        return instructions, operand

    def fetch(self):
        self.SR[0] = 0
        self.SR[1] = 0
        if self.acc == 0:
            self.SR[0] = 1
        if self.acc < 0:
            self.SR[1] = 1

        self.mar = self.pc
        self.mdr = self.ram[0][self.mar]
        self.cir = self.mdr
        self.pc += 1
        if self.jumped:
            self.pc = self.tempLoc + 1

    def decode(self):
        self.instr, self.opr = self.stripInstruction(self.cir)
        self.opr = int(self.opr)
        #This would be stored in the control unit, but it would be pointless packaging it into 
        #a small array just to unpack it literally lines later.

    def execute(self):
        self.jumped = False
        match self.instr:
            case "LOAD":
                print(f"Loading mem location {self.opr} ({self.ram[1][self.opr]})")
                self.acc = self.ram[1][self.opr]
            case "ADD":
                print(f"Adding value in memLoc {self.opr} ({self.ram[1][self.opr]})")
                self.acc += self.ram[1][self.opr]
            case "STA":
                print(f"Storing value in acc ({self.acc}) in mem loc {self.opr}")
                self.ram[1][self.opr] = self.acc
            case "HALT":
                print("HALTING")
                self.end = True
            case "OUT":
                print("OUTPUT:")
                print(self.acc)
            case "SUB":
                print(f"Subtracting {self.ram[1][self.opr]} from accumulator ({self.acc})")
                self.acc -= self.ram[1][self.opr]
            case "JUMP":
                self.tempLoc = self.pc
                self.jumped = True
                self.pc = self.ram[1][self.opr]
            case "JZ":
                if self.acc == 0:
                    self.tempLoc = self.pc
                    self.jumped = True
                    self.pc = self.ram[1][self.opr]
            case "INP":
                self.acc = int(input("Input value: "))
            case _:
                print(f"INVALID OPCODE {self.cir}")

test = machine()

while test.end == False:
    test.fetch()
    test.decode()
    test.execute()