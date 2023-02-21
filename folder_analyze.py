import os
import json


folder = r"C:\Users\sriharsha\Desktop\repo\decode-cx-backend"

def count_folder():
    total_files = 0
    total_folders = 0
    extensions = {}
    non_ext_files = 0
    for root, dirs, files in os.walk(folder):
        total_folders += len(dirs)
        total_files += len(files)
        for file in files:
            name, ext = os.path.splitext(file)
            if ext == '':
                non_ext_files += 1
                continue
            extensions[ext] = extensions.get(ext, 0) + 1
    return {
        'Total number of files': total_files,
        'Total number of folders': total_folders,
        'Total': total_folders + total_files,
        'Extensions': extensions,
        'Non-extension files': non_ext_files
    }

result = count_folder()
print(json.dumps(result, indent=4))
