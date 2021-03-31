
def trasformazione(ip, subnet):
    for a in ip("."):
        subnetbin = bin(subnet).replace("0b", "")
    bit = 32
    stringa = subnetbin[0:subnet]
    for b in range(bit):
        stringa = stringa + "1"
    for b in range()    


    def main():
    
        ip = str(input("inserisci l'indirizzo ipv4"))
        subnet = int(input("inserisci la subnet mask"))
        lista = []
        lista = ip.split(".")
        trasformazione(ip,subnet)

    if __name__=="__main__":
        main()
