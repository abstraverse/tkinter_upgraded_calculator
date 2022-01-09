from tkinter import * #Import the library
import math #import math

root = Tk() #Create root container
root.title("Calculator") #Change window name
root.geometry("260x400") #Define window size
root.resizable(0, 0) #Disallow the user from resizing the window
root.attributes('-alpha',0.98) #Add transparency

input_text = StringVar() #Prepare a variable for the input box

def btn_click(item):
    global expression #prepare a variable to store the input
    global back #create a restore point
    expression = expression + str(item) #update the input
    input_text.set(expression) #apply to the input frame
    back=expression #create a restore point

def btn_clear():
    global expression
    expression = "" #clear the input variable
    input_text.set("") #set it

def btn_del():
    global expression
    global back #create a restore point
    back=expression #create a restore point
    expression=expression[:-1] #delete the last character
    input_text.set(expression)

def btn_back():
    global expression
    global back
    input_text.set(back) #rollback the last change (math function, equals, delete, clear)
    expression=back

def btn_equal():
    global expression
    expression = str(eval(expression)) #evaluate the expression
    input_text.set(expression)

def btn_equal_fabs():
    global expression
    expression = str(math.fabs(eval(expression))) #evaluate the expression and apply the function
    input_text.set(expression)

def btn_equal_factorial():
    global expression
    expression = str(math.factorial(eval(expression))) #evaluate the expression and apply the function
    input_text.set(expression)

def btn_equal_sqrt():
    global expression
    expression = str(math.sqrt(eval(expression))) #evaluate the expression and apply the function
    input_text.set(expression)

def btn_equal_log():
    global expression
    expression = str(math.log10(eval(expression))) #evaluate the expression and apply the function
    input_text.set(expression)

expression = "" #set the expression as an empty string

input_frame = Frame(root, width = 260, height = 50, bd = 0, highlightbackground = "white", highlightcolor = "white", highlightthickness = 1) #add an input field
input_frame.pack(side = TOP) #position the field
input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#f0f0f0", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0) #Position the field
input_field.pack(ipady=10) #Add padding to the input field

btns_frame = Frame(root, width = 260, height = 272.5, bg = "#484848")
btns_frame.pack()
#BUTTONS
btback = Button(btns_frame, text = "Back", fg = "white", width = 8, height = 3, bd = 0, bg = "#5a48af", cursor = "hand2", command = lambda: btn_back()).grid(row = 0, column = 0, padx = 1, pady = 1)
clear = Button(btns_frame, text = "Clear", fg = "white", width = 8, height = 3, bd = 0, bg = "#5a48af", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 1, padx = 1, pady = 1)
delete = Button(btns_frame, text = "Delete", fg = "white", width = 8, height = 3, bd = 0, bg = "#5a48af", cursor = "hand2", command = lambda: btn_del()).grid(row = 0, column = 2, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", fg = "white", width = 8, height = 3, bd = 0, bg = "#5a48af", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
seven = Button(btns_frame, text = "7", fg = "white", width = 8, height = 3, bd = 0, bg = "#1d2325", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "white", width = 8, height = 3, bd = 0, bg = "#1d2325", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "white", width = 8, height = 3, bd = 0, bg = "#1d2325", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", fg = "white", width = 8, height = 3, bd = 0, bg = "#5a48af", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
four = Button(btns_frame, text = "4", fg = "white", width = 8, height = 3, bd = 0, bg = "#1d2325", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "white", width = 8, height = 3, bd = 0, bg = "#1d2325", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "white", width = 8, height = 3, bd = 0, bg = "#1d2325", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "white", width = 8, height = 3, bd = 0, bg = "#5a48af", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
one = Button(btns_frame, text = "1", fg = "white", width = 8, height = 3, bd = 0, bg = "#1d2325", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "white", width = 8, height = 3, bd = 0, bg = "#1d2325", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "white", width = 8, height = 3, bd = 0, bg = "#1d2325", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "white", width = 8, height = 3, bd = 0, bg = "#5a48af", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
zero = Button(btns_frame, text = "0", fg = "white", width = 17, height = 3, bd = 0, bg = "#1d2325", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btns_frame, text = ".", fg = "white", width = 8, height = 3, bd = 0, bg = "#1d2325", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btns_frame, text = "=", fg = "white", width = 8, height = 3, bd = 0, bg = "#f3b907", cursor = "hand2", command = lambda: btn_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
#math
fabs = Button(btns_frame, text = "|x|", fg = "white", width = 8, height = 3, bd = 0, bg = "#297A6A", cursor = "hand2", command = lambda: btn_equal_fabs()).grid(row = 5, column = 0, padx = 1, pady = 1)
factorial = Button(btns_frame, text = "x!", fg = "white", width = 8, height = 3, bd = 0, bg = "#297A6A", cursor = "hand2", command = lambda: btn_equal_factorial()).grid(row = 5, column = 1, padx = 1, pady = 1)
sqrt = Button(btns_frame, text = "√x", fg = "white", width = 8, height = 3, bd = 0, bg = "#297A6A", cursor = "hand2", command = lambda: btn_equal_sqrt()).grid(row = 5, column = 2, padx = 1, pady = 1)
log = Button(btns_frame, text = "log(x)", fg = "white", width = 8, height = 3, bd = 0, bg = "#297A6A", cursor = "hand2", command = lambda: btn_equal_log()).grid(row = 5, column = 3, padx = 1, pady = 1)



#Credits
credit = Label(root, text="Abstraverse 2022")
credit.pack()
root.mainloop()