# **Lab 10 Report**  
##### CSCY 4742 – Cybersecurity Programming and Analytics, Spring 2026

**Name & Student ID**: John Paul Bennett Jr., 110412273  

---

# **Task 1: RSA Key Generation**

## 🔹 Screenshots:
- [x] Terminal output: `RSA keys generated for Alice and Bob.

![Screenshot 1](/Lab10/Screenshots/Task_1_RSA_Key_Terminal_Output.png)

- [x] Created files: `alice_priv.pem`, `alice_pub.pem`, `bob_priv.pem`, `bob_pub.pem`

![Screenshot 2](/Lab10/Screenshots/Task_1_RSA_Key_Files.png)

## 🔹 Questions:
1. What does the `default_backend()` do?
- The `default_backend()` function provides a trusted cryptographic engine that handles low-level operations securely and efficiently.
 
2. Why use a library for key generation rather than writing our own algorithm?
- Using a library avoids mistakes and vulnerabilities that often occur in custom-built cryptographic algorithms.

3. What is the role of the public exponent (65537)?
- The public exponent (65537) balances security and performance, being large enough to prevent attacks but efficient for computation.

4. What are the trade-offs of using larger vs. smaller key sizes?
- Larger key sizes increase security but slow down performance, while smaller keys are faster but more vulnerable to attacks.

5. Why are private keys usually stored in PEM format?
- Private keys are stored in PEM format because it is a standardized, portable, and widely supported text-based encoding.

6. What are the risks of not encrypting private key files?
- Not encrypting private key files risks unauthorized access, leading to identity theft or decryption of sensitive data.

7. Why can public keys be shared openly?
- Public keys can be shared openly because they cannot be used to derive the private key.

8. What format is `SubjectPublicKeyInfo`, and why do we use it?
- `SubjectPublicKeyInfo` is an ASN.1 structure that standardizes how public keys and their algorithms are represented.

9. Why do Alice and Bob each need their own key pair?
- Alice and Bob each need their own key pair to securely exchange messages and verify identities independently.

10. Can one key pair be reused for both parties?
- One key pair should not be reused for both parties, as it breaks the principle of separate identities and reduces security.

---

# **Task 2: Sender Encryption Pipeline**

## 🔹 Screenshots:
- [x] Terminal output showing AES, HMAC keys and IV
![Screenshot 3](/Lab10/Screenshots/Task_2_Keys_and_IV.png)

- [x] Output of digital signature  
![Screenshot 4](/Lab10/Screenshots/Task_2_Signature_output.png)

- [x] Encrypted keys file saved  
![Screenshot 5](/Lab10/Screenshots/Task_2_Saved_Encrypted_Keys_File.png)

- [x] Encrypted message file saved  
![Screenshot 6](/Lab10/Screenshots/Task_2_Saved_Encrypted_Message_File.png)

- [x] HMAC file saved  
![Screenshot 7](/Lab10/Screenshots/Task_2_HMAC_File.png)

## 🔹 Questions:
1. Why should new keys be generated for each session?
- New keys per session ensure forward secrecy and limit damage if a key is compromised.

2. What role does the IV play in CTR mode encryption?  
- The IV in CTR mode provides uniqueness so identical plaintexts produce different ciphertexts.

3. Why we generate a separate key for AES (encryption) and HMAC?  
- Separate keys prevent cross-protocol attacks and isolate encryption from integrity functions.

4. What is Alice proving by signing the keys?  
- Alice is proving authenticity and ownership of the keys.

5. What would happen if we didn’t sign the keys?  
- Without signatures, an attacker could substitute their own keys (man-in-the-middle).

6. Why does RSA use PSS padding for signatures and OAEP padding for encryption? What security properties does each padding scheme provide, and why are they not interchangeable?  
- RSA uses PSS for signatures (secure randomness, forgery resistance) and OAEP for encryption (semantic security); they serve different security goals and aren’t interchangeable.

7. Why is Bob’s public key used here?  
- Bob’s public key is used so only Bob can decrypt with his private key.

8. What protection does this provide over just storing the keys locally?  
- It protects keys in transit and ensures only the intended recipient can access them.

9. What is the difference between using RSA for encryption and for digital signing? Which key is used in each case, and why?  
- Encryption uses the recipient’s public key to ensure confidentiality; signing uses the sender’s private key to ensure authenticity.

10. Why is padding required before encrypting with RSA? What risks arise if we encrypt raw data without padding?  
- Padding adds randomness and structure; without it, RSA is deterministic and vulnerable to attacks.

11. What is OAEP padding, and how does it work? How does it differ from PSS padding, and why is each suited for its specific purpose (encryption vs. signing)?  
- OAEP randomizes plaintext for secure encryption; PSS randomizes signatures for unforgeability—each is tailored to its role.

12. Why is AES used to encrypt the message instead of RSA?  
- AES is faster and more efficient for large data, while RSA is slow and used mainly for key exchange.

13. Why do we add the sender name and timestamp?  
- They provide context, freshness, and help prevent replay attacks.

14. Why do we generate the HMAC *after* encryption?  
- HMAC is computed after encryption to protect the ciphertext’s integrity (encrypt-then-MAC).

15. What would happen if the encrypted message were changed in transit?  
- The HMAC verification would fail, revealing tampering.

16. Why must the HMAC use a separate key from the AES encryption key? What could go wrong if the same key were reused for both encryption and integrity?  
- Reusing the same key could leak information or enable attacks that break confidentiality or integrity.

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
- [x] Output: successful verification
- [x] Output: HMAC failure
- [x] Output: signature failure

### Step 1: Test the Correct (Expected) Case
![Successful Verification](/Lab10/Screenshots/task3_receiver_success.png)

### Step 2: Simulate Message Tampering (HMAC Failure)
![HMAC Failure](/Lab10/Screenshots/task4_hmac_fail.png)

### Step 3: Simulate Signature Forgery (Wrong Public Key)
![Signature Failure](/Lab10/Screenshots/task4_signature_fail.png)

---

## 🔹 Questions:
1. What role does the HMAC play in this process?  
**Answer:** It ensures message integrity, confirming that the ciphertext was not altered, corrupted, or tampered with while in transit.

2. What is the digital signature verifying?  
**Answer:** It verifies the authenticity and non-repudiation of the message. It mathematically proves that the owner of Alice's private key generated the session keys.

3. Why is HMAC verification done before decryption?  
**Answer:** It guarantees the data is safe to process. Decrypting tampered ciphertext can lead to unhandled exceptions, resource exhaustion, or cryptographic padding oracle attacks.

4. What would happen if Bob skipped this check?  
**Answer:** Bob would process potentially malicious or malformed data, resulting in garbage output and breaking the trust model of the communication channel.

5. Why combine symmetric (AES) and asymmetric (RSA) encryption instead of just using RSA for everything?  
**Answer:** RSA is slow and computationally expensive, with strict limits on the size of the data it can encrypt. AES is incredibly fast and can encrypt massive files. Hybrid encryption uses the security of RSA to safely share the keys, and the speed of AES to handle the actual data.

6. Why do we use digital signatures (signing with RSA) if we already use HMAC for integrity?  
**Answer:** HMAC relies on a shared symmetric key, meaning either Alice or Bob could have generated the HMAC (lacking non-repudiation). A digital signature uses a private key that only Alice has, proving indisputably that she sent it.

7. Why are session keys (AES/HMAC/IV) randomly generated for each message instead of reused?  
**Answer:** Random generation provides perfect forward secrecy. If an attacker compromises a single session key, they only gain access to that specific message, not the entire history of communications. It also prevents replay attacks.

8. Why do we encrypt the keys, and not the entire message, using RSA?  
**Answer:** Encrypting large datasets with RSA is incredibly slow and constrained by the RSA key size limit. Encrypting just the small session key bundle is highly efficient and leaves the heavy lifting to AES.

9. How does adding a timestamp improve the security of the message? What are replay attacks?  
**Answer:** A replay attack occurs when an adversary intercepts a valid, encrypted message and maliciously re-transmits it later to duplicate an action. A timestamp allows the receiver to check the message's age and reject it if it is too old.

10. What threat would be harder to detect if the signature was placed on the full message rather than just the key materials?  
**Answer:** If only the message ciphertext is signed, an attacker who compromises the session keys could potentially separate the payload, encrypt a new message, and cause confusion. Signing the key material tightly binds the cryptographic parameters of that specific session to Alice's identity.

11. How does separating encryption (AES) from integrity (HMAC) help modularize cryptographic responsibilities?  
**Answer:** It allows the system to follow the principle of separation of concerns. If a vulnerability is discovered in the hashing algorithm (HMAC), it can be swapped out independently without having to re-architect the AES encryption implementation.
