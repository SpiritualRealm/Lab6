from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def generate_rsa_keypair(person):
	private_key = rsa.generate_private_key(
		public_exponent=65537,
		key_size=2048,
		backend=default_backend()
	)
	public_key = private_key.public_key()
	
	with open(f"{person}_priv.pem", 'wb') as f:
		f.write(private_key.private_bytes(
			encoding=serialization.Encoding.PEM,
			format=serialization.PrivateFormat.TraditionalOpenSSL,
			encryption_algorithm=serialization.NoEncryption()
		))
	
	with open(f"{person}_pub.pem", 'wb') as f:
		f.write(public_key.public_bytes(
			encoding=serialization.Encoding.PEM,
			format=serialization.PublicFormat.SubjectPublicKeyInfo
		))

generate_rsa_keypair('alice')
generate_rsa_keypair('bob')

print("RSA keys generated for Alice and Bob.")
