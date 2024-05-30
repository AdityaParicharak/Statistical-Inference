from Stat_Method import Hyp_Test_1Pop as parentCode

import pandas as pd


testList = [1.6, 1.8, 7.3, 5.7, 3.0, 1.6, 3.8, 3.1, 7.8, 7.4, 4.2, 1.6, 2.1, 2.1, 5.5, 4.4]

A = parentCode("patients", "vaccine dosage", "mls", testList, 3, 0.5, 'mu', 'left-sided', 5)

#A.hypotheses()
#A.assumptions()
#print(A.sampleSize()) 
#print(A.sampleMean())
#print(A.sampleStdDev())
#A.t_c()
A.runAnalysis()
A.TestStatistic()

