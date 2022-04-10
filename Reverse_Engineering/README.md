# Reverse Engineering

The idea works behind reverse engineering is that we attempt to understand the pre-defined deductive process and reasonings of a program. Most of the CTF challenges involve process of converting compiled programs (in machine code) back to more human-readable format. 

## Summary 
1. ```Program script``` - given a script, try to analyse the logic and reverse it
   - first look for functions that ```return or print the flag```
   - from that, reverse back to see the previous process
2. ```gdb``` - debug a program to catch the flag
   - ```gdb-peda``` - enhanced enviroment of ```gdb``` to ease the debugging process
   - ```assembler knowledge``` - register, address, memory
   - ```cmp``` - always look for ```cmp``` code or ```functions that compare two values``` since they may be comparing the user input with the correct flag
   - ```ni``` or ```s``` to navigate through the program
   - ```b``` - set breakpoints so that the program will break at the address 