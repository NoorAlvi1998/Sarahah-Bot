from bs4 import BeautifulSoup
from urllib.request import urlopen

usernames=open("accounts.txt","r")
names_data=usernames.read()
usernames.close()
names=names_data.split("\n")
names=names[0:len(names)-1]
count=1
verified_names=[]
verified_file=open("verified.txt","a+")
already_verified=verified_file.read()
for x in names:
    page=urlopen("http://"+x+".sarahah.com")
    bsObj_data=BeautifulSoup(page.read()).get_text()
    if "constructive message" in bsObj_data and x not in already_verified:
        print(x+" Exists")
        verified_names.append(x)
        verified_file.write(x+"\n")
        count+=1
        print(str(count)+" Accounts Verified")
    else:
        print(x+"doesn't exist")
verified_file.close()
print(count)
