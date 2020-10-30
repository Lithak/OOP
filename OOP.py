# Creating a class.
class intro:
    # creating a method.
    def intro_oop(self):
        print("I am a", self.name)
        print("My colour is", self.color)


# creating an Object.
object_shape1 = intro()

object_shape1.name = "Square"
object_shape1.color = "Black"

object_shape1.intro_oop()
