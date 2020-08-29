class student:
    def sname(self,name):
        self.name=name
        print(self.name)
    def sroll(self,roll):
        self.roll=roll
        print(self.roll)
    def sreg(self):
        self.reg="1217103060"+self.roll
        print(self.reg)
    def sgen(self,gen):
        self.gen=gen
        print(self.gen)
    def marks(self,ma):
        self.ma=ma
        print((int(self.ma)/470)*100)
s1=student()
s1.sname("karthik")
s1.sroll("37")
s1.sreg()
s1.sgen("m")
s1.marks("456")