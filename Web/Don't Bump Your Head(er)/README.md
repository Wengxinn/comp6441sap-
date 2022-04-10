# Don't Bump Your Head(er)

## [CTFlearn Challenge](https://ctflearn.com/challenge/109)
<img src="don't bump your header - solved.png">

## Solutions
### Step 1: 
Here's the site of the link attached in the question: 

<img src="don't bump your header - 6.png">

The hint is that ```user agent``` was incorrect. 

### Step 2: 
Same as POST Practice, I first inspected the website to look for any hidden data. 

<img src="don't bump your header - 1.png">

In the ```html``` body, there is a hidden data:

```Sup3rS3cr3tAg3nt```

### Step 3: 
For this challenge, I utilised a useful toolkit for web app security testing, ```Burp Suite```. 

I changed the value of ```User-Agent``` to ```Sup3rS3cr3tAg3nt```.  

<img src="don't bump your header - 2.png">

### Step 4: 
The flag was not shown but the message displayed on the website altered. It indicates that the server recognised incorrect```Referer``` (absolute or partial address that makes the request) in HTTP request. 

<img src="don't bump your header - 3.png">

To get the flag, we have to change its value to ```awesomesauce.com```.  

<img src="don't bump your header - 4.png">

### Step 5: 
This time round, the HTTP request satisfied all conditions and the flag was displayed on the site. 

<img src="don't bump your header - 5.png">

### Flag: 
```flag{did_this_m3ss_with_y0ur_h34d}```

## End Notes
Kinda :P but I loved this challenge so much. Not only it refreshes my memory regarding HTTP server and requests, it gets me learned about HTTP header - ```User Agent and Referer```. I was also able to explore a new toolkit for web exploitation. 