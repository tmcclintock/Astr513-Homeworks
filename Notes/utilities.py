import numpy as np
import matplotlib.pyplot as plt
import corner

"""
Given two flat distributions in x1 and x2,
return two distributions z1 and z2 that are Gaussian
distributed.
"""
def boxmuller(x1,x2):
    z1 = np.sqrt(-2*np.log(x1))*np.cos(2*np.pi*x2)
    z2 = np.sqrt(-2*np.log(x1))*np.sin(2*np.pi*x2)
    return z1,z2

"""
This 
"""
def get_fake_gaussian_data(N):
    x1,x2 = np.random.rand(N),np.random.rand(N)
    return boxmuller(x1,x2)

"""
Given a histogram P with bin centers y,
find the levels of P (Pjs) that contain some fraction of the total
probability under them (Cjs). Then, find the values of P and y (P0 , y0)
that contain C0 amount of probability within them.
"""
def conf_intervals(y,P,C0=0.683,k=1000):
    #Step 1 find where the maximum value is
    i_Pmax = np.argmax(P)
    Pmax, y_Pmax, M  = P[i_Pmax],y[i_Pmax], len(y)
    dy = (np.max(y)-np.min(y))/(M-1)
    
    #Step 2 grid P with K Points, j = 1...k
    #Step 3 find C_j, the integral over P(y)H[P(y)-Pj], i.e. the fraction
    #in the grid of P
    Pjs = []
    Cjs = []
    for j in range(1,k+1):
        Pj = (j-1.0)/(k-1.0)*Pmax
        Pjs.append(Pj)
        Cj = 0
        for i in range(2,M):
            if P[i] > Pj:
                Cj+=dy*P[i]
            else:
                Cj+=0
        Cjs.append(Cj)

    #Step 4 scan through the Cjs and find j
    j = 0
    for i in range(len(Cjs)-1):
        if Cjs[i+1] < C0:
            j = i
            break
    
    #Step 5 interpolate for P at that point
    P0 = (Pjs[j+1]-Pjs[j])/(Cjs[j+1]-Cjs[j]) * (C0 - Cjs[j]) + Pjs[j]
    
    #Step 6 interpolate again to find i_left, i_right and y0_left and y0_right
    i_left,iIright = 0,0
    for l in range(len(P)-1):
        if P[l+1] > P0 > P[l]:# or P[l+1] <= P0 < P[l]:
            i_left = l
            break
    for l in range(np.argmax(P),len(P)-1):
        if P[l+1] <= P0 < P[l]:
            i_right = l
            break
    y_left = (y[i_left+1]-y[i_left])/(P[i_left+1]-P[i_left])*(P0-P[i_left]) + y[i_left]
    y_right = (y[i_right+1]-y[i_right])/(P[i_right+1]-P[i_right])*(P0-P[i_right]) + y[i_right]

    """
    We return the confidence interval edges in yleft,yright. The height of 
    the histogram at that location, P0, and the two arrays that contain Cjs and Pjs.
    """
    return (y_left,y_right,P0,np.array(Cjs),np.array(Pjs))


"""
Given a 2D histogram P with bins centered on (a,b),
find the levels of P (Pjs) that contain some fraction of the total
probability under them (Cjs). Then, find the values of P and (a,b) (P0 , (a0,b0))
that contain C0 amount of probability within them.
IN PROGRESS!!!!! - Tom 3/21/2016
"""
def conf_intervals_2D(y,P,C0=0.683,k=1000):
    #Step 1 find where the maximum value is
    i_Pmax = np.argmax(P)
    Pmax, y_Pmax, M  = P[i_Pmax],y[i_Pmax], len(y)
    dy = (np.max(y)-np.min(y))/(M-1)
    
    #Step 2 grid P with K Points, j = 1...k
    #Step 3 find C_j, the integral over P(y)H[P(y)-Pj], i.e. the fraction
    #in the grid of P
    Pjs = []
    Cjs = []
    for j in range(1,k+1):
        Pj = (j-1.0)/(k-1.0)*Pmax
        Pjs.append(Pj)
        Cj = 0
        for i in range(2,M):
            if P[i] > Pj:
                Cj+=dy*P[i]
            else:
                Cj+=0
        Cjs.append(Cj)

    #Step 4 scan through the Cjs and find j
    j = 0
    for i in range(len(Cjs)-1):
        if Cjs[i+1] < C0:
            j = i
            break
    
    #Step 5 interpolate for P at that point
    P0 = (Pjs[j+1]-Pjs[j])/(Cjs[j+1]-Cjs[j]) * (C0 - Cjs[j]) + Pjs[j]
    
    #Step 6 interpolate again to find i_left, i_right and y0_left and y0_right
    i_left,iIright = 0,0
    for l in range(len(P)-1):
        if P[l+1] > P0 > P[l]:# or P[l+1] <= P0 < P[l]:
            i_left = l
            break
    for l in range(np.argmax(P),len(P)-1):
        if P[l+1] <= P0 < P[l]:
            i_right = l
            break
    y_left = (y[i_left+1]-y[i_left])/(P[i_left+1]-P[i_left])*(P0-P[i_left]) + y[i_left]
    y_right = (y[i_right+1]-y[i_right])/(P[i_right+1]-P[i_right])*(P0-P[i_right]) + y[i_right]

    """
    We return the confidence interval edges in yleft,yright. The height of 
    the histogram at that location, P0, and the two arrays that contain Cjs and Pjs.
    """
    return (y_left,y_right,P0,np.array(Cjs),np.array(Pjs))
