from cache import Cache
from memory import Memory

CPU_COUNTER_INIT_VALUE = 0
NUMBER_OF_REGISTERS = 9

ADD_INSTRCTION_OPERATOR = "ADD"
ADD_I_INSTRUCTION_OPERATOR = "ADDI"
JUMP_INSTRUCTION_OPERATOR = "J"
CACHE_INSTRUCTION_OPERATOR = "CACHE"

CACHE_OF_VALUE = 0
CACHE_ON_VALUE = 1
CACHE_FLUSH_VALUE = 2


# Helper function to convert register string to index. I.e. register labelled 'R2' should correspond to int index 2
def convert_register_to_index(value):
    return int(value[1:])

# CPU class to implement the bulk of CPU Simulator requirements. Member properties include:
# CPU Counter - Int representing the number of the instruction being parsed
# Registers - List used to represent internal registers used by the CPU
# Cache Flag - boolean representing whether or not the cache is to be used
# Cache - instance of Cache object instantiated for CPU
# Memory Bus - instance of Memory Bus object instantiated for CPU
class CPU:

    def __init__(self):
      self.cpu_counter = CPU_COUNTER_INIT_VALUE
      self.registers = [0] * NUMBER_OF_REGISTERS
      self.cache_flag = False
      self.cache = Cache()
      self_memory_bus = Memory()
