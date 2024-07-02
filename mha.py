import sys
import numpy as num
import matplotlib as plot


###############################################################
#### Calculate Norm and return N = 1/Norm for simplisity I will use a basic numarical intergartion method here.
def NormCal(mu,omega,alpha,beta):
    n = 1000 # number of parts the domine is bing split into
    # set a general range [-4,4]centered on mu
    Rmin = -4 + mu
    Rmax = 4 + mu
    dh=(Rmax-Rmin)/n
    x=Rmin
    N=0
    for i in range(n):
        if x>a:
            N=N+(exp(-((x-mu)/omega)/2.0)-beta*(x-alpha))
        else:
            N=N+(exp(-((x-mu)/omega)/2.0))
        x=x+dh
    return 1/N


################################################################
#### generate prob from F(x)
def ModGause(mu,omega,alpha,beta,N,x):
  if x>a:
    prob=(N)*(exp(-((x-mu)/omega)/2.0)-beta*(x-alpha))
  else:
    prob=(N)*(exp(-((x-mu)/omega)/2.0))
  return prob


###############################################################
####### Main program  

steps = 10000

##################################################################################
##################################################################################
### takeing the inputs for the parameters or using defults
if len(sys.argv)>1:
  mu=int(sys.argv[1])
  omega=int(sys.argv[2])
  alpha=float(sys.argv[3])
  beta=float(sys.argv[4])
else:
  mu=0.0
  omega=1.0
  alpha=1.0
  beta=0.5

# create the norm N 
N = NormCal(mu,omega,alpha,beta)

# setting up initial value for x
x = []
x.append(0.0)
xp = ModGause(mu,omega,alpha,beta,N,x[0])

# preforming the sampling
for i in range(steps)
    y=x[i]+numpy.random.normal(0,0.5) # move x by a random number generated by a gaussian centered at 0
    yp = ModGause(mu,omega,alpha,beta,N,y)
    if (yp/xp)>1:
        x.append(y)
        xp=yp
    else:
        x.append(x[i])
    
