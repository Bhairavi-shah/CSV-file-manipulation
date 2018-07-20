import pandas as pd
from os import sys

def read_file2(filename,cols):
    """
    Function to read 'cols' columns from 'filename' csv File 
    :param filename: File Name
    :param cols: List of Column Names
    :return: Dataframe of the read File
    """
    return(pd.read_csv(filename, usecols=cols, keep_default_na=False))

def read_file(filename):
    """
    Function to read a csv file
    :param filename: File Name
    :return: Dataframe of the read file
    """
    try:
        return(pd.read_csv(filename))
    except IOError :
        print("Error while reading the file. Please check the filename")
        sys.exit()
    except Exception :
        print("Error while reading the file")
        sys.exit()

def write_csv(df,filename):
    """
    Function to write to 'filename'
    :param df: DataFrame
    :param filename: File Name
    """
    df.to_csv(filename)
    print("New File has been written to : splitcols-result.csv")

if __name__ == '__main__':
    filename = input("Enter file to split columns : ")
    df = read_file(str(filename))
    print(list(df.columns))
    i=0
    while(True):
        no_of_cols = int(input("Enter number of columns to split : "))
        cols=[]
        if(no_of_cols>0):
            while True:
                if(i==no_of_cols):
                    break
                column=str(input("Enter column name: "))
                if(column not in list(df.columns)):
                    print("Incorrect column name. Try again!")
                    continue
                else:
                    cols.append(column)
                    i+=1
            break
        else :
            print("Number of columns should be greater than zero. Enter n again.")

    df = read_file2(file_name,cols)
    write_csv(df,"splitcols-result.csv")