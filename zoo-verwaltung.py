class Art:
    def __init__(self, bezeichnung):
        self.bezeichnung = bezeichnung

class Tier:

    def __init__(self, name, bezeichnung):
        self.name = name
        self.tierart = Art

class Pfleger:

    def __init__(self, name):
        self.name = name
        self.tiere = []

    def tier_hinzufuegen(self, tier: Tier):
        self.tier.append(tier)

    def tiere_anzeigen(self):
        print(f"Die Teiere die dem Pfleger zugeteilt sind sind: {self.tiere}")
        for tier in self.tiere:
            print(tier.name)

class Fuetterung:

    def __init__(self, pfleger, tier):
        self.pfleger = pfleger
        self.tier = tier

    def starten(self, name, bezeichnung):
        print(f"Pfleger Horst füttert das Tier {name} (Art: {bezeichnung})")
        

simba = Tier("Simba", "Löwe")
melman = Tier("Melman", "Giraffe")

pfleger = Pfleger("Horst")
pfleger.tier_hinzufuegen(simba)
pfleger.tier_hinzufuegen(melman)

futterrunde = Fuetterung(pfleger, simba)
futterrunde.starten()
    
        