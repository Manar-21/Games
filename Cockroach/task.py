'''
    import libraries
'''
import numpy as np                                  #import numpy module to do array and choose random number                  
from tkinter import *                               #import all module inside tkinter
from PIL import Image, ImageTk                      #import pillow module and related module like

def rando(room_row, room_col, rand, n):
    ''' A function: Returns the new
        row and column number to
        which the cockroach will move
    '''
    if (room_row!=0)and(room_col!=0):
        if (room_row==(n-1))and(room_col==(n-1)):
            if (rand==3):
                room_row = room_row-1
            elif (rand==4):
                room_row = room_row-1
                room_col = room_col-1
            elif (rand==5):
                room_col = room_col-1     
        elif (room_row==(n-1)):
            if (rand==1):
                room_col = room_col+1
            elif (rand==2):
                room_row = room_row-1
                room_col = room_col+1
            elif (rand==3):
                room_row = room_row-1
            elif (rand==4):
                room_row = room_row-1
                room_col = room_col-1
            elif (rand==5):
                room_col = room_col-1  
        elif (room_col==(n-1)):
            if (rand==3):
                room_row = room_row-1
            elif (rand==4):
                room_row = room_row-1
                room_col = room_col-1
            elif (rand==5):
                room_col = room_col-1
            elif (rand==6):
                room_row = room_row+1
                room_col = room_col-1
            elif (rand==7):
                room_row = room_row+1
            
        else :
            if (rand==1):
                room_col = room_col+1
            elif (rand==2):
                room_row = room_row-1
                room_col = room_col+1
            elif (rand==3):
                room_row = room_row-1
            elif (rand==4):
                room_row = room_row-1
                room_col = room_col-1
            elif (rand==5):
                room_col = room_col-1
            elif (rand==6):
                room_row = room_row+1
                room_col = room_col-1
            elif (rand==7):
                room_row = room_row+1
            elif (rand==8):
                room_row = room_row+1
                room_col = room_col+1
                
    else :     
        if (room_row==0)and(room_col==0):
            if (rand==1):
                room_col = room_col+1
            elif (rand==7):
                room_row = room_row+1
            elif(rand==8):
                room_row = room_row+1
                room_col = room_col+1
        elif (room_row==0 and room_col==(n-1)):
            if (rand==5):
                room_col = room_col-1
            elif (rand==6):
                room_row = room_row+1
                room_col = room_col-1
            elif (rand==7):
                room_row = room_row+1     
        elif (room_row==(n-1) and room_col==0):
            if (rand==1):
                room_col = room_col+1
            elif (rand==2):
                room_row = room_row-1
                room_col = room_col+1
            elif (rand==3):
                room_row = room_row-1
        elif (room_row==0):
            if (rand==5):
                room_col = room_col-1
            elif (rand==6):
                room_row = room_row+1
                room_col = room_col-1
            elif (rand==7):
                room_row = room_row+1
            elif (rand==8):
                room_row = room_row+1
                room_col = room_col+1
        else :  # room_col==0
            if (rand==1):
                room_col = room_col+1
            elif (rand==2):
                room_row = room_row-1
                room_col = room_col+1
            elif (rand==3):
                room_row = room_row-1
            elif (rand==7):
                room_row = room_row+1
            elif (rand==8):
                room_row = room_row+1
                room_col = room_col+1  
    return room_row, room_col

def process(n):
    ''' A function: Returns
        The sum of random numbers 
    '''
    global label
    for i in range(n):
        for j in range(n):
            label = Label(root, text=0, font=("Helvetice", 15), width=4).grid(row=i+1 ,column=j+1)

    room = np.array([[0]*n]*n)
    room_row, room_col = np.random.randint(0,n) , np.random.randint(0,n)       # index [1 - 9]
    while (True):
        if (np.all(room!=0)):
            break
        rand = np.random.randint(1,9)
        room_row, room_col = rando(room_row, room_col, rand, n)
        room[room_row][room_col] = room[room_row][room_col] + 1
        label = Label(root, text=room[room_row][room_col], font=("Helvetice", 15), height=1, width=4).grid(row=(room_row+1) ,column=(room_col+1))
    label = Label(root, text=room[room_row][room_col], font=("Helvetice", 15), height=1, width=4, bg='#663300').grid(row=room_row+1 ,column=room_col+1)
    label2 = Label(root, text=sum(sum(room)), font=("Helvetice", 15), bg='#006666', width=4).grid(row=0 ,column=2)

def Delete(n):
    ''' A function: Delete
        the extra label
    '''
    if (n==0):
        return
    if (n==1):
        return
    for label in root.grid_slaves():
        if int(label.grid_info()["column"]) >= n:
          label.grid_forget()
    for label in root.grid_slaves():
        if int(label.grid_info()["row"]) >= n:
            label.grid_forget()

def click():
    '''
     A function: getting
        the number that was
        entered in the entry
        ,Call the Delete
        to delete the extra label
        and process function
        to build a new labels
    '''    
    try:
        current = int(entry.get())
        Delete(current)
        process(current)
    except:
        pass

############################################################################
###################### The beginning of the program ########################
############################################################################

### GUI ###
    
root = Tk()
root.title("Cockroach Task")
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
label1 = Label(root, text="Enter number", font=("Helvetice", 15), bg='#a3c2c2', width=10).grid(row=0, column=0)
entry = Entry(root, font=("Helvetice", 15), width=4)
entry.grid(row=0, column=1)
button = Button(root, text="Start", font=("Helvetice", 15), bg='#cc6600', width=10, command=click).grid(row=1, column=0)
label2 = Label(root, text="SUM",  font=("Helvetice", 15), bg='#006666', width=4).grid(row=0, column=2)

root.mainloop()











