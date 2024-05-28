
from MathStatLibrary import math_N_stat as ms
import pandas as pd

class Hyp_Test_1Pop():

# Method "__init__" establishes that when the object for the class is created,
#it will require the following format: Hyp_Test_1Pop(X, Y, dt, h_o, a, pr, tt, s)
#------X: independent variable as a string
#------Y: dependent variable as a string
#------dt: data that requires the hypothesis test, and can be a list, or file if pandas is imported
#------h_o: hypothesized parameter as a floating point number
#------a: alpha or the significance level as a floating point number
#------pr: the population paramter that is being hypothesized as a string
#------tt: test type to determine hypotheses
#------s: the optional population standard deviation parameter that can be used to if sigma is known
#To clarify, the object will be structured as follows:
#class(independent, dependent, data, hypothesized parameter, significance level, parameter, test, sigma)
#________________________________________________________________________________________________________
    def __init__(self, var_X, var_Y, unit, data_Y, P_hyp, alp, 
                 para, testType = 'double-sided', P_StdDev = 0.0):
        self.var_X = str(var_X)
        self.var_Y = str(var_Y)
        self.unit = str(unit)
        self.data_Y = data_Y
        self.P_hyp = float(P_hyp)
        self.alp = float(alp)
        self.para = str(para)
        self.testType = str(testType)
        self.P_StdDev = float(P_StdDev)
        


#Method 'independentVariable' requires a print statement in the main program to output X variable
#________________________________________________________________________________________________________
    def independentVariable(self):
        return self.var_X
    


#Method 'dependentVariable' requires a print statement in the main program to output Y variable
#________________________________________________________________________________________________________
    def dependentVariable(self):
        return self.var_Y
   


#Method 'Data' requires a print statement in the main program to output the data being used
#________________________________________________________________________________________________________
    def Data(self):
        return self.data_Y
    


#Method 'hypothesisedValue' requires a print statement in the main program to output the hypothesized parameter
#________________________________________________________________________________________________________
    def hypothesisedValue(self):
        return self.P_hyp
    


#Method 'alpha' requires a print statement in the main program to output the significance level of the test
#________________________________________________________________________________________________________
    def alpha(self):
        return self.alp
    


#Method 'TestType' returns the type of test (used in 'assumptions' mainly), and requires print statement to show
#________________________________________________________________________________________________________
    def TestType(self):
        TT = ''
        inputTestType = self.testType.lower()
        TwoTail = ['double-sided', 'two-tailed', 'not equal']
        OTRight = ['right-sided', 'right-tailed', 'greater than']
        OTLeft = ['left-sided', 'left-tailed', 'less than']
        if inputTestType in TwoTail:
            TT = 'D'
        elif inputTestType in OTRight:
            TT = 'R'
        elif inputTestType in OTLeft:
            TT = 'L'
        else:
            TT = 'invalid'
        return TT
    


#Method 'populationStdDev' requires a print statement in the main program to output the population standard dev
#________________________________________________________________________________________________________
    def populationStdDev(self):
        return self.P_StdDev



#Method 'sampleSize' uses the len() python function to calculate n, or the sample size
#________________________________________________________________________________________________________
    def sampleSize(self):
        S_size = len(self.data_Y)
        return S_size
    


#Method 'sampleMean' inherits my 'Personal_Math' class to calculate the mean of the data provided
#________________________________________________________________________________________________________
    def sampleMean(self):
        S_mean = float(ms.mean(self.data_Y))
        return S_mean



#Method 'sampleStdDev' inherits my 'Personal_Math' class to calculate the standard deviation of the data
#________________________________________________________________________________________________________
    def sampleStdDev(self):
        S_StdDev = float(ms.standardDeviation(self.data_Y))
        return S_StdDev
    


#Method 'popnParameter' identifies the population parameter being tested as well as any discrepencies
#this method is later used in method 'hypotheses' to ensure the correct parameter in the hypothesis statement
#________________________________________________________________________________________________________
    def popnParameter(self):
        m = 'mean'
        p = 'proportion'
        i = 'invalid population parameter'
        identify_m = ['mean', 'mu', 'average']
        identify_p = ['rho', 'p', 'proportion', 'one-proportion']
        inputParameter = self.para.lower()
        if inputParameter in identify_m:
            self.para = m
        elif inputParameter in identify_p:
            self.para = p
        else:
            self.para = i
        return self.para



    def assumptions(self):
        _sign_ = ''
        Y = self.var_Y
        X = self.var_X
        u = self.unit
        h_0 = self.P_hyp
        alpha = self.alp
        variant = self.popnParameter()
        TT = self.TestType()
        popSTDdev = self.populationStdDev()
        if TT == 'D':
            _sign_ = 'not equal to'
        elif TT == 'R':
            _sign_ = 'greater than'
        elif TT == 'L':
            _sign_ = 'less than'
        else:
            sign = '_invalid_'

        words = '\nAssuming the '
        norm =  f"probabilty distribution of {Y} is approximately normal, "
        rand = f"and the sample of {X} is selected at random, \n"
        conduct = f"we can conduct a hypothesis test at \u03B1 = {alpha} "
        toDo = f"to determine if the actual {variant} of {Y} is {_sign_} {h_0} {u}.\n"
        if popSTDdev == 0:
            STDdev = 'Since the population standard deviation is unknown, we will use a t-statistic.\n'
        else:
            STDdev = f"We know that the population standard deviation is {popSTDdev}, so we will use a z-score.\n"

        print(words + norm + rand + conduct + toDo + STDdev)



       


#Method 'hypothesis' is for producing a null and alternative hypothesis
#taking the focus population parameter and hypothesized parameter under consideration
#We have first declared all the variables that will be used.
#The lists 'TwoTail', 'OTRight', 'OTLeft', are used for possible test type inputs
#Three main conditionsconsidered when constructing the hypothesis statements here are:
#------The definded population parameter being 'mean'
#------The definded population parameter being 'proportion'
#------The definded population parameter being 'invalid'
#The alternative is defined separaretly for each sub condition intentionally
#________________________________________________________________________________________________________
    def hypotheses(self):
        #Initializing the null and alternative hypothesis as local variables_______________#
        nullHyp = ''
        altHyp = ''
        
        #Using outside functions to define crucial variables______________________________#
        inputTestType = self.TestType()
        variant = self.popnParameter()
        u = self.unit

        #Defining statements stored are variables for simplicity__________________________#
        h_0 = str(self.P_hyp)
        a_null = f"population {variant} is equal to {h_0} {u}"
        a_alt = f"population {variant} is not equal to {h_0} {u}"
        b_null = f"population {variant} is less than or equal to {h_0} {u}"
        b_alt = f"population {variant} is greater than {h_0} {u}"
        c_null = f"population {variant} is greater than or equal to {h_0} {u}"
        c_alt = f"population {variant} is less than {h_0} {u}"
        f = 'failed to identify test'
        i = 'invalid population parameter'

        #Dertermining if parameter is 'mean' or 'proportion'_______________________________#
        if variant == 'mean':
            if inputTestType == 'D':
                nullHyp = a_null
                altHyp = a_alt
            elif inputTestType == 'R':
                nullHyp = b_null
                altHyp = b_alt
            elif inputTestType == 'L':
                nullHyp = c_null
                altHyp = c_alt
            else:
                nullHyp = f
                altHyp = f
        elif variant == 'proportion':
            if inputTestType == 'D':
                nullHyp = a_null
                altHyp = a_alt
            elif inputTestType == 'R':
                nullHyp = b_null
                altHyp = b_alt
            elif inputTestType == 'L':
                nullHyp = c_null
                altHyp = c_alt
            else:
                nullHyp = f
                altHyp = f
        else:
            nullHyp = i
            altHyp = i

        #Printing Hypothesis Statements___________________________________________________#
        print("Hypotheses:")
        if nullHyp == altHyp == f:
            print("please identify 'Test-type': "
                  "double-sided, right-tailed, or left-tailed")
        elif nullHyp == altHyp == i:
            print(i + ": 'mean' or 'proportion' needs to be specified")
        else:
            statement_hyp = 'H\u2092: ' + nullHyp
            statement_alt = 'H\u2090: ' + altHyp
            print(statement_hyp)
            print(statement_alt + "\n")



    def t_c(self):
        S_mean = self.sampleMean()
        P_hyp = self.hypothesisedValue()
        S_StdDev = self.sampleStdDev()
        S_size = self.sampleSize()
        t = ((S_mean - P_hyp) / 
             (S_StdDev / ms.sqRT(S_size)))
        d_f_ = S_size - 1
        print("t statistic = ", t)
        print(f"degrees of freedom = {d_f_}")



#Method 'z_c' calculates the Z-score using functions in this class
#________________________________________________________________________________________________________
    def z_c(self):
        S_mean = self.sampleMean()
        hyp_prm = self.hypothesisedValue()
        P_StdDev = self.populationStdDev()
        S_size = self.sampleSize()
        # unbiased preditor of population std dev is sigma_xBar
        sigma_xBar = (P_StdDev / 
                      ms.sqRT(S_size))
        if sigma_xBar == 0:
            print("Population standard deviation needs to be known " 
                  "and defined to calculate Z score")
        else:
            z = (S_mean - hyp_prm) / sigma_xBar
            print("Z score = ", z)

    def desition(self):
        alp = self.alpha





    def runStatInference(self):
        self.assumptions()
        self.hypotheses()
        popSTDdev = self.populationStdDev()
        
        if popSTDdev == 0:
            self.t_c()
        else:
            self.z_c()




        
        
        
       
        




#if: Ppopulation standard deviation is 0, then we will be using t_c
#else: we wil be using z_c