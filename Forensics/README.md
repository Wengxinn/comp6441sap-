# Forensics

Forensics in CTF involved the process of recovering the digital trail left on a computer. These kind of challenges require us to examine and process a hidden piece of information in data files. 

## Summary
1. ```exiftool``` - extract the metadata of the data
2. ```strings``` - print out all the strings embedded in the data 
3. ```Base64 decode``` - some of the data has been encoded in Base64 format
4. ```XOR``` - the flag is the result of XOR
5. ```Steganography``` - extract hidden files embedded in the data
    - ```binwalk``` command
    - [CyberChef](https://gchq.github.io/CyberChef)
6. ```Hex editors``` - examine the data with hex editors as some flags could be hidden in hex dumps
    - ```HxD```
    - ```hexedit``` command
    - ```xxd``` command for hex dumps
7. ```Dimensions``` - sometimes the flags may be hidden outside the image so we have to modify the dimension of the image