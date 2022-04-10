# Riyadh

## [CTFlearn Challenge](https://ctflearn.com/challenge/991)
<img src="riyadh - solved.png">

## Solutions
### Step 1: 
I first downloaded the ```.zip``` file and unzipped the file. 

### Step 2: 
I began with debugging ```Riyadh``` program file using ```gdb```, with  ```CTFlearn{flag}``` passed as the argument. 

<img src="riyadh - 1.png">

### Step 3: 
By running `start` and `disas` command, I noticed that there is a ```strcmp``` function at address ```0x80010e0```, which most probably compares two strings. 

<img src="riyadh - 2.png">

When I set a breakpoint at the address and re-ran the program, the program didn't break at the breakpoint, meaning that the function didn't execute. 

### Step 4: 
There's also another function called ```strlen```, which computes the length of a string. 

<img src="riyadh - 3.png">

Below ```strlen``` function, the value stored in ```rax``` is compared with ```0x1e```. I guessed that ```0x1e``` would most probably be the length of the valid flag. 

### Step 5: 
Hence, I set another breakpoint at the address at ```0x0000000008001170```, where the function is called in the main. The point of the breakpoint was to allow me to examine the changes of values stored in the registers. 

<img src="riyadh - 4.png">
<img src="riyadh - 5.png">

## Step 6: 
```0x1e``` equals to 30 in decimal form (converted using [this tool](https://www.rapidtables.com/convert/number/hex-to-decimal.html)). 

<img src="riyadh - 6.png">

This tells that the length of the flag is 30. 

### Step 7: 
Since we have known the length of the flag, this time we can passed in a different argument which has length 30. 
<img src="riyadh - 7.png">

### Step 8: 
After passed the length check, I tried to extract the flag from ```_Z4Msg5PC``` function. 

<img src="riyadh - 8.png">

The reason that I thought the flag might be inside this function is that the function was not executed previously when the length checked was not passed. 

However, when the length check was passed, the program broke at the function address - ```0x8001192```. 

<img src="riyadh - 9.png">

### Step 9: 
By navigating the function through ```s```, I was able to capture the flag. 

<img src="riyadh - 10.png">

### Flag: 
```CTFlearn{Masmak_Fortress_1865}```