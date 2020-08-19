import simplecrypt

with open('encrypted.bin', 'rb') as inp:
    encrypted = inp.read()
with open("passwords.txt", "r") as pas:
    lst = pas.read().strip().split('\n') # strip() нужен для того что бы при split() не образовывался дополнительный пустой элемент в lst
    for i in lst:
        try:
            a = simplecrypt.decrypt(i, encrypted)
            
        except simplecrypt.DecryptionException:
            continue
        print(a.decode("utf-8"))        
# import simplecrypt

# encrypted = open("encrypted.bin", "rb").read()
# passwords = open("passwords.txt").readlines()

# for p in passwords:
#     p = p.strip()
#     try:
#         s = simplecrypt.decrypt(p, encrypted)
#     except simplecrypt.DecryptionException:
#         continue

#     print(s.decode("utf-8"))