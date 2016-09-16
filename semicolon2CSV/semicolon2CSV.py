import csv

def semicolon2CSV(inFile, outFile):

	with open( inFile, 'r') as semicolonFile:
		semiFile = csv.reader(semicolonFile, delimiter=';')
		with open(outFile, 'w') as result:
			csvOut = csv.writer(result)
			for row in semiFile:
				csvOut.writerow(row)

if __name__ == "__main__":
     import argparse

     parser = argparse.ArgumentParser()
     parser.add_argument('inFile', nargs=1, help="Choose the in file to use")
     parser.add_argument('outFile', nargs=1, help="Choose the out file to use")
     args = parser.parse_args()
     semicolon2CSV( args.inFile[0] , args.outFile[0] );