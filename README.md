# Statistical-Inference <sup> $\gamma$.
This personal project aims to delve into fundamental statistical inference techniques, enabling users to draw meaningful conclusions from datasets. At the time of this state of development, the repository houses code dedicated to single population hypothesis testing. However, this is just the beginning.

# Purpose
A p-value is just a number if you don't know what to do with it. For instance, what does a person not versed in statistics do when they see "p-value = 0.04" on a matrix of statistical numbers? There are several software programs, like MiniTab, R, and SAS, that help in inferential statistics by providing numerical values that we use to draw conclusions. This project does somewhat the same, but instead of just the numbers, you will be given an understanding of what those numbers mean. In other words, the interpretation will be done for you.

There may be other programs that provide similar or even better solutions to the focus of this project. However, this is my personal project that I plan to further develop by automating and evolving it with the use of machine learning, deep learning, neural networks, natural language processing, and other artificial intelligence concepts. At the moment, I am restricted by my knowledge, but this will soon no longer be a limitation once I expand my intellectual horizons. For now, this is my take on a program that makes statistical inferences for you.

# From Creator to Respected Viewer
I appreciate your time and interest in my work. If you have any question or suggestions, or would like to connect with me, you may email me at **adi.paricharak@gmail.com**. My **LinkedIn** page can be accessed [here](www.linkedin.com/in/aditya-paricharak-2003asp).

Please note that this project is a work in progress and is being worked on as you read this. You may not be seeing the most recent python file when navigating through this repository. I will make updates as I progress. Thank you!

# About The Code

This project has used the language python, and consists of one class so far. The class **Hyp_Test_1Pop**, conducts hypothesis tests for single-populations.

## __Hyp_Test_1Pop Attributes__
Object uses the inputs: **var_X, var_Y, unit, data_Y, P_hyp, alp, para, testType,** and **P_StdDev**.

`var_X`: the independent variable of the test.

`var_Y`: the dependent variable of the test.

`unit`: this is unit being used in for the data.

`data_Y`: these are the data values, which can be in the form of a list or can be read from a file using the **pandas** library.

`P_hyp`: this is the hypothesized value of the parameter which is usually decided prior to the test.

`alp`: this is the significance level, also known as $\alpha$, which is the probability of rejecting the null hypothesis, $H_{o}$.

`para`: this is the parameter being tested, i.e. mean or proportion.

`testType`: this is the type of test being performed, i.e. double-sided, right-sided, or left sided.

`P_StdDev`: this is an optional attribute which used when the population standard deviation is known.

#### Examples for Objects of Hyp_Test_1Pop: 
- `exampleVariable1 = Hyp_Test_1Pop('X', 'Y', 'kilos', list, 20, 0.05, 'proportion', 'double-sided')`
- `exampleVariable2 = Hyp_Test_1Pop('age', 'gained weight', 'grams', data_list, 80, 0.01, 'mean', 'left-sided', 5.4)`



