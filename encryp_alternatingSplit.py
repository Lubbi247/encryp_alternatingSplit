def encrypt(text,n):   ## this function repeat encrypt_once n times for n> 1. 
  if ( n <= 0 or not text): return text
  if ( n == 1): return text[1::2]+text[::2]
  s=[text]  
  for i in range(1,n+1):
    s.append(encrypt_once(s[i-1]))      
  return s[n]

def decrypt(text,n):
  if ( n <= 0 or not text): return text
  s=[text]  
  for i in range(1,n+1):
    s.append(decrypt_once(s[i-1]))      
  return s[n]

def encrypt_once(text):  
  oddString , evenString = text[::2], text[1::2]
  return evenString+oddString


def decrypt_once(text):  
  decry_one=""
  decry_two=""
  mid=int(len(text)/2)   ##find mid index
  decry_one += text[0:mid]    ## breaks string into two strings
  decry_two += text[mid:]
  s=""
  
  for i in range(0,mid):
    s += decry_two[i]+decry_one[i]  ## combine alternating even and odd indices    

  if len(text)%2!=0:
    s += decry_two[mid]  ## if length is odd , add the last index of decry_two
  
  return s

print(encrypt("This is a test!",1))
print(decrypt("This is a test!",-5))
print(encrypt("This is a test!",-1))
print(decrypt("s eT ashi tist!",5))
