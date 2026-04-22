import time
j=3

for i in range(236):
 print(i)
 print("_______")

 time.sleep(1)
 print("I'm infinite.")
 print("_______")
 time.sleep(1)
 
 if j<10:
  print(j)
  print("_______")
  j+=3
 else:
  j=3   
 time.sleep(1)
