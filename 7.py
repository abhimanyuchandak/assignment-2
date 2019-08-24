def cc(path):
    f=path
    f=open(path,'r')
    lines=f.readlines()
    numwords=0
    numchara=0
    print ("lines =",len(lines))
    for line in lines:
        word=line.split()
        numwords+=len(word)
        chara=line.strip()
        numchara+=len(chara)
    print(numwords,numchara)
path= "C:\\Users\\Abhimanyu Chandak\\Desktop\\open\\a1\\try.txt"
cc(path)
