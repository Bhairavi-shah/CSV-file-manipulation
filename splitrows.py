import pandas as pd
from os import sys

def split_read(filename, chunk_size):
    """
    Function to read a csv File chunkwise
    :param file_name: File Name
    :param chunk_size: Number of rows in each new File
    """
    try:
        df = pd.read_csv(filename, chunksize=chunk_size, keep_default_na=False)
        i=1
        for chunk in df:
            write_csv(chunk, str("splitrows-result"+str(i))+".csv")
            i+=1
    except IOError :
        print("Error while reading the file. Please check the filename")
        sys.exit()
    except Exception:
        print("Error while reading the file")
        sys.exit()
        

def write_csv(df,filename):
    """
    Function to write to 'filename'
    :param df: Dataframe
    :param filename: File Name
    """
    df.to_csv(filename)

if __name__ == '__main__':
    filename = input("Enter file name to split rows : ")
    chunk_size = int(input("Enter number of rows in a chunk to split : "))
    if(chunk_size>0):
        split_read(filename,chunk_size)
        print("New files have been written")
    else:
        print("Incorrect size to split")