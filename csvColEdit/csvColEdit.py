import csv
import itertools

def csvColRemove( inFile, outFile, index ):
	index.sort()
	print "Removing columns in index position(s):  "
	print index
	with open(inFile,'rb') as csvFile:
	    rdr1, rdr2 = itertools.tee(csv.reader( csvFile ))
	    numCols =len(next(rdr1))
	    del rdr1
	    columns = range(0, numCols)
	    for i in index:
			filtered = [c for c in columns if c not in index ]
	    with open(outFile, 'wb') as result:
	        wtr= csv.writer( result )
	        for r in rdr2:
	            wtr.writerow( [r[f] for f in filtered])

def csvColKeep( inFile, outFile, index ):
	index.sort()
	print "Removing all columns except those in index position(s):  "
	print index
	with open(inFile,'rb') as csvFile:
	    rdr = csv.reader( csvFile )
	    with open(outFile, 'wb') as result:
	        wtr= csv.writer( result )
	        for r in rdr:
	            wtr.writerow( [r[i] for i in index])
	        

if __name__ == "__main__":
     import argparse

     parser = argparse.ArgumentParser()
     parser.add_argument('inFile', nargs=1, help="Choose the in file to use")
     parser.add_argument('outFile', nargs=1, help="Choose the out file to use")
     parser.add_argument('-r', '--remove', nargs='*', type=int)
     parser.add_argument('-k', '--keep', nargs='*', type=int)
     args = parser.parse_args()
     if args.remove:
     	csvColRemove( args.inFile[0] , args.outFile[0] , args.remove);
     elif args.keep:
     	csvColKeep( args.inFile[0] , args.outFile[0] , args.keep);