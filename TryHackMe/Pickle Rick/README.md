# Solutions

## What is the first ingredient Rick needs?

we enter the IP to the browser and a page is presented

in the HTTP code there is a comment about ricks username, so we jot that down 

since we dont know any of the directories for the page we decide to http-enum to get information about where we can navigate the page

using nmap command: `nmap -sV --script=http-enum <IP>`

we get a **robots.txt** directory

we navigate to `<IP>/robots.txt` where a string is represented, maybe a password?

nmap also returns a **login.php** page, we enter the information given and we are logged on

## Whats the second ingredient Rick needs?



## Whats the final ingredient Rick needs?


## (Bonus) Easter egg kinda?
