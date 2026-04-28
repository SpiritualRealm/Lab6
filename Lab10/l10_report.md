# **Lab 10 Report**  
##### CSCY 4742 – Cybersecurity Programming and Analytics, Spring 2026

**Name & Student ID**: [Your Full Name], [Your Student ID]  

---

# **Task 1: RSA Key Generation**

## 🔹 Screenshots:
- [ ] Terminal output: `RSA keys generated for Alice and Bob.`
- [ ] Created files: `alice_priv.pem`, `alice_pub.pem`, `bob_priv.pem`, `bob_pub.pem`

## 🔹 Questions:
1. What does the `default_backend()` do?  
2. Why use a library for key generation rather than writing our own algorithm?  
3. What is the role of the public exponent (65537)?  
4. What are the trade-offs of using larger vs. smaller key sizes?  
5. Why are private keys usually stored in PEM format?  
6. What are the risks of not encrypting private key files?  
7. Why can public keys be shared openly?  
8. What format is `SubjectPublicKeyInfo`, and why do we use it?  
9. Why do Alice and Bob each need their own key pair?  
10. Can one key pair be reused for both parties?  

---

# **Task 2: Sender Encryption Pipeline**

## 🔹 Screenshots:
- [ ] Terminal output showing AES, HMAC keys and IV  
- [ ] Output of digital signature  
- [ ] Encrypted keys file saved  
- [ ] Encrypted message file saved  
- [ ] HMAC file saved  

## 🔹 Questions:
1. Why should new keys be generated for each session?  
2. What role does the IV play in CTR mode encryption?  
3. Why we generate a separate key for AES (encryption) and HMAC?  
4. What is Alice proving by signing the keys?  
5. What would happen if we didn’t sign the keys?  
6. Why does RSA use PSS padding for signatures and OAEP padding for encryption? What security properties does each padding scheme provide, and why are they not interchangeable?  
7. Why is Bob’s public key used here?  
8. What protection does this provide over just storing the keys locally?  
9. What is the difference between using RSA for encryption and for digital signing? Which key is used in each case, and why?  
10. Why is padding required before encrypting with RSA? What risks arise if we encrypt raw data without padding?  
11. What is OAEP padding, and how does it work? How does it differ from PSS padding, and why is each suited for its specific purpose (encryption vs. signing)?  
12. Why is AES used to encrypt the message instead of RSA?  
13. Why do we add the sender name and timestamp?  
14. Why do we generate the HMAC *after* encryption?  
15. What would happen if the encrypted message were changed in transit?  
16. Why must the HMAC use a separate key from the AES encryption key? What could go wrong if the same key were reused for both encryption and integrity?  

---

# **Task 3: Receiver Verification Pipeline**

## 🔹 Screenshots:
- [ ] File and key loading  
- [ ] Decrypted AES, HMAC, IV values  
- [ ] HMAC verification output  
- [ ] Decrypted message output  
- [ ] Parsed sender, timestamp, message  
- [ ] Digital signature verification output  

## 🔹 Questions:
1. Why does Bob need both Alice’s public key and his own private key?  
2. Why is it secure to share public keys, but not private keys?  
3. Why is Bob the only person who can decrypt the session keys?  
4. Why is the decrypted byte stream split into these three parts?  
5. Why is HMAC checked before decrypting the message?  
6. What would happen if we skipped HMAC verification?  
7. Why is AES-CTR used over other AES modes like CBC?  
8. What would happen if the IV used here didn’t match the sender’s IV?  
9. Why is `rsplit(..., 3)` used here?  
10. What are some risks of relying on `\n` as a delimiter?  
11. What is Alice signing, and why not the full message?  
12. Why is the digital signature the final check in the process?  

---

# **Task 4: Verification & Error Handling**

## 🔹 Screenshots:
- [ ] Output: successful verification  
- [ ] Output: HMAC failure  
- [ ] Output: signature failure  

## 🔹 Questions:
1. What role does the HMAC play in this process?  
2. What is the digital signature verifying?  
3. Why is HMAC verification done before decryption?  
4. What would happen if Bob skipped this check?  
5. Why combine symmetric (AES) and asymmetric (RSA) encryption instead of just using RSA for everything?  
6. Why do we use digital signatures (signing with RSA) if we already use HMAC for integrity?  
7. Why are session keys (AES/HMAC/IV) randomly generated for each message instead of reused?  
8. Why do we encrypt the keys, and not the entire message, using RSA?  
9. How does adding a timestamp improve the security of the message? What are replay attacks?  
10. What threat would be harder to detect if the signature was placed on the full message rather than just the key materials?  
11. How does separating encryption (AES) from integrity (HMAC) help modularize cryptographic responsibilities?  

