from tkinter import *
from tkinter import messagebox
from random import randint

#GLOABAL VARIABLES
ActivePlayer=1
p1=[]# what player one selected
p2=[]# what player rwo selected
Count=0
ScoreX=0
ScoreO=0

root=Tk()
root.title("Tic Tac Toe : Player 1")
root.config(bg='light blue')

label1=Label(root,text='Tic Tac Toe',font="Times 15 bold",bg='#4649FF',fg='white',bd=4,height=2,width=10,relief=RAISED,)
label1.grid(row=0,column=2,padx=5,pady=5,sticky='nsnew')

label2=Label(root,text=f'Score Player 1 : {ScoreX}',font="Times 15 bold",bg='#3CCF4E',fg='black',bd=4,height=1,width=10,relief=RAISED,)
label2.grid(row=0,column=0, padx=5,pady=5,sticky='nsnew')

label5=Label(root,text=f'Score Player 2 : {ScoreO}',font="Times 15 bold",bg='#3CCF4E',fg='black',bd=4,height=1,width=10,relief=RAISED,)
label5.grid(row=0,column=4, padx=5,pady=5,sticky='nsnew')

label3=Label(root,text='PLAYER 1',font="Times 15 bold",bg='#EDE4E0',fg='black',bd=4,height=2,width=10,relief=RAISED,)
label3.grid(row=0,column=1,padx=5,pady=5,sticky='nsnew')

label4=Label(root,text='PLAYER 2',font="Times 15 bold",bg='#E6CBA8',fg='black',bd=4,height=2,width=10,relief=RAISED,)
# label4.grid(row=0,column=3,padx=5,pady=5,sticky='nsnew')


#BUTTONS
b1=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b1.grid(row=1,column=0,padx=5,pady=5,sticky='snew')
b1.config(command=lambda:ButtonClick(1))

b2=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b2.grid(row=1,column=1,padx=5,pady=5,sticky='snew')
b2.config(command=lambda:ButtonClick(2))

b3=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b3.grid(row=1,column=2,padx=5,pady=5,sticky='snew')
b3.config(command=lambda:ButtonClick(3))

b4=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b4.grid(row=1,column=3,padx=5,pady=5,sticky='snew')
b4.config(command=lambda:ButtonClick(4))

b5=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b5.grid(row=1,column=4,padx=5,pady=5,sticky='snew')
b5.config(command=lambda:ButtonClick(5))

b6=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b6.grid(row=2,column=0,padx=5,pady=5,sticky='snew')
b6.config(command=lambda:ButtonClick(6))

b7=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b7.grid(row=2,column=1,padx=5,pady=5,sticky='snew')
b7.config(command=lambda:ButtonClick(7))

b8=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b8.grid(row=2,column=2,padx=5,pady=5,sticky='snew')
b8.config(command=lambda:ButtonClick(8))

b9=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b9.grid(row=2,column=3,padx=5,pady=5,sticky='snew')
b9.config(command=lambda:ButtonClick(9))

b10=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b10.grid(row=2,column=4,padx=5,pady=5,sticky='snew')
b10.config(command=lambda:ButtonClick(10))

b11=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b11.grid(row=3,column=0,padx=5,pady=5,sticky='snew')
b11.config(command=lambda:ButtonClick(11))

b12=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b12.grid(row=3,column=1,padx=5,pady=5,sticky='snew')
b12.config(command=lambda:ButtonClick(12))

b13=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b13.grid(row=3,column=2,padx=5,pady=5,sticky='snew')
b13.config(command=lambda:ButtonClick(13))

b14=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b14.grid(row=3,column=3,padx=5,pady=5,sticky='snew')
b14.config(command=lambda:ButtonClick(14))

b15=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b15.grid(row=3,column=4,padx=5,pady=5,sticky='snew')
b15.config(command=lambda:ButtonClick(15))

b16=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b16.grid(row=4,column=0,padx=5,pady=5,sticky='snew')
b16.config(command=lambda:ButtonClick(16))

b17=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b17.grid(row=4,column=1,padx=5,pady=5,sticky='snew')
b17.config(command=lambda:ButtonClick(17))

b18=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b18.grid(row=4,column=2,padx=5,pady=5,sticky='snew')
b18.config(command=lambda:ButtonClick(18))

b19=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b19.grid(row=4,column=3,padx=5,pady=5,sticky='snew')
b19.config(command=lambda:ButtonClick(19))

b20=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b20.grid(row=4,column=4,padx=5,pady=5,sticky='snew')
b20.config(command=lambda:ButtonClick(20))

b21=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b21.grid(row=5,column=0,padx=5,pady=5,sticky='snew')
b21.config(command=lambda:ButtonClick(21))

b22=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b22.grid(row=5,column=1,padx=5,pady=5,sticky='snew')
b22.config(command=lambda:ButtonClick(22))

b23=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b23.grid(row=5,column=2,padx=5,pady=5,sticky='snew')
b23.config(command=lambda:ButtonClick(23))

b24=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b24.grid(row=5,column=3,padx=5,pady=5,sticky='snew')
b24.config(command=lambda:ButtonClick(24))

b25=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b25.grid(row=5,column=4,padx=5,pady=5,sticky='snew')
b25.config(command=lambda:ButtonClick(25))

# Button Restart
b26=Button(root,text='RESTART',font="Times 15 bold",bg='#F0C929',fg='black',width=12)
b26.grid(row=6,column=0,padx=5,pady=5,sticky='snew')
b26.config(command=lambda:Restart())

# Button End
b27=Button(root,font="Times 15 bold",text='END',bg='#FF5D5D',fg='white',height=2,width=10)
b27.grid(row=6,column=4,padx=5,pady=5,sticky='snew')
b27.config(command=lambda:game_terminate())

def game_terminate():
    root.destroy()

def Restart():
    global label3
    global label4
    global ActivePlayer
    ActivePlayer=1
    
    global Count
    Count=0

    label3.destroy()
    label4.destroy()

    root.title("Tic Tac Toe : Player 1")

    label3=Label(root,text='PLAYER 1',font="Times 15 bold",bg='#EDE4E0',fg='black',bd=4,height=2,width=10,relief=RAISED,)
    label3.grid(row=0,column=1,padx=5,pady=5,sticky='nsnew')

    b1['state']='active'
    b1['text']=''
    b1['bg']='white'
    b2['state']='active'
    b2['text']=''
    b2['bg']='white'
    b3['state']='active'
    b3['text']=''
    b3['bg']='white'
    b4['state']='active'
    b4['text']=''
    b4['bg']='white'
    b5['state']='active'
    b5['text']=''
    b5['bg']='white'
    b6['state']='active'
    b6['text']=''
    b6['bg']='white'
    b7['state']='active'
    b7['text']=''
    b7['bg']='white'
    b8['state']='active'
    b8['text']=''
    b8['bg']='white'
    b9['state']='active'
    b9['text']=''
    b9['bg']='white'
    b10['state']='active'
    b10['text']=''
    b10['bg']='white'
    b11['state']='active'
    b11['text']=''
    b11['bg']='white'
    b12['state']='active'
    b12['text']=''
    b12['bg']='white'
    b13['state']='active'
    b13['text']=''
    b13['bg']='white'
    b14['state']='active'
    b14['text']=''
    b14['bg']='white'
    b15['state']='active'
    b15['text']=''
    b15['bg']='white'
    b16['state']='active'
    b16['text']=''
    b16['bg']='white'
    b17['state']='active'
    b17['text']=''
    b17['bg']='white'
    b18['state']='active'
    b18['text']=''
    b18['bg']='white'
    b19['state']='active'
    b19['text']=''
    b19['bg']='white'
    b20['state']='active'
    b20['text']=''
    b20['bg']='white'
    b21['state']='active'
    b21['text']=''
    b21['bg']='white'
    b22['state']='active'
    b22['text']=''
    b22['bg']='white'
    b23['state']='active'
    b23['text']=''
    b23['bg']='white'
    b24['state']='active'
    b24['text']=''
    b24['bg']='white'
    b25['state']='active'
    b25['text']=''
    b25['bg']='white'
    p1.clear()
    p2.clear()

def game_ended():
    
    global Count
    Count=0

    b1['state']='disable'
    b1['text']=''
    b2['state']='disable'
    b2['text']=''
    b3['state']='disable'
    b3['text']=''
    b4['state']='disable'
    b4['text']=''
    b5['state']='disable'
    b5['text']=''
    b6['state']='disable'
    b6['text']=''
    b7['state']='disable'
    b7['text']=''
    b8['state']='disable'
    b8['text']=''
    b9['state']='disable'
    b9['text']=''
    b10['state']='disable'
    b10['text']=''
    b11['state']='disable'
    b11['text']=''
    b12['state']='disable'
    b12['text']=''
    b13['state']='disable'
    b13['text']=''
    b14['state']='disable'
    b14['text']=''
    b15['state']='disable'
    b15['text']=''
    b16['state']='disable'
    b16['text']=''
    b17['state']='disable'
    b17['text']=''
    b18['state']='disable'
    b18['text']=''
    b19['state']='disable'
    b19['text']=''
    b20['state']='disable'
    b20['text']=''
    b21['state']='disable'
    b21['text']=''
    b22['state']='disable'
    b22['text']=''
    b23['state']='disable'
    b23['text']=''
    b24['state']='disable'
    b24['text']=''
    b25['state']='disable'
    b25['text']=''
    p1.clear()
    p2.clear()
        

def ButtonClick(id):

    global label3
    global label4
    global ActivePlayer
    global p15
    global p2
    if ActivePlayer==1:
        label3.destroy()
        SetLayout(id,"X","#EDE4E0")
        p1.append(id)

        label4=Label(root,text='PLAYER 2',font="Times 15 bold",bg='#E6CBA8',fg='black',bd=4,height=2,width=10,relief=RAISED,)
        label4.grid(row=0,column=3,padx=5,pady=5,sticky='nsnew')

        root.title("Tic Tac Toe : Player 2")
        ActivePlayer=2
        print(f"P1:{p1}")

    else:
        label4.destroy()
        SetLayout(id,"O","#E6CBA8")
        p2.append(id)

        label3=Label(root,text='PLAYER 1',font="Times 15 bold",bg='#EDE4E0',fg='black',bd=4,height=2,width=10,relief=RAISED,)
        label3.grid(row=0,column=1,padx=5,pady=5,sticky='nsnew')

        root.title("Tic Tac Toe : Player 1")
        ActivePlayer=1
        print(f"P2:{p2}")
    # if Count==5 or Count>5:
    if Count>5:
        CheckWiner()

def SetLayout(id,PlayerSymbol,colr):

    global Count
    if id==1:
        b1['text']=PlayerSymbol
        b1['state']='disabled'
        b1['bg']=colr
        b1['fg']='black'
        Count = Count+1

    elif id==2:
        b2['text']=PlayerSymbol
        b2['state']='disable'
        b2['bg']=colr
        Count= Count+1

    elif id==3:
        b3['text']=PlayerSymbol
        b3['state']='disable'
        b3['bg']=colr
        Count= Count+1

    elif id==4:
        b4['text']=PlayerSymbol
        b4['state']='disable'
        b4['bg']=colr
        Count=Count+1

    elif id==5:
        b5['text']=PlayerSymbol
        b5['state']='disable'
        b5['bg']=colr
        Count= Count+1

    elif id==6:
        b6['text']=PlayerSymbol
        b6['state']='disable'
        b6['bg']=colr
        Count= Count+1

    elif id==7:
        b7['text']=PlayerSymbol
        b7['state']='disable'
        b7['bg']=colr
        Count= Count+1

    elif id==8:
        b8['text']=PlayerSymbol
        b8['state']='disable'
        b8['bg']=colr
        Count= Count+1

    elif id==9:
        b9['text']=PlayerSymbol
        b9['state']='disable'
        b9['bg']=colr
        Count= Count+1

    elif id==10:
        b10['text']=PlayerSymbol
        b10['state']='disable'
        b10['bg']=colr
        Count= Count+1

    elif id==11:
        b11['text']=PlayerSymbol
        b11['state']='disable'
        b11['bg']=colr
        Count= Count+1

    elif id==12:
        b12['text']=PlayerSymbol
        b12['state']='disable'
        b12['bg']=colr
        Count= Count+1

    elif id==13:
        b13['text']=PlayerSymbol
        b13['state']='disable'
        b13['bg']=colr
        Count= Count+1

    elif id==14:
        b14['text']=PlayerSymbol
        b14['state']='disable'
        b14['bg']=colr
        Count= Count+1
        
    elif id==15:
        b15['text']=PlayerSymbol
        b15['state']='disable'
        b15['bg']=colr
        Count= Count+1
        
    elif id==16:
        b16['text']=PlayerSymbol
        b16['state']='disable'
        b16['bg']=colr
        Count= Count+1

    elif id==17:
        b17['text']=PlayerSymbol
        b17['state']='disable'
        b17['bg']=colr
        Count= Count+1

    elif id==18:
        b18['text']=PlayerSymbol
        b18['state']='disable'
        b18['bg']=colr
        Count= Count+1

    elif id==19:
        b19['text']=PlayerSymbol
        b19['state']='disable'
        b19['bg']=colr
        Count= Count+1

    elif id==20:
        b20['text']=PlayerSymbol
        b20['state']='disable'
        b20['bg']=colr
        Count= Count+1

    elif id==21:
        b21['text']=PlayerSymbol
        b21['state']='disable'
        b21['bg']=colr
        Count= Count+1

    elif id==22:
        b22['text']=PlayerSymbol
        b22['state']='disable'
        b22['bg']=colr
        Count= Count+1

    elif id==23:
        b23['text']=PlayerSymbol
        b23['state']='disable'
        b23['bg']=colr
        Count= Count+1

    elif id==24:
        b24['text']=PlayerSymbol
        b24['state']='disable'
        b24['bg']=colr
        Count= Count+1

    elif id==25:
        b25['text']=PlayerSymbol
        b25['state']='disable'
        b25['bg']=colr
        Count= Count+1

def AssignSeperateColorToWiner(id):
    # Rows
    if id=='R1':
        b1['bg']='light green'
        b2['bg']='light green'
        b3['bg']='light green'
        b4['bg']='light green'
        b5['bg']='light green'
    if id=='R2':
        b6['bg']='light green'
        b7['bg']='light green'
        b8['bg']='light green'
        b9['bg']='light green'
        b10['bg']='light green'
    if id=='R3':
        b11['bg']='light green'
        b12['bg']='light green'
        b13['bg']='light green'
        b14['bg']='light green'
        b15['bg']='light green'
    if id=='R4':
        b16['bg']='light green'
        b17['bg']='light green'
        b18['bg']='light green'
        b19['bg']='light green'
        b20['bg']='light green'
    if id=='R5':
        b21['bg']='light green'
        b22['bg']='light green'
        b23['bg']='light green'
        b24['bg']='light green'
        b25['bg']='light green'

    # Columns
    if id=='C1':
        b1['bg']='light green'
        b6['bg']='light green'
        b11['bg']='light green'
        b16['bg']='light green'
        b21['bg']='light green'
    if id=='C2':
        b2['bg']='light green'
        b7['bg']='light green'
        b12['bg']='light green'
        b17['bg']='light green'
        b22['bg']='light green'
    if id=='C3':
        b3['bg']='light green'
        b8['bg']='light green'
        b13['bg']='light green'
        b18['bg']='light green'
        b23['bg']='light green'
    if id=='C4':
        b4['bg']='light green'
        b9['bg']='light green'
        b14['bg']='light green'
        b19['bg']='light green'
        b24['bg']='light green'
    if id=='C5':
        b5['bg']='light green'
        b10['bg']='light green'
        b15['bg']='light green'
        b20['bg']='light green'
        b25['bg']='light green'

    # Diagonals
    if id=='D1':
        b1['bg']='light green'
        b7['bg']='light green'
        b13['bg']='light green'
        b19['bg']='light green'
        b25['bg']='light green'
    if id=='D2':
        b21['bg']='light green'
        b17['bg']='light green'
        b13['bg']='light green'
        b9['bg']='light green'
        b5['bg']='light green'
    

def CheckWiner():
    global ScoreX
    global ScoreO
    Winer=-1
    #Rows
    if ( (1 in p1) and (2 in p1) and (3 in p1) and (4 in p1) and (5 in p1) ):
        Winer=1
        AssignSeperateColorToWiner('R1')
    if ( (1 in p2) and (2 in p2) and (3 in p2) and (4 in p2) and (5 in p2) ):
        Winer=2
        AssignSeperateColorToWiner('R1')

    if ( (6 in p1) and (7 in p1) and (8 in p1) and (9 in p1) and (10 in p1)):
        Winer=1
        AssignSeperateColorToWiner('R2')
    if ( (6 in p2) and (7 in p2) and (8 in p2) and (9 in p2) and (10 in p2)):
        Winer=2
        AssignSeperateColorToWiner('R2')

    if ( (11 in p1) and (12 in p1) and (13 in p1) and (14 in p1) and (15 in p1)):
        Winer=1
        AssignSeperateColorToWiner('R3')
    if ( (11 in p2) and (12 in p2) and (13 in p2) and (14 in p2) and (15 in p2)):
        Winer=2
        AssignSeperateColorToWiner('R3')

    if ( (16 in p1) and (17 in p1) and (18 in p1) and (19 in p1) and (20 in p1)):
        Winer=1
        AssignSeperateColorToWiner('R4')
    if ( (16 in p2) and (17 in p2) and (18 in p2) and (19 in p2) and (20 in p2)):
        Winer=2
        AssignSeperateColorToWiner('R4')
    
    if ( (21 in p1) and (22 in p1) and (23 in p1) and (24 in p1) and (25 in p1)):
        Winer=1
        AssignSeperateColorToWiner('R5')
    if ( (21 in p2) and (22 in p2) and (23 in p2) and (24 in p2) and (25 in p2)):
        Winer=2
        AssignSeperateColorToWiner('R5')

    #Columns
    if ( (1 in p1) and (6 in p1) and (11 in p1) and (16 in p1) and (21 in p1)):
        Winer=1
        AssignSeperateColorToWiner('C1')
    if ( (1 in p2) and (6 in p2) and (11 in p2) and (16 in p2) and (21 in p2) ):
        Winer=2
        AssignSeperateColorToWiner('C1')

    if ( (2 in p1) and (7 in p1) and (12 in p1) and (17 in p1) and (22 in p1) ):
        Winer=1
        AssignSeperateColorToWiner('C2')
    if ( (2 in p2) and (7 in p2) and (12 in p2) and (17 in p2) and (22 in p2) ):
        Winer=2
        AssignSeperateColorToWiner('C2')

    if ( (3 in p1) and (8 in p1) and (13 in p1) and (18 in p1) and (23 in p1)):
        Winer=1
        AssignSeperateColorToWiner('C3')
    if ( (3 in p2) and (8 in p2) and (13 in p2) and (18 in p2) and (23 in p2) ):
        Winer=2
        AssignSeperateColorToWiner('C3')
        
    if ( (4 in p1) and (9 in p1) and (14 in p1) and (19 in p1) and (24 in p1)):
        Winer=1
        AssignSeperateColorToWiner('C4')
    if ( (4 in p2) and (9 in p2) and (14 in p2) and (19 in p2) and (24 in p2) ):
        Winer=2
        AssignSeperateColorToWiner('C4')

    if ( (5 in p1) and (10 in p1) and (15 in p1) and (20 in p1) and (25 in p1)):
        Winer=1
        AssignSeperateColorToWiner('C5')
    if ( (5 in p2) and (10 in p2) and (15 in p2) and (20 in p2) and (25 in p2) ):
        Winer=2
        AssignSeperateColorToWiner('C5')

    #Diagonals
    if ( (1 in p1) and (7 in p1) and (13 in p1) and (19 in p1) and (25 in p1) ):
        Winer=1
        AssignSeperateColorToWiner('D1')
    if ( (1 in p2) and (7 in p2) and (13 in p2) and (19 in p2) and (25 in p2)):
        Winer=2
        AssignSeperateColorToWiner('D1')

    if ( (21 in p1) and (17 in p1) and (13 in p1) and (9 in p1) and (5 in p1) ):
        Winer=1
        AssignSeperateColorToWiner('D2')
    if ( (21 in p2) and (17 in p2) and (13 in p2) and (9 in p2) and (5 in p2) ):
        Winer=2
        AssignSeperateColorToWiner('D2')

    #check
    if Winer==1:
        messagebox.showinfo(title="Congrat.",message="Player 1 is the winner")
        ScoreX+=1
        label2['text']=f'Score Player 1 : {ScoreX}'
        game_ended()
    elif Winer==2:
        messagebox.showinfo(title="Congrat.",message="Player 2 is the winner")
        ScoreO+=1
        label5['text']=f'Score Player 2 : {ScoreO}'
        game_ended()
    elif Winer==-1 and Count==25:
        messagebox.showinfo(title="Oops!!",message="Match is Draw")
        game_ended()

for i in range(1,6):
    root.grid_rowconfigure(i,weight=1)

for i in range(5):
    root.grid_columnconfigure(i,weight=1)

def enter_function(event):
    b26.invoke()
root.bind('<Return>',enter_function)


root.mainloop()
