# RSA-Decryption-Tool
Python3 Tool that helps decrypt RSA encryption.  

In order to work c, n, and e variables must be known.  

This tool was developed in order to solve PicoCTF's "Mind Your P's and Q's" challenge.  
My official write-up in my PicoCTF repo provides more details and images on how to use this program.  
c, n, e, p, and q values for the PicoCTF challenge are hard-coded into the program but can be changed.  

This code is not my own, but has been used in many similar RSA decryption challenge write-ups.  
Credit cannot be pinned to an original source, but here is the source I used: https://www.youtube.com/watch?v=_lg2AEqRTjg    
I changed the last line of code to convert deciphered hex to plaintext.  

To use:  
1) Hard-code c, n, and e variables into the program.  
2) Use an online web-tool to decipher the p and q values from n.  
3) Hard-code the p and q values into the program.  
4) Running the prgram will generate the plaintext.   

To learn more about RSA encryption go to page 6: https://picoctf.org/learning_guides/Book-2-Cryptography.pdf
