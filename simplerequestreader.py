import requests
r  = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
print(r.text.strip())
while r.text[0:2] != "We":
    print(r.text[0:2])
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r.text.strip())
    print(r.text)
print(r.text)