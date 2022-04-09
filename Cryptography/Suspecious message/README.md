# Suspecious message

## [CTFlearn Challenge](https://ctflearn.com/challenge/887)
<img src="suspecious message - solved.png">

## Solutions
### Step 1:
First, I downloaded the given photo and renamed it as ```suspecious message - algo.png```. 

<img src="suspecious message - algo.png">

Looking at this picture, I could immediately tell this is a ```Playfair Cipher```, since I have learned that from one of the weekly module. 

### Step 2: 
To decipher, we need to split the ciphertext into pairs of letters (ignoring non-alphabetical characters). 

For each pair: 
- If they are in the same row, the corresponding plaintext characters are their left characters (warpping arround).
- If they are in the same column, the corresponding plaintext characters are their above characters (warpping arround).
- If they are in diagonal, the corresponding plaintext characters are their opposite direction of the diagonal. 


### Flag: 
```CTFlearn{Pl4Yf41R_1S_C00l_c1PheRrRR}```
