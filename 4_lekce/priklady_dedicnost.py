class Package:
    def __init__(self, address, weight):
        self.address = address
        self.weight = weight
        self.delivered = False

    def deliver(self):
        self.delivered = True

    def get_info(self):
        return f'Adresa: {self.address}, Vaha: {self.weight}, Stav doruceni: {self.delivered}'

class ValuablePackage(Package):
    def __init__(self, address, weight, value):
        super().__init__(address, weight)
        self.value = value

    def get_info(self):
        return f'Adresa: {self.address}, Vaha: {self.weight}, Stav doruceni: {self.delivered}, Ma hodnototu {self.value}'

FirstPackage = ValuablePackage("Straznice", "20kg", 1000)
SecondPackege = Package ("Petrov", "10kg")
print(FirstPackage.get_info())
print(SecondPackege.get_info())


class Employee:
  def takeHoliday(self, days):
    if self.remainingHolidayDays >= days:
      self.remainingHolidayDays -= days
      return f"Užij si to."
    else:
      return f"Bohužel už máš nárok jen na {self.remainingHolidayDays} dní."
  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.remainingHolidayDays = 25

class PartTimeEmployee(Employee):
    def __init__(self, name, position, workload):
        super().__init__(name, position)
        self.workload = workload

    def getInfo(self):
        # return f"{self.name} pracuje na pozici {self.position} a jeho uvazek je {self.workload}"
        return  super().getInfo() + f"Uvazek je {self.workload}"

FirstPartTimeEmployee = PartTimeEmployee("Marketa", "analytik", 0.5)
print(FirstPartTimeEmployee.getInfo())

# PŘÍKLAD ŘIDIČ
class Package:
    def __init__(self, address, weight):
        self.address = address
        self.weight = weight
        self.delivered = False

    def deliver(self):
        self.delivered = True

    def get_info(self):
        return f'Adresa: {self.address}, Vaha: {self.weight}, Stav doruceni: {self.delivered}'

class Driver:
    def __init__(self, name):
        self.name = name
        self.packageList = []
    def assignPackage(self, package):
        if package.delivered:
            print('Balik uz byl dorucen.')
        else:
            self.packageList.append(package)

    def remainingPackages(self):
        return len(self.packageList)

balik = Package("Brno", 200)
balik2 = Package("Praha", 200)

print(balik.get_info())

ridic = Driver("Martin")
print(ridic.remainingPackages())
ridic.assignPackage(balik)
print(ridic.remainingPackages())
# ridic.assignPackage(balik2)
# print(ridic.remainingPackages())

