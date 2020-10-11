from simplecrypt import  decrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    print(encrypted)

with open("passwords.txt", "r") as p:
    for s in p:
        try: print(decrypt(s.strip(), encrypted))
        except Exception as e: print(e)
        finally: print(s)
