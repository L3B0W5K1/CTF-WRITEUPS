# Solution


- here we are supposed to use netcat 
- we are given this this address and port: **mercury.picoctf.net 35652**
- into terminal:

      nc mercury.picoctf.net 35652

we get the following:

    112 
    105 
    99 
    111 
    67 
    84 
    70 
    123 
    103 
    48 
    48 
    100 
    95 
    107 
    49 
    116 
    116 
    121 
    33 
    95 
    110 
    49 
    99 
    51 
    95 
    107 
    49 
    116 
    116 
    121 
    33 
    95 
    57 
    98 
    51 
    98 
    55 
    51 
    57 
    50 
    125 
    10
    
- The numbers represent ASCII
- I save the numbers into a file and wrote a python script to convert it into the flag

      f = open("dude","r")

      myList = []
      for line in f:
         myList.append(line)

      nums = []
      for i in myList:
          nums.append(int(i))

      flag = ""
      for number in nums:
          flag += chr(number)

      print(flag)
      
- The script makes a list of numbers from the given numbers
- Chr converts the numbers into ascii



# Takeaways

- Numbers represent Ascii
