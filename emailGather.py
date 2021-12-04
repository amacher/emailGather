import csv
import os
#where to read files from, replace 'C:...' with our path
directory = r'C:...'
#where to save the email addresses, replace 'C:...' with our path
csvFile='C:.../emails.csv'

def get_addresses(indItems):
    toFile = indItems.split(',')
    for file in toFile:
        file = file.strip()
        splitFile = file.split(' ')
        with open(csvFile, 'a') as email_file:
            writer = csv.writer( email_file )
            if len( splitFile ) is 3:
                first = splitFile[0].strip()
                last = splitFile[1]
                email = replaceChar( splitFile[2] )
                full = first, last, email
            elif len( splitFile ) is 2:
                first = splitFile[0].strip()
                last = ' '
                email = replaceChar( splitFile[1] )
                full = first, last, email
            elif len( splitFile ) is 4:
                first = splitFile[0].strip() + ' ' + splitFile[1].strip()
                last = splitFile[2]
                email = replaceChar( splitFile[3] )
                full = first, last, email
            if doubles( email ) is not True:
                writer.writerow( full )

def replaceChar(item):
#goes through to strip the characters not needed.
    remove_characters = ['<', '>', ',']
    for char in remove_characters:
        item = item.replace( char, '' )
    return item.strip()

def doubles(check):
    with open(csvFile) as f:
        datafile = f.readlines()
        for line in datafile:
            if check in line:
                return True

with open(csvFile, 'w') as email_file:
    #Creates CSV file and writes the first name elements
    firstLine = ('First Name', 'Last Name', 'Email Address')
    writer = csv.writer( email_file )
    writer.writerow( firstLine )
    #Goes through files in the folder
for filename in os.listdir(directory):
    if filename.endswith(".eml"):
        f = open( directory+filename, "r" )
        read = f.readlines()
        count = 0
        for line in read:
            count += 1
            if line.startswith( ('From', 'To', 'Cc', 'Bcc') ):
                #Clears the extras From, to, etc
                removeStart = line.split(":")[1].strip()
                #breaks it down to individual pieces (names, email)
                get_addresses(removeStart)
                subCount = count
                while read[subCount].startswith( '\t' ) == True:
                    removeStart2 = read[subCount].strip('\t')
                    get_addresses( removeStart2 )
                    subCount += 1
    else:
        #to ignore any none .eml file
        continue
    f.close()