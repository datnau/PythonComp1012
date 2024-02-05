from time import ctime 

def main(): 
    infile = open(r'C:\Users\ADMIN\Downloads\data1.txt', 'r')
    for line in infile: 
        print(line, end='') 
    infile.close() 
    print("""\n 
Programmed by Stew Dent. 
Date: %s. 
End of processing.""" % ctime()) 

main()






