# Cryptography

## Reading
[Encryption, Decryption, & Hacking](https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:online-data-security/xcae6f4a7ff015e7d:data-encryption-techniques/a/encryption-decryption-and-code-cracking)
- Encrypting a message
  - scrambles message content
  - caesar cipher shifts letters in alphabet

- decrypting
  - frequency analysis
    - some letters are used more than others in human languages
  - known plaintext
    - if some part of the message is known 
  - brute force
    - all possible shifts tried

[Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
- replaces each letter of the alphabet with a different letter shifted by a certain amount
- crack with frequency distro or brute force

## Videos
[Cryptography Crash Course](https://www.youtube.com/watch?v=jhXCTbFnK8o)
- typical defense in depth
  - layered defenses
- cryptography
  - cipher
    - algo to make text secret message
    - Substitution cipher
      - letter frequencies are preserved
    - columnar cryptography
      - 5x5 grid mapped through vertically left-right bottom -top
    - data encryption standard
      - nsa and ibm
    - advanced encryption standard
      - 128bit key: trillions of years to brute force
        - chops data into 16-byte blocks
        - applies series of substitutions and permutations, based on key value, plus some other ops to obscure message, repeated ten+ times
      - wpa2, iphone, etc
  - key exchange
    - two computers agree on a key without sharing it
    - public paint, two secrets sent 
    - one-way math works the same way
  - diffie - hellman
    - modular exponentiation
  - asymmetric encryption
    - lockbox sent to and from 
    - RSA
      - identity verification



## Additional Resources
[Introduction to Cryptography](https://thebestvpn.com/cryptography/)

[How Computers Generate Random Numbers](https://www.howtogeek.com/183051/htg-explains-how-computers-generate-random-numbers/)

## Things I'd like to know more about
- what sort of functionality is out there to make encryption convenient for novice coders??