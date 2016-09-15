import csv

def csvColRemove( inFile, outFile ):
	with open(inFile,'rb') as csvFile:
	    rdr= csv.reader( csvFile )
	    with open(outFile, 'wb') as result:
	        wtr= csv.writer( result )
	        for r in rdr:
	            wtr.writerow( (r[1], r[2], r[3], r[4], r[7], r[8], r[9], r[10], r[11], r[50], r[51], r[52], r[53], r[54], r[55]) )

if __name__ == "__main__":
     import argparse

     parser = argparse.ArgumentParser()
     parser.add_argument('inFile', nargs=1, help="Choose the in file to use")
     parser.add_argument('outFile', nargs=1, help="Choose the out file to use")
     args = parser.parse_args()
     csvColRemove( args.inFile[0] , args.outFile[0] )