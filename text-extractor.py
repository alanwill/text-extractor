fname = raw_input("Enter file name: ")
startextraction = raw_input("Enter start extraction point: ")
endextraction = raw_input("Enter end extraction point: ")

fh = open(fname)
count = 0

for line in fh:
    firstextract = line.split(startextraction,1)[1]
    lastextract = firstextract.split(endextraction,1)[0]
    print lastextract
    count = count + 1

print "There were", count, "strings extracted."