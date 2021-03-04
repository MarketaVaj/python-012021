class Employee:
#každý název třídy musí začínat velkým písmenem
    def get_info(self):
        return f" {self.name} pracuje na pozici {self.position}."
    def __init__(self, name, position): #holiday, probation = False):
        self.name = name
        self.position = position
        self.holiday = 25
#        self.probation = False

# funkce se bude spoustet v momente kdyz funkci vytvarim
#parametr e funkci init je name, proto pisu znovu name
    def __str__(self):
        return  self.name + "," + self.position + "," + str(self.holiday)

# bude převádět hodnotu na řetězec


# frantisek = Employee()
# frantisek.name = 'Frantisek Novak'
# frantisek.position = 'konstrukter'
# print(frantisek.get_info())
# #funkce musí být volána pomocí parametru, proto je na zacatku frantisek
#
# klara = Employee()
# klara.name = 'Klara Novak'
# klara.position = 'konstrukterla'
# print(klara.get_info())

#trida je formicka na cukrovi a objekty jsou potom kousky cuktovi z te formicky

#po zalozeni funkce init
frantisek = Employee("Frantisek Novak","konstrukter" )
klara = Employee("Klara Nova", "konstrukterka")
print(frantisek.get_info())
print(klara.get_info())