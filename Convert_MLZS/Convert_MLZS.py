import tkinter
    
def reset():
    entry1.delete(0,tkinter.END)
    entry2.insert(0,"0.0")
    entry1.delete(0,tkinter.END)
    entry2.delete(0,"0.0")
        
def convert_to_celsius():
    fahrenheit=float(entry1.get())
    celsius=(fahrenheit-32.0)*5.0/9.0
    entry2.delete(0,tkinter.END)
    entry2.insert(0,f"{celsius:.2f}")
    
def convert_to_farenheit():
    celsius = float(entry2.get())
    fahrenheit=(celsius*9.0/5.0)+32.0
    entry1.delete(0, tkinter.END)   
    entry1.insert(0,f"{fahrenheit:.2f}")
    
app= tkinter.Tk()
app.title("Conversor de temperatura")
    
label1=tkinter.Label(app,text="Fahrenheit:")
label1.grid(row=0,column=0)
    
entry1=tkinter.Entry(app)
entry1.grid(row=0,column=1)
    
button1=tkinter.Button(app, text="Convertir a Celsius", command=convert_to_celsius)
button1.grid(row=0,column=2)    
    
label2=tkinter.Label(app,text="Celsius")
label2.grid(row=1,column=0)
    
entry2=tkinter.Entry(app)
entry2.grid(row=1,column=1)

button2=tkinter.Button(app,text="Convertit a Farenheit", command=convert_to_farenheit)
button2.grid(row=1,column=2)

button3=tkinter.Button(app,text="Restablecer",command=reset())
button3.grid(row=2,column=1)

app.mainloop()

