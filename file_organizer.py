import os
import shutil

folder_path = input("Enter folder path to organize: ")

file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".doc", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Python": [".py"]
}

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    if os.path.isfile(file_path):
        file_extension = os.path.splitext(file_name)[1].lower()
        category_found = False

        for folder_name, extensions in file_categories.items():
            if file_extension in extensions:
                new_folder = os.path.join(folder_path, folder_name)

                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)

                shutil.move(file_path, os.path.join(new_folder, file_name))
                print(file_name, "->", folder_name)
                category_found = True
                break

        if not category_found:
            new_folder = os.path.join(folder_path, "Others")

            if not os.path.exists(new_folder):
                os.makedirs(new_folder)

            shutil.move(file_path, os.path.join(new_folder, file_name))
            print(file_name, "-> Others")

print("File organization completed!")