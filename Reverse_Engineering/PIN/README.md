# PIN

## [CTFlearn Challenge](https://ctflearn.com/challenge/379)
<img src="pin - solved.png">

## Solutions
### Step 1: 
After downloading the program file, I renamed it as ```pin - task```. 

### Step 2: 
First, I debugged the file using ```gdb``` command. 
<img src="pin - 1.png">

### Step 3: 
When I ran the program, it prompted for user input (PIN). I randomly input a 4-digit pin - ```0000```. 
<img src="pin - 2.png">

The pin was incorrect (as expected) so I proceeded to start debugging. 

### Step 4: 
I used ```disas``` for ```gbd-peda``` to diassemble the program. I noticed there is a function called ```cek```, which I assumed it checks the user input (from ```scanf``` function) with some pre-definined values. 

<img src="pin - 3.png">

### Step 5: 
Hence, I set a ```breakpoint``` at the function address, which is ```0x4005b6```.  

<img src="pin - 4.png">

### Step 6: 
Using `s` to navigate through the new program, I found an interesting line - ```0x4005c3 <cek+12>```, which compares some values stored in the registers.  

<img src="pin - 6.png">

### Step 7: 
Above the line, I noticed that the valid pin was moved (in line ```0x4005bd<cek+7>```). 

<img src="pin - 7.png">

### Step 8: 
When executing this line, I noticed that ```RAX``` value changed, which means the valid pin was stored in RAX.

<img src="pin - 8.png">

### Step 9: 
Since the value was stored as hexadecimal form, converting it to decimal using an [online tool](https://www.rapidtables.com/convert/number/hex-to-decimal.html) gave me the correct pin. 

<img src="pin - 9.png">

### Flag (PIN): 
333333
