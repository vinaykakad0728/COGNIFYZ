def rec_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(rec_fibo(n-1) + rec_fibo(n-2))  

nterms = int(input("How many terms? "))  
 
if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(rec_fibo(i))  
