import glob

# Choose correct folder with Textfiles
filenames = glob.glob('./text/*.txt')  # list of all .txt files in the directory
count = 0

with open('outputfile.txt', 'w') as f:
    for file in filenames:
        with open(file) as infile:
        #Extra lines 
            f.write('Minute: ')
            f.write("{0}".format(count))
            f.write(':00:00  ------------\n')
            f.write(infile.read()+'\n')
            f.write('\n')
            count = count + 1
