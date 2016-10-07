def fib(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 0            
   else:                      
      return fib(n-1) + fib(n-2)

def fibonachi_sequence(length):
    sequence = []
    for i in range(1, length + 1):
        sequence.append(fib(i))
    return sequence
    
