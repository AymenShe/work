def est_base(c):
    """Fonction permettant de savoir si le characteres correspond a une base de l'ADN
        :param:str
        :return:bool
    """

    if c not in  ["A","T","C","G"]:
        return False
    return True

def est_adn(s):
    """Fonction permet de savoir si la chaine de char. est adn
        :param:str
        :return:bool
        """
    i=0
    while i<len(s):
        if not est_base(s[i]):
            return False
        i+=1
    return True


def arn(adn):
    """fonction qui transforme une base adn en base arn
        :param:str
        :return:str or none
    """
    i=0
    if not est_adn(adn):
        return
    while i < len(adn):
        if adn[i]=="T":
            adn = adn.replace("T","U")
        i+=1
    print(adn)
    return adn

arn("ATA")

def arn_to_codons(Aarn):
    """fonction qui transforme une base arn en codons
        :param:str
        :return:list
    """
    i=0
    codons=[]
    while len(Aarn)%3!=0:
        Aarn.replace(Aarn[len(Aarn)-1],"")
    while i < len(Aarn):
        j=0
        tmp=""
        while j < 3:
            tmp+=Aarn[i]
            i+=1
            j+=1
        codons.append(tmp)
    print(codons)
    return codons

arn_to_codons("AATAGT")






dicocodon={
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "CUU": "Leucine",
    "CUC": "Leucine",
    "CUA": "Leucine",
    "CUG": "Leucine",
    "AUU": "Isoleucine",
    "AUC": "Isoleucine",
    "AUA": "Methionine",
    "AUG": "Methionine",
        }

def codons_stop(dico):
    nom_adn=list(dico.values())
    codon_adn=list(dico)
    codonStop=""
    i=0
    tmp = nom_adn[i]
    while i < len(dico)-1:
        if tmp !=  nom_adn[i+1]:
            codonStop+=codon_adn[i]
            tmp = nom_adn[i+1]
        i+=1
    codonStop+=codon_adn[len(dico)-1]
    print(codonStop)
    return codonStop

codons_stop(dicocodon)




def codons_to_aa(codons, dico):
    acides_amines=[]
    i=0
    while i < len(codons):
        acides_amines+=dico[codons[i]]
    




def nextIndice(tab, ind, elements):
    pass


def decoupe_sequence(seq, start, stop):
    pass


def codons_to_seq_codantes(codons, dico):
    pass


def seq_codantes_to_seq_aas(seq_codantes, dico):
    pass


def adn_encode_molecule(adn, dico, molecule):
    pass
