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

What the code does exactly:

1. Takes the first element (ascii symbol) in the flag and turns it into its unicode value with *ord* function (all symbols have a certain unicode value)
2. the **<<** operator shifts the Unicode number one bit to the right, meaning the binary number equvalent gets a zero added from the right, example:

if we have the **~** symbol, its unicode value is **126**, which translates to **0111 1110** in binary

shifting the unicode value for **~** one step to the left makes the unicode value double, which is logical, since the new binary value is **1111 1100**

![Screenshot 2021-11-24 at 21 17 10](https://user-images.githubusercontent.com/74051842/143307942-123edd2e-658c-4944-ac25-090286637618.png)

3. de
4. 


