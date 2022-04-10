# Basic Android RE 1

## [CTFlearn Challenge](https://ctflearn.com/challenge/962)
<img src="basic android - solved.png">

## Solutions
### Step 1: 
First, I downloaded the ```.apk``` file and renamed it as ```basic android - task.apk```. 

### Step 2: 
I used an [online apk file decompiler](https://www.decompiler.com/) to decompile it into a ```.zip``` file. 

<img src="basic android - 1.png">

**Note:** Due to the extremely large file sizes, I extracted files from the ZIP file by using another [online tool](https://zipextractor.app/). The extracted files were stored in my Google Drive instead of my local storage. 

### Step 3: 
For this kind of challenge, we would usually start by looking for ```Main Activity```. By opening ```AndroidManifest.xml```, I was able to locate the file named ```MainActivity```.

```location: /sources/com/example/secondapp/MainActivity.java```

<img src="basic android - 2.png">

### Step 4: 
In ```submitPassword(View view)```, I was able to find information related to the flag (based on ```CTFlearn{```). 
<img src="basic android - 3.png">

Variable ```editText``` stores relevant information about the targeted flag. So basically, if the MD5 hash of ```editText``` is equal to ```b74dec4f39d35b6a2e6c48e637c8aedb```, ```editText``` is the flag. 

<img src="basic android - 4.png">
<img src="basic android - 5.png">

### Step 5: 
We have to decode the MD5 hash, ```b74dec4f39d35b6a2e6c48e637c8aedb```. Here, I used an [online MD5 Decryption tool](https://www.md5online.org/md5-decrypt.html). 

<img src="basic android - 6.png">

### Step 6: 
I got the complete flag by concatenating ```Spring2019``` with the string specified in ```submitPassword(View view)```. 

### Flag: 
```CTFlearn{Spring2019_is_not_secure!}```
