This is a repository to manipulate csv files in different ways.  

#### Use Case  
The following use-cases are implemented in the different files:  

	1. Find duplicates comparing only selected columns.  
	2. Join columns from 2 different csv files based on a key value compared from the 2 files.  
	3. Join rows of 2 or more csv files by merely appending them.  
	4. To check if the given Linkedin of a person belongs to First Name and Last Name given using conditions.  
	5. Searching in a file a keyword in selected columns and writing the matching column rows to a new csv file.  
	6. To replace all special characters in the whole csv file with their nearest alphabet using unicode.  
	7. Splitting a csv file to obtain only the required columns.  
	8. Splitting a csv file to obtain chunks of rows in the new csv files making them easier to handle and manipulate.  

#### Implementation details.  

The above functionalities are satisfied by running the required files and giving the required inputs. The csv files along with other necessary inputs should be given to get the desired resulting csv file.  

#### Usage  
Go to `/Programs` and run the following command, making sure your input file is in the same directory.  

```bash  
python3 filename.py  
```   
where filename should be replaced with the following according to the required use-case :  
	1. `duplicate`  
	2. `joincols`  
	3. `joinrows`  
	4. `linkedin`  
	5. `search`  
	6. `specialcharacters`  
	7. `splitcols`  
	8. `splitrows`  

These tools will apply the corresponding rules on the input csv files and write the result to the following based on the chose use-case :  
	1. `duplicate-result.csv`  
	2. `joincols-result.csv`  
	3. `joinrows-result.csv`  
	4. `linkedin-result.csv`  
	5. `search-result.csv`  
	6. `specialchar-result.csv`  
	7. `splitcols-result.csv`  
	8. `splitrows-result1.csv`,`splitrows-result2.csv`, etc. depending upon the chunksize given as input  
