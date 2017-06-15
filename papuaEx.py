import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy.optimize import leastsq
import numpy as np



# define the functions for equation expressions
def a11(p):
    return p[0] + p[2]
def a12(p):
    return -1*p[3]
def a21(p):
    return -1*p[2]
def a22(p):
    return p[1] + p[3]

def lambdaneg(p):
    return (1.0/2.0)*((a11(p) + a22(p)) - np.sqrt(((a11(p) - a22(p))**2.0 + 4.0*p[2]*p[3])))
def lambdapos(p):
    return (1.0/2.0)*((a11(p) + a22(p)) + np.sqrt(((a11(p) - a22(p))**2.0 + 4.0*p[2]*p[3])))

def Iaa(p,t):
    return p[4]*(-1*(lambdaneg(p) - a22(p)) * np.exp(-1*lambdapos(p)*t) + (lambdapos(p) - a22(p))*np.exp(-1*lambdaneg(p)*t))/(lambdapos(p) - lambdaneg(p))
def Ibb(p,t):
    return p[5]*(-1*(lambdaneg(p) - a11(p)) * np.exp(-1*lambdapos(p)*t) + (lambdapos(p) - a11(p))*np.exp(-1*lambdaneg(p)*t))/(lambdapos(p) - lambdaneg(p))
def Iab(p,t):
    return p[4]*(a12(p)*np.exp(-1*lambdapos(p) * t) - a12(p)*np.exp(-1*lambdaneg(p)*t))/(lambdapos(p) - lambdaneg(p))
def Iba(p,t):
    return p[5]*(a21(p)*np.exp(-1*lambdapos(p) * t) - a21(p)*np.exp(-1*lambdaneg(p)*t))/(lambdapos(p) - lambdaneg(p))

def fnMin(p,t,IAA,IBB,IAB,IBA):
    diffIAA = IAA-Iaa(p,t)
    diffIBB = IBB-Ibb(p,t)
    diffIAB = IAB-Iab(p,t)
    diffIBA = IBA-Iba(p,t)
    return np.concatenate((diffIAA, diffIBB, diffIAB, diffIBA))

def fit(data, figure=0, pdf=''):
    
    t = data['t'].values.astype(float)

    IAA = data['IAA'].values.astype(float)
    IBB = data['IBB'].values.astype(float)
    IAB = data['IAB'].values.astype(float)
    IBA = data['IBA'].values.astype(float)
    
    maxIAA = IAA.max()
    maxIBB = IBB.max()
    par_init = np.array([5.0,5.0,10.0,10.0,maxIAA*1.5,maxIBB*1.5]).astype(float)

    best, cov, info, message, ier = leastsq(fnMin,
                                        par_init, args=(t, IAA,IBB,IAB,IBA),
                                        full_output=True)
    
    
    
    if figure==1:
        plt.figure(figsize=(5,5))
        ax = plt.subplot(1, 1, 1)
        plt.scatter(data['t'],data['IAA'])
        plt.scatter(data['t'],data['IBB'])
        plt.scatter(data['t'],data['IAB'])
        plt.scatter(data['t'],data['IBA'])
        
        times = np.arange(0, t.max()*1.0, 0.0001)
        plt.plot(times, Iaa(best,times))
        plt.plot(times, Ibb(best,times))
        plt.plot(times, Iab(best,times))
        plt.plot(times, Iba(best,times))
        

        plt.text(0.8, 0.7, 
                 r'$k_{ab}$ = ' + "{0:.4f}".format(best[2]) + '\n' + 
                 r'$k_{ba}$ = ' + "{0:.4f}".format(best[3]) + '\n' + 
                 r'$R1_{a}$ = ' + "{0:.4f}".format(best[0]) + '\n' + 
                 r'$R1_{b}$ = ' + "{0:.4f}".format(best[1]) + '\n' + 
                 r'$IA_{0}$ = ' + "{0:.0f}".format(best[4]) + '\n' + 
                 r'$IB_{0}$ = ' + "{0:.0f}".format(best[5]),
                 ha='center', va='center', transform=ax.transAxes)
        
        if pdf != '':
            plt.savefig(pdf, format='pdf')

        plt.show()
        #print('A0 (Arbitary intenisty): ' + str(best[4]))
        #print('B0 (Arbitary intenisty): ' + str(best[5]))
        #print('R1A (sec):               ' + str(best[0]))
        #print('R1B (sec):               ' + str(best[1]))
        #print('kab (sec^-1):            ' + str(best[2]))
        #print('kba (sec^-1):            ' + str(best[3]))
        return best

    if figure==0:
        return best


def plotfit(datasets, datasetNames=''):
    numSets = len(datasets)
    i = 1
    numCols = 3
    numRows = math.ceil(numSets/numCols)+1
    
    plt.figure(figsize=(20,20))
    
    for set in datasets:
        setFit = fit(set, figure=0)
        ax = plt.subplot(numRows, numCols, i)
        plt.scatter(set['t'],set['IAA'])
        plt.scatter(set['t'],set['IBB'])
        plt.scatter(set['t'],set['IAB'])
        plt.scatter(set['t'],set['IBA'])
        
        times = np.arange(0, t.max()*1.2, 0.0001)
        plt.plot(times, Iaa(setFit,times))
        plt.plot(times, Ibb(setFit,times))
        plt.plot(times, Iab(setFit,times))
        plt.plot(times, Iba(setFit,times))
        
        plt.text(0.6, 0.7, 
                 r'$\underline{'+datasetNames[i-1]+'}$:' + '\n' +
                 r'$k_{ab}$ = ' + "{0:.4f}".format(setFit[2]) + '\n' + 
                 r'$k_{ba}$ = ' + "{0:.4f}".format(setFit[3]) + '\n' + 
                 r'$R1_{a}$ = ' + "{0:.4f}".format(setFit[0]) + '\n' + 
                 r'$R1_{b}$ = ' + "{0:.4f}".format(setFit[1]) + '\n' + 
                 r'$IA_{0}$ = ' + "{0:.0f}".format(setFit[4]) + '\n' + 
                 r'$IB_{0}$ = ' + "{0:.0f}".format(setFit[5]),
                 ha='center', va='center', transform=ax.transAxes)
        
        
        i +=1
       
    plt.show()
        


def mcfit(data, numSims, figure=0, pdf=''):
    
    t = data['t'].values.astype(float)
    IAA = data['IAA'].values.astype(float)
    IBB = data['IBB'].values.astype(float)
    IAB = data['IAB'].values.astype(float)
    IBA = data['IBA'].values.astype(float)
    IAAn = data['IAAn'].values.astype(float)
    IBBn = data['IBBn'].values.astype(float)
    IABn = data['IABn'].values.astype(float)
    IBAn = data['IBAn'].values.astype(float)
    
    #best = np.zeros(numSims)
    results = np.zeros([numSims, 6])
    
    # do a noiseless fit
    par_init = fit(data, figure=0)
    
    for i in range(numSims):
        
        IAA = data['IAA'].values.astype(float)
        IBB = data['IBB'].values.astype(float)
        IAB = data['IAB'].values.astype(float)
        IBA = data['IBA'].values.astype(float)
        #IAAn = data['IAAn'].values.astype(float)
        #IBBn = data['IBBn'].values.astype(float)
        #IABn = data['IABn'].values.astype(float)
        #IBAn = data['IBAn'].values.astype(float)
        
        IAA = np.random.normal(IAA, IAAn)
        IBB = np.random.normal(IBB, IBBn)
        IAB = np.random.normal(IAB, IABn)
        IBA = np.random.normal(IBA, IBAn)
        
        
        maxIAA = IAA.max()
        maxIBB = IBB.max()
        #par_init = np.array([5.0,5.0,10.0,10.0,maxIAA*1.5,maxIBB*1.5]).astype(float)

        best, cov, info, message, ier = leastsq(fnMin,
                                        par_init, args=(t, IAA,IBB,IAB,IBA),
                                        full_output=True)
        results[i] = best
    
    
    #print best
    #best = np.mean(best)
    
    
    
    mean = np.mean(results, axis=0)
    std = np.std(results, axis=0)
    
    #print best
    #print best_std
    
    if figure==1:
        plt.figure(figsize=(5,5))
        ax = plt.subplot(1, 1, 1)
        plt.scatter(data['t'],data['IAA'])
        plt.scatter(data['t'],data['IBB'])
        plt.scatter(data['t'],data['IAB'])
        plt.scatter(data['t'],data['IBA'])
        
        times = np.arange(0, t.max()*1.0, 0.0001)
        plt.plot(times, Iaa(mean,times))
        plt.plot(times, Ibb(mean,times))
        plt.plot(times, Iab(mean,times))
        plt.plot(times, Iba(mean,times))
        

        plt.text(0.6, 0.7, 
                r'$k_{ab}$ = ' + "{0:.4f}".format(mean[2]) + ' +/- ' + "{0:.4f}".format(std[2]) + '\n' + 
                r'$k_{ba}$ = ' + "{0:.4f}".format(mean[3]) + ' +/- ' + "{0:.4f}".format(std[3]) + '\n' + 
                r'$R1_{a}$ = ' + "{0:.4f}".format(mean[0]) + ' +/- ' + "{0:.4f}".format(std[0]) + '\n' + 
                r'$R1_{b}$ = ' + "{0:.4f}".format(mean[1]) + ' +/- ' + "{0:.4f}".format(std[1]) + '\n' + 
                r'$IA_{0}$ = ' + "{0:.0f}".format(mean[4]) + ' +/- ' + "{0:.4f}".format(std[4]) +'\n' + 
                r'$IB_{0}$ = ' + "{0:.0f}".format(mean[5]) + ' +/- ' + "{0:.4f}".format(std[5]),
                ha='center', va='center', transform=ax.transAxes)
        
        
        if pdf != '':
            plt.savefig(pdf+".pdf", format='pdf') 
        
        plt.show()
        return mean, std

    if figure==0:
        return mean, std
        
    
     