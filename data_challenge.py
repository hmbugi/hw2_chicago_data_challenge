"""Created by Harrison Mbugi"""

from csv import *


def socioparser():
    ''' Fetching community area number & name,
per capita income and hardship index into a list  '''
    soc_list = []
    soc_obj = open("socio_eco_ind.csv")
    soc_reader = reader(soc_obj)
    for row in soc_reader:
        soc_list.append([row[0], row[1], row[7], row[8]])
    return soc_list
        
def birthparser():
    ''' Fetching community area number and birth rate  '''
    bir_list = []
    bir_obj = open("health_ind.csv")
    bir_reader = reader(bir_obj)
    for row in bir_reader:
        bir_list.append([row[0], row[2]])
    return bir_list

def deathparser():
    ''' Fetching community area number, average annual deaths
and cumulative death ranks '''
    dea_list = []
    dea_obj = open("death_causes.csv")
    dea_reader = reader(dea_obj)
    for row in dea_reader:
        dea_list.append([row[1], row[5], row[4]])
    return dea_list

def populationparser():
    ''' Fetching community area number and population in 2010 '''
    pop_list = []
    pop_obj = open("population_2010.csv")
    pop_reader = reader(pop_obj)
    for row in pop_reader:
        pop_list.append([row[0], row[2]])
    return pop_list

def incomebirth():
    '''Manipulates return values of socioparser() and birthparser()
and return a list containing values to be used for colleration
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
    '''Manipulates return values of socioparser() and birthparser()
and return a list containing values to be used for colleration
income-birth correlation'''
    incomedeath, x, y, xy, x2, y2 = ([] for i in range(6)) #same as [[]]*6 . Both initialize empty lists to variables


