Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/Bharath/AppData/Local/Programs/Python/Python36/file encryption/EncryptAndDecrypt.py 
******THIS IS FOR ENCRYPTION*******
cipher.nonce
: b'v\xb4w\xb0}\x83\\*\xcc\xb09' 
 tag is
: b'\xac\xa5\xa9=\x8fh\xe4|6|\xd8\xad\x97\x9b\xd6\x8f' 
 ciphertext
: b'\xe7*4WR\x05\x0f\xfd\x1b\xf8\xde\x12\xc70\x059U\xb9\xa1\xc7\xe9\xdd \n\xae\xa2\xa7Z\xa1D\r\xbe\x0f8\x81\xda\xe1E\xa7\x1e\x95f\xf2w\x1e\xe4zh\x17\x13\xac\xc4\xcc0\xf3\xd1\xaa\x90\xf3I\x14\xf3@\xf6\xbb'
_______________________________________________________________________________
******THIS IS FOR DECRYPTION*******
>>> 
 RESTART: C:/Users/Bharath/AppData/Local/Programs/Python/Python36/file encryption/EncryptAndDecrypt.py 
******THIS IS FOR ENCRYPTION*******
cipher.nonce
: b'\xb4\xb2/\xa5\xfd\x7fV\x14%nI' 
 tag is
: b'96_"x\x02\xefQ\x81\x8fM\xc4\xaa<\xd7\xb8' 
 ciphertext
: b'!\xf3\xdf\x1cRZ\xa0\x84Wm\n\xbdJ\xc5\x94\xe7HQ\xf7\xcd\xca\xd4\xa5\xcc?\xccW\x0e\xde\x9e\xb4\x98i\xe9k\xbc\x85\xf2\xcf\xc4\x95W\x17O\xc5\xbd,\xd4\x91\x1a\x98\xd0L\x8a\xb7\xa9\xed\xc3:\xaep0\xac\x1dw'
_______________________________________________________________________________
******THIS IS FOR DECRYPTION*******
all the keys must be enterd here to get the decrypted string
Traceback (most recent call last):
  File "C:/Users/Bharath/AppData/Local/Programs/Python/Python36/file encryption/EncryptAndDecrypt.py", line 44, in <module>
    cipher = AES.new(key, AES.MODE_CCM,nonce)
NameError: name 'nonce' is not defined
>>> 
 RESTART: C:/Users/Bharath/AppData/Local/Programs/Python/Python36/file encryption/EncryptAndDecrypt.py 
******THIS IS FOR ENCRYPTION*******
cipher.nonce
: b'\xd8?W3\x1a\x8e\x8b\x85\xbd\x0f\xb3' 
 tag is
: b'\xf4\x96\xe8\xc9{\xaa\x01\xc9\x8fzw\xc8\xcaS\xfe\xe0' 
 ciphertext
: b'<\xe2\x01G\x92k*L\x86\x83\x8fh;\x02\xb9\xa20\x13\xf4\xc8\x1a|\xf67.\x84j>\xec\x93d\xf0\x82\xa4\xc7\x93z\x83\xaa\xaa\xf6vv+v\xb5\x0fz\xd2\xb4Q\xd98u\x92\xaa^\x86\x81\xdf\x18\xa8\xfa\x19 '
_______________________________________________________________________________
******THIS IS FOR DECRYPTION*******
all the keys must be enterd here to get the decrypted string
Traceback (most recent call last):
  File "C:/Users/Bharath/AppData/Local/Programs/Python/Python36/file encryption/EncryptAndDecrypt.py", line 43, in <module>
    cipher = AES.new(key, AES.MODE_CCM,nonce)
NameError: name 'nonce' is not defined
>>> 
 RESTART: C:/Users/Bharath/AppData/Local/Programs/Python/Python36/file encryption/EncryptAndDecrypt.py 
******THIS IS FOR ENCRYPTION*******
cipher.nonce
: b'\xc2\x10\xaeI\x8e\x00\xeaA1\xf8\xe4' 
 tag is
: b'\xdd`\x0c\x19pA@\x99T\xabZv\xe2\x006d' 
 ciphertext
: b'\xa4\x01\xaf\n\x8e(\xd1\x9b\xd8\xe2\xc9j\x86M/\xccr\xf9\xb4<\xf5h\x89\x97)\xe5\x80\x01\xe8\x19\x14\xbfllV\t\x93iY\x04\xb0\x05\xb7\xcfZ\xa1\xb9\xa6-\x9c\xfcv\xbd{\xebq\xd6~~\x8c^\xaf\xae\x14\xbc'
_______________________________________________________________________________
******THIS IS FOR DECRYPTION*******
all the keys must be enterd here to get the decrypted string
Traceback (most recent call last):
  File "C:/Users/Bharath/AppData/Local/Programs/Python/Python36/file encryption/EncryptAndDecrypt.py", line 44, in <module>
    data = cipher.decrypt_and_verify(Ciphertext, tag)
NameError: name 'Ciphertext' is not defined
>>> 
 RESTART: C:/Users/Bharath/AppData/Local/Programs/Python/Python36/file encryption/EncryptAndDecrypt.py 
******THIS IS FOR ENCRYPTION*******
cipher.nonce
: b'@\xcb\x9a^\x0c\xae9\xae\x821\x1d' 
 tag is
: b'\xddh\xbehy`\xd5\xd0\xfb\xf8$\x83\xc3\xfc\xf5T' 
 ciphertext
: b'\xa7\x0f\xb8\xd1K\xf4\xa6\xa7\xd6Qf\xf0\x02\xef~\x17G\xe8\xccWA\xf0\xd6W\xdd\xba8:\x8f\xcb\xc8r\xd4+A8$#\xef\t)NT,\x89\x99_\xdf\xf5\xab\xbc=\x9d\xeb\xd9\xb2\x9aG\xf7\x11\xbb=#j#'
_______________________________________________________________________________
******THIS IS FOR DECRYPTION*******
all the keys must be enterd here to get the decrypted string
b'get off you hacker i will show a big black buffalo ash to you kid'
>>> 
