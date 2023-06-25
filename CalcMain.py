# Matthew Svenson 2023
# THIS PROGRAM REQUIRES pysimplegui
# Lets make the intro sequence for the calculator
#s = "----------------------MATTS PYTHON CALCULATOR----------------------"
#s1 = "Helping you calculate the hard hitting facts"
# MAKE SURE TO OPEN VSCODE WITH THE FILE OPEN AS WELL

# This function will be used later to do the calculation
def equalsfunc(result):
      #find the first num
      firstnum = ""
      for c in result:
         if c.isdigit():
            firstnum += c
         if not c.isdigit():
            break
      
      #find the operator
      operator = ""
      for c in result:
         if not c.isdigit():
            operator += c

      #finds the second number
      secondnumbool = False
      secondnum = ""
      for c in result:
         if c.isdigit() and secondnumbool == True:
            secondnum += c
         if not c.isdigit():
            secondnumbool = True

      if operator == " + ":
         result = int(firstnum) + int(secondnum)
      
      if operator == " - ":
         result = int(firstnum) - int(secondnum)
      
      if operator == " * ":
         result = int(firstnum) * int(secondnum)

      if operator == " / ":
         result = int(firstnum) / int(secondnum)

      return str(result) 



import PySimpleGUI as sg

sg.theme("Neutral Blue")

result = ""

Layout = [
[sg.HorizontalSeparator(), sg.Text("WELCOME TO MATTS PYTHON CALCULATOR"), sg.HorizontalSeparator()],
[sg.Image('BuffSnake.png'), sg.Text(result, size=(45,6), key='out', justification="center"), sg.Image('BuffSnake.png')],
[sg.HorizontalSeparator(), sg.Button("7", size=(12,2)), sg.Button("8",size=(12,2)),sg.Button("9",size=(12,2)), sg.Button("/", size=(12,2)), sg.HorizontalSeparator()],
[sg.HorizontalSeparator(), sg.Button("4",size=(12,2)), sg.Button("5",size=(12,2)),sg.Button("6",size=(12,2)), sg.Button("*", size=(12,2)), sg.HorizontalSeparator()],
[sg.HorizontalSeparator(), sg.Button("1",size=(12,2)), sg.Button("2",size=(12,2)),sg.Button("3",size=(12,2)), sg.Button("+", size=(12,2)), sg.HorizontalSeparator()],
[sg.HorizontalSeparator(), sg.Button("Clear",size=(12,2)), sg.Button("0",size=(12,2)),sg.Button("=",size=(12,2), bind_return_key=True), sg.Button("-", size=(12,2)), sg.HorizontalSeparator()],
]

window = sg.Window("MATTS CALCULATOR", Layout, keep_on_top=True, return_keyboard_events=True)

twooperators = False
# Get the result to print
while True:
   event, values = window.read()
   print(event, values)

   #This allows buttons to print nums on output screen
   #First number and second num
   if event == "0" or event == "1" or event == "2" or event == "3" or event == "4" or event == "5" or event == "6" or event == "7" or event == "8" or event == "9":
      result += event
      window['out'].update(result)

   #Operator
   if event == "/" or event == "*" or event == "+" or event == "-":
      if twooperators == True:
         result = equalsfunc(result)
         result += " " + event + " "
      else:
         result += " " + event + " "
         twooperators = True

      window['out'].update(result)   

   #Time to actually evaluate the equation
   if event == "=":
      print(twooperators)
      twooperators = False
      result = equalsfunc(result)
      window["out"].update(result)
   
   if event == "Clear" or event == "BackSpace:8":
      result = ""
      window["out"].update(result)

   if event == sg.WIN_CLOSED:
      break



