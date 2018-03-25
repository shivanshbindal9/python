class FileInfo:
    def __init__(self,inp,outp):
        self.inp=inp
        self.outp=outp
 
    def vow_cons(self):
        with open(self.inp) as f:
            for i, l in enumerate(f):
                pass
        num_lines = sum(1 for word in open('test.txt').read().split())

        infile = open(self.inp, "r")
        vowels = set("AEIOUaeiou")
        cons = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
        sym = ("@#!$%^&*>?<|:;,./")
        numb= ("1234567890")

        countV = 0
        countC = 0
        countS = 0
        countN = 0
        for c in infile.read():
             if c in vowels:
                countV += 1
             elif c in cons:
                countC += 1
             elif c in sym:
                countS += 1
             elif c in numb:
                countN +=1
        file1 = open(self.outp,"w")
        file1.write ("no of vowels {}, consonents {}, symbols {} , numbers {}, word count {} ,line count {}".format(countV,countC,countS,countN,num_lines,i+1))
        

f = FileInfo('test.txt','out.txt')

f.vow_cons()

print("executed sucessfully")


