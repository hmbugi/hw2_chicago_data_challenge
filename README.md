# hw2_chicago_data_challenge
Repository for a data challenge assignment  


Project Name: INCOME AND HARDSHIP RELATION TO BIRTH AND DEATH   
Github repository: hw2_chicago_data_challenge   
Language used: Python  
Author: Harrison Mbugi  
Date: June 2015  

PROJECT FOCUS  
To find if there is any relationship between per capital income and birth rate/average annual deaths in Chicago  
To find if there is any relationship between life hardship and birth rate/average annual deaths in Chicago  

DATASET INVOLVED  
Census Data - Selected socioeconomic indicators in Chicago, 2008 – 2012  
Public Health Statistics- Selected public health indicators by Chicago community area  
Public Health Statistics- Selected underlying causes of death in Chicago, 2006 – 2010  
It has to be noted that all the above datasets where taken from City of Chicago data portal   

Interesting data from the above datasets  
This project deals with the following data to establish conclusion on this problem:  
1.  Per capital income of every community area in Chicago  
2.  Hardship index of every community area in Chicago  
3.  Birth rates of every community area in Chicago  
4.  Average annual number of deaths of every community area in Chicago  

PROCEDURE TAKEN TO ESTABLISH CONCLUSION  
A python program was created to manipulate all the data needed for this problem and display the results. This program was also tested. The python program, all the needed datasets and the tester program were uploaded to the github repository hw2_chicago_data_challenge which has 5 files(excluding the README.md) used to come up wit the result of the relationships.  
Two files are explained in details below. the remaining three files are holding the datasets in csv format  

data_challenge.py  
This is the python program written to manipualate the datasets and come up with the relatiohship among them.  
1. Functions fileexists and isreadable makes sure that the csv files to be parsed exist and are readable  
2. datasets were parsed to lists using functions socialparser, birthparser and deathparser.  
3. Functions incomebirth, incomedeath, harshipbirth and hardshipdeath prepare data needed for the correlation process.  
4. the correlation is found withing function correlation which returns the correlation coeefficient  
 
test.py  
This is a tester program which does unit testing for the python program data_challenge.py . It tests all the methods. It has five functions to accomplish its work.  
1. test_fileexists - tests function fileexist  
2. test_isreadable - tests function isreadable  
3. test_parserreturn - tests functions socioparser, birthparser and deathparser  
4. test_rightrow - tests functions incomebirth, incomedeath, hardshipbirth and hardshipdeath  
5. test_correlation - tests the function correlation  
All the functions tested are those in the program data_challenge.py  

RESULT  
The findings come as a program output after running the program data_challenge.py .  
A positive correlation coefficient means that the two data are direct proposional and more the value is close to 1 the strongest their relationship.  
A negative correlation coefficient means that the two data are inversely proposional and the more their value is close to -1 the strongest that relationship gets.  
If correlation coefficient is zero or almost negligible that means there is no relationship between the two data.
