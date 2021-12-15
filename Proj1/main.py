from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print("Project 1");

df = pd.read_excel('../Stats1/COVID-19-geographic-disbtribution-worldwide-2020-12-14.xlsx', index_col=0)  

#ContinentSplitdf = [ x for x in df.groupby(df["continentExp"])]     

#splitdf = [ x for x in df.groupby(df["countriesAndTerritories"])]


def specifc_countries_phase(df):
    countries = ["United_Kingdom", "Germany", "Poland", "France"]
    for country in countries:
        day = df[df["countriesAndTerritories"] == country]["day"]
        month = df[df["countriesAndTerritories"] == country]["month"]
        cases = df[df["countriesAndTerritories"] == country]["cases"]
        deaths = df[df["countriesAndTerritories"] == country]["deaths"]
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot3D(day + 30 * month, cases, deaths/cases)
        
    plt.legend(countries)    
    plt.show()



def specifc_countries(df):
    countries = ["United_Kingdom", "Germany", "Poland", "France"]
    for country in countries:
        day = df[df["countriesAndTerritories"] == country]["day"]
        month = df[df["countriesAndTerritories"] == country]["month"]
        deaths = df[df["countriesAndTerritories"] == country]["deaths"]
        cases = df[df["countriesAndTerritories"] == country]["Cumulative_number_for_14_days_of_COVID-19_cases_per_100000"]
        
        #plt.plot(day + 30 * month, cases);
        plt.plot(deaths, cases);
        
    plt.legend(countries)    
    plt.show()



def seperate_countries(splitdf):
    numberOfCountries = 15
    labels = []
    for n in range(0, len(countries)):
        day = splitdf[n][1]["day"]
        month = splitdf[n][1]["month"]
        cases = splitdf[n][1]["Cumulative_number_for_14_days_of_COVID-19_cases_per_100000"]
        labels.append(splitdf[n][1]["countriesAndTerritories"][0])
        plt.plot(day + 30 * month, cases);
        
    plt.legend(labels)    
    plt.show()#
    
specifc_countries_phase(df)