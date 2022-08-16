#Ecnrypt By GarudaID
#Author : ClarityCode

def Encrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open("GarudaID-" + filename, "wb")
    file.write(data)
    file.close()
    
def Decrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open(filename, "wb")
    file.write(data)
    file.close()
    

choice = ""
while choice != "3":
    print("[ID] : Pilih File anda untuk di Encrypt atau Decrypt\n[ENG]: Choise ur file for Encrypt or Decrypt\nNoted: Place this file Encrypt in same folder wat u Encrypt.")
    print("===================================================")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Quit")
    choice = input()
    if choice == "1" or choice == "2":
        key = int(input("[GarudaID]: Enter a key 1-40!\n"))
        filename = input("[GarudaID]: Enter filename want you Encrypt with extension:\n[GarudaID]: Example: garudaid.py\n")
    if choice == "1":
        Encrypt(filename, key)
    if choice == "2":
        Decrypt(filename, key)