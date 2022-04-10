# Rangoon

## [CTFlearn Challenge](https://ctflearn.com/challenge/994)
<img src="rangoon - solved.png">

## Solutions
### Step 1: 
Same as before, I first downloaded the ```.zip``` file and unzipped the file. 

### Step 2: 
I passed in the incorrect flag, ```CTFlearn{flag}``` as the argument to debug the program file named as ```Rangoon```. 

<img src="rangoon - 1.png">

### Step 3: 
Whe I ran the program, as expected, ```CTFlearn{flag}``` is the wrong flag. 

<img src="rangoon - 2.png">

### Step 4: 
I started to learn and examine the assembler code of this program. I would always pay more attention to  ```cmp``` command as well as functions that compare two strings or numbers such as ```strcmp```. 

<img src="rangoon - 3.png">

There we go. I noticed a ```strcmp``` function.

### Step 5: 
I set a breakpoint at the address where the function is called in ```main``` and then re-ran the program. 

<img src="rangoon - 4.png">

As we can see, the function was not executed. This means that the program ends before it reached ```strcmp```.  

### Step  5: 
Based on previous experience on Riyadh challenge, this happened because the argument didn't pass the length check.  

There is a ```cmp``` command at line ```0x00000000080012ea <+426>```. I reckoned that ```0x1c``` could be the valid length. 

<img src="rangoon - 5.png">

### Step 6: 
Using a [Hexadecimal to Decimal converter](https://www.rapidtables.com/convert/number/hex-to-decimal.html), ```0x1c``` is converted to decimal as 28. 

<img src="rangoon - 6.png">

### Step 7: 
I passed in a new argument with length 28 while running ```gdb```. 

<img src="rangoon - 7.png">

### Step 8: 
I set a breakpoint at address where ```strcmp``` was called in ```main``` and ran the program again (same as ```Step 5).

<img src="rangoon - 8.png">

### Step 9: 
This time, the function was executed and broke at the breakpoint. No further steps were needed because the flag just appeared! YAY!

<img src="rangoon - 9.png">

### Flag: 
```CTFlearn{Princess_Maha_Devi}```