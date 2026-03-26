class father:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def add(self,*args):
        addd=0
        for i in args:
            addd+=i
        return addd
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
class son(father):
    def __init__(self,name,age,school):
        self.name=name
        self.age=age
        self.school=school

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, School: {self.school}")
        super().display()
        


son1=son("tanzeel",30,"city school")
son1.display()
father1=father("rafi",56)
father1.display()   

