import matplotlib.pyplot as plt
from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size

    # Loop through each pixel
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            # Example encryption: add key to each RGB value
            encrypted_pixel = tuple((p + key) % 256 for p in pixel)
            img.putpixel((x, y), encrypted_pixel)

    encrypted_image_path = image_path.replace('.png', '_encrypted.png')
    img.save(encrypted_image_path)
    return encrypted_image_path

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size

    # Loop through each pixel
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            # Example decryption: subtract key from each RGB value
            decrypted_pixel = tuple((p - key) % 256 for p in pixel)
            img.putpixel((x, y), decrypted_pixel)

    decrypted_image_path = image_path.replace('_encrypted.png', '_decrypted.png')
    img.save(decrypted_image_path)
    return decrypted_image_path

# Example usage
image_path = 'nature.png'
encryption_key = 50

encrypted_path = encrypt_image(image_path, encryption_key)
print("Image encrypted. Encrypted image saved as:", encrypted_path)

decrypted_path = decrypt_image(encrypted_path, encryption_key)
print("Image decrypted. Decrypted image saved as:", decrypted_path)

# Display images
plt.figure(figsize=(10, 5))

# Original image
plt.subplot(1, 3, 1)
original_image = Image.open(image_path)
plt.imshow(original_image)
plt.title('Original Image')
plt.axis('off')

# Encrypted image
plt.subplot(1, 3, 2)
encrypted_image = Image.open(encrypted_path)
plt.imshow(encrypted_image)
plt.title('Encrypted Image')
plt.axis('off')

# Decrypted image
plt.subplot(1, 3, 3)
decrypted_image = Image.open(decrypted_path)
plt.imshow(decrypted_image)
plt.title('Decrypted Image')
plt.axis('off')

plt.show()
