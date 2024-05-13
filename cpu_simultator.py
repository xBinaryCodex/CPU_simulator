#defining CPU class
class CPU:
    def __init__(self):
        self.registers = [0] * 32
        self.PC = 0
        self.running = True
        self.memory = Memory()

    def fetch (self):
        instruction = self.memory.load(self.PC)
        self.PC += 4
        return instruction
    
    def decode(self, instruction):
        opcode = instruction >> 26
        return opcode
    
    def execute(self, opcode):
        if opcode == 0:
            self.running = False

    def run(self):
        while self.running:
            instruction = self.fetch()
            opcode - self.decode(instruction)
            self.execute(opcode)

 # Define Memory class

class Memory:
    def __init__(self):
        self.data = [0] * 1024

    def load(self, address):
        return self.data[address // 4]
    
    def store(self, address, value):
        self.data[address // 4] = value

# Parsing for instructions

def load_instructions_to_memory(filename, memory):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            memory.store(index * 4, int(line.strip()))

def main():
    cpu = CPU()
    load_instructions_to_memory('instructions.txt', cpu.memory)
    cpu.run()

if __name__ == "__main__":
    main()

    