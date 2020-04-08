import hashlib
import json
import base64
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad
from base64 import b64decode, b64encode
from Crypto.Util.Padding import unpad
from Crypto.Random import random
from Crypto import Random

#1
def GeneratePublicAndPrivateKey():
    

    #RSA KEY Creation
    key = RSA.generate(2048)
    return key

#2
def ExportPublicORPrivateKeyToAFile(path, key):
    
    #Exporting de key
    k = key.exportKey('PEM')
    
    #Opening a file and writing the key inside
    file_out = open(path+ ".pem", "wb")
    file_out.write(k)

    file_out.close()
   
#3
def ImportPublicORPrivateKeyFromAFile(path):

    #Returning de key
    return RSA.import_key(open(path).read())

#4
def EncryptingDataWithRSA(data,k):
    
    # Encrypt the session key with the public RSA key
    cipher = PKCS1_OAEP.new(k)

    return cipher.encrypt(data.encode())

#5
def DesencryptingDataWithRSA(encryptedData, k):

    # Decrypt the session key with the private RSA key
    cipher = PKCS1_OAEP.new(k)
    return cipher.decrypt(encryptedData).decode('utf-8')


#6 Encypting with SHA256
BLOCK_SIZE = 16
def pad(s): return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
def unpad(s): return s[:-ord(s[len(s) - 1:])]


def GeneratingSHA256Key():

    #The password entered by client
    password = input("Enter encryption password: ")

    #Creating a key with the SHA256 HASH
    key = hashlib.sha256(password.encode("utf-8")).digest()

    return key

#7
def EncryptingDataWithAES(data, k):
    
    #Calculating if the message length is multiple of 16
    data = pad(data)

    #Initializing vector
    #iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    iv = Random.new().read(AES.block_size)
    
    #Creating a symmetric cipher .encode("utf8")
    cipher = AES.new(k, AES.MODE_CBC, iv = iv)
 
    #Encrypting data
    encData = cipher.encrypt(data.encode())
     
    #Returning data
    return base64.b64encode(iv + encData)

#8 Desencryption with AES in mode CBC
def DesencryptingDataWithAES(encryptedData,k):

    encryptedData = base64.b64decode(encryptedData)
    #Extracting the vector
    iv = encryptedData[:AES.block_size]

    #Extracting encrypted data
    encData = encryptedData[AES.block_size:]

    #Creating a symmetric cipher
    cipher = AES.new(k, AES.MODE_CBC, iv)
    
    #Desencrypting and printing the message
    return cipher.decrypt(encData).decode('utf-8')




