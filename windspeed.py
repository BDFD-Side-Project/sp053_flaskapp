
# Inputs

# Primary

zm=40#6 #10 # the elevation of known windspeed and temperture above water/ground level (m)
U=20#20/1.25 # 30# known average wind speed for the duration(m/s)
atm=5 # averaging time of known windspped (min)
Ta=16 # known air temperature at zm (C Degrees)
Tw=12 # known water surface temperature at C Degrees 
TaaC=6.667#6.667 # known mean air temperature of the constant-stress layer (C Degrees)
wdu=10 # required averaging time for windspped (min) (A wanrning will show if wdu<=1/60 or wdu>=600!!)
zu=120 # the maximum height for profile illustration (<=zcsy)

o1=1 # catagory of water environment: 1 open ocean (offshore), 2 others, such as coastal waters (including bays or estuaries) and large lakes or reserviors 

o2=3 # catagory of known windspeed: 1) low-level overwater data; 2) geostrophic winds; 3) low-level overland data.   
if o2==2:# or (o2==3 and o3==2):
    Rg=.7#None#.7 # Rg=U10/Ug, read from Figure II-2-13 in CEM 2015
if o2==3:
    o3=2 # scanario of known overland wind speed : 1) onshore wind at an anemometer immediately adjacent to water, 2) other scenarios
if o2==2 or (o2==3 and o3==2):    
    Xlat=-44 # average latitude of fetch (+: for the Northern hemisphere, -: for the Southern hemisphere); required when o2 = 2 or 3
if o2==3 and o3==2:
    X=42 # distance from an overwater loaction to the shore, or fetch length (km)

# Secondary (default)
tol=0.0001 # Iteration tolerance
z0l=0.03#0.3 # overland z0 (m) (when o2=3 and o3=2). A high z0l gives a very high Ug.
z0=0.003# initial value of z0 (m): 0.003 (工程水文学), or 0.001 (Mikhail 1977; Foken 2008)
z02=z0 # for B-D
k=0.4 # von Karman Constant (approximately 0.4)
c1=.11#.48#10*0.1525/1.388#(ACES)#10*0.684/1.388(Cardone)##0.48#0.1 # a coefficient in estimating z0 for wind profile in JONSWAP-CEM 
c2=.0185#1/81.1#0.019*9.81/9.8#(ACES)#4.28*9.81/1000#(Cardone)#1/81.1#1/56 # a coefficient in estimating z0 for wind profile in JONSWAP-CEM 
c3=0#-0.00371/100#(ACES)#-4.43/10000#(Cardone)# a coefficient in estimating z0 for wind profile in JONSWAP-CEM 
gammap=18
phi1u=5 # somewhat sensitive? (for example, 5 may make some difference, and 2 or 3 may cause a dead loop in estimating Uf and Lp?)
phi1l=0.0
va=1.4607/100000#1.388/100000 # kinematic viscosity of air at 280 K degrees (https://www.engineeringtoolbox.com/air-absolute-kinematic-viscosity-d_601.html)
Cdlc=0.00255 # an coefficient in Cdland
dU=0.001 # step applied for the numerical derivative in the Newton-Raphson method solving 1-h U10 for API RP 2A-WSD (m/s)
zcsy=120 # height of constant-stress later
Uu=50 # the maximum windspeed for profile illustration (m/s)

# Calculations
import numpy as np
import math
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus']=False

# Functions 
def phi1f(z,x): # a function of solving phi (phi^4-gammap*phi^3*z/L'=1), in which x=L'.
    le=phi1l # the upper end of phi range
    ue=phi1u # the lower end of phi range
    mp=0.5*(le+ue) # the mid point between both ends
    while abs(mp**4-gammap*mp**3*z/x-1)>tol:   
        if mp**4-gammap*mp**3*z/x-1>0:
            ue=mp 
        else:
            le=mp
        mp=0.5*(le+ue)
    return mp

def psi1f(x): # the psi function in terms of phi (for KEYPS Model) 
    y=1-x-3*math.log(x)+2*math.log(0.5+0.5*x)+2*math.atan(x)-0.5*math.pi+math.log(0.5+0.5*x**2)
    return y

def psi2f(x): # the psi function in terms of phi (for B-D Model) 
    y=math.log((1+x)**2*(1+x**2)/8)-2*math.atan(x)+0.5*math.pi 
    return y

def A(x): # A function in the ABL resistance law
    if x<=0:
        Af = 1.1+3.7241*math.log(1-0.02*x)
    else:
        Af = 1.1-6.364*math.log(1+0.02*x)			 
    return Af

def B(x): # B function in the ABL resistance law
    if x<=0:
        Bf = 4.3-(4.3-0.23)*(1-math.exp(0.03*x))         
    else:
        Bf = 4.3+0.7*x**0.5			 
    return Bf

def att(u1,t1,t2): # a function transforming widnspeeds between different averaging times (AT) by the CEM method
# u1: windspeed (m/s) at AT t1 (min), u2: windspeed (m/s) at AT t2 (min)
    if 1/60<t1<=60:
        if 1/60<t2<=60:
            if t2==60:                
                u2=np.array(u1)/(1.277+0.296*math.tanh(0.9*math.log10(45/t1/60)))*(t1!=60)+np.array(u1)*(t1==60)
            else:
                u2=(1.277+0.296*math.tanh(0.9*math.log10(45/t2/60)))*np.array(u1)/(1.277+0.296*math.tanh(0.9*math.log10(45/t1/60)))*(t1!=60)+(1.277+0.296*math.tanh(0.9*math.log10(45/t2/60)))*np.array(u1)*(t1==60)
        if 60<t2<600:
            u2=(1.5334-0.15*math.log10(t2*60))*np.array(u1)/(1.277+0.296*math.tanh(0.9*math.log10(45/t1/60)))*(t1!=60)+(1.5334-0.15*math.log10(t2*60))*np.array(u1)*(t1==60)       
    if 60<t1<600:
        if 1/60<t2<=60:
            if t2==60:
                u2=np.array(u1)/(1.5334-0.15*math.log10(t1*60))
            else:
                u2=(1.277+0.296*math.tanh(0.9*math.log10(45/t2/60)))*np.array(u1)/(1.5334-0.15*math.log10(t1*60))
        if 60<t2<600:
            Up1=(1.5334-0.15*math.log10(t2*60))*np.array(u1)/(1.5334-0.15*math.log10(t1*60))
    return u2

# 1. Basic Windspeed Calculations
print('')
print('---滨水工的风速计算---')
nn=0 # order number of notes

if TaaC==None:
    TaaC=Ta
Taa=TaaC+273.15 # known mean air temperature of the constant-stress layer (K)

#dT=Ta-Tw
dT=Ta+zm*9.8/1000-Tw # air-sea potential temperature difference at C Degrees (= air temeprature - water surface temperature)
if dT==None:
    dT=0

nn=nn+1
print(nn,'. 图中的风速廓线均指水上风速。')
nn=nn+1
print(nn,'. 水面以上10 m处风速(U\u2081\u2080)的数值结果见下表。')

nn=nn+1
if dT==0:
    print(nn,'. 大气边界层常应力层的稳定性状态：中性')
if dT>0:
    print(nn,'. 大气边界层常应力层的稳定性状态：稳定')
if dT<0:
    print(nn,'. 大气边界层常应力层的稳定性状态：不稳定')

ssBD1=0 # for B-D

zp1=[j for j in range(0,zu+1)] # z values for KEYPS profile
zp2=[j for j in range(0,zu+1)] # z values for B-D profile
Up1=[1 for j in range(0,zu+1)] # windspeeds on KEYPS profile
Up2=[1 for j in range(0,zu+1)] # windspeeds on B-D profile

# KEYPS和B-D风速廓线及大气层阻力定律

# various initial values
if o2==1 or (o2==3 and o3==1):

    plt.scatter(U,zm,c="blue",marker="*",s=60,edgecolors="blue",label='已知的'+str(round(atm))+'-min水上风速及对应高度')
    if o2==3 and o3==1:
        nn=nn+1
        print(nn,'. 本例中的已知风速可视为水上风速。')
    
    Uf0=k*U/math.log(zm/z0) # the initial value of friction velocity
    Uf20=Uf0# for B-D
    if dT!=0:
        Lp0=Taa/k**2/9.81*Uf0**2*math.log(zm/z0)/dT      
        
    z0=c1*va/Uf0+c2*Uf0**2/9.81+c3
    z02=c1*va/Uf20+c2*Uf20**2/9.81+c3

    if dT==0: # neutral
        Uf=k*U/math.log(zm/z0)
        
    if dT>0: # stable
        Uf=k*U/(math.log(zm/z0)+7*zm/Lp0)
        Lp=Taa/k**2/9.81*Uf**2*(math.log(zm/z0)+7*zm/Lp0-7*z0/Lp0)/dT

        Ri2=min(0.199,9.81*k**2*(zm-z02)*dT*0.95/Taa/Uf20**2/math.log(zm/z02)) # for B-D # this quation only for stable air. How about unstable? 
        L0=(1-5*Ri2)*(zm-z02)/Ri2
        Uf2=k*U/(math.log(zm/z02)+6*zm/L0-6*z02/L0) 
        Ri2=min(0.199,9.81*k**2*(zm-z02)*dT*(0.95+7.8*(zm-z02)/L0)/Taa/Uf2**2/(math.log(zm/z02)+7.8*zm/L0-7.8*z02/L0)/(1+6*(zm-z02)/L0)**2) # for B-D
        L=(1-5*Ri2)*(zm-z02)/Ri2
        
    if dT<0: # unstable
        phi1=phi1f(zm,Lp0)
        psi1=psi1f(phi1)
        Uf=k*U/(math.log(zm/z0)-psi1+psi1f(phi1f(z0,Lp0)))
        Lp=Taa/k**2/9.81*Uf**2*(math.log(zm/z0)-psi1+psi1f(phi1f(z0,Lp0)))/dT

        Ri2=9.81*k**2*(zm-z02)*dT*0.95/Taa/Uf20**2/math.log(zm/z02) # for B-D # this quation only for stable air. How about unstable?
        L0=(zm-z02)/Ri2
        psi2=psi2f((1-19.3*zm/L0)**0.25)
        Uf2=k*U/(math.log(zm/z02)-psi2+psi2f((1-19.3*z02/L0)**0.25))
        Ri2=9.81*k**2*(zm-z02)*dT*(0.95*(1-11.6*(zm-z02)/L0))**(-0.5)/Taa/Uf2**2/(math.log(zm/z02)-psi2+psi2f((1-19.3*z02/L0)**0.25))/(1-19.3*(zm-z02)/L0)**(-0.5)  # for B-D
        L=(zm-z02)/Ri2

if o2==2 or (o2==3 and o3==2):

    fCo=1.45*math.sin(Xlat*math.pi/180)/10000 # original Coriolis parameter
    fC=abs(fCo) # the absolute value of original Coriolis parameter
    
    if o2==3: 
        Ufl=k*U/math.log(zm/z0l) # friction velocity for overland wind       
        Ug=Ufl*((math.log(Ufl/fC/z0l)-A(0))**2+B(0)**2)**0.5/k # estimated geostrophic windspeed
        #Ug=Ufl/.0275
        plt.scatter(U,zm,c="blue",marker="*",s=50,edgecolors="blue",label='已知的'+str(round(atm))+'-min陆上风速及对应高度')
        plt.axvline(Ug,ls="--",color="blue",linewidth=0.5,label='推算的'+str(round(atm))+'-min $U_g$ (自由大气中)')
        nn=nn+1
        print(nn,'. 陆域风速对数分布律参数： 摩擦风速U*=',round(Ufl,3),'m/s')
        nn=nn+1
        print(nn,'. 根据已知陆域风推算的地转风速Ug=',round(Ug,3),'m/s')            
    if o2==2:
        Ug=U # geostrophic windspeed (measured)
        plt.axvline(U,ls="--",color="blue",linewidth=0.5,label='已知的'+str(round(atm))+'-min Ug (自由大气中)')
    plt.text(Ug,-2.5,'Ug',fontdict=None)    

    #overwater    
    Uf0=1 # initial value
    Uf20=Uf0# for B-D
    if dT!=0:
        Lp0=Taa/k**2/9.81*Uf0**2*math.log(zm/z0)/dT

    Uf=k*Ug/((math.log(Uf0/fC/z0)-A(0))**2+B(0)**2)**0.5    
    theta=math.asin(B(0)*Uf/k/Ug)*(Xlat<=0)+math.asin(-B(0)*Uf/k/Ug)*(Xlat>0)

    Uf2=k*Ug/((math.log(Uf20/fC/z02)-A(0))**2+B(0)**2)**0.5    
    theta2=math.asin(B(0)*Uf2/k/Ug)*(Xlat<=0)+math.asin(-B(0)*Uf2/k/Ug)*(Xlat>0)
    
    if dT>0:
        Lp=Taa/k**2/9.81*Uf**2*(math.log(zm/z0)+7*zm/Lp0-7*z0/Lp0)/dT

        Ri2=min(0.199,9.81*k**2*(zm-z02)*dT*0.95/Taa/Uf20**2/math.log(zm/z02)) # for B-D # this quation only for stable air. How about unstable? 
        L0=(1-5*Ri2)*(zm-z02)/Ri2
        Ri2=min(0.199,9.81*k**2*(zm-z02)*dT*(0.95+7.8*(zm-z02)/L0)/Taa/Uf2**2/(math.log(zm/z02)+7.8*zm/L0-7.8*z02/L0)/(1+6*(zm-z02)/L0)**2) # for B-D
        L=(1-5*Ri2)*(zm-z02)/Ri2
         
    if dT<0:
        Lp=Taa/k**2/9.81*Uf**2*math.log(zm/z0)/dT

        Ri2=9.81*k**2*(zm-z02)*dT*0.95/Taa/Uf20**2/math.log(zm/z02) # for B-D # this quation only for stable air. How about unstable?
        L0=(zm-z02)/Ri2
        psi2=psi2f((1-19.3*zm/L0)**0.25)
        Ri2=9.81*k**2*(zm-z02)*dT*(0.95*(1-11.6*(zm-z02)/L0))**(-0.5)/Taa/Uf2**2/(math.log(zm/z02)-psi2+psi2f((1-19.3*z02/L0)**0.25))/(1-19.3*(zm-z02)/L0)**(-0.5)  # for B-D
        L=(zm-z02)/Ri2

# various iterations

if dT==0:
    if o2==1 or (o2==3 and o3==1):
        while abs(Uf-Uf0)>tol:#0.001:
            z0=c1*va/Uf+c2*Uf**2/9.81+c3    
            Uf0=Uf
            Uf=k*U/math.log(zm/z0)
    else:
        miu=0
        while abs(Uf-Uf0)>tol:#0.001:        
            z0=c1*va/Uf+c2*Uf**2/9.81+c3
            Uf0=Uf               
            Uf=k*Ug*math.cos(theta)/(math.log(Uf/fC/z0)-A(0))
            theta=math.asin(B(0)*Uf/k/Ug)*(Xlat<=0)+math.asin(-B(0)*Uf/k/Ug)*(Xlat>0)

    zp1[0]=z0
    Up1=Uf*(np.log(zp1)-np.log(z0))/k
    Up2=Up1
    U100=Uf*math.log(10/z0)/k # at 10 m elevation, after stability adjustment        
    U1002=U100
    
if dT!=0:
    z0=c1*va/Uf+c2*Uf**2/9.81+c3
    z02=c1*va/Uf2+c2*Uf2**2/9.81+c3
    
    if o2==1 or (o2==3 and o3==1):    
        while max(abs(Uf-Uf0),abs(Lp-Lp0))>tol:#0.01 KEYPS
            z0=c1*va/Uf+c2*Uf**2/9.81+c3    
            Uf0=Uf
            Lp0=Lp

            if dT>0: # stable
                Uf=k*U/(math.log(zm/z0)+7*(zm-z0)/Lp0)
                Lp=Taa/k**2/9.81*Uf**2*(math.log(zm/z0)+7*(zm-z0)/Lp0)/dT # initial value of L'
                
            if dT<0: # unstable
                Uf=k*U/(math.log(zm/z0)-psi1f(phi1f(zm,Lp0))+psi1f(phi1f(z0,Lp0)))
                Lp=Taa/k**2/9.81*Uf**2*(math.log(zm/z0)-psi1f(phi1f(zm,Lp0))+psi1f(phi1f(z0,Lp0)))/dT

        while max(abs(Uf2-Uf20),abs(L-L0))>tol:#0.01 B-D
            z02=c1*va/Uf2+c2*Uf2**2/9.81+c3
            Uf20=Uf2
            L0=L

            if dT>0: # stable
                Ri2=9.81*k**2*(zm-z02)*dT*(0.95+7.8*(zm-z02)/L0)/Taa/Uf2**2/(math.log(zm/z02)+7.8*(zm-z02)/L0)/(1+6*(zm-z02)/L0)**2 # for B-D
                if Ri2>0.199:
                    ssBD1=1
                    Ri2=0.199
                    L=(1-5*Ri2)*(zm-z02)/Ri2
                    Uf2=k*U/(math.log(zm/z02)+6*(zm-z02)/L)# the factor 6 from Foken (2008)
                    L0=L
                    Uf20=Uf2
                    z02=c1*va/Uf2+c2*Uf2**2/9.81+c3
                else:
                    L=(1-5*Ri2)*(zm-z02)/Ri2
                    Uf2=k*U/(math.log(zm/z02)+6*(zm-z02)/L)

            if dT<0:
                Ri2=9.81*k**2*(zm-z02)*dT*(0.95*(1-11.6*(zm-z02)/L0))**(-0.5)/Taa/Uf2**2/(math.log(zm/z02)-psi2+psi2f((1-19.3*z02/L)**0.25))/(1-19.3*(zm-z02)/L0)**(-0.5) 
                L=(zm-z02)/Ri2
                psi2=psi2f((1-19.3*zm/L)**0.25)
                Uf2=k*U/(math.log(zm/z02)-psi2+psi2f((1-19.3*z02/L)**0.25))
                
        if dT>0:
            z0=c1*va/Uf+c2*Uf**2/9.81+c3  # necessary?
            Uf=k*U/(math.log(zm/z0)+7*(zm-z0)/Lp) # a final update
            Uzm1=Uf*(math.log(zm/z0)+7*(zm-z0)/Lp)/k # at the measurement elevation for checking
            zp1[0]=z0
            Up1=Uf*(np.log(np.array(zp1)/z0)+7*(np.array(zp1)-z0)/Lp)/k
            Up1n=Uf*np.log(np.array(zp1)/z0)/k # a nuetral profile based on KEYPS model for comparison 

            z02=c1*va/Uf2+c2*Uf2**2/9.81+c3# necessary?
            Uf2=k*U/(math.log(zm/z02)+6*(zm-z02)/L)
            Uzm2=Uf2*(math.log(zm/z02)+6*(zm-z02)/L)/k # at the measurement elevation for checking
            zp2[0]=z02
            Up2=Uf2*(np.log(np.array(zp2)/z02)+6*(np.array(zp2)-z02)/L)/k
            Up2n=Uf2*np.log(np.array(zp2)/z02)/k # a nuetral profile based on B-D model for comparison 
                        
        if dT<0:
            z0=c1*va/Uf+c2*Uf**2/9.81+c3  # necessary?
            Uf=k*U/(math.log(zm/z0)-psi1f(phi1f(zm,Lp))+psi1f(phi1f(z0,Lp)))# a final update
            
            phi1zm=phi1f(zm,Lp)         
            psi1zm=psi1f(phi1zm)
            Uzm1=Uf*(math.log(zm/z0)-psi1zm+psi1f(phi1f(z0,Lp)))/k # at the measurement elevation for checking

            zp1[0]=z0
            for i in range(0,zu+1):
                phi1z=phi1f(zp1[i],Lp)  
                psi1z=psi1f(phi1z) 
                Up1[i]=Uf*(np.log(zp1[i]/z0)-psi1z+psi1f(phi1f(z0,Lp)))/k
                if Up1[i]<0:
                    Up1[i]=0
            Up1n=Uf*np.log(np.array(zp1)/z0)/k # a nuetral profile based on KEYPS model for comparison 
            
            z02=c1*va/Uf2+c2*Uf2**2/9.81+c3# necessary?
            Ri2=9.81*k**2*(zm-z02)*dT*(0.95*(1-11.6*(zm-z02)/L0))**(-0.5)/Taa/Uf2**2/(math.log(zm/z02)-psi2+psi2f((1-19.3*z02/L)**0.25))/(1-19.3*(zm-z02)/L0)**(-0.5)
            L=(zm-z02)/Ri2
            
            psi2zm=psi2f((1-19.3*zm/L)**0.25)
            Uzm2=Uf2*(math.log(zm/z02)-psi2zm+psi2f((1-19.3*z02/L)**0.25))/k
            
            zp2[0]=z02
            for i in range(0,zu+1):
                psi2z=psi2f((1-19.3*zp2[i]/L)**0.25)
                Up2[i]=Uf2*(math.log(zp2[i]/z02)-psi2z+psi2f((1-19.3*z02/L)**0.25))/k
                if Up2[i]<0:
                    Up2[i]=0
            Up2n=Uf2*np.log(np.array(zp2)/z02)/k # a nuetral profile based on B-D model for comparison 
            
    if (o2==3 and o3==2) or o2==2:
        
        while max(abs(Uf-Uf0),abs(Lp-Lp0))>tol:#0.01 # KEYPS    
            z0=c1*va/Uf+c2*Uf**2/9.81+c3    
            Uf0=Uf
            Lp0=Lp
            
            miu=k*Uf/fC/Lp
            Uf=k*Ug*math.cos(theta)/(math.log(Uf/fC/z0)-A(miu))
            theta=math.asin(B(miu)*Uf/k/Ug)*(Xlat<=0)+math.asin(-B(miu)*Uf/k/Ug)*(Xlat>0)
                               
            if dT>0: # stable
                Lp=Taa/k**2/9.81*Uf**2*(math.log(zm/z0)+7*(zm-z0)/Lp0)/dT
               
            if dT<0: # unstable
                phi1=phi1f(zm,Lp0)
                psi1=psi1f(phi1)
                Lp=Taa/k**2/9.81*Uf**2*(math.log(zm/z0)-psi1+psi1f(phi1f(z0,Lp0)))/dT
 
        miu=k*Uf/fC/Lp
        Uf=k*Ug*math.cos(theta)/(math.log(Uf/fC/z0)-A(miu))

        while max(abs(Uf2-Uf20),abs(L-L0))>tol:#0.01 # B-D
            z02=c1*va/Uf2+c2*Uf2**2/9.81+c3
            Uf20=Uf2
            L0=L
                        
            miu2=k*Uf2/fC/L
            Uf2=k*Ug*math.cos(theta2)/(math.log(Uf2/fC/z02)-A(miu2))
            theta2=math.asin(B(miu2)*Uf2/k/Ug)*(Xlat<=0)+math.asin(-B(miu2)*Uf2/k/Ug)*(Xlat>0)
                 
            if dT>0: # stable
                Ri2=9.81*k**2*(zm-z02)*dT*(0.95+7.8*(zm-z02)/L0)/Taa/Uf2**2/(math.log(zm/z02)+7.8*(zm-z02)/L0)/(1+6*(zm-z02)/L0)**2 # for B-D
                L=(1-5*Ri2)*(zm-z02)/Ri2
                if Ri2>0.199:
                    ssBD1=1
                    Ri2=0.199                    
                    miu2=200
                    L=k*Uf2/miu2/fC
                    theta2i=math.asin(B(miu2)*Uf2/k/Ug)*(Xlat<=0)+math.asin(-B(miu2)*Uf2/k/Ug)*(Xlat>0)
                    Uf2i=Uf2
                    z02i=z02
                    while max(abs(theta2i-theta2),abs(Uf2i-Uf2),abs(z02i-z02))>tol:
                        theta2=theta2i
                        Uf2=Uf2i
                        z02=z02i

                        z02i=c1*va/Uf2i+c2*Uf2i**2/9.81+c3
                        Uf2i=k*Ug*math.cos(theta2)/(math.log(Uf2/fC/z02)-A(miu2))                    
                        theta2i=math.asin(B(miu2)*Uf2/k/Ug)*(Xlat<=0)+math.asin(-B(miu2)*Uf2/k/Ug)*(Xlat>0)
                        L=k*Uf2/miu2/fC
                        
                    theta2=theta2i
                    Uf2=Uf2i
                    L0=L
                    Uf20=Uf2
                    z02=c1*va/Uf2+c2*Uf2**2/9.81+c3                    
              
            if dT<0: # unstable
                Ri2=9.81*k**2*(zm-z02)*dT*(0.95*(1-11.6*(zm-z02)/L0))**(-0.5)/Taa/Uf2**2/(math.log(zm/z02)-psi2+psi2f((1-19.3*z02/L)**0.25))/(1-19.3*(zm-z02)/L0)**(-0.5) #???????
                L=zm/Ri2
                psi2=psi2f((1-19.3*zm/L)**0.25)
            
        Uf2=k*Ug*math.cos(theta2)/(math.log(Uf2/fC/z02)-A(miu2))# a final update
        
        if dT>0:
            Uzm1=Uf*(math.log(zm/z0)+7*(zm-z0)/Lp)/k # at the measurement elevation for checking  
            zp1[0]=z0
            Up1=Uf*(np.log(np.array(zp1)/z0)+(7*np.array(zp1)-z0)/Lp)/k
            Up1n=Uf*np.log(np.array(zp1)/z0)/k # a nuetral profile based on KEYPS model for comparison 

            Uzm2=Uf2*(math.log(zm/z02)+6*(zm-z02)/L)/k # at the measurement elevation for checking
            zp2[0]=z02
            Up2=Uf2*(np.log(np.array(zp2)/z02)+(6*np.array(zp2)-z02)/L)/k
            Up2n=Uf2*np.log(np.array(zp2)/z02)/k # a nuetral profile based on B-D model for comparison 
        if dT<0:
            
            phi1zm=phi1f(zm,Lp)         
            psi1zm=psi1f(phi1zm)
            Uzm1=Uf*(math.log(zm/z0)-psi1zm+psi1f(phi1f(z0,Lp)))/k # at the measurement elevation for checking

            zp1[0]=z0
            for i in range(0,zu+1):
                phi1z=phi1f(zp1[i],Lp)  
                psi1z=psi1f(phi1z) 
                Up1[i]=Uf*(np.log(zp1[i]/z0)-psi1z+psi1f(phi1f(z0,Lp)))/k
                if Up1[i]<0:
                    Up1[i]=0
            Up1n=Uf*np.log(np.array(zp1)/z0)/k # a nuetral profile based on KEYPS model for comparison
            
            psi2zm=psi2f((1-19.3*zm/L)**0.25)
            Uzm2=Uf2*(math.log(zm/z02)-psi2zm+psi2f((1-19.3*z02/L)**0.25))/k
            
            zp2[0]=z02
            for i in range(0,zu+1):
                psi2z=psi2f((1-19.3*zp2[i]/L)**0.25)
                Up2[i]=Uf2*(math.log(zp2[i]/z02)-psi2z+psi2f((1-19.3*z02/L)**0.25))/k
                if Up2[i]<0:
                    Up2[i]=0
            Up2n=Uf2*np.log(np.array(zp2)/z02)/k # a nuetral profile based on B-D model for comparison
            
if o2==3 and o3==2:
    if X<2:
        RF=1.0
    if 2<=X<30:
        RF=0.5*(1.1+1.14)
    if 30<=X<50:
        RF=0.5*(1.14+1.23)
    if 50<=X<100:
        RF=0.5*(1.23+1.3)
    if X>=100:
        RF==1.3 # assumed
    Up1=RF*np.array(Up1)
    Up2=RF*np.array(Up2)
    nn=nn+1
    print(nn,'. 陆上风进入水域后随风距的增大系数RF=',round(RF,2))    

if o2==3:
    nn=nn+1
    print(nn,'. 图中已知陆上风速的位置按地面以上的高度绘出。')    
    
# Duration adjustment for required averaging time
if atm!=wdu:
    Up1=att(Up1,atm,wdu)
    Up2=att(Up2,atm,wdu)
    Up1n=att(Up1n,atm,wdu)
    Up2n=att(Up2n,atm,wdu)    
        
nn=nn+1
if dT==0:
    print(nn,'. 水域风速廓线参数： 粗糙度z0=',round(z0*1000,2),'mm, 摩擦风速U*=',round(Uf,3),'m/s')
else:
    print(nn,'. 水域风速KEYPS廓线参数： 粗糙度z0=',round(z0*1000,2),'mm, 摩擦风速U*=',round(Uf,3),'m/s, 修改后的Obukhov稳定长度L\u2032=',round(Lp,3),'m')
    nn=nn+1
    print(nn,'. 水域风速B-D廓线参数： z0=',round(z02*1000,2),'mm, U*=',round(Uf2,3),'m/s, Obukhov稳定长度L=',round(L,3),'m,','梯度Richardson数Ri=',round(Ri2,3))
    if ssBD1==1:
        nn=nn+1
        if o2==1 or (o2==3 and o3==1):  
            print(nn,'. 在迭代求解B-D廓线时，由于求得的Ri出现了一个大于0.2的值，计算程序令Ri=0.199, 据此求得其它参数，并终止迭代。')
        if (o2==3 and o3==2) or o2==2:
            print(nn,'. 在迭代求解B-D廓线时，由于求得的Ri出现了一个大于0.2的值，计算程序令Ri=0.199, 令大气边界层阻力定律中的稳定性参数\u03BC=',round(miu2,1),', 据此求得其它参数，并终止迭代。')            

if o2==2 or (o2==3 and o3==2):
    nn=nn+1
    print(nn,'. 大气边界层阻力定律参数')    
    print('     Coriolis参数=',round(fCo,7),'rad/s')
    if dT==0:
        print('     地转风与近水面风之间的夹角\u03B8=',round(180*theta/math.pi,2),'\u00B0, 稳定性参数\u03BC=',round(miu,1),', A(\u03BC)=',round(A(miu),2),', B(\u03BC)=',round(B(miu),2))
    else:        
        print('     结合KEYPS廓线： 地转风与近水面风之间的夹角\u03B8=',round(180*theta/math.pi,2),'\u00B0, 稳定性参数\u03BC=',round(miu,1),', A(\u03BC)=',round(A(miu),2),', B(\u03BC)=',round(B(miu),2))
        print('     结合B-D廓线： \u03B8=',round(180*theta2/math.pi,2),'\u00B0, \u03BC=',round(miu2,1),', A(\u03BC)=',round(A(miu2),2),', B(\u03BC)=',round(B(miu2),2))

plt.plot([0,Uu],[10,10],color='black',linestyle='--',linewidth=0.5)
plt.scatter(Up1[10],10,c="None",marker="o",s=50,edgecolors="red",label=str(round(wdu))+'-min $U_{10}$（滨水工）')

if dT==0:
    plt.plot(Up1,zp1,label=str(round(wdu))+'-min风速对数分布律',color='black',linewidth=1)
else: 
    plt.plot(Up1,zp1,label=str(round(wdu))+'-min风速KEYPS廓线',color='red',linewidth=1)    
    plt.plot(Up2,zp2,label=str(round(wdu))+'-min风速B-D廓线',color='red',linestyle='--',linewidth=1.5)
    plt.plot(Up1n,zp1,label=str(round(wdu))+'-min风速对数分布律(按KEYPS参数)',color='grey',linewidth=1)    
    plt.plot(Up2n,zp2,label=str(round(wdu))+'-min风速对数分布律(按B-D参数)',color='black',linestyle='--',linewidth=1.5)
    plt.scatter(Up2[10],10,c="None",marker="o",s=50,edgecolors="red")
    
# 2. 港口与航道水文规范 (JTS 145-2015)
print('')
print('---港口与航道水文规范 (JTS 145-2015)---')
nn=0 # order number of notes
ss1=None

if wdu!=atm:# or atm!=10: # this part is for the windspeed routine only, and must be removed for the wind-wave routine.
    nn=nn+1 # this part is for the windspeed routine only, and must be removed for the wind-wave routine.
    print(nn,'. JTS 145-2015未提供不同时距风速之间的转换方法。U\u2081\u2080只能通过其它方法获取。')    
    ss1=1# this part is for the windspeed routine only, and must be removed for the wind-wave routine.

if dT!=0:# or atm!=10: # this part is for the windspeed routine only, and must be removed for the wind-wave routine.
    nn=nn+1 # this part is for the windspeed routine only, and must be removed for the wind-wave routine.
    print(nn,'. JTS 145-2015未提供在稳定或不稳定大气条件下推算U\u2081\u2080的方法。U\u2081\u2080只能通过其它方法获取。')    
    ss1=1# this part is for the windspeed routine only, and must be removed for the wind-wave routine.

if dT==0 and wdu==atm:
    
    if o2==3 and o3==2:
        nn=nn+1
        print(nn,'. JTS 145-2015未提供风速从陆域到水域的转换方法。U\u2081\u2080只能通过其它方法获取。') # this part is for the windspeed routine only, and must be removed for the wind-wave routine.
        ss1=1# this part is for the windspeed routine only, and must be removed for the wind-wave routine.
        
    if o2==1 or (o2==3 and o3==1):
        Ua1=U*math.log10(10/.03)/math.log10(zm/.03)
        if zm!=10:
            nn=nn+1
            print(nn,'. 按第7.1.2.2条求得',str(round(atm,1))+'-min时距的U\u2081\u2080=',round(Ua1,3),'m/s')   
            
    if o2==2:
        if o1==1:          
            Ua1=(.7-0.01*dT)*U # 邱大洪(2010)中的公式(6-11)
            nn=nn+1
            print(nn,'. 按图7.1.3估计海面风速=',round(Ua1,3),'m/s。(在此假设该图中的"海面风速"系指U\u2081\u2080。)')
        else:
            nn=nn+1
            print(nn,'. JTS 145-2015未提供可用于沿海海区、大湖、水库的有效方法。U\u2081\u2080只能通过其它方法获取。') # this part is for the windspeed routine only, and must be removed for the wind-wave routine.      
            ss1=1# this part is for the windspeed routine only, and must be removed for the wind-wave routine.
if ss1!=1:  
    plt.scatter(Ua1,10,c="None",edgecolor='purple',marker="p",s=60,label=str(round(wdu))+'-min $U_{10}$ (JTS 145-2015)')
                 
# 3. Shore Protection Manual (1984)
print('') 
print('---Shore Protection Manual (SPM 1984)---')
nn=0
                  
if o2!=2:    
    Ue2=U*(10/zm)**(1/7) # at 10 m elevation
    if zm!=10:
        nn=nn+1
        if o2==3 and o3==2:
            print(nn,'. 按公式(3-26)求得地面以上10m处的风速：',round(Ue2,3),'m/s')
        else:
            print(nn,'. 按公式(3-26)求得',str(round(atm,1))+'-min时距的U\u2081\u2080=',round(Ue2,3),'m/s')        
        if zm>=20:
            nn=nn+1
            print(nn,'. 警告：SPM 1984建议在风速高度低于20 m时使用公式(3-26)，但本例中已知风速的高度并不低于20 m。')
    if o2==1 or (o2==3 and o3==1):  
        Uel2=Ue2 #(location effect)
    if o2==3 and o3==2: #(location effect)    
        if X<16:
            Uel2=1.2*Ue2
            nn=nn+1
            print(nn,'. 按第3-IV-3-(c)条,陆-水转换系数RL=1.2,由陆上风估计的U\u2081\u2080=',round(Uel2,3),'m/s。')                      
        else:
            RL=(0.04*0.0357*Ue2**2-0.2*0.3423*Ue2+1.724)*(Ue2<=18.5)+0.9*(Ue2>18.5)
            #Uel2=Ue2*(0.04*0.0357*Ue2**2-0.2*0.3423*Ue2+1.724)*(Ue2<=18.5)+Ue2*0.9*(Ue2>18.5)
            Uel2=Ue2*RL
            nn=nn+1
            print(nn,'. 按图3-15，陆-水转换系数RL=',round(RL,2),'，对应的U\u2081\u2080=',round(Uel2,3),'(m/s)')                       
else:
    Uel2=U*0.89/U**0.192 # at 10 m elevation (by Figure 3-19)
    nn=nn+1
    print(nn,'. 按图3-19，Rg=',round(0.89/U**0.192,2),'，由Ug估计的U\u2081\u2080=',round(Uel2,3),'m/s。')

if dT==0:
    RT=1.0
else:
    RT=1-dT*(abs(dT)/1900)**(1/3)/abs(dT) # stability ((by Figure 3-14)   
Uels2=Uel2*RT    
nn=nn+1
print(nn,'. 按图3-14，RT=',round(RT,2),'，考虑大气稳定性以后的U\u2081\u2080=',round(Uels2,3),'m/s')

# Duration adjustment for required averaging time
if atm!=wdu:
    U1021h=att(Uels2,atm,60)
    U102=att(Uels2,atm,wdu)   
    nn=nn+1
    print(nn,'. 按图3-13，1-h时距的U\u2081\u2080=',round(U1021h,3),'m/s，而',str(round(wdu,1))+'-min时距的U\u2081\u2080=', round(U102,3),'m/s。')        
else:
    U102=Uels2

plt.scatter(U102,10,c="None",marker="s",s=50,edgecolors="darkblue",label=str(round(wdu))+'-min $U_{10}$ (SPM 1984)')    
Ua2=0.71*U102**1.23
    
# 4. Coastal Engineering Manual  (CEM 2015)
print('')
print('---Coastal Engineering Manual (CEM)---')
nn=0
ss3=None

nn=nn+1
print(nn,'. 对于风速计算，CEM 2015提供了一套简易方法，也建议采用ACES软件。在此仅采用其推荐的简易方法进行风速计算。')
    
if o2==2 and Rg==None:
    ss3=1
    nn=nn+1
    print(nn,'. 图II-2-13中的Rg值未提供，故无法按Rg直接估算U\u2081\u2080。')

if ss3==None:
                     
    if o2!=2:    
        Ue3=U*(10/zm)**(1/7) # at 10 m elevation
        if zm!=10:
            nn=nn+1
            if o2==3 and o3==2:
                print(nn,'. 按公式(II-2-28)求得地面以上10m处的风速：',round(Ue3,3),'m/s')
            else:
                print(nn,'. 按公式(II-2-28)求得',str(round(atm,1))+'-min时距的U\u2081\u2080=',round(Ue3,3),'m/s')        
            if zm<8 or zm>12:
                nn=nn+1
                print(nn,'. 警告：CEM 2015建议当风速高度在8~12 m之间时使用公式(II-2-28)，但本例中已知风速的高度并未在这一范围。')
        if o2==1 or (o2==3 and o3==1):  
            Uel3=Ue3 #(location effect)
        if o2==3 and o3==2: #(location effect)    
            if X<16:
                Uel3=1.2*Ue3
                nn=nn+1
                print(nn,'. 按图II-2-20，陆-水转换系数RL=1.2,由陆上风估计的U\u2081\u2080=',round(Uel3,3),'m/s。')                      
            else:
                RL=(0.04*0.0357*Ue3**2-0.2*0.3423*Ue3+1.724)*(Ue3<=18.5)+0.9*(Ue3>18.5)
                Uel3=Ue3*RL
                nn=nn+1
                print(nn,'. 按图II-2-20和图II-2-7，陆-水转换系数RL=',round(RL,2),'，对应的U\u2081\u2080=',round(Uel3,3),'(m/s)')                       
    else:
        Uel3=Rg*Ug # at 10 m elevation (by Figure II-2-13)
        nn=nn+1
        print(nn,'. 按图II-2-13，由Ug估计的U\u2081\u2080=',round(Uel3,3),'m/s。')

    if dT==0:
        RT=1.0
    if dT>0:
        RT=0.9 # stability   
    if dT<0:
        RT=1.1
        
    if o2!=2 or (o2==2 and  Rg!=None):   
        U103=Uel3*RT
        nn=nn+1
        print(nn,'. 按图II-2-20，RT=',round(RT,2),'，考虑大气稳定性以后的U\u2081\u2080=',round(U103,3),'m/s。\
(RT可按气水温差\u0394T在图II-2-8中读取，该图由ACES软件生成。然而，该图未明确说明气温的高度，且该软件中某些参数的取值有待进一步核实。故在此RT采用图II-2-20中建议的简易取值。）')
    # Duration adjustment for required averaging time
        if atm!=wdu:
            U1031h=att(U103,atm,60)
            Ua3=att(U103,atm,wdu) 
            nn=nn+1
            print(nn,'. 按图II-2-1，1-h时距的U\u2081\u2080=',round(U1031h,3),'m/s，而',str(round(wdu,1))+'-min时距的U\u2081\u2080=', round(Ua3,3),'m/s。')        
        else:
            Ua3=U103
    plt.scatter(Ua3,10,c="None",marker="v",s=50,edgecolors="limegreen",label=str(round(wdu))+'-min $U_{10}$ (CEM)')

# 5. API RP 2A-WSD
print('')
print('---API RP 2A-WSD---')
nn=0
ss6=None

if o1==2:
    ss6=1
    nn=nn+1
    print(nn,'. API RP 2A-WSD的方法仅适用于外海环境，故在此不适用。')  
else:    
    if o2==2:
        nn=nn+1
        print(nn,'. API RP 2A-WSD未提供根据地转风推算U\u2081\u2080的方法。U\u2081\u2080只能通过其它方法获取。') # this part is for the windspeed routine only, and must be removed for the wind-wave routine.
        ss6=1# this part is for the windspeed routine only, and must be removed for the wind-wave routine.

    if o2==3 and o3==2:
        nn=nn+1
        print(nn,'. API RP 2A-WSD未提供风速从陆域到水域的转换方法。U\u2081\u2080只能通过其它方法获取。') # this part is for the windspeed routine only, and must be removed for the wind-wave routine.
        ss6=1# this part is for the windspeed routine only, and must be removed for the wind-wave routine.
     
    if o2==1 or (o2==3 and o3==1):
        if dT==0:
            aU10=U # assumed U10 (m/s)
            if1=aU10*(1+0.0573*(1+0.15*aU10)**0.5*math.log(0.1*zm))*(1-0.41*0.06*(1+0.043*aU10)*math.log(atm*60/3600)/(0.1*zm)**0.22)-U # an iteration function 
            while (abs(if1)>tol):
                if1u=(aU10+dU)*(1+0.0573*(1+0.15*(aU10+dU))**0.5*math.log(0.1*zm))*(1-0.41*0.06*(1+0.043*(aU10+dU))*math.log(atm*60/3600)/(0.1*zm)**0.22)-U # updated wave length (m)
                if1l=(aU10-dU)*(1+0.0573*(1+0.15*(aU10-dU))**0.5*math.log(0.1*zm))*(1-0.41*0.06*(1+0.043*(aU10-dU))*math.log(atm*60/3600)/(0.1*zm)**0.22)-U # updated wave length (m)
                if abs(if1u-if1l)>tol:
                    aU10=aU10-2*dU*if1/(if1u-if1l)
                    if1=aU10*(1+0.0573*(1+0.15*aU10)**0.5*math.log(0.1*zm))*(1-0.41*0.06*(1+0.043*aU10)*math.log(atm*60/3600)/(0.1*zm)**0.22)-U # an iteration function 
                else:
                    if1=aU10*(1+0.0573*(1+0.15*aU10)**0.5*math.log(0.1*zm))*(1-0.41*0.06*(1+0.043*aU10)*math.log(atm*60/3600)/(0.1*zm)**0.22)-U # an iteration function 
                    if abs(if1)>tol:
                        if1=0
                        ss6=1
            if ss6==None:        
                U1061h=aU10
                Ua6=U1061h*(1+0.0573*(1+0.15*U1061h)**0.5*math.log(0.1*10))*(1-0.41*0.06*(1+0.043*U1061h)*math.log(wdu*60/3600)/(0.1*10)**0.22) # updated wave length (m)
                nn=nn+1
                print(nn,'. 根据已知风速按公式(5.3)求得一小时时距的U\u2081\u2080，再按该公式求得指定时距的U\u2081\u2080') # this part is for the windspeed routine only, and must be removed for the wind-wave routine.
                plt.scatter(Ua6,10,marker="x",s=50,color="cyan",label=str(round(wdu))+'-min $U_{10}$ (API RP 2A-WSD)')
            else:
                nn=nn+1
                print(nn,'. 公式(5.3)无解，无法求得一小时时距的U\u2081\u2080。') # this part is for the windspeed routine only, and must be removed for the wind-wave routine.
        else:
            ss6=1
            nn=nn+1
            print(nn,'. API RP 2A-WSD未提供在稳定或不稳定大气条件下推算U\u2081\u2080的方法。U\u2081\u2080只能通过其它方法获取。') # this part is for the windspeed routine only, and must be removed for the wind-wave routine.

# More outputs 
print('')
print('---结果汇总：',str(round(wdu,1))+'-min时距U\u2081\u2080(m/s)---')

if dT==1:
    print('滨水工',round(Up1[10],3))
else:
    print('滨水工',str(round(Up1[10],3))+'(KEYPS)',str(round(Up2[10],3))+'(B-D)')

if ss1==None:
    print('JTS 145-2015',round(Ua1,3))
else:
    print('JTS 145-2015','无有效方法')
 
print('SPM 1984',round(U102,3))

if ss3==None:
    print('CEM',round(Ua3,3))
else:
    print('CEM','信息不足')

if ss6==None:
    print('API RP 2A-WSD',round(Ua6,3))
else:
    print('API RP 2A-WSD','无有效方法')

print('') 
print('---结果展示结束---')

plt.xlabel('风速 (m/s)')
plt.ylabel('距水面的高度 (m)')
plt.xlim(0,Uu)
plt.ylim(0,zu)
plt.legend()
plt.rcParams['font.sans-serif'] = ['Kaiti'] 
plt.show()



