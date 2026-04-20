import os
import shutil

print(" JPG Mover Starting...")

source_dir = 'source_folder'
dest_dir = 'destination_folder'

os.makedirs(dest_dir, exist_ok=True)

files = os.listdir(source_dir)
jpg_files = [f for f in files if f.lower().endswith('.jpg')]
print(f"Found {len(jpg_files)} JPG files in {source_dir}")

moved_count = 0
for filename in files:
    if filename.lower().endswith('.jpg'):
        shutil.move(os.path.join(source_dir, filename), 
                   os.path.join(dest_dir, filename))
        print(f" Moved: {filename}")
        moved_count += 1

print(f"\n {moved_count} files moved to {dest_dir}!")


print(" Opening destination folder...")
os.startfile(dest_dir)  