def neighborCheck(liveCells: list)->list:
    try:
        liveCells = sorted(liveCells)
    except TypeError:
        return []

    toUpdate = []

    for center in liveCells:
        neighbors = 0
        n = []
        for checker in liveCells:
            if center == checker:
                continue
            elif yCheck(center[1],checker[1]) and xCheck(center[0],checker[0]):
                neighbors += 1
                n.append((checker[0],checker[1]))
                #print(f'{checker} is a neighbor of {center}')
        if (neighbors < 2 or neighbors > 3):
            toUpdate.append((center[0],center[1],-1))
        elif neighbors == 2:
            if center[0] == n[0][0] and center[0] == n[1][0]:
                n.append((center[0],center[1],center[2]))
                
                nSorted = sorted(n)
                print("here")
                toUpdate.append((n[1][0] - 1,n[1][1] - 1,1))
                toUpdate.append((n[1][0] + 1,n[1][1] - 1,1))
                toUpdate.append((center[0],center[1],1))
            
            elif center[1] == n[0][1] and center[1] == n[1][1]:
                n.append((center[0],center[1],center[2]))
               
                nSorted = sorted(n)

                toUpdate.append((n[1][0] - 1,n[1][1] + 1,1))
                toUpdate.append((n[1][0] - 1,n[1][1] - 1,1))
                toUpdate.append((center[0],center[1],1))
            else:
                print("here")
                xVal = max((n[0][0] - center[0],n[1][0] - center[0]))
                yVal = max((n[0][1] - center[1],n[1][1] - center[1]))
                
                toUpdate.append((xVal,yVal,1))
                toUpdate.append((center[0],center[1],1))

        #print(f'{center} has {neighbors} neighbors\n')
    return toUpdate
