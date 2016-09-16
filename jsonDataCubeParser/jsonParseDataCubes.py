import json

def jsonFilter( inFile, outFile, index, values ):
    # make a dictionary instead.
    out = {};
    i = int(index)
    values = [value[:1].upper() + value[1:] for value in values]

    with open( inFile, 'r') as jsonFile:
       json_data = jsonFile.read()
       d = json.loads(json_data)
       # build the data you want to save to look like the original
       # by taking the data in the d['data'] element filtering what you want
       # elements where b[0] is 'x' or b[0] is 'column_header'
       for value in values:
           out['data'] = [b for b in d['data'] if b[i] in values]


    if out:
        with open( outFile, 'w' ) as jsonFile:
            jsonFile.write( json.dumps( out ) );
            print values

    else:
       print "Error creating new jsonFile!"

if __name__ == "__main__":
     import argparse

     parser = argparse.ArgumentParser()
     parser.add_argument('inFile', nargs=1, help="Choose the in file to use")
     parser.add_argument('outFile', nargs=1, help="Choose the out file to use")
     parser.add_argument('index', nargs=1, help="Declare in which index position you would like to search for values")
     parser.add_argument('-f', '--find', nargs='*')
     args = parser.parse_args()
     jsonFilter( args.inFile[0] , args.outFile[0] , args.index[0], args.find );