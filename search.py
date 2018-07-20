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
    print("New file written to search-result.csv")

def find(df, col_name, keyword):
    """
    Function to find 'keyword' in column 'col_name' in 'df
    :param df: DataFrame
    :param col_name: Column Name
    :param keyword: Keyword to search
    """
    df2 = pd.DataFrame(columns=df.columns) 
    for index, row in df.iterrows() :
        if(keyword.lower() in row[col_name].lower()): 
            df2 = df2.append(df.loc[index])
    return df2

def read_col_names_and_search(df):
    """
    Function to read column names, search keyword in that column name and append to new Dataframe
    :param df: Dataframe
    :return: New Dataframe
    """
    df_final = pd.DataFrame(columns=df.columns)
    i=0
    while(True):
        keyword=input("Enter keyword to search : ")
        no_of_cols = int(input("Enter number of columns to search : "))

        if(no_of_cols>0):
            while True:
                if(i==no_of_cols):
                    break
                col_name=str(input("Enter column name: "))
                if(col_name not in list(df.columns)):
                    print("Incorrect column name. Try again!")
                    continue
                else:
                    df_final = df_final.append(find(df,col_name, keyword))
                    i+=1
            break
        else :
            print("Number of columns should be greater than zero. Enter number of columns again.")
    return df_final


if __name__ == '__main__':
    filename = input("Enter file to search columns : ")
    df = read_file(filename)
    print(list(df.columns))

    df_final = read_col_names_and_search(df)

    df_final = df_final.drop_duplicates()

    write_csv(df_final,"search-result.csv")