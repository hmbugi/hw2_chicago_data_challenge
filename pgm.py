"""Created by Harrison Mbugi"""


from csv import *

#socio_list = []
#birth_list = []
#death_list = []
#popul_list = []

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





