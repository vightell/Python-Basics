def judge():
 name=input("Tell Me What's ur Name?")
 level=int(input("Okay, Now addTell Me What's ur level?"))
 if name=="vightell":
  print("Queen")
 else:
  print("Nice to Meet ya")
 if level>100:
  print("You Are The Master Now.") 
 elif 50<=level<=100:
  print("ur growing")
 elif level<50:
  print("keep up")   
judge()   
