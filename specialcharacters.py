import pandas as pd
import unicodedata
import string
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

def convert(df,col_name):
    """
    Convert column to normal text
    :param df: Dataframe
    :param col_name: Column Name
    :return: Dataframe
    """
    for index, row in df.iterrows() : 
        col=df.loc[index,col_name] 

        col = str(col)
        col = "".join(x for x in unicodedata.normalize("NFKD",col) if x in string.ascii_letters or x==" ")

        col=col.split(" ") 
        for word in range(len(col)) : 
            col[word]=col[word].capitalize()
        col=" ".join(col)
        df.loc[index,col_name]=col
    return df

def check_type(col_name):
    """
    Function to check type of col_name is str
    :param col_name: Column Name
    :return: Boolean
    """
    if(isinstance(col_name,str)):
        return True
    else:
        return False

def write_csv(df,filename):
    """
    Function to write to 'filename'
    :param df: Dataframe
    :param filename: File Name
    """
    df.to_csv(filename)
    print("New file has been written to : ",filename)

if __name__ == '__main__':
    filename = input("Enter file to change special characters : ")
    df = read_file(filename)
    for col_name in df.columns :
        if(check_type(col_name)):
            df = convert(df,col_name)
    write_csv(df,"specialchar-result.csv")