from PIL import Image 
import os 
 
for filename in os.listdir('.'): 
    if filename.lower().endswith('.jpg'): 
        img = Image.open(filename) 
        new_name = filename.replace('.jpg', '.webp') 
        img.save(new_name, 'webp', quality=85) 
        print(f'Converted: {new_name}') 
print('All done!') 
