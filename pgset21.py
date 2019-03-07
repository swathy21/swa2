def power(x, y): 
  
    if (y == 0): return 1
    elif (int(y % 2) == 0): 
      
               power(x, int(y / 2))) 
    else: 
     
                   power(x, int(y / 2))) 
  

x = 2; y = 3
print(power(x, y)) 
