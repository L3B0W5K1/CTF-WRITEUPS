# Solutions

## What is the first ingredient Rick needs?

we enter the IP to the browser and a page is presented

in the HTTP code there is a comment about ricks username, so we jot that down 

since we dont know any of the directories for the page we decide to http-enum to get information about where we can navigate the page

using nmap command: `nmap -sV --script=http-enum <IP>`

we get a **robots.txt** directory

we navigate to `<IP>/robots.txt` where a string is represented, maybe a password?

nmap also returns a **login.php** page, we enter the information given and we are logged on

the web applications has a **Command Pannel** for the user, so we can use unix commands

we use `ls` and a file **Sup3rS3cretPickl3Ingred.txt** is presented

we head to `<IP>/Sup3rS3cretPickl3Ingred.txt` and get the first ingredient


## Whats the second ingredient Rick needs?

we 

## Whats the final ingredient Rick needs?


## (Bonus) Easter egg kinda?
