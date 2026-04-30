from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import utils
import base64


def load_rsa_key(filename, is_private=False):
    with open(filename, 'rb') as f:
        key_data = f.read()
    if is_private:
        return serialization.load_pem_private_key(key_data, password=None, backend=default_backend())
    else:
        return serialization.load_pem_public_key(key_data, backend=default_backend())


def main():
    # Load public key of Alice (for verification) and private key of Bob (for decryption)
    alice_pub_key = load_rsa_key("alice_pub.pem")
    bob_priv_key = load_rsa_key("bob_priv.pem", is_private=True)

    # Load encrypted files from disk
    with open("encrypted_keys.bin", "rb") as f:
        encrypted_keys = f.read()
    with open("encrypted_message.bin", "rb") as f:
        encrypted_message = f.read()
    with open("hmac.bin", "rb") as f:
        received_hmac = f.read()

    print("✅ Loaded all required keys and encrypted files.")

    decrypted_keys = bob_priv_key.decrypt(
        encrypted_keys,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    AES_key = decrypted_keys[:32]
    HMAC_key = decrypted_keys[32:64]
    iv = decrypted_keys[64:]

    print("✅ Session keys decrypted.")


    h = HMAC(HMAC_key, hashes.SHA256(), backend=default_backend())
    h.update(encrypted_message)

    try:
        h.verify(received_hmac)
        print("✅ HMAC verification succeeded.")
    except InvalidSignature:
        print("❌ HMAC verification failed. Message integrity compromised.")
        exit(1)

    cipher = Cipher(algorithms.AES(AES_key), modes.CTR(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()

    print("✅ Message decrypted.")

    sender, message, timestamp, signature = decrypted_message.rsplit(b'\n', 3)

    print("Sender:", sender.decode())
    print("Timestamp:", timestamp.decode())
    print("Message:", message.decode())


    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(AES_key + HMAC_key + iv)
    hashed_keys = digest.finalize()

    try:
        alice_pub_key.verify(
            base64.b64decode(signature),
            hashed_keys,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            utils.Prehashed(hashes.SHA256())
        )
        print("✅ Signature verification succeeded.")
    except InvalidSignature:
        print("❌ Signature verification failed. Sender not authenticated.")
        exit(1)


if __name__ == "__main__":
    main()