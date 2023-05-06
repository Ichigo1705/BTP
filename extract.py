def extrct(Text):

    a = Text.split()
    b = []
    numerals = []

    for x in a:
        if x.isdigit():
            numerals.append(int(x))
        else:
            b.append(x)

    l1 = ['forward', 'ahead', 'further', 'onwards', 'front']
    l2 = ['backward', 'behind', 'rearwards', 'back']
    l3 = ['right', 'clockwise', 'rightward']
    l4 = ['left', 'anticlockwise', 'leftward']
    l5 = ['stop', 'quit', 'abort', 'end']

    res = []
    idx = 0

    for x in b:
        temp = []
        if x in l1:
            temp.append(1)
            temp.append(numerals[idx])
            idx += 1
        if x in l2:
            temp.append(2)
            temp.append(numerals[idx])
            idx += 1
        if x in l3:
            temp.append(3)
            temp.append(numerals[idx])
            idx += 1
        if x in l4:
            temp.append(4)
            temp.append(numerals[idx])
            idx += 1
        if x in l5:
            temp.append(5)
        if(len(temp) != 0): 
            res.append(temp)

    return res
    
