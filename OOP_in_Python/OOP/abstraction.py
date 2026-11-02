from abc import ABC
class animal():
    def make_sound(self):
        pass
    
    
class lion(animal):
    def make_sound(self):
        
        print("roar!!!!")
        
        
        
class cat(animal):
    def make_sound(self):
        
        print("mew!!!!")
        
        
#================================================
lion=lion()
lion.make_sound()

cat=cat()
cat.make_sound()