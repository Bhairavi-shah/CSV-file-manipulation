import pandas as pd
from os import sys

def read_file(filename):
    """
    Function to read a csv File
    :param filename: File Name
    :return: Dataframe of the read File
    """
    try:
        return(pd.read_csv(filename, keep_default_na=False))
    except IOError :
        print("Error while reading the file. Please check the filename")
        sys.exit()
    except Exception :
        print("Error while reading the file")
        sys.exit()

def write_csv(df,filename):
    """
    Function to write to 'filename'
    :param df: Dataframe
    :param filename: File Name
    """
    df.to_csv(filename) 
    print("New file written to : joincols-result.csv")

def join(df1,df2,col_name1,col_name2):
    """
    Function to join 2 dataframes using equal 'col_name1' and 'col_name2' in 'df1' and 'df2' respectively
    :param df1: First Dataframe
    :param df2: Second Dataframe
    :param col_name1: Key Column name in df1
    :param col_name2: Key Column name in df2
    """
    merged = df1.merge(df2, left_on=col_name1, right_on=col_name2, how="outer")
    return merged

if __name__ == '__main__':

    filename1 = input("Enter 1st file : ")
    df1 = read_file(filename1)

    filename2 = input("Enter 2nd file : ")
    df2 = read_file(filename2)

    print(list(df1.columns))
    col_name1 = input("Enter column name in 1st file to merge with : ")
    if(str(col_name1) not in list(df1.columns)):
        print("Incorrect column name")
        sys.exit()

    print(list(df2.columns))
    col_name2 = input("Enter column name in 2nd file to merge with : ")
    if(str(col_name2) not in list(df2.columns)):
        print("Incorrect column name")
        sys.exit()

    result = join(df1,df2,col_name1,col_name2)
    write_csv(result,"joincols-result.csv")
    