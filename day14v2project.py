import random
def food():
 meal=["Banana","Sushi","Crisps","Soda","Water",
 "Milk","Lemon","burger","Ghee","someone","cucumber"
 ,"Honey"]
 print(meal)
 while True:
  choice=input("Choose One or exit.")
  if choice=="exit":
   break
  elif choice in meal:
   random1=(random.choice(meal))   
   random2=(random.choice(meal)) 
   print("Your cursed meal is:",choice,",",random1,"and",random2)
  else:
   print("Dude be serious for a sec, CHOOSE AGAIN.")   
food()