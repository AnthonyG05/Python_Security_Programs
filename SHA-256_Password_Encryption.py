import hashlib 
import csv
import string
import secrets
import random
passwordList = []
def generate_sha256():
    with open("your_computer\\rainbow.csv", "w") as myFile:
        writer = csv.writer(myFile)
        writer.writerow(["password","sha256_hash"])
        for i in range(0,10):
            userInput = input(f"Please input 10 passwords. they must be 7 characters long {i + 1}: ")
            if len(userInput) < 7:
                print("The password you inputted is too short it must be 7 characters long!")
            else:
                passwordList.append(userInput)
                
        for passwords in passwordList:
            hashObject = hashlib.sha256(passwords.encode("utf-8"))
            hash_256 = hashObject.hexdigest()
            writer.writerow([passwords,hash_256])

def generate_sha256withSalt():
    with open("your_computer\\rainbow.csv", "r+") as myFile, \
        open("your_computer\\rainbow2.csv", "w+", newline="") as outfile:
        hashFile = csv.DictReader(myFile, delimiter=",")
        column_name=['PIN', 'SALT', 'Password_Hash']
        csvWriter = csv.writer(outfile)
        csvWriter.writerow(column_name)
        
        for row in hashFile: 
            hashValues = row["sha256_hash"]
            pin = random.randint(1, 999999)
            pinString = f"{pin:06}"    
            alphanumeric = string.ascii_letters + string.digits
            salt= ''.join(secrets.choice(alphanumeric) for i in range(8))
            hashCombined = f"{salt}{pinString}{salt}{hashValues}{salt}{pinString}{salt}"
            csvWriter.writerow([pinString, salt, hashCombined])

generate_sha256()
generate_sha256withSalt()
