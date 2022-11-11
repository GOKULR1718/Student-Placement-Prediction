from tkinter import *
from joblib import Parallel, delayed
import joblib
rf = joblib.load('model.pkl')
confidence = ""
anxiety = ""
selfesteem = ""
calmness = ""
selfcontrol=""
happiness=""
emotionalintell=""


def clear():
	global expression
	expression = ""
	equation.set("")

def predict():

    a1=lconfidence.get()
    b1=lanxiety.get()
    c1=lselfesteem.get()
    d1=lcalmness.get()
    e1=lselfcontrol.get()
    f1=lselfeffi.get()
    g1=lhappiness.get()
    h1=lemotionalintell.get()
    x_new=[[a1,b1,c1,d1,e1,f1,g1,h1]]
    x=rf.predict(x_new)
    if x==[0]:
        equation.set("Will not be Placed!!!")
    else:
        equation.set("Will be Placed !!")
    

if __name__ == "__main__":

	gui = Tk()
	
	gui.configure(background="grey")
	
	gui.title("Placement Predictor")

	gui.geometry("500x500")
	
	equation = StringVar()

	Confidence = Label(gui,text = "Confidence")
	anxiety = Label(gui,text = "Anxiety")
	selfesteem = Label(gui,text = "Self-Esteem")
	calmness = Label(gui,text = "Calmness")
	selfcontrol = Label(gui,text = "Self-Control")
	selfeffi = Label(gui,text = "Self-Efficacy")
	happiness = Label(gui,text = "Happiness")
	emotionalintell = Label(gui,text = "Emotional Intelligence")

	Confidence.grid(row=2,column=0)
	anxiety.grid(row=3,column=0)
	selfesteem.grid(row=4,column=0)
	calmness.grid(row=5,column=0)
	selfcontrol.grid(row=6,column=0)
	selfeffi.grid(row=7,column=0)
	happiness.grid(row=8,column=0)
	emotionalintell.grid(row=9,column=0)

	lconfidence = Entry(gui)
	lanxiety = Entry(gui)
	lselfesteem = Entry(gui)
	lcalmness=Entry(gui)
	lselfcontrol = Entry(gui)
	lselfeffi = Entry(gui)
	lhappiness=  Entry(gui)
	lemotionalintell= Entry(gui)

	lconfidence.grid(columnspan=4, ipadx=80,row=2, column=1)
	lanxiety.grid(columnspan=4, ipadx=80,row=3, column=1)
	lselfesteem.grid(columnspan=4, ipadx=80,row=4, column=1)
	lcalmness.grid(columnspan=4, ipadx=80,row=5, column=1)
	lselfcontrol.grid(columnspan=4, ipadx=80,row=6, column=1)
	lselfeffi.grid(columnspan=4, ipadx=80,row=7, column=1)
	lhappiness.grid(columnspan=4, ipadx=80,row=8, column=1)
	lemotionalintell.grid(columnspan=4, ipadx=80,row=9, column=1)

	button1 = Button(gui, text=' Predict ', fg='black', bg='red',command=predict, height=1, width=7)
	button1.grid(row=10, column=1)

	expression_field = Entry(gui, textvariable=equation, state="readonly")
	expression_field.grid(row=11,column=1)
	

	gui.mainloop()
