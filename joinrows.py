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
        print("Please check the filename")
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
    print("New file written to : joinrows-result.csv")

def join(df1,df2):
    """
    Function to append 'df1' to 'df2'
    :param df1: Dataframe 1
    :param df2: Dataframe 2
    """
    result = df1.append(df2)
    result = result.drop(result.columns[0], axis=1)
    return result

if __name__ == '__main__':
    no_of_files = int(input("Enter how many files you want to append : "))
    i=1
    flag=False
    while flag==False :
        if(no_of_files>1):
            df = read_file(input("Enter file name : "))
            while True:
                if(i<no_of_files):
                    df1 = read_file(input("Enter file name : ")) 
                    df = join(df,df1) 
                    i+=1
                else :
                    flag=True
                    break
        else:
            print("There should be more than one files to append.")
            sys.exit()
    write_csv(df,"joinrows-result.csv") 