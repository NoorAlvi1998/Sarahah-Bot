file=open("verified.txt",'r')
data=file.read().split('\n')
data=data[:len(data)-1]
file.close()
file2=open('ready.txt','a+')
for x in data:
    file2.write("#Trends #Sarahah\nhttp://"+x+'.sarahah.com\n')
file2.close()
