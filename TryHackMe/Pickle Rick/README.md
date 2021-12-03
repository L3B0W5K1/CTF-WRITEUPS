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

in order to retrieve everything in the directory and get an overview we want to use grep

we use command: `grep -r .` 

we find the **rick** folder within the **home** folder, where the file **second ingredents** is found

## Whats the final ingredient Rick needs?

all commands are not allowed in the web interface, so we cant get sudo access

since nmap reveals that the website has port 22 open we want to try to get a reverse shell going since we have access to a Command pannel

the outgoing traffic from the machine has less restrictions than ingoing traffic, this is why reverse shells often times work



## (Bonus) Easter egg kinda?
