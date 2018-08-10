class dummy:
    num=1
    def Num(self):
        print('class dummy num:',self.num)
        print('global num: ',num)
        self.num+=1

n=dummy()
num=1
for i in range(5):
    num*=10
    n.Num()
