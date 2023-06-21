import sys
import os

alvo = str(sys.argv[1])

print(os.system('nmap ' + alvo))