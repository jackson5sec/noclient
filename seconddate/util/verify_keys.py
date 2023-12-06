
import nacl.secret
import nacl.utils
from base64 import urlsafe_b64encode, urlsafe_b64decode

# Replace with your hardcoded private key as an uppercase hex string
PRIVATE_KEY_HEX = "1DB3E967438E6B2D656325713C4C1823CE4438B2AFB6E75F932C092EB29539AF"
# Replace with your hardcoded public key as an uppercase hex string
PUBLIC_KEY_HEX = "40B9A214763487D4C3486D46440216D171A13355BE03A207CBACC700C1066E5D"

# Replace with your hardcoded private key as an uppercase hex string
#PRIVATE_KEY_HEX = "39CA7E13B8CAB401146F1DA3B0DAE7D207E4069B28B35F38D13926ABB41D91ED"
# Replace with your hardcoded public key as an uppercase hex string
#PUBLIC_KEY_HEX = "02B644817C8BD9B8EFB2E59A1967FB0EB02AC6828571644ED7A246D4EAD03E36"



def generate_key():
    return bytes.fromhex(PRIVATE_KEY_HEX)

def encrypt(key, plaintext):
    box = nacl.secret.SecretBox(key)
    nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
    ciphertext = box.encrypt(plaintext.encode(), nonce)
    return ciphertext

def decrypt(key, ciphertext):
    box = nacl.secret.SecretBox(key)
    decrypted = box.decrypt(ciphertext)
    return decrypted.decode()

if __name__ == "__main__":
    # Generate the key from the hardcoded private key
    key = generate_key()

    plaintext = "verify this text yo"

    # Encrypt the plaintext
    encrypted_data = encrypt(key, plaintext)

    print("Encrypted Data:")
    print(urlsafe_b64encode(encrypted_data).decode())

    # Decrypt the ciphertext
    decrypted_text = decrypt(key, encrypted_data)
    print("\nDecrypted Message:")
    print(decrypted_text)
