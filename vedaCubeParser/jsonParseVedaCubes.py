import json

def jsonFilter( inFile, outFile ):
    # make a dictionary instead.
    out = {};

    with open( inFile, 'r') as jsonFile:
       json_data = jsonFile.read()
       d = json.loads(json_data)
       # build the data you want to save to look like the original
       # by taking the data in the d['data'] element filtering what you want
       # elements where b[0] is 'x' or b[0] is 'column_header'
       out['data'] = [b for b in d['data'] if b[0] == 'Premium' or b[0] == 'VEDA FEC Donor Class' ]


    if out:
        with open( outFile, 'w' ) as jsonFile:
            jsonFile.write( json.dumps( out ) );

    else:
       print "Error creating new jsonFile!"

if __name__ == "__main__":
     import argparse

     parser = argparse.ArgumentParser()
     parser.add_argument('inFile', nargs=1, help="Choose the in file to use")
     parser.add_argument('outFile', nargs=1, help="Choose the out file to use")
     args = parser.parse_args()
     jsonFilter( args.inFile[0] , args.outFile[0] );