import csv
def filterCSV(inFile, outFile, column, values):
     print values  

     with open(inFile,'rb') as csvFile:
		rdr = csv.reader( csvFile )
		with open (outFile,'wb') as result:
		    wtr = csv.writer(result)         
		    for r in rdr:
		        if r[column] in values:
		             wtr.writerow(r)


if __name__ == "__main__":
     import argparse

     parser = argparse.ArgumentParser()
     parser.add_argument('inFile', nargs=1, help="Choose the in file to use")
     parser.add_argument('outFile', nargs=1, help="Choose the out file to use")
     parser.add_argument('column', nargs=1, type=int)
     parser.add_argument('-f', '--find', nargs='*')
     args = parser.parse_args() 
     filterCSV( args.inFile[0] , args.outFile[0], args.column[0], args.find )