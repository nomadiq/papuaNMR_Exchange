import csv as csv
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import math
from scipy.optimize import leastsq
import numpy as np
from matplotlib import rc
rc('text', usetex=True)
import papuaEx as ex 
import argparse

### Get the arguments

def getArgs():
    parser = argparse.ArgumentParser(description='Perform Nz/ZZ exchange fitting of data')
    parser.add_argument('-data', '--data_file', help='Input Data File. CSV format with proper headings')
    parser.add_argument('-plot', '--plot_output', help='Make PDF files of the fits. Answer Y/N')
    parser.add_argument('-mc', '--monte_carlo', help='Number of Monte Carlo Simulations (Requires Noise figure in Data file). 0 Means dont do Monte Carlo Simulations')
    args = vars(parser.parse_args())

    return args

args = getArgs()

do_plot = 0
if args['plot_output'] == '1' or args['plot_output'] == 'Y' or args['plot_output'] == 'y' or args['plot_output'] == 'yes' or args['plot_output'] == 'Yes' or args['plot_output'] == 'YES':
    do_plot = 1

mcSims = int(args['monte_carlo'])


dataframe = pd.read_csv(args['data_file'])

if mcSims == 0:
    datafit = ex.fit(dataframe, figure=do_plot)
    print(datafit)

if mcSims > 0:
    mcdatafit = ex.mcfit(dataframe, mcSims, figure=do_plot)
    print(mcdatafit)



