import os

def arrange_files(files, ext):
    files_with_ext = [file for file in files if file.endswith(ext)]
    print(f"Arranging files with extension: {files_with_ext}")
    for file in files_with_ext:
        os.rename(file, f"")

if __name__ == "__main__":
    files = os.listdir()
    arrange_files(files, '.py')