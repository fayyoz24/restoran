class Ali:
    def __init__(self, kurtka, yosh, jinsi, millat):
        self.kurtka = kurtka
        self.yosh = yosh
        self.jins = jinsi
        self.millat = millat
        
    def ishlamoq(self):

        if self.yosh >= 18:
            return "Yaxshi Ishlang"
        return "Sizga ish mumkinmas!"
    
    def ovqatlanmoq(self):
        return "thanks"
    
    def __str__(self):
        return f"{self.yosh}-{self.jins}-{self.millat}"