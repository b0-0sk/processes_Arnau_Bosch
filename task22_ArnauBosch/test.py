from RSA_Key_Generate import *

"""
    RSA
"""
#1
key = GeneratePublicAndPrivateKey()
print(key.exportKey())

#2

# Private key
ExportPublicORPrivateKeyToAFile("private_key", key)

# Public key
ExportPublicORPrivateKeyToAFile("public_key", key.publickey())

#3
private_key = ImportPublicORPrivateKeyFromAFile("private_key.pem")
print("PRIVATE KEY:" + str(private_key))

public_key = ImportPublicORPrivateKeyFromAFile("public_key.pem")
print("PUBLIC KEY:" + str(public_key))

#4
encData = EncryptingDataWithRSA('Fins els collons de la pracitca', public_key)
print(str(encData))


#5
desData = DesencryptingDataWithRSA(encData,private_key)
print("Message: " + str(desData))

"""

    SHA256 

"""
#6
sha256Key = GeneratingSHA256Key()
print(sha256Key)


#7
ivPlusEncData = EncryptingDataWithAES("Vols funcionar de una vegada", sha256Key)
print("IVivPlusEncData :" + str(ivPlusEncData))

#8
desData = DesencryptingDataWithAES(ivPlusEncData , sha256Key)
print("The message is: " + desData)




