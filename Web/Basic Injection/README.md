# Basic Injection

## [CTFlearn Challenge](https://ctflearn.com/challenge/88)
<img src="basic injection - solved.png">

## Solutions
### Step 1:
The link specified in the question brought me to a website ```You know what to do```. 

### Step 2: 
The aim of the question is to test understanding on basic SQL injection. 

Here what we got: 

```Original Query: SELCT * FROM webfour.webfour where name = '$input'```

We have to fill in ```$input``` to make a complete query so that the query leaks the whole database. 

### Step 2: 
From my own understanding of SQL injection, I could enter anything as name. I entered ```hi``` in this case. But this may not work because there may be no person whose name is ```hi```. Even there is, this SQL statement still couldn't leak the whole database. 

### Step 3: 
I proceeded to add ```1 = 1``` to make the statement ```TRUE```.

```Your Resulting Query: SELCT * FROM webfour.webfour where name = 'hi' or '1' = '1'```

### Step 4: 
```Input: hi' or '1' = '1``` 

Be careful of the format of the input, especially the single quotes. 

### Step 5: 
After I submitted the input, the whole database leaked and the flag was shown somewhere in the output. 

The reason works behind this is that the SQL statement will always equate to True because 1 will always equal to 1 no matter what. Therefore, this statement returns every row in the database. 

<img src="basic injection - 1.png">
<img src="basic injection - 2.png">

### Flag: 
```CTFlearn{th4t_is_why_you_n33d_to_sanitiz3_inputs}```

## End Notes
Did my first ever SQL Injection... It's really interesting how a small change to the SQL statement can leak the whole database. Nothing is secured at this point.