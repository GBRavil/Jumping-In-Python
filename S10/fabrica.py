   
class Animal:

    def __init__(self, name: str, rase: str):
        self.name = name
        self.rase = rase

    def who_is(self):
        return f"{self.name} {self.rase}"
    
    def eat(self):
        return "I can eat"

class Fish(Animal):

    def __init__(self, live: str, *args, **kwargs):
        self.live = live
        super().__init__(*args, **kwargs)

    def live_in(self):
        return self.live

    def swim(self):
        return "I can swim"
    
class Birds(Animal):

    def __init__(self, sound: str, name: str, rase: str):
        self.sound = sound
        super().__init__(name, rase)    

    def sound_as(self):
        return self.sound 
    
    def fly(self):
        return "I can fly"

class Fabric(Fish, Birds):

    def __init__(self, kind: str, params: str, name: str=None, rase: str=None, live: str=None, sound: str=None):
        self.kind = kind
        self.params = params
        Fish.__init__(self, live, name, rase)
        Birds.__init__(self, sound, name, rase)
        
    def getKind(self):
        return self.kind
    
    def getParams(self):
        return self.params
    
fi2 = Fish("water", "Zuza", "fish")
print(fi2.swim())
