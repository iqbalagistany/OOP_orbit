from turtle import Terminator


class Robot:
    #definisi class atribut

    def __init__(self, kepala, kaki):
        self.head = kepala
        self.foot = kaki
    
    #method (Perilakunnya)
    #method-1
    def showresult(self):
        print("Robot ini kepalanya ", self.head, "dan kakinya ", self.foot)

    #method-2
    def changehead(self, kepala):
        self.head = kepala
    
    #method-3
    def changefoot(self, kaki):
        self.foot = kaki

#buat object dari kelas robot
T = Robot("bulat", "pendek")
T.showresult()
T.changefoot("KAKI X")


