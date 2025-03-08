class employee:
    def __init__(self):
        print("Employee object is created")
        self.id = 123
        self.salary = 5000
        self.designation = "SDE"
        print("attributes are set")

    def travel(self, destination):
        print("Manually called travel method")
        print(f"Employee is now travelling to {destination}")


sam = employee()
sam.travel("Bangalore") 
print(type(sam))