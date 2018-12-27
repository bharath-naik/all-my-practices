from Cryptodome.PublicKey import RSA
secret_code = input("please enter something to get public and encrypt key:\n")
key = RSA.generate(2048)
encrypted_key = key.export_key(passphrase = secret_code , pkcs= 8, protection = "scryptAndAES128-CBC" )

print("The following code generates a new RSA key pair (secret) and  protected by a password. We use the scrypt key derivation function to thwart dictionary attacks. At the end ,the code prints our the RSA public key and encrypted key  in ASCII/PEM format:")
print("________________________________________________________________")
print("public_key")
print(key.publickey())
print("________________________________________________________________")
print("encrypt_key")
print(encrypted_key)

