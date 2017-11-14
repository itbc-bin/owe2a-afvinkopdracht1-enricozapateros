
# Naam:Rick Schoenmaker
# Datum:03-11-2017
# Versie:

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.

def main():
    try:
        bestand = "testbestand.fasta" # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
        """
        Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
        De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
        """
        headers, seqs = lees_inhoud(bestand)
       
    
        zoekwoord = input("Geef een zoekwoord op: ")
    

    except:
        print("helaas")
    
    
def lees_inhoud(bestand):
    try:
        bestand = open(bestand).readlines()
        headers = []
        seqs = []

        for element in bestand:
            if ">" in element:
                headers.append(element.strip())
                print (headers)
                seq = ""
                
        for element in bestand:
         
             if ">" not in element:
                 seq += element.strip()
             else:
                     seqs.append(seq)
                     seq= ""
                     seqs.remove("")
                     seqs.append(seq)
    
    
            
        print (seqs)
    
    
        """
        Schrijf hier je eigen code die het bestand inleest en deze splitst in headers en sequenties.
        Lever twee lijsten op:
            - headers = [] met daarin alle headers
            - seqs = [] met daarin alle sequenties behorend bij de headers
            Hieronder vind je de return nodig om deze twee lijsten op te leveren
            """
            
    except:
        print("helaas1")
    
    return headers, seqs

def is_dna(seq):
    try:
        verify = True
        for nucleotiden in seqs:
            if nucleotiden not in (A,C,T,G):
                verify = False

        return verify
    except:
        print("helaas2")
        


    

def knipt(seq):
    try:
        bestand1 =  open ("enzymen.txt").readlines()
        enzymenlijst = []
        teller= 0
        for enzym in bestand1:
            enzymenlijst.append(enzym.strip())
            enzymenlijst [teller]= enzymenlijst [teller].replace("^","")
            teller= teller+1

    
        enzymenlijst2= []

        for enzym in enzymenlijst:
            enzymenlijst2.append(enzym.split(" "))
   

        for enzym in enzymenlijst2:
            if enzym [1] in seq1:
                locatie= seq1.find(enzym[1])
                print(enzym[0], "Matched op locatie: ", locatie )
                
                """Bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken
                Deze functie bepaald of een restrictie enzym in de sequentie (een element uit seqs) knipt.
                Hiervoor mag je kiezen wat je returnt, of wellicht wil je alleen maar printjes maken.
                """
    except:
        print("helaas3")
    return enzym
main()
