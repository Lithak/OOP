class Sick:
    pass


class Cancer(Sick):
    def __init__(self, medication, scan):
        self.medication = medication
        self.scan = scan


def treatment(self):
    if self.scan > 600:
        self.amount = self.medication + self.scan
        print("sorry we cannot treat you")

    else:
        self.scan <= 600
        self.amount = self.medication + self.scan
        print(self.amount)


# instantiate object e.g(obj_odd) and properties e.g (.medication = 400)
obj_odd = Cancer(0.0)
obj_odd.medication(400)
obj_odd.scan(600)
obj_odd.treatment()


class Influenza(Sick):
    def __init__(self, medication, consultation):
        self.medication = medication
        self.consultation = consultation


def treatment(self):
    if self.consultation > 600:
        self.amount = self.medication + self.consultation * 0.98
        print(self.amount)

    else:
        self.amount = self.medication + self.consultation
        print(self.amount)


# instantiate object e.g(obj_od) and properties e.g (.medication = 400)
obj_od = Influenza(0.0)
obj_od.medication = 350
obj_od.consultation = 900
obj_od.treatment()
