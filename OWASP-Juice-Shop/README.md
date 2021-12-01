# How to set this thing up

Since this isnt an online based CTF we have to download some things to make it work

1. Download nodejs with `sudo apt install nodejs`
2. Download juice shop `git clone https://github.com/juice-shop/juice-shop.git`
3. `cd juice-shop`
4. `npm install`
5. `npm start`
6. Navigate to <http://localhost:3000>


### Configure Burp Suite to work with Juice-shop

This only works in firefox due to some localhost hijacking stuff, and this security measure can only be disabled in firefox
1. Navigate to `about:config`
2. Search for `network.proxy.allow_hijacking_localhost` and make `true`
3. Change firefox proxy settings to `127.0.0.1` port `8080`
4. Make a configuration on burp proxy listeners to the same as above
5. Navigate to `localhost:3000` in firefox
6. Install certificate and add it to the firefox browser
