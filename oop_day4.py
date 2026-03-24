# class car:
#     def __init__(self, model, brand , colour):
#         self.model = model
#         self.brand = brand
#         self.colour = colour
    
#     def start(self):
#         print("car is starting")
    
#     def info(self):
#         print(f"model: {self.model},\n brand: {self.brand},\n colour: {self.colour}")

# car1 = car("1995", "BMW", "black")
# car1.start()
# car1.info()

class student:
    marks_list = []
    def __init__(self,name,marks):
        self.name = name
        for i in range(4):
            if marks == 0 and marks > 100:
                print("Invalid marks. Please enter marks between 0 and 100.")   
            marks = int(input("Enter student marks: "))
            self.marks_list.append(marks)

        self.marks = marks

    def avg_marks(self):
        total_marks = sum(self.marks_list)
        num_students = len(self.marks_list)
        average = total_marks / num_students    
        return average
    
    def total_marks(self):
        return sum(self.marks_list)

student1 = student("John", 0)
print(f"{student1.name}'s average marks: {student1.avg_marks()}")
print(f"{student1.name}'s total marks: {student1.total_marks()}")