import csv
import itertools

def csvColRemove( inFile, outFile, remove ):
	index = remove
	index.sort(reverse=True)
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
	        
	# print "File " + outFile + " exported with the following columns: "
	# print filtered

if __name__ == "__main__":
     import argparse

     parser = argparse.ArgumentParser()
     parser.add_argument('inFile', nargs=1, help="Choose the in file to use")
     parser.add_argument('outFile', nargs=1, help="Choose the out file to use")
     parser.add_argument('-r', '--remove', nargs='*', type=int)
     args = parser.parse_args()
     csvColRemove( args.inFile[0] , args.outFile[0] , args.remove);