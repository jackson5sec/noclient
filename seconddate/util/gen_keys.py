import nacl.public
import binascii
from base64 import urlsafe_b64encode, urlsafe_b64decode


def generate_keys():
    private_key = nacl.public.PrivateKey.generate()
    public_key = private_key.public_key

    private_key_hex = binascii.hexlify(private_key.encode()).decode().upper()
    public_key_hex = binascii.hexlify(public_key.encode()).decode().upper()

    return private_key_hex, public_key_hex


def encrypt(public_key, plaintext):
    public_key = nacl.public.PublicKey(public_key)
    box = nacl.public.SealedBox(public_key)
    ciphertext = box.encrypt(plaintext.encode())
    return ciphertext


def decrypt(private_key, ciphertext):
    private_key = nacl.public.PrivateKey(private_key)
    box = nacl.public.SealedBox(private_key)
    decrypted = box.decrypt(ciphertext)
    return decrypted.decode()


def main():
    private_key_hex, public_key_hex = generate_keys()

    print("Private Key Hex:")
    print(private_key_hex)

    print("\nPublic Key Hex:")
    print(public_key_hex)

    plaintext = "verify text yo"

    encrypted_data = encrypt(bytes.fromhex(public_key_hex), plaintext)

    print("Encrypted Data:")
    print(urlsafe_b64encode(encrypted_data).decode())

    # Decrypt the ciphertext using the private key
    decrypted_text = decrypt(bytes.fromhex(private_key_hex), encrypted_data)

    print("\nDecrypted Message:")
    print(decrypted_text)


if __name__ == "__main__":
    main()
