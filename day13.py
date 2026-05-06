def calculator():
 while True:
  num1=float(input("What's your first chosen"))
  operation=input("choose ur poison(+,-,*,/:)")
  num2=float(input("ur second chosen, traitor?"))

  if operation=="+":
   print(num1+num2)
  elif operation=="-":
   print(num1-num2)
  elif operation=="*":
   print(num1*num2)
  elif operation=="/":
   if num1==0:
    print("invalid Unless You sacrifice yourself.")
   else:
    print(num1/num2)
  else:
   print("operation invalid")
calculator()              