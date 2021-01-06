import string
from random import *
caratteri = 'qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM"£$%&/()='  #inseisco tutti i caratteri che possono esserci nelle password

password_semplice =  "".join(choice(caratteri) for x in range(8))  #operazione per generare una password casuale con 8 caratteri
password_complicata =  "".join(choice(caratteri) for x in range(12))  #operazione per generare una password casuale con 12 caratteri

#stampo le 2 password
print (password_semplice)
print (password_complicata)