import os

def arrange_files(files, ext):
    files_with_ext = [file for file in files if file.endswith(ext)]
    print(files_with_ext)

    if(not os.path.exists("images")):
        os.mkdir("images")


    for i, file in enumerate(files_with_ext, start=1):
        os.rename(file, f"images/photo-{i}{ext}")

if __name__=="__main__":
    files = os.listdir()
    jpg_files = arrange_files(files, ".jpg")
    print(jpg_files)