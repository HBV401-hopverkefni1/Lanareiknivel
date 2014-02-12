class Lan:
    def __init__(self,upphaed,vextir,trygging):
        self.upphaed=upphaed
        self.vextir=vextir
        self.trygging=trygging
    
    def breytaupphaed(self):
        self.upphaed=raw_input("Sladu inn nyja upphaed a laninu: ")
    
    def breytavoxtum(self):
        self.vextir=raw_input("Sladu inn nyja vexti a laninu: ")
    
    def breytatryggingu(self):
        self.trygging=raw_input("Er lanid verdtryggt? (True/False): ")
    
    def prenta(self):
        print "Upphaed: ", self.upphaed
        print "Vextir: ", self.vextir
        print "Verdtrygging: ", self.trygging