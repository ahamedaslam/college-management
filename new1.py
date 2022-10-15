class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def met(self):
        print("my name is",self.name,"and","my age is",self.age)

obj = person("aslam",22)
obj1 = person("abdul",21)


obj.met()
obj1.met()
