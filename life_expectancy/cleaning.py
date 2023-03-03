"""
Cleaning script
"""
import pandas as pd

def clean_data():
    
    data = pd.read_csv("data/eu_life_expectancy_raw.tsv", sep='\t')
    print(data.columns)
    new_name = "col_mesh"
    data = data.rename(columns={'unit,sex,age,geo\time': new_name})
    print("CHEGOOOOO")
    print(data.columns)
    # print(data['unit,sex,age,geo\time'])
    data = pd.melt(data, id_vars=new_name, value_vars=['2021 ', '2020 ', '2019 ', '2018 ', '2017 ',
       '2016 ', '2015 ', '2014 ', '2013 ', '2012 ', '2011 ', '2010 ', '2009 ',
       '2008 ', '2007 ', '2006 ', '2005 ', '2004 ', '2003 ', '2002 ', '2001 ',
       '2000 ', '1999 ', '1998 ', '1997 ', '1996 ', '1995 ', '1994 ', '1993 ',
       '1992 ', '1991 ', '1990 ', '1989 ', '1988 ', '1987 ', '1986 ', '1985 ',
       '1984 ', '1983 ', '1982 ', '1981 ', '1980 ', '1979 ', '1978 ', '1977 ',
       '1976 ', '1975 ', '1974 ', '1973 ', '1972 ', '1971 ', '1970 ', '1969 ',
       '1968 ', '1967 ', '1966 ', '1965 ', '1964 ', '1963 ', '1962 ', '1961 ',
       '1960 '])
    print(data)
    data[['unit', 'sex', 'age', 'region']] = data[new_name].str.split(',', expand=True)

    print(data)
    print(data.columns)

clean_data()


