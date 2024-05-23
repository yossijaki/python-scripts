import os
import re

def rename_mp4_files(root_dir):
    # Traverse through subdirectories
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            # Check if folder name matches the pattern "Class XX.X {whatever}"
            match = re.match(r"Class (\d+\.\d+) (\w+)", dirname)
            if match:
                lesson_number, topic = match.groups()
                # Look for the .mp4 file
                mp4_files = [f for f in os.listdir(os.path.join(dirpath, dirname)) if f.lower().endswith(".mp4")]
                if mp4_files:
                    mp4_file = mp4_files[0]
                    # Rename the .mp4 file
                    new_mp4_name = f"Class {lesson_number}-{topic}_1.mp4"
                    os.rename(os.path.join(dirpath, dirname, mp4_file), os.path.join(dirpath, dirname, new_mp4_name))
                    print(f"Renamed '{mp4_file}' to '{new_mp4_name}'")

if __name__ == "__main__":
    parent_folder = r"C:\CURSOS\Ingles_YouTalkTVPlus"
    rename_mp4_files(parent_folder)