import tkinter as tk

root = tk.Tk()
root.title('Calculator by Vipashana')
root.geometry('644x900')
root.wm_iconbitmap('calculator_3534.ico')

def click(event):
    global input_val
    text = event.widget.cget('text')
    print(text)
    if text == '=':
        if input_val.get().isdigit():
            value = int(input_val.get())
        else:
            try:
                value = eval(insert_num.get())
            except Exception as e:
                print(e)
                value = 'Error'

        input_val.set(value)
        insert_num.update()
    elif text == 'C':
        input_val.set('')
        insert_num.update()
    else:
        input_val.set(input_val.get() + text)
        insert_num.update()


input_val = tk.StringVar()
input_val.set('')
insert_num = tk.Entry(root, textvariable=input_val, font='lucida 40 bold',)
insert_num.pack(fill='both', ipadx=8, padx=10, pady=10)

f = tk.Frame(root, bg='grey')

button = tk.Button(f, text='9', font='lucida 35 bold', padx=18, pady=8)
button.configure()
button.pack(side='left',padx=18,pady=5)
button.bind('<Button-1>',click)

button = tk.Button(f, text='8', font='lucida 35 bold', padx=18, pady=8)
button.pack(side='left',padx=18,pady=5)
button.bind('<Button-1>',click)

button = tk.Button(f, text='7', font='lucida 35 bold', padx=18, pady=8)
button.pack(side='left',padx=18,pady=5)
button.bind('<Button-1>',click)

f.pack()


f = tk.Frame(root, bg='grey')

button = tk.Button(f, text='6', font='lucida 35 bold', padx=18, pady=8)
button.configure()
button.pack(side='left',padx=18,pady=5)
button.bind('<Button-1>',click)

button = tk.Button(f, text='5', font='lucida 35 bold', padx=18, pady=8)
button.pack(side='left',padx=18,pady=5)
button.bind('<Button-1>',click)

button = tk.Button(f, text='4', font='lucida 35 bold', padx=18, pady=8)
button.pack(side='left',padx=18,pady=5)
button.bind('<Button-1>',click)

f.pack()


f = tk.Frame(root, bg='grey')

button = tk.Button(f, text='3', font='lucida 35 bold', padx=18, pady=8)
button.configure()
button.pack(side='left',padx=18,pady=5)
button.bind('<Button-1>',click)

button = tk.Button(f, text='2', font='lucida 35 bold', padx=18, pady=8)
button.pack(side='left',padx=18,pady=5)
button.bind('<Button-1>',click)

button = tk.Button(f, text='1', font='lucida 35 bold', padx=18, pady=8)
button.pack(side='left',padx=18,pady=5)
button.bind('<Button-1>',click)

f.pack()


f = tk.Frame(root, bg='grey')

button = tk.Button(f, text='0', font='lucida 35 bold', padx=18, pady=8)
button.configure()
button.pack(side='left',padx=18,pady=5)
button.bind('<Button-1>',click)

button = tk.Button(f, text='+', font='lucida 35 bold', padx=18, pady=8)
button.pack(side='left',padx=18,pady=5)
button.bind('<Button-1>',click)

button = tk.Button(f, text='-', font='lucida 35 bold', padx=22, pady=8)
button.pack(side='left',padx=18,pady=5)
button.bind('<Button-1>',click)

f.pack()


f = tk.Frame(root, bg='grey')

button = tk.Button(f, text='/', font='lucida 35 bold', padx=23, pady=8)
button.configure()
button.pack(side='left',padx=19,pady=5)
button.bind('<Button-1>',click)

button = tk.Button(f, text='%', font='lucida 35 bold', padx=10, pady=8)
button.pack(side='left',padx=19,pady=5)
button.bind('<Button-1>',click)

button = tk.Button(f, text='*', font='lucida 35 bold', padx=20, pady=8)
button.pack(side='left',padx=19,pady=5)
button.bind('<Button-1>',click)

f.pack()


f = tk.Frame(root, bg='grey')

button = tk.Button(f, text='.', font='lucida 35 bold', padx=22, pady=8)
button.configure()
button.pack(side='left',padx=19,pady=5)
button.bind('<Button-1>',click)

button = tk.Button(f, text='C', font='lucida 35 bold', padx=15, pady=8)
button.pack(side='left',padx=20,pady=5)
button.bind('<Button-1>',click)

button = tk.Button(f, text='=', font='lucida 35 bold', padx=15.2, pady=8)
button.pack(side='left',padx=18,pady=5)
button.bind('<Button-1>',click)

f.pack()
root.configure(bg='black')
root.mainloop()
