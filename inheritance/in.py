class animal:
    def speak(self):
        print("some sound")

class cat(animal):
    def speak(self):
        print("meow")
c = cat()
c.speak()