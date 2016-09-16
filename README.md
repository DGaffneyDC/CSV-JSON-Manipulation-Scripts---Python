# CSV-and-JSON-Manipulation-Scripts---Python

Helpful python scripts for csv and json manipulation. 

# CSV-Column-Remover

Helpful cli tool to remove columns from a CSV file by their index position. Columns begin at index 0. 

Arguments:
	
	inFile: filename for input csv (e.g. exampleFile1.csv)
	
	outFile: Filename for output csv created (e.g. outputFile1.csv)
		
		*Optional: designate relative path to desired output directory (e.g. ~/Desktop/Outputs/outputFile1.csv)
	
	-r, --remove: Index positions of column(s) you want to remove.

Examples:

~$ python csvColRemove.py exampleFile1.csv outputFile1.csv -r 1 5 17 2 9 10

~$ python csvColRemove.py ~/Desktop/Outputs/exampleFile1.csv outputFile1.csv --remove 1 5 17 2 9 10




# JSON Data Cube Parsing

Provide inFile, outFile, index position and value(s) to filter JSON data cubes.

Example:

~$ python jsonParseDataCubes.py inFile.json outFile.json 3 --find Elite Premium

(Find all cube rows with either Elite or Premium in the 3rd index position)



# Filter CSV

Simply supply an inFile name, and outFile name, a column number and a value or values on the command line to create a new CSV containing rows with your designated value present.

Example:

~$ Python filterCSV.py exampleIn.csv exampleOut.csv 2 -f Bananas

~$ Python filterCSV.py exampleIn.csv exampleOut.csv 2 --filter Bananas Grapes



