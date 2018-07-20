import pandas as pd
from os import sys

def read_file(filename):
    """
    Function to read a csv File
    :param filename: File Name
    :return: dataframe of the read File
    """
    try:
        df = pd.read_csv(filename, keep_default_na=False) 
        df["check status"]="Default"
        return(df)
    except IOError :
        print("Error while reading the file. Please check the filename")
        sys.exit()
    except Exception :
        print("Error while reading the file")
        sys.exit()
   
def read_cols(df):
    """
    Fuction to read column names as user input
    :param df: DataFrame
    :return: list of column names
    """
    cols=[]
    while(True):
        column=str(input("Enter first-name column name: "))
        if(str(column) not in list(df.columns)):
            print("Incorrect column name. Try again!")
        else:
            cols.append(column)
            break 
    
    while(True):
        column=str(input("Enter last-name column name: "))
        if(str(column) not in list(df.columns)):
            print("Incorrect column name. Try again!")
        else:
            cols.append(column)
            break 

    while(True):
        column=str(input("Enter linkedin column name: "))
        if(str(column) not in list(df.columns)):
            print("Incorrect column name. Try again!")
        else:
            cols.append(column)
            break 
    return cols

def verify(df,cols):
    """
    Function to Verify Linkedin using First Name and Last Name
    :param df: Data Frame
    :param cols: list of column names of FirstName, LastName and Linkedin
    :return: DataFrame with Status column 
    """
    for index, row in df.iterrows() : 
        f=df.loc[index, cols[0]] 
        l=df.loc[index, cols[1]] 
        link=df.loc[index, cols[2]] 

        f=f.split(" ")   
        l=l.split(" ") 

        for i in range(len(f)):
            f[i]=f[i].lower()
        for i in range(len(l)):
           l[i]=l[i].lower()
        link=link.lower()        
       
        if(check_linkedin(link)==True):
            stat=check_constraints(f,l,link[28:]) 
            if(stat==1):
               df.loc[index,'check status']="true"
            elif(stat==2):
                df.loc[index,'check status']="maybe"
            else:
                df.loc[index,'check status']="false"
        else:
           df.loc[index,'check status']="Not a LinkedIn ID"
    return df

def check_linkedin(link): 
    """
    Function to check if 'link' is a linkedin id
    :param link: Linkedin ID
    :return: Boolean
    """
    if(link[:25]=="https://www.linkedin.com/" or link[:24]=="http://www.linkedin.com/"): 
        return True
    else:
        return False

def check_constraints(f,l,lin):
    """
    Function to check constraints
    :param f: First Name
    :param l: Last Name
    :param lin: Linkedin ID
    :return: 
                0 - False
                1 - True
                2 - Maybe
    """
    for i in range(len(f)):
        for j in range(len(l)):
            if( (f[i] in lin) and (l[j] in lin) ): #every combination of words in lists of First_Name and Last_Name  
                return 1
    if(len(f)>1):
        for i in range(len(f)):
            for j in range(i+1,len(f)):
                if( (f[i] in lin) and (f[j] in lin) ): #every combination of first names
                    return 1
    if(len(l)>1):
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if( (l[i] in lin) and (l[j] in lin) ): #every combination of last names
                    return 1
    for i in range(len(f)):
        for j in range(len(l)):
            if((f[i]+l[j][0] in lin) or (f[i][0]+l[j] in lin)): #first letter of first name and last name OR first name and first letter of last name
                return 2
    name1="" #To store all first letters of first names and then last names
    name2="" #To store all first letters of last names  and then first names 
    for i in range(len(f)): 
        name1+=f[i][0]
    for j in range(len(l)):
        name1+=l[j][0]
        name2+=l[j][0]
    for i in range(len(f)):
        name2+=f[i][0]
    if(name1 in lin or name2 in lin):
        return 2
    for i in range(len(f)): 
        if(len(f[i])>2 and f[i][:3] in lin): #First 3 letters if numberofletters>2
            return 2
        elif(f[i] in lin): #Check if first name in lin
            return 2
    for i in range(len(l)): 
        if(len(l[i])>2 and l[i][:3] in lin): #First 3 letters if numberofletters>2
            return 2
        elif(l[i] in lin): #Check if first name in lin
            return 2
    return 0

def write_csv(df,filename):
    """
    Function to write to 'filename'
    :param df: Dataframe
    :param filename: File Name
    """
    df.to_csv(filename) 
    print("New file has been written to : ",filename)


if __name__ == '__main__':
    filename = input("Enter file to check linkedin : ")
    df = read_file(filename)
    print(list(df.columns))
    
    cols=read_cols(df)

    df = verify(df,cols) 
    write_csv(df,"linkedin-result.csv") 

