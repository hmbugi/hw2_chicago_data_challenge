"""Created by Harrison Mbugi"""

from csv import *
import os

def fileexist(filename):
    ''' Return true if the file exists '''
    return os.path.isfile(filename)

def isreadable(filename):
    ''' Return true if the file is readable '''
    return os.access(filename, os.R_OK)

def socioparser():
    ''' Fetching community area number & name,
per capita income and hardship index into a list
and return a list containing these values from the csv file '''
    soc_list = [] 
    soc_obj = open("socio_eco_ind.csv")
    soc_reader = reader(soc_obj)
    for row in soc_reader:
        soc_list.append([row[0], row[1], row[7], row[8]])
    soc_obj.close()
    return soc_list
        
def birthparser():
    ''' Fetching community area number and birth rate into a list
and return a list containing these values from the csv file '''
    bir_list = [] 
    bir_obj = open("health_ind.csv")
    bir_reader = reader(bir_obj)
    for row in bir_reader:
        bir_list.append([row[0], row[2]])
    bir_obj.close()
    return bir_list

def deathparser():
    ''' Fetching community area number and average annual deaths into a list
and return a list containing these values from the csv file '''
    dea_list = [] 
    dea_obj = open("death_causes.csv")
    dea_reader = reader(dea_obj)
    for row in dea_reader:
        dea_list.append([row[1], row[5], row[4]])
    dea_obj.close()
    return dea_list

def incomebirth():
    '''Manipulates return values of socioparser() and birthparser()
and return a list containing values needed for calculating the coefficient of
income-birth correlation'''
    incomebirth, x, y, xy, x2, y2 = ([] for i in range(6)) #same as [[]]*6 . Both initialize empty lists to variables
    for n in range (1,78): #range start from index 1 avoiding headings and end at index 77
        x.append(int(socioparser()[n][2])) #it is index n-1 because n starts from 1 not 0.
        y.append(float(birthparser()[n][1]))
        xy.append(x[n-1]*y[n-1])
        x2.append(x[n-1]**2) #equivalent to pow(x[n-1],2)
        y2.append(y[n-1]**2)
        incomebirth.append([x[n-1], y[n-1], xy[n-1], x2[n-1], y2[n-1]]) 
    return incomebirth

def incomedeath():
    '''Manipulates return values of socioparser() and deathparser()
and return a list containing values needed for calculating the coefficient of
income-death correlation'''
    incomedeath, x, y, xy, x2, y2 = ([] for i in range(6)) #same as [[]]*6 . Both initialize empty lists to variables
    for n in range (1,78): #range start from index 1 avoiding headings and end at index 77
        x.append(int(socioparser()[n][2])) #it is index n-1 because n starts from 1 not 0.
        y.append(int(deathparser()[n][1]))
        xy.append(x[n-1]*y[n-1])
        x2.append(x[n-1]**2) #equivalent to pow(x[n-1],2)
        y2.append(y[n-1]**2)
        incomedeath.append([x[n-1], y[n-1], xy[n-1], x2[n-1], y2[n-1]])
    return incomedeath

def hardshipbirth():
    '''Manipulates return values of socioparser() and birthparser()
and return a list containing values needed for calculating the coefficient of
hardship-birth correlation'''
    hardshipbirth, x, y, xy, x2, y2 = ([] for i in range(6)) #same as [[]]*6 . Both initialize empty lists to variables
    for n in range (1,78): #range start from index 1 avoiding headings and end at index 77
        x.append(int(socioparser()[n][3])) #it is index n-1 because n starts from 1 not 0.
        y.append(float(birthparser()[n][1]))
        xy.append(x[n-1]*y[n-1])
        x2.append(x[n-1]**2) #equivalent to pow(x[n-1],2)
        y2.append(y[n-1]**2)
        hardshipbirth.append([x[n-1], y[n-1], xy[n-1], x2[n-1], y2[n-1]]) 
    return hardshipbirth

def hardshipdeath():
    '''Manipulates return values of socioparser() and deathparser()
and return a list containing values needed for calculating the coefficient of
hardship-death correlation'''
    hardshipdeath, x, y, xy, x2, y2 = ([] for i in range(6)) #same as [[]]*6 . Both initialize empty lists to variables
    for n in range (1,78): #range start from index 1 avoiding headings and end at index 77
        x.append(int(socioparser()[n][3])) #it is index n-1 because n starts from 1 not 0.
        y.append(int(deathparser()[n][1]))
        xy.append(x[n-1]*y[n-1])
        x2.append(x[n-1]**2) #equivalent to pow(x[n-1],2)
        y2.append(y[n-1]**2)
        hardshipdeath.append([x[n-1], y[n-1], xy[n-1], x2[n-1], y2[n-1]])
    return hardshipdeath

def correlation(clist):
    '''Calculate correlation value and return it'''
    sx, sy, sxy, sx2, sy2 = [0]*5 #initializing variables
    n = len(clist)
    for row in clist:
        sx = sx + row[0]
        sy = sy + row[1]
        sxy = sxy + row[2]
        sx2 = sx2 + row[3]
        sy2 = sy2 + row[4]
    r = ((n*sxy)-(sx*sy))/pow(((n*sx2)-pow(sx,2))*((n*sy2)-pow(sy,2)),0.5)
    return round(r,2)

def rstrength(r):
    if  .75 <= r <= 1.0:
        return "very strong positive relationship"
    elif .5 <= r < .75:
        return "strong positive relationship"
    elif .25 <= r < .5:
        return "moderate positive relationship"
    elif 0.0 < r < .25:
        return "weak positive relationship"
    elif 0.0:
        return "there is no relationship"
    elif -.25 < r < 0.0:
        return "weak negative relationship"
    elif -.5 < r <= -.25:
        return "moderate negative relationship"
    elif -.75 < r <= -.5:
        return "strong negative relationship"
    elif -1.0 <= r <= -.75:
        return "very strong negative relationship"

def main():
    status = "True"
    print("\t********** CHICAGO DATA CHALLENGE **********\t\n")
    print("Using the city of chicago data portal to find the relationship between per capital income, hardship index and birthrate, average annual deaths")
    print("Checking if the dataset files exists and readable.......\n")
    
    if fileexist("socio_eco_ind.csv") and isreadable("socio_eco_ind.csv"):
        print("File socio_eco_ind.csv exists and is readable")
    else:
        print("**Problems with file socio_eco_ind.csv in the current directory. Correct this problem first")
        status = "False"
    if fileexist("health_ind.csv") and isreadable("health_ind.csv"):
        print("File health_ind.csv exists and is readable")
    else:
        print("**Problems with file health_ind.csv in the current directory. Correct this problem first")
        status = "False"
    if fileexist("death_causes.csv") and isreadable("death_causes.csv"):
        print("File death_causes.csv exists and is readable")
    else:
        print("**Problems with file death_causes.csv in the current directory. Correct this problem first")
        status = "False"
    print()
    
    if status is "True":
        print("The correlation coefficient between per capita income and birth rate is ", correlation(incomebirth()))
        print("This means there is a "+rstrength(correlation(incomebirth()))+ " between per capita income and birth rate\n")
        
        print("The correlation coefficient between per capita income and death is ", correlation(incomedeath()))
        print("This means there is a "+rstrength(correlation(incomedeath()))+ " between per capita income and average annual number of deaths\n")
        
        print("The correlation coefficient between hardship index and birth is ", correlation(hardshipbirth()))
        print("This means there is a "+rstrength(correlation(hardshipbirth()))+ " between hardship index and birth rate\n")
        
        print("The correlation coefficient between hardship index and death is ", correlation(hardshipdeath()))
        print("This means there is a "+rstrength(correlation(hardshipdeath()))+ " between hardship index and average annual number of deaths\n")
        
main()
