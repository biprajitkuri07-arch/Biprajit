class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        total = sum(self.marks)
        average = total / len(self.marks)

        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print("Total Marks:", total)
        print("Average Marks:", average)


# Creating object
student1 = Student("Rahul", 101, [80, 75, 90])

# Calling function
student1.display()