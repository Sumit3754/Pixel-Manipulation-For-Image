from PIL import Image
import numpy as np


def encrypt_image(input_image_path, output_image_path, key):

    img = Image.open(input_image_path)
    img = img.convert('RGB')
    
   
    img_data = np.array(img)

    
    height, width, channels = img_data.shape
    
   
    for y in range(height):
        for x in range(width):
            for c in range(channels):
                img_data[y][x][c] ^= key  

    
    encrypted_img = Image.fromarray(img_data)
    
   
    encrypted_img.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")


def decrypt_image(input_image_path, output_image_path, key):
    encrypt_image(input_image_path, output_image_path, key)  


key = 123  
encrypt_image('original_image.jpg', 'encrypted_image.jpg', key)  
decrypt_image('encrypted_image.jpg', 'decrypted_image.jpg', key)  
