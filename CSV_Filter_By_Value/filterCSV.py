import csv

def filterCSV(inFile, outFile, column, value):
	with open(inFile,'rb') as csvFile:
		rdr = csv.reader( csvFile )
		with open (outFile,'wb') as result:
		    wtr = csv.writer(result)            
		    for r in rdr:
		        if r[column] == value:
		             wtr.writerow(r)

if __name__ == "__main__":
     import argparse

     parser = argparse.ArgumentParser()
     parser.add_argument('inFile', nargs=1, help="Choose the in file to use")
     parser.add_argument('outFile', nargs=1, help="Choose the out file to use")
     parser.add_argument('column', nargs=1, type=int)
     parser.add_argument('value', nargs=1, help="Provide the value you wish to find")
     args = parser.parse_args() 
     filterCSV( args.inFile[0] , args.outFile[0], args.column[0], args.value[0] )