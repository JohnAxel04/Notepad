import tkinter as pad
from tkinter import filedialog

def saveMo():
    def saved():
        newEnter = Enter.get()
        newtxt = txt.get("1.0","end-1c")
        with open(newEnter + ".txt","w+") as files:
            files.write(newtxt)
            print("succesfull")
            top.destroy()
    def canceldaw():
        top.destroy()
    top = pad.Toplevel(window)
    top.grab_set()
    top.transient(window)
    lbl = pad.Label(top,text="Name of the File")
    lbl.pack()
    Enter = pad.Entry(top)
    Enter.pack(padx=5)
    saveBtn = pad.Button(top,text="Save",command=saved)
    saveBtn.pack()
    cancelBtn = pad.Button(top,text="Cancel",command=canceldaw)
    cancelBtn.pack()
def opened():
    openfile = filedialog.askopenfile(initialdir="C:\\Users\\user\\Documents\\Js",
                                      title="Select File? ",
                                      filetypes= (("text File","*.txt"),("All Files","*.*")))
    if openfile:
        content = openfile.read()
        txt.delete("1.0","end")
        txt.insert("1.0",content)
        openfile.close()

def new():
    txt.delete("1.0","end-1c")
window = pad.Tk()
window.title("Unknown Title")
menus = pad.Menu(window)
window.config(menu=menus)
listmenu = pad.Menu(menus, tearoff=0)
listmenu.add_command(label="New",command=new)
listmenu.add_command(label="Open",command=opened)
listmenu.add_command(label="Save",command=saveMo)
listmenu.add_separator()
listmenu.add_command(label="Exit",command=window.destroy)
menus.add_cascade(label="Edit",menu=listmenu)

txt = pad.Text(window,width=30,height=20)
txt.pack()
window.mainloop()