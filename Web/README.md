# Web

Web exploitation in CTF involves the process of exploiting bugs in webs to obtain the hidden information. 

## Summary
1. ```SQL injection``` - a code injection techniqe to gain access to the database 
   - through ```queries``` that an application makes to its database
    - make the queries to always be ```True``` so that it returns every records in the table
    - ```1 = 1``` - always True
    - ```UNION``` attacks
2. ```Inspect``` - inspect the browser source code 
   - ```Properties``` - ```Inspect``` to find the hidden data
   - ```HTTP request``` - make POST request with the hidden information found
   - ```HTTP header``` - some hints may be related to the information of HTTP header
   - Useful developer tools and command: 
     - ```curl``` command
     - ```Burp Suite```