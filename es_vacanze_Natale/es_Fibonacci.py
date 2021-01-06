def Fibonacci(n):                                   #funzione ricorsiva
   if n <= 1:                                       
       return n
   else:
       return(Fibonacci(n-1) + Fibonacci(n-2))      #calcolo della sequenza di Fibonacci

ntermini = int(input("Inserire il numero di termini che si vogliono ottenere: \n"))   #chiedo in input all'utente il numero di termini che vuole utilizzare


if ntermini <= 0:                                   #controllo se il numero di termini inseriti è corretto
   print("Inserire un numero intero positivo")      
else:
   print("Sequenza di Fibonacci richiesta:")        
   for i in range(ntermini):                        #ciclo for per il numero di termini che ha inserito l'utente
       print(Fibonacci(i))                          #stampo i numeri 