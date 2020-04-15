#Neuron M-P


def f(x):
    if x >=0.0:
        return 1.0
    else:
        return 0.0


def NOT(u):
    w=[-0.6,0.5]
    n=2
    x=0.0
    for i in range (0,n):
        x+=w[i]*u[i]
    return f(x)

def AND(u):
    w=[0.3,0.3,-0.5]
    n=3
    x=0.0
    for i in range (0,n):
        x+=w[i]*u[i]
    return f(x)

def NAND(u):
    w=[-0.3,-0.3,0.5]
    n=3
    x=0.0
    for i in range (0,n):
        x+=w[i]*u[i]
    return f(x)

def OR(u):
    w=[0.6,0.6,-0.5]
    n=3
    x=0.0
    for i in range (0,n):
        x+=w[i]*u[i]
    return f(x)


def main():


    while 1:
        print("WYBIERZ BRAMKE:\n1 NOT  \n2 AND \n3 NAND \n4 OR")
        x=input()

        if x=="1":
            u=[]
            u.append(float(input("PODAJ U1\n")))
            u.append(1.0)
            print("y=",NOT(u))
            print("\n")
        elif x=="2":
            u=[]
            u.append(float(input("PODAJ U1\n")))
            u.append(float(input("PODAJ U2\n")))
            u.append(1.0)
            print("y=",AND(u))
            print("\n")

        elif x=="3":
            u=[]
            u.append(float(input("PODAJ U1\n")))
            u.append(float(input("PODAJ U2\n")))
            u.append(1.0)
            print("y=",NAND(u))
            print("\n")
        elif x=="4":
            u=[]
            u.append(float(input("PODAJ U1\n")))
            u.append(float(input("PODAJ U2\n")))
            u.append(1.0)
            print("y=",OR(u))
            print("\n")
        else:
            print("WYBIERZ JESZCZE RAZ")



if __name__ == '__main__':
    main()
