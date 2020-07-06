

import hashlib
print('do u want to encrypt?')
plaintext=input("write here: ")
md5 = hashlib.md5()
md5.update(plaintext.encode("ascii"))
print ("Nilai hash md5:", md5.hexdigest())
