import sys

class Animal:
    def print_description(self):
        print("My favorite animal is")
        print(f"{self.fav_animal}.")
        print(f"Lenght of upper extremities={self.Ue_length} inches.")
        print(f"Length of lower extremities={self.Le_length} inches.")
        print(f"Number of eyes={self.eyes}.")
        print(f"Tail?{self.tail}.")
        print(f"furry?{self.furry}.")
        tail = "yes" if self.tail else "no"
        furry = "yes" if self.furry else "no"
    
    def __init__(self, animal="tiger",front_length=30.0, rear_length=32.0,tail=True,eyes=2, furry=True):
        self.fav_animal=animal
        self.Ue_length=front_length
        self.Le_length=rear_length
        self.eyes=eyes
        self.tail=tail
        self.furry=furry
    
    def tail(self):
        return "yes" if self.tail else "no"
    
def main():
    Myanimal = Animal()
    Myanimal.print_description()
    
if __name__=="__main__":
    main()