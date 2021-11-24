# Solution

we are given this encrypted flag:

    灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽
    
and this piece of code:

    ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
     
indented:
     
    ''.join(
    [
        chr(
            (
                ord(flag[i]) << 8) +
                ord(flag[i + 1]
            )
        )
        for i in range(
            0,
            len(flag),
            2
        )
    ]
)

so what this code does is its taken the flag as input (the flag that we want)

and it has encrypted the flag returning this string: 灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷

what we have to figure out is how the code does this and reverse engineer it

and creating our own code that decrypts the string
