import pandas as pd 
from os import sys

def read_file(filename):
    """
    Function to read a csv File
    :param filename: File Name
    :return: Dataframe of the read File
    """
    try:
        df = pd.read_csv(filename) 
        return(df)
    except IOError :
        print("Error while reading the file. Please check the filename")
        sys.exit()
    except Exception :
        print("Error while reading the file")
        sys.exit()

def find(df,cols):
    """
    Function to find duplicate rows in 'df' comparing 'cols'
    :param df: Dataframe
    :param cols: list of column names
    :return: Resultant Dataframe
    """
    df = df.sort_values(by=cols)
    result = pd.DataFrame(columns=df.columns)
    for index, row in df.iterrows() :
        if(index!=len(df.index)-1): 
            i=0
            flag=True
            while(flag==True and i<len(cols)):
                if(df.loc[index,str(cols[i])]!=df.loc[index+1,str(cols[i])]): 
                    flag=False
                    break
                i+=1
            if(flag==True and i==len(cols)):
                result = result.append(df.loc[index])
                result = result.append(df.loc[index+1])
    return(result)                


def write_csv(df,filename):
    """
    Function to write to 'filename'
    :param df: Dataframe
    :param filename: File Name
    """
    df.to_csv(filename) 
    print("New file has been written to : ",filename)

if __name__ == '__main__':
    file_name = input("Enter file to find duplicates : ")
    df = read_file(file_name) 
    print(list(df.columns))
    i=0
    while(True):
        no_of_cols = int(input("Enter number of columns to compare : "))
        cols=[]
        if(no_of_cols>0):
            while True:
                if(i==no_of_cols):
                    break
                column=str(input("Enter column name: "))
                if(str(column) not in list(df.columns)):
                    print("Incorrect column name. Try again!")
                    continue
                else:
                    cols.append(column)
                    i+=1
            break
        else :
            print("Number of columns should be greater than zero. Enter n again.")

    result = find(df,cols)
    result = result.sort_values(by=[result.columns[0]])
    write_csv(result,"duplicate-result.csv")