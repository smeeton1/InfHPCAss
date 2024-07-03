import sys                       # Used for command line options
import numpy as num              # Gerneral math functions
import matplotlib.pyplot as plot # plotting
import tracemalloc
import time


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
        if x>alpha:
            N+=(num.exp(-num.square((x-mu)/omega)/2.0)-beta*(x-alpha))
        else:
            N+=(num.exp(-num.square((x-mu)/omega)/2.0))
        x=x+dh
    return 1/N


################################################################
#### generate prob from F(x)
def ModGause(mu,omega,alpha,beta,x):
  if x>alpha:
    prob=(num.exp(-num.square((x-mu)/omega)/2.0)-beta*(x-alpha))
  else:
    prob=(num.exp(-num.square((x-mu)/omega)/2.0))
  return prob

###########################################################
#### Calculate expectation values gotten from (https://www.geeksforgeeks.org/expectation-expected-value-array/)
def ExpVal(A,steps):
    p=1/steps
    expval = 0
    for i in range(0, steps):
        expval+=(A[i] * p) 
    return expval


###############################################################
####### Main program  

steps = range(1000,10000,1000)

##################################################################################
##################################################################################
### takeing the inputs for the parameters or using defults
if len(sys.argv)>1:
  mu=float(sys.argv[1])
  omega=float(sys.argv[2])
  alpha=float(sys.argv[3])
  beta=float(sys.argv[4])
else:
  mu=0.0
  omega=1.0
  alpha=1.0
  beta=0.5

# create the norm N 
# N = NormCal(mu,omega,alpha,beta)
# setting up initial value for x
tracemalloc.start()
t=[]  # time taken
m=[]  # memory usage 
sd=[] # the calculated sd for eash set of stepps
E=[]  # the calculated expectation value for eash set of stepps
RanOmega=omega/2 # setting to sd for the step generator 

# preforming the sampling
for j in steps:
    start = time.time()
    x = []
    x.append(1)
    xp = ModGause(mu,omega,alpha,beta,x[0])
    for i in range(j):
        y=num.random.normal(x[i],RanOmega) # move x by a random number generated by a gaussian centered at x[i]
        # num.random.normal give a random number centerd on x[i] with an sd of RanOmega 
        # this is used so as to have a symmetric generator function g giving g(xt|xi)/g(xi|xt)=1
    
        yp = ModGause(mu,omega,alpha,beta,y)
        if (yp/xp)>1:
            x.append(y)
            xp=yp
        else:
            if num.random.rand()< (yp/xp):
                x.append(y)
                xp=yp
            else:
                x.append(x[i])
    
    E.append(ExpVal(x,j))
    sd.append(num.std(x))
    end = time.time()
    t.append(end - start)
    m.append(tracemalloc.get_traced_memory()[0])

tracemalloc.stop()
#########################################
##### ploting
n_bins = 40

fig, axs = plot.subplots(tight_layout=True)
axs.hist(x, bins=n_bins)
plot.show()

fig2, axs2 = plot.subplots(2,sharex=True)
axs2[0].set_title('Time taken per number of steps')
axs2[0].plot(steps, t)
axs2[0].set_ylabel('Time(s)')
axs2[1].set_title('Memory taken per number of steps')
axs2[1].plot(steps, m)
axs2[1].set_xlabel('number of steps')
axs2[1].set_ylabel('memory')
plot.show()

fig3, axs3 = plot.subplots(2,sharex=True)
axs3[0].set_title('Standard deviation per number of steps')
axs3[0].plot(steps, sd)
axs3[0].set_ylabel('sd')
axs3[1].set_title('Expectation values per number of steps')
axs3[1].plot(steps, E)
axs3[1].set_xlabel('number of steps')
axs3[1].set_ylabel('E')
plot.show()