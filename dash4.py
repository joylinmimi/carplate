with open("license.txt", "r") as ins:
    array = []
    i=0
    plate=0
    for line in ins:
        if (i==1 and line[4]=='-'):         
            p = line.index("c")
            #print line[:p]
            plate=line[:p-2][6:]
            #print plate
            if (len(str(plate))==7 and plate[3:].isdigit()):
                plate=plate[:3]+'-'+plate[3:]
                
                print(plate )                
                i=0
            elif (len(str(plate))==6):
                #print plate
                if (plate[2:].isdigit()):
                    print(plate[:2]+'-'+plate[2:])
                    i=0
                else:
                    if (plate[3:].isdigit()):
                        print(plate[:3]+'-'+plate[3:])
                        i=0
                    else:
                        if (plate[:4].isdigit()):
                            print(plate[:4]+'-'+plate[4:])
                            i=0
                        else:
                            if (plate[:3].isdigit()):
                                print(plate[:3]+'-'+plate[3:])
                                i=0
                      
            elif (len(str(plate))==5):
                if (plate[2:].isdigit()):
                    print(plate[:2]+'-'+plate[2:])
                    i=0
                else:
                    if (plate[:3].isdigit()):
                        print(plate[:3]+'-'+plate[3:])
                        i=0
            else:     
                    i=1
        if (line[2]=='L'):
            print line
        if (line[0]=='p'):
            i=1
