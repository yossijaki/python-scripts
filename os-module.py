import os
import re

print(os.getcwd())
def rename_folders(root_dir):
    # List the three subfolders
    subfolders = ["Avanzado", "Básico", "Intermedio"]

    for subfolder in subfolders:
        subfolder_path = os.path.join(root_dir, subfolder)
        if not os.path.exists(subfolder_path):
            print(f"Folder '{subfolder}' does not exist.")
            continue

        # Traverse through subdirectories
        for dirpath, dirnames, filenames in os.walk(subfolder_path):
            for dirname in dirnames:
                # Check if folder name matches the patterns
                if dirname.startswith("U ") or dirname.startswith("UNIT "):
                    try:
                        # Extract the unit number
                        unit_number = int(dirname.split()[-1])
                        # Format the new folder name
                        new_folder_name = f"Unit {unit_number:02}"
                        # Rename the folder
                        os.rename(os.path.join(dirpath, dirname), os.path.join(dirpath, new_folder_name))
                        print(f"Renamed '{dirname}' to '{new_folder_name}'")

                        # Now handle the .mp4 files
                        for topic in ["Grammar", "Sentences", "Vocabulary"]:
                            topic_folder = os.path.join(dirpath, f"Class {unit_number:.1f} {topic}")
                            mp4_files = [f for f in os.listdir(topic_folder) if f.lower().endswith(".mp4")]
                            if mp4_files:
                                mp4_file = mp4_files[0]
                                # Extract the lesson number (XX.X) and topic from the folder name
                                lesson_number, topic_name = re.match(r"Class (\d+\.\d+) (\w+)", topic_folder).groups()
                                new_mp4_name = f"Class {lesson_number}-{topic_name}_1.mp4"
                                # Rename the .mp4 file
                                os.rename(os.path.join(topic_folder, mp4_file), os.path.join(topic_folder, new_mp4_name))
                                print(f"Renamed '{mp4_file}' to '{new_mp4_name}'")
                    except ValueError:
                        print(f"Skipping invalid folder name: '{dirname}'")

if __name__ == "__main__":
    parent_folder = r"C:\CURSOS\Ingles_YouTalkTVPlus"
    rename_folders(parent_folder)