    flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽'
    out = ""
    for l in flag:
        l = ord(l) 
        out += chr((l)>>8 & 0xFF00) 
        out += chr((l & 0x00FF)) 
    print(out)
