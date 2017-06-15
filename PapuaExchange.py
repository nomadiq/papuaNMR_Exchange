import math
import argparse

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy.optimize import leastsq
import pandas as pd

import papuaEx as ex 


### Get the arguments

def getArgs():
    parser = argparse.ArgumentParser(description='Perform Nz/ZZ exchange fitting of data')
    parser.add_argument('-data', '--data_file', required=True, help='Input Data File. CSV format with proper headings')
    parser.add_argument('-plot', '--plot_output', default=0, help='Make PDF files of the fits. Answer Y/N')
    parser.add_argument('-mc', '--monte_carlo', default=0, help='Number of Monte Carlo Simulations (Requires Noise figure in Data file). 0 Means dont do Monte Carlo Simulations')
    parser.add_argument('-pdf', '--pdf_plot', default='', help='Give a file name and a pdf file will be saved with that name')
    args = vars(parser.parse_args())

    return args

args = getArgs()

do_plot = 0
if args['plot_output'] == '1' or args['plot_output'] == 'Y' or args['plot_output'] == 'y' or args['plot_output'] == 'yes' or args['plot_output'] == 'Yes' or args['plot_output'] == 'YES':
    do_plot = 1

mcSims = int(args['monte_carlo'])


dataframe = pd.read_csv(args['data_file'])

if mcSims == 0:
    datafit = ex.fit(dataframe, figure=do_plot, pdf=str(args['pdf_plot']))
    #print(datafit)
    print('IAA0: ' + str("{0:.4f}".format(datafit[4])))
    print('IBB0: ' + str("{0:.4f}".format(datafit[5])))
    print('R1A: ' + str("{0:.4f}".format(datafit[0])))
    print('R1B: ' + str("{0:.4f}".format(datafit[1])))
    print('k_ab: ' + str("{0:.4f}".format(datafit[2])))
    print('k_ba: ' + str("{0:.4f}".format(datafit[3])))


if mcSims > 0:
    mcdatafit = ex.mcfit(dataframe, mcSims, figure=do_plot, pdf=args['pdf_plot'])
    #print(mcdatafit)
    print('IAA0: ' + str("{0:.4f}".format(mcdatafit[0][4])) + ' +/- ' + str("{0:.4f}".format(mcdatafit[1][4])))
    print('IBB0: ' + str("{0:.4f}".format(mcdatafit[0][5])) + ' +/- ' + str("{0:.4f}".format(mcdatafit[1][5])))
    print('R1A: ' + str("{0:.4f}".format(mcdatafit[0][0])) + ' +/- ' + str("{0:.4f}".format(mcdatafit[1][0])))
    print('R1B: ' + str("{0:.4f}".format(mcdatafit[0][1])) + ' +/- ' + str("{0:.4f}".format(mcdatafit[1][1])))
    print('k_ab: ' + str("{0:.4f}".format(mcdatafit[0][2])) + ' +/- ' + str("{0:.4f}".format(mcdatafit[1][2])))
    print('k_ba: ' + str("{0:.4f}".format(mcdatafit[0][3])) + ' +/- ' + str("{0:.4f}".format(mcdatafit[1][3])))



