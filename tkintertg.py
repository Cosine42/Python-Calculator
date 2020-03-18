from tkinter import*
from functools import partial

i=0
history=[]

def setDisplay(s):
     text = displayEntry.get()
     
     if text=='Error' or text=='':
          Clear()
          
     text = displayEntry.get()
          
     last = text[-1]
     if last in ('+','-','*','/') and s in ('+','-','*','/'):
          pass
          
     else:
          displayEntry.insert(END, s)

def Evaluate():
     try:
          expr = displayEntry.get()
          displayEntry.delete(0,END)
          displayEntry.insert(END, eval(expr))
          history.insert(END, displayEntry.get())
          history.see(END)
               
     except:
          displayEntry.delete(0,END)
          displayEntry.insert(END, 'Error')
   
          

def Clear():
     displayEntry.delete(0,END)
     displayEntry.insert(END,' ')

def Del():
     if displayEntry.get()=='Error':
          Clear()
     displayEntry.delete(  len(displayEntry.get())-1  )
     if displayEntry.get()=='':
          displayEntry.insert(END,' ')
     



root=Tk()
root.config(width=400, height=600)






displayFrame = Frame(root, bg='black')
displayFrame.place(relwidth=1, relheight=0.15)

displayEntry=Entry(displayFrame, font=84, justify=RIGHT)
displayEntry.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.8, anchor=CENTER)
Clear()

keypad = Frame(root, bg='wheat')
keypad.place(rely=0.18, relwidth=1, relheight=0.82)

#DELS

buttAC=Button(root, text='AC', command=Clear )
buttAC.place(rely=0.2,  relwidth=0.20, height=50)

buttDel=Button(root, text='Del', command=Del )
buttDel.place(rely=0.2, relx=0.5, relwidth=0.20, height=50)


#1st ROW

butt1=Button(root, text='1', command=partial(setDisplay,'1'))
butt1.place(rely=0.3,  relwidth=0.20, height=50)

butt2=Button(root, text='2', command=partial(setDisplay,'2'))
butt2.place(rely=0.3, relx=0.25, relwidth=0.20, height=50)

butt3=Button(root, text='3', command=partial(setDisplay,'3'))
butt3.place(rely=0.3, relx=0.5, relwidth=0.20, height=50)

#2nd ROW
 
butt4=Button(root, text='4', command=partial(setDisplay,'4') )
butt4.place(rely=0.5, relwidth=0.20, height=50)

butt5=Button(root, text='5', command=partial(setDisplay,'5'))
butt5.place(rely=0.5, relx=0.25, relwidth=0.20, height=50)

butt6=Button(root, text='6', command=partial(setDisplay,'6'))
butt6.place(rely=0.5, relx=0.5, relwidth=0.20, height=50)

#3rd ROW

butt7=Button(root, text='7', command=partial(setDisplay,'7'))
butt7.place(rely=0.7, relwidth=0.20, height=50)

butt8=Button(root, text='8', command=partial(setDisplay,'8'))
butt8.place(rely=0.7, relx=0.25, relwidth=0.20, height=50)

butt9=Button(root, text='9', command=partial(setDisplay,'9'))
butt9.place(rely=0.7, relx=0.5, relwidth=0.20, height=50)

#ZERO

butt0=Button(root, text='0', command=partial(setDisplay,'0'))
butt0.place(rely=0.9, relwidth=0.20, height=50)

#OPERATORS

buttPlus=Button(root, text='+', command=partial(setDisplay,'+'))
buttPlus.place(rely=0.9, relx=0.75, relwidth=0.20, height=50)

buttPlus=Button(root, text='-', command=partial(setDisplay,'-'))
buttPlus.place(rely=0.7, relx=0.75, relwidth=0.20, height=50)

buttPlus=Button(root, text='*', command=partial(setDisplay,'*'))
buttPlus.place(rely=0.5, relx=0.75, relwidth=0.20, height=50)

buttPlus=Button(root, text='/', command=partial(setDisplay,'/'))
buttPlus.place(rely=0.3, relx=0.75, relwidth=0.20, height=50)

#EQUALS

buttEquals=Button(root, text='=', command=Evaluate)
buttEquals.place(rely=0.9, relx=0.5, relwidth=0.20, height=50)

#HISTORY

history=Listbox(root, bg='lightgreen', font=32, bd=2) 

history.place(rely=0.15,relwidth=1, relheight=0.05)



root.mainloop()

print(history)
