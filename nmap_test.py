import sys
import os

target = str(sys.argv[1])

print(os.system('nmap ' + target))