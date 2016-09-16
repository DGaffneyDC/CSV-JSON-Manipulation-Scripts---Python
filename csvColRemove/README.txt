Helpful cli tool to remove columns from a CSV file by their index position. Columns begin at index 0. 

Arguments:
	
	inFile: filename for input csv (e.g. exampleFile1.csv)
	
	outFile: Filename for output csv created (e.g. outputFile1.csv)
		
		*Optional: designate relative path to desired output directory (e.g. ~/Desktop/Outputs/outputFile1.csv)
	
	-r, --remove: Index positions of column(s) you want to remove.

Examples:

~$ python csvColRemove.py exampleFile1.csv outputFile1.csv -r 1 5 17 2 9 10

~$ python csvColRemove.py ~/Desktop/Outputs/exampleFile1.csv outputFile1.csv --remove 1 5 17 2 9 10
