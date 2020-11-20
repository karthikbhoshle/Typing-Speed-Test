import tkinter
from tkinter import *
import random
import sys
##############
root=tkinter.Tk()
w = '#FFFFFF'
g = '#20FF0F'
lg = '#778899'
r = '#8B0000'
global word,user,t,k,sm
t=120
k=0
sm=StringVar()
word=['Computer','Science','Common','School','Impossible','Selection','Random','Python','Javascript','Function','Children',
      'Family','Mirzapur','Birthday','Independence day','Republic','Orange','Karnataka','Bengalure','Maharastra','Himalaya','Mountains',
      'Western-Ghats','Shivamogga','Badlapur','Election','Parliment','Assembly','Anaconda','Ayodhya','Hindustan','Subtitle','Episode','Bluetooth',
      'Government','Bulletin','Interview','Oxford','Confusion','Engagement','Member']
user=[]
#######################
def Quit():
    sys.exit()
def evaluate():
    frame1.destroy()
    frame2 = Frame(root, bg=w)
    frame2.pack(pady=5)
    Correct=0
    print(k-1)
    print(user)
    for i in range(k-1):
        print(i)
        print(word[i],user[i])
        if word[i]==user[i]:
            Correct+=1
    l1 = Label(frame2, text='Result.', justify='center',bg=w,fg=r, font='Courier 20 underline')
    l1.pack(pady=10)
    log_col = Label(frame2, text='', justify='center', width=100, bg=lg)  # , font='Courier 10')
    log_col.pack(pady=5)
    l1 = Label(frame2, text='Total Answered:= '+str(k-1), relief='solid', justify='center', font='Courier 12',
               bg=g)
    l1.pack(pady=10)
    l1 = Label(frame2, text='Correct Answer:= '+str(Correct), relief='solid', justify='center', font='Courier 12',
               bg=lg)
    l1.pack(pady=10)
    l1 = Label(frame2, text='Wrong Answer:= '+str(k-Correct-1), relief='solid', justify='center', font='Courier 12',
               bg=g)
    l1.pack(pady=10)
    l1 = Label(frame2, text='Score:= '+str(Correct*10), relief='solid', justify='center', font='Courier 12',
               bg=lg)
    l1.pack(pady=10)
    l1 = Label(frame2, text='WPM:= ' + str(int(k/2))+' wpm', relief='solid', justify='center', font='Courier 12',
               bg=g)
    l1.pack(pady=10)
    l6 = Button(frame2, text='Quit', font='Courier 12', activebackground=lg, relief='solid', bg=r, command=Quit)
    l6.pack(pady=10)
    log_col = Label(frame2, text='', justify='center', width=100, bg=r)  # , font='Courier 10')
    log_col.pack(pady=5)






def change(event):
    global l2,k,user

    user.append(sm.get())
    sm.set('')
    l2.config(text=word[k])
    k += 1
def time():
    global l5,t
    if t>0:
        t-=1
        l5.config(text='Time-Left\n' + str(t))

    if t==0:
        evaluate()
    l5.after(1000, time)

def Start():
    global k,l5,l1,l2,frame1
    random.shuffle(word)

    frame.destroy()
    frame1=Frame(root,bg=w)
    frame1.pack(pady=5)
    l1 = Label(frame1, text='Type Word And Hit Enter.',relief='solid', justify='center', font='Courier 12',
               bg=lg)
    l1.pack(pady=10)
    log_col = Label(frame1, text='', justify='center', width=100, bg=r)  # , font='Courier 10')
    log_col.pack(pady=5)
    l2 = Label(frame1, text=word[k],relief='solid', justify='center', font='Courier 12',bg=lg)
    l2.pack(pady=10)
    k+=1
    entry = Entry(frame1,text=sm, justify='center', font='Courier 12', width=30, bg=g)
    entry.pack(pady=5)
    log_col = Label(frame1, text='', justify='center', width=100, bg=r)  # , font='Courier 10')
    log_col.pack(pady=5)
    l5=Label(frame1, text='Total Time Left:-'+str(t),relief='solid', justify='center', font='Courier 12',bg=lg)
    l5.pack(pady=10)
    l6 = Button(frame1, text='Quit',font='Courier 12',activebackground=lg,relief='solid',bg=r,command=evaluate)
    l6.pack(pady=10)
    time()
    root.bind('<Return>', change)
    entry.focus_set()

    pass
#################################
root.title("Typing Speed Application")
root.geometry('700x600')
root.configure(background=w)
root.resizable(False,False)
l1=Label(root,text='Typing Speed Test using Python.',fg=r, bg=w,font='Courier 20 underline')
l1.pack(pady=5)
log_col = Label(root, text='', justify='center', width=100,bg=g)#, font='Courier 10')
log_col.pack(pady=5)
frame=Frame(root,bg=w)
frame.pack(pady=5)
l2=Label(frame,text='Read The Rules And\nClick Start Once You Are Ready.',justify='center',relief='solid',font='Courier 12',bg=lg)
l2.pack(pady=10)
m='The duration of the English type test will be 2 minutes.\nTry to not look at the keyboard while practicing.\n' \
  'Know the finger positions.\n Use the Shift keys.\nAll the best'
l3=Label(frame,text=m,justify='center',font='Courier 12',relief='solid',bg=lg)
l3.pack(pady=10)
b1=Button(frame,justify='center',text='Start',font='Courier 12',activebackground=lg,relief='solid',bg=r,command=Start)
b1.pack(pady=10)
log_col = Label(frame, text='', justify='center', width=100,bg=g)#, font='Courier 10')
log_col.pack(pady=5)
root.mainloop()