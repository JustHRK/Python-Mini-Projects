import random
def randchars():
    s=""
    for i in range(3):
        a=random.randint(97,122)
        s+=chr(a)
    return s
    

#Encryption
str=input("Enter Your Message : ")

msg=str.split()
encrypted_msg=""
for i in msg:
    if (len(i)<=3):
        encrypted_msg+=i[::-1]
    else:
        encrypted_msg=encrypted_msg+randchars()+(i[1:]+i[0])+randchars()
    encrypted_msg+=" "

print("\nThe Encrypted Message is :")
print(encrypted_msg)

#Decryption

msg=encrypted_msg.split()
decrypted_msg=""
for i in msg:
    if(len(i)<=3):
        decrypted_msg+=i[::-1]
    else:
        decrypted_msg+=(i[-4]+i[3:-4])
    decrypted_msg+=" "

print("\nThe Decrypted Message is :")
print(decrypted_msg)