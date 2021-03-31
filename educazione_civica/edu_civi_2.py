import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv
def tempFile():
    anno = []
    value = []
    temp_file = open("./Temperature_Anomaly.csv")
    temp_reader = csv.reader(temp_file, delimiter=',')
    i = 0
    while(i<5):
        next(temp_file)
        i+=1
    for row in temp_reader:
        print(row)
        anno.append(int(row[0]))
        value.append(float(row[1]))

    fig, ax = plt.subplots(1,1)  
    fig.suptitle("temperatura")  

    ax.plot(anno,value,'o-r')
    ax.set_xlabel("Anno")
    ax.set_ylabel("Temperatura in c°") 

    plt.show()

def dispersione():
    temperatura = []
    co2 = []
    temp_file = open("./Temperature_Anomaly.csv")
    temp_reader = csv.reader(temp_file, delimiter=',')
    CO2_file = open("./CO2_emissions.csv")
    CO2_reader = csv.reader(CO2_file, delimiter=',')
    i = 0
    while(i<5):
        next(temp_reader)
        i+=1
    for row in temp_reader:
        temperatura.append(float(row[1]))
    a = 0
    while (a<123):
        next(CO2_reader)
        a+=1
    for row in CO2_reader:
        co2.append(str(row[7]))
    fig, ax2 = plt.subplots(1,1)
    fig.suptitle("relazione tra emissioni di co2 e innalzamento della temperatura")

    ax2.plot(co2,temperatura,("o b"))
    ax2.set_xlabel("emissioni a persona, in milioni di tonnellate")
    ax2.set_ylabel("Temperatura in c°")               

    plt.show()

def co2File():
    year = []
    total = []
    gasFuel = []
    liquidFuel = []
    solidFuel = []
    cement = []
    gasFlaring = []
    perCapita = []
    CO2_file = open("./CO2_emissions.csv")
    CO2_reader = csv.reader(CO2_file, delimiter=',')
    next(CO2_reader)
    for row in CO2_reader:
        year.append(float(row[0]))
        total.append(float(row[1]))
        gasFuel.append(float(row[2]))
        liquidFuel.append(float(row[3]))
        solidFuel.append(float(row[4]))
        cement.append(float(row[5]))
        gasFlaring.append(float(row[6]))
        if (row[7] == " "):
            perCapita.append(0)
        perCapita.append(str(row[7]))

    temperatura = []
    anno = []
    temp_file = open("./Temperature_Anomaly.csv")
    temp_reader = csv.reader(temp_file, delimiter=',')       
    i = 0
    while(i<5):
        next(temp_reader)
        i+=1
    for row in temp_reader:
        anno.append(float(row[0]))    
        temperatura.append(float(row[1]))

    fig, ax1 = plt.subplots(1,1)  
    fig.suptitle("Emissioni (in milioni di tonnellate)")

    #ax1.plot(year,total,("o-r"))
    #ax1.set_xlabel("Anno")
    #ax1.set_ylabel("Total") 

    #ax2.plot(year,gasFuel,("o-r"))
    #ax2.set_xlabel("Anno")
    #ax2.set_ylabel("GasFuel")    

    #ax3.plot(year,liquidFuel,("o-r"))
    #ax3.set_xlabel("Anno")
    #ax3.set_ylabel("LiquidFuel")   

    #ax4.plot(year,solidFuel,("o-r"))
    #ax4.set_xlabel("Anno")
    #ax4.set_ylabel("SolidFuel")    

    #ax5.plot(year,cement,("o-r"))
    #ax5.set_xlabel("Anno")
    #ax5.set_ylabel("Cement")     

    #ax6.plot(year,gasFlaring,("o-r"))
    #ax6.set_xlabel("Anno")
    #ax6.set_ylabel("GasFlaring")   

    #ax7.plot(year,perCapita,("o-r"))
    #ax7.set_xlabel("Anno")
    #ax7.set_ylabel("PerCapita")        

    #ax8.plot(temperatura,total, ("o-r"))
    #ax8.set_xlabel("temperatura in c°")
    #ax8.set_ylabel("totale emissioni")   

    plt.show()

def main():
    scelta = int(input("inserire 1 per il primo file, 2 per il secondo, 3 per i grafici a dispersione: "))
    if (scelta == 1):
        tempFile()
    elif (scelta == 2):
        co2File()
    elif (scelta == 3):
        dispersione()
    else:
        print("input sbagliato")

if __name__ == "__main__":
    main()