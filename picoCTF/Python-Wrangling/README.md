# Solution

We are given
 
 1. A python script (named ende.py)
 2. An encrypted txt-file (named flag.txt.en)
 3. A password (67c6cc9667c6cc9667c6cc9667c6cc96)

Running the following in terminal:

    python3 ende.py
    
Returns the following:

    Usage: ende.py (-e/-d) [file]
    
So -d probably stands for decrypt, we type the following into terminal:

    python3 ende.py -d flag.txt.en

The script asks for the password, so we print it in, and we then get the flag.

Done!

# Takeaways

- try running the script if you dont know what to do
