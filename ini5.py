def ReadEvenLines(file):
    f = open(file,'r');
    file_contents = f.readlines();
    outputFile = open('ReadEvenLinesOutput.txt','w');
    if len(f.readlines()) > 1000:
        print("The file must contain at most 1,000 lines.")
    else:
        for i in range(len(file_contents)):
            if (i+1)%2 == 0:
                print(file_contents[i])
                outputFile.write(file_contents[i])
    f.close()
    outputFile.close()
