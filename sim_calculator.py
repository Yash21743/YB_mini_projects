import tkinter as tk

def click(btn_text):
    current = entry.get()
    if btn_text== "=":
        try:
            result= str(eval(current))
            entry.delete(0,tk.END)
            entry.insert(0,result)
        except:
            entry.delete(0,tk.END)
            entry.insert(0,"Error")
    elif btn_text == "C":
        entry.delete(0,tk.END)
    elif btn_text =="DEL":
        entry.delete(len(current)-1,tk.END)
    else:
        entry.insert(tk.END,btn_text)

#Main window:
root = tk.Tk()
root.title("YB Calculator")
root.geometry("300x420")
root.configure(bg="dark blue")

#Entry:
entry=tk.Entry(root,font=("Arial",20), bd=5, justify="right")
entry.pack(fill="both", ipadx=8,ipady=15, padx=10, pady=10)

#Button layout with button addded:
buttons=[
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["0", "DEL",  "+"],
    ["C", "="]
]

#create buttons..
for row in buttons:
    frame=tk.Frame(root,bg="dark blue")
    frame.pack(expand=True, fill="both")
    for btn in row:
        b=tk.Button(frame,text=btn,font=("Arial",18),bg="#333",fg="white",
                command=lambda bt=btn: click(bt))
        b.pack(side="left",expand=True, fill="both", padx=2, pady=2)

root.mainloop()
