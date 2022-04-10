# Reykjavik

## [CTFlearn Challenge](https://ctflearn.com/challenge/990)
<img src="reykjavik - solved.png">

## Solutions
### Step 1: 
First, I downloaded the compressed file and extracted all the files. 

### Step 2: 
For this kind of challenge, I would start by debugging the program using ```gdb``` command. 

<img src="reykjavik - 1.png">

Note that we are debugging the program in this case, so we are expecting the program to run into errors (in this case, it means the flag is incorrect). 

Consequently, ```CTFlearn{flag}``` (which I expected it to be the false flag) was passed in as the argument to run ```Reykjavik program```. 

<img src="reykjavik - 2.png">

### Step 3: 
Since I have pre-installed the enhanced environment, ```gdb-peda```, I could use ```start``` command to display the disassembly codes, register, etc. 

<img src="reykjavik - 3.png">

### Step 4: 
I examined the diassembly codes by navigating through the program via ```ni``` command, until I found the flag.  

<img src="reykjavik - 4.png"> 
<img src="reykjavik - 5.png">

### Flag: 
```CTFlearn{Eye_L0ve_Iceland_}```

## End Notes
This was my first reversing challenge and it is so useful because it equipped me with all  knowlegde requires for later challenges such as Riyadh, Rangoon and PIN since all of them assume basic knowlegde about assembler and ```gdb```. I was stuck for so long because I was not familiar with ```gdb``` debugging zzz...