# POST Practice

## [CTFlearn Challenge](https://ctflearn.com/challenge/114)
<img src="post practice - solved.png">

## Solutions
### Step 1: 
The link in the question took me to a site as shown in the picture. 

<img src="post practice - 1.png">

### Step 2: 
Based on the message ```This site takes POST data that you have not submitted!```, I knew that the I first had to look for the missing data. 

In order to capture the flag, we have to POST the missing data while making HTTP request. 

To begin with, I started examine the webpage through ```Inspect``` - right click the page and select ```Inspect```.

### Step 3: 
There we go. The hidden data could be seen in the ```html``` body, which is:

```username: admin | password: 71urlkufpsdnlkadsf``` 

<img src="post practice - 2.png">

### Step 4: 
I tried to send a POST request from ```curl``` command, with ```-d``` option which stands for data. 

The data was sent as ```username=admin& password=71urlkufpsdnlkadsf```. 

<img src="post practice - 3.png">

### Step 5: 
Got the flag! 

<img src="post practice - 4.png">

### Flag: 
```flag{p0st_d4t4_4ll_d4y}```

