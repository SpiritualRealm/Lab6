# Inclusion of Libraries
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding, utils
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.hmac import HMAC
import time
import base64
import os

AES_key = os.urandom(32)    # AES-256
HMAC_key = os.urandom(32)   # HMAC-SHA256
iv = os.urandom(16)         # AES CTR IV


print("AES Key:", AES_key.hex())
print("HMAC Key:", HMAC_key.hex())
print("IV:", iv.hex())


# Function for loading the private key
def load_private_key(path):
	with open(path, 'rb') as f:
		return serialization.load_pem_private_key(f.read(), None)

# Variable to call the load_private_key() function
alice_priv = load_private_key("alice_priv.pem")


digest = hashes.Hash(hashes.SHA256())
digest.update(AES_key + HMAC_key + iv)
hashed = digest.finalize()

# Signature of Alice's private key
signature = alice_priv.sign(
	hashed,
	padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
	utils.Prehashed(hashes.SHA256())
)

# Print the signature
print("Signature:", signature.hex())

# Function for loading the public key
def load_public_key(path):
	with open(path, 'rb') as f:
		return serialization.load_pem_public_key(f.read())

# Variables to load public key and combine AES_key, HMAC_key and iv
bob_pub = load_public_key("bob_pub.pem")
combined_keys = AES_key + HMAC_key + iv

# Variable for encrypted keys
encrypted_keys = bob_pub.encrypt(
	combined_keys,
	padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

# Create encrypted key bundle
with open("encrypted_keys.bin", "wb") as f:
	f.write(encrypted_keys)


# Print message showing that encrypted key bundle has been saved
print("Encrypted key bundle saved.")

with open("secret.txt", "rb") as f:
	file_data = f.read()

# Sender variable
sender = b'Alice'
timestamp = str(int(time.time())).encode()

msg = sender + b'\n' + file_data + b'\n' + timestamp + b'\n' + base64.b64encode(signature)

cipher = Cipher(algorithms.AES(AES_key), modes.CTR(iv))
encryptor = cipher.encryptor()
encrypted_msg = encryptor.update(msg) + encryptor.finalize()

with open("encrypted_message.bin", "wb") as f:
	f.write(encrypted_msg)

# Message that indicates the encrypted message is saved.
print("Encrypted message saved.")


h = HMAC(HMAC_key, hashes.SHA256())
h.update(encrypted_msg)
hmac_val = h.finalize()


with open("hmac.bin", "wb") as f:
	f.write(hmac_val)

# Message indicating HMAC was saved.
print("HMAC saved.")
