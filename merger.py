filenames = ['1-bundesliga-i.txt', '1-bundesliga-ii.txt']
with open('bundesliga2016.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
        outfile.write('\n')
outfile.close()
