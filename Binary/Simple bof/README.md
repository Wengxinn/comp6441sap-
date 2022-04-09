# Simple bof

## [CTFlearn Challenge](https://ctflearn.com/challenge/1010)
<img src="simple bof - solved.png">

## Solutions
### Step 1:
I downloaded the ```.c``` file and connected to the server through the command line ```nc thekidofarcrania.com 35235```. 

<img src="simple bof - 1.png">

### Step 2: 
The program output the memory representation of a ```stack``` of the ```.c``` file. This tells me that the challenge would most probably involve buffer overflows, in which data can be overwritten when the allocated space has been overflowed (excceeded). 

Based on ```vuln()``` in ```bof.c```, I could easily recognise the position of variables in the stack according to their order of execution. 

In the ```stack```, 
1. ```buff``` (32 bytes)
2. ```padding``` (16 bytes)
3. ```secret```
4. ```notsecret```

<img src="simple bof - 2.png">
<img src="simple bof - 3.png">
<img src="simple bof - 4.png">

```0xffed06e8: secret```

### Step 3: 
In order to exploit the flag, we have to overflow the ```secret```buffer. Thus, I first filled all the ```buff``` and ```padding``` buffers with `'_'`. This means I would need ```32 + 16 = 48``` underscores to overflow the buffer. 

<img src="simple bof - 7.png">
<img src="simple bof - 8.png">

### Step 4: 
As we can see from the message prompted in the command prompt, I successfully overflowed the ```secret``` value. Now I only have to overwrite the data. 

By examining ```bof.c```, I knew that the secret has to be ```0x67616c66``` in order for the program to print the flag. Thus, all I have to do was to overwrite the secret value with ```0x67616c66```.
```
 if (secret == 0x67616c66) {
    puts("You did it! Congratuations!");
    print_flag(); // Print out the flag. You deserve it.
```

Since the only way I could write data into the memory is through the user input ```Input some text:```, I had to convert ```0x67616c66``` to ASCII characters. 

```secret values: flag```

Hence, the complete input string would be:
```'_' * 48 + 'flag'```. 

<img src="simple bof - 9.png">
<img src="simple bof - 10.png">

### Flag: 
```CTFlearn{buffer_0verflows_4re_c00l!}```

## End Notes
Fantastic challenge for beginners like me! I have heard of buffer overflows for so many times but never really dived deeper into the topic. This challenge and the buffer representation helps me understand it perfectly. 

