import random


STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZACETEK = "S"
ZMAGA = 'W'
PORAZ = 'X'


class Vislice:
    def __init__(self):
        self.igre = {}
        self.max_id = 0

    def prost_id_igre(self):
        self.max_id += 1
        return self.max_id

     """ Druga moznost:
    def prost_id_igre_drugace(self):
        if not self.igre: return 0
        m = max(self.igre.keys())
        return m + 1
    """

    def nova_igra(self):
        nov_id = self.prost_id_igre()
        sveza_igra = nova_igra()

        self.igre[nov_id] = (sveza_igra, ZACETEK)

        return nov_id

    def ugibaj(self, id_igre, crka):
        # Najdi
        # Trenutno stanje nas ne zanima
        igra, _ = self.igre[id.igre]

        # Posodobi z deligiranjem
        novo_stanje = igra.ugibaj(crka)

        # Popravi v slovarju
        self.igre[id_igre] = (igra, novo_stanje)

        return novo_stanje

class Igra:

    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke
    
    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]
    
    def pravilne_crke(self):
        return [ crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return all(crka in self.crke for crka in self.geslo)

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        s = ''
        for crka in self.geslo:
            if crka in self.crke:
                s += crka + ''
            else:
                s += '_ '
        return s
    
    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA

with open('besede.txt', encoding='utf-8') as f:
    bazen_besed = [vrstica.strip().upper() for vrstica in f]

def nova_igra():
    return Igra(random.choice(bazen_besed))