import os
import shutil

def clean_desk():


    path = os.path.join(os.path.expanduser("~"), "Escritorio")

    os.makedirs(os.path.join(path, "Documents"), exist_ok=True)
    os.makedirs(os.path.join(path, "Images"), exist_ok=True)

    files = os.listdir(path)

    for item in files:
        if item == "janitor.py":
            continue

        old_path = os.path.join(path, item)

        if item.endswith(".txt"):
            new_path = os.path.join(path, "Documents", item)        
            shutil.move(old_path, new_path)
            print(f"[Moved] {item} to Documents/")

        elif item.endswith((".jpg", ".png", ".jpeg", ".gif")):
            new_path = os.path.join(path, "Images", item)
            shutil.move(old_path, new_path)
            print(f"[Moved] {item} to Images/")

        elif item.endswith(".py"):
            new_path = os.path.join(path, "Old_Code", item)
            shutil.move(old_path, new_path)
            print(f"[Moved] {item} to Old_Code/")

        elif item.endswith(".html"):
            new_path = os.path.join(path, "HTML_PROJECTS", item)
            shutil.move(old_path, new_path)
            print(f"[Moved] {item} to HTML_PROJECTS/")

        else:
            print(f"[SKIPPED] {item} - No rule for this file type")
    print("\n[DONE] Desktop Cleaned.")


if __name__ == "__main__": 
    clean_desk()
    	
