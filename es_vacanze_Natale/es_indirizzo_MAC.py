import random

def MACcasuale():        #creo una funzione chiamata MACcasuale
        esadecimale = [ 
                random.randint(0x00, 0xff),   #operazione per randomizzare i 2 numeri in base esadecimale
                random.randint(0x00, 0xff),
                random.randint(0x00, 0xff),
                random.randint(0x00, 0xff),
                random.randint(0x00, 0xff),
                random.randint(0x00, 0xff) ]
        return ':'.join(map(lambda x: "%02x" % x, esadecimale))  #operazione per stampare le coppie di numeri con i due punti in mezzo

print (MACcasuale())