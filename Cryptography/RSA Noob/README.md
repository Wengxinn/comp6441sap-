# RSA Noob

## [CTFlearn Challenge](https://ctflearn.com/challenge/120)
<img src="rsanoob - solved.png">

## Solutions
### Step 1:
I first downloaded te file and renamed it as ```rsanoob - task.txt```. 

### Step 2: 
Inside the text file, we are given ```public key e```, ```ciphertext c``` and ```n```. 
```
e: 1
c:9327565722767258308650643213344542404592011161659991421
n: 245841236512478852752909734912575581815967630033049838269083
```

Since the numbers given are extremly large, it wouldn't make sense to compute the RSA manually by hand. 

Therefore, I wrote a simple python script to decrypt the cipher. The script was named as ```rsanoob - script.py```

### Step 3: 
I actually tried to write a function in python to prime factorise a number. Unfortunately, the runtime took longer than what I expected due to extremely huge numbers, hence I directly factorised ```n``` through an [online factorisation tool](http://factordb.com/) to get ```p``` and ```q```, which are the prime factors of ```n```. 

<img src="rsanoob - 1.png">

```
# Factorise n to 2 primes,  p and q  (http://factordb.com/)
p = 416064700201658306196320137931
q = 590872612825179551336102196593
```

### Step 4: 
I computed the Euler's totient- ```phi of n``` as well as the ```private key d```. 
```
# Find Euler's totient
phi = (p-1) * (q-1)

# Find private key, d - inverse of e (mod  n)
# pow function take base e, inverse exp (for inverse) and modulo
d = pow(e, -1, phi)
```

### Step 5: 
The ciphertext can be decrypted by using ```c ** d mod n```. 
```
# Decrypt message - c ** d mod n
m = (c ** d) % n
print(m)
```

<img src="rsanoob - 2.png">

### Step 6: 
The program output the message as long types. However, the correct flag should be converted to bytes. 

Since I was lazy to install a new python package, I decided to just decode the cipher through an [online decoder](https://www.dcode.fr/rsa-cipher). 

<img src="rsanoob - 3.png">

### Flag: 
```abctf{b3tter_up_y0ur_e}```

## End Note: 
Actually I could just straightaway use the decoder from the beginning HAHAHA... But anyways, writing a decryption script is still useful - refresh my memory and make it as an exercise for exam!