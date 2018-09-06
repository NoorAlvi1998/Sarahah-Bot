import pyautogui, time, pygame, tkinter


##file=open("D:\\Mymatrix2.txt");
##file_text=file.read();
##img_arr=[]
##img_arr2=file_text.split("\n")
##for x in range(len(img_arr2)):
##    img_arr.append(img_arr2[x].split(" "))
###print(img_arr[0])
##print(len(img_arr[1]))

root=tkinter.Tk()
root.withdraw()
tkinter.messagebox.showinfo("Please read me!", '''Hello Noor!
Something is going to happen right now.
Make sure you turn the volume up,
plug your earphones(not necessary),
and do not touch your keyboard or mouse after clicking 'OK'!
Press 'OK' when you are ready!''')
pygame.mixer.init()
pygame.mixer.music.load("sng")
pygame.mixer.music.play(loops=-1)
temp="hello"
toWrite='''Examination Hall,
City A.B.C.
A.B.C. School.
Respected ma'am!
	It is stated that today is your birthday. Therefore, I request you to please stay happy, leave all tensions aside, and feel relaxed. Because ma'am, everything is temporary but the good memories..... They last forever, and are a treasure for anyone!.... I am not giving you an advice(Sorry if it feels like that!), but I want you to keep smiling, live your life like a boss, and believe in yourself. .......... May you live a thousand years, with every year having a thousand days. 
Once Again,          
Happy Birthday!

Sincerely,
Hamza.'''
pyautogui.press("win")
pyautogui.typewrite("wordpad", interval=0.5)
time.sleep(3)
pyautogui.press("enter")
time.sleep(2)
pyautogui.typewrite(temp, interval=0.25)
pygame.mixer.music.stop()
pyautogui.hotkey('win','down')
pyautogui.hotkey('win','down')
tkinter.messagebox.showinfo("Read me if you want to!","Show Khatam! xD \n Now you can use your computer! :)")
