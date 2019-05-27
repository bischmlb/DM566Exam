
import numpy

def calulcateAll(p, q):
    dist2 = 0
    dist1 = 0
    distinf = 0
    distw = 0
    distM = 0
    w = [1,1.5,2.5]

    dist2 = ((abs(p[0]-q[0])**2)+(abs(p[1]-q[1])**2)+(abs(p[2]-q[2])**2))**(1/2)
    dist1 = (abs(p[0]-q[0]))+(abs(p[1]-q[1]))+(abs(p[2]-q[2]))
    distinf = max((abs(p[0]-q[0])),(abs(p[1]-q[1])),(abs(p[2]-q[2])))
    distw = ((w[0]*abs(p[0]-q[0])**2)+(w[1]*abs(p[1]-q[1])**2)+(w[2]*abs(p[2]-q[2])**2))**(1/2)
    #distM1 = ((p-q)*M*(p-q))

    print("dist2 = ", dist2)
    print("----------------")
    print("dist1 = ", dist1)
    print("----------------")
    print("distinf = ", distinf)
    print("----------------")
    print("distw = ", distw)
    print("----------------")




#a (1, 4, 4), b(8, 1, 7), c(2, 4, 10), d(1, 2, 13), q(1, 8, 7)\


if __name__ == "__main__":
    q = [1,8,7]
    p = [8,1,7]
    calulcateAll(p,q)
