from tkinter import *
import tkinter.messagebox as tkMessageBox
from tkinter.filedialog import askopenfilename
import docx2txt
from os import listdir
from os.path import isfile, join, dirname, abspath


file_path = dirname(abspath(__file__))+"\documents"
onlyfiles = [f for f in listdir(file_path) if isfile(join(file_path, f))]

def _on_click(event):
    textbox1.tag_config("n", foreground="red")
    textbox1.insert("insert lineend","\nHello to you too.","n")

def fix():
    textbox1.tag_config("n", foreground="red")
    textbox1.insert("insert lineend", "\nHello to you too.", "n")

def insert_file():
    filename = askopenfilename()
    try:
        my_text = docx2txt.process(filename).encode('utf-8').decode('cp437').split('\n')
        for i in range(len(my_text)):
            textbox1.insert(INSERT, my_text[i] + "\n")
            document_name["text"] = filename
    except Exception as e:
        tkMessageBox.showinfo("Error!!", e)

def list_of_file():
    top = Toplevel(window)
    scrollbar1 = Scrollbar(top)
    scrollbar1.pack(side=RIGHT, fill=Y)
    top.title("Please choose file from below.")
    Lb1 = Listbox(top,width=50,height=30)
    number = 1
    for i in onlyfiles:
        Lb1.insert(number, i)
        number = number+1
    Lb1.pack()
    Lb1.bind('<ButtonRelease-1>',lambda e: CurSelet(Lb1,top))
    scrollbar1.config(command=Lb1.yview)

def CurSelet(Lbl,top):
    value="documents/"+str((Lbl.get(ACTIVE)))
    try:
        my_text = docx2txt.process(value).encode('utf-8').decode('cp437').split('\n')
        for i in range(len(my_text)):
            textbox1.insert(INSERT, my_text[i] + "\n")
            document_name["text"] = value
    except Exception as e:
        tkMessageBox.showinfo("Error!!", e)

    top.withdraw()



def meteprofilling():
    try:
        my_text = docx2txt.process(document_name.cget("text")).encode('utf-8').decode('cp437').split('\n')
        textbox2.tag_config("n", background="yellow", foreground="red")
        keyword = []

        for a in my_text:
            test = a.split(" ")
            join_word = test[0] + " " + test[1]
            if join_word not in keyword:
                keyword.append(join_word)

        for a in keyword:
            textbox2.insert(INSERT, "Keyword: "+a+"\n","n")
            for b in my_text:
                test = b.split(" ")
                join_word = test[0] + " " + test[1]
                if join_word == a:
                    textbox2.insert(INSERT, b+"\n")
    except IOError as e:
        tkMessageBox.showinfo("Error!!", e)

def clear():
    textbox1.delete('1.0', END)
    textbox2.delete('1.0', END)

window = Tk()
window.title("Welcome to GoodDocument app")
window.geometry('1000x500')

left_frame = LabelFrame(window)
left_frame.place(width=100,height=700,x=0,y=0)

middle_frame = LabelFrame(window)
middle_frame.place(width=650,height=700,x=100,y=0)

right_frame = LabelFrame(window)
right_frame.place(width=600,height=700,x=750,y=0)

document_name = Label(middle_frame,text="")
document_name.place(x=0,y=0)

# Scrollbar
scrollbar1 = Scrollbar(middle_frame)
scrollbar1.pack( side = RIGHT, fill = Y )

scrollbar2 = Scrollbar(right_frame)
scrollbar2.pack( side = RIGHT, fill = Y )

# Text (User input for multiple line)
textbox1 = Text( middle_frame, width=77,height=43 )
textbox1.place(x=0,y=21)

textbox2 = Text( right_frame, width=71,height=43 )
textbox2.place(x=0,y=0)

# Button
btn = Button(left_frame, text="Insert file", command=list_of_file)
btn.place(x=0,y=0)

btn = Button(left_frame, text="Metaprofilling", command=meteprofilling)
btn.place(x=0,y=33)

btn = Button(left_frame, text="Clean", command=clear)
btn.place(x=0,y=73)

btn = Button(left_frame, text="Fix", command=fix)
btn.place(x=0,y=113)

btn = Button(left_frame, text="Clear", command=clear)
btn.place(x=0,y=153)

scrollbar1.config( command = textbox1.yview )
scrollbar2.config( command = textbox2.yview )
window.mainloop()