import math
def pyramid(num) :
    
        try :
            for i in range(0,num):
                for j in range(0,i):
                    print(str(j)+"x"+str(i)+"="+str(i*j))
        except ValueError:
            print("please input 1~9")
pyramid(3)
