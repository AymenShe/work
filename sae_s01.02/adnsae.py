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
            adn[i]="U"
        i+=1
    return adn
