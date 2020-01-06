from cryptography.fernet import Fernet
import os
import sys

if os.path.exists('.key'):
    sys.exit()

key = Fernet.generate_key()
with open('.key','wb') as fh:
    fh.write(key)

