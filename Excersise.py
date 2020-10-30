# Creating a class.
class rectangle:
    # creating a method.
    def Area(self):
        self.answer = self.lenght * self.width
        print(self.answer)


# creating an Object.
object = rectangle()

object.lenght = int(input("Enter lenght: "))
object.width = int(input("Enter width: "))
object.Area()

