import os

def arrange_files(files, ext,folder):
    files_with_ext =  [file for file in files if file.endswith(ext)]
    print(files_with_ext)

    if not os.path.exists(folder):
        os.mkdir(folder)    

    for i, file in enumerate(files_with_ext, start=1):
        os.rename(file, f"{folder}/file-{i}{ext}")

if __name__ == "__main__":
    files = os.listdir()
    
    arrange_files(files, ".jpg", "Images")
    arrange_files(files, ".jpeg", "Images")
    arrange_files(files, ".png", "Images")

    arrange_files(files, ".pdf", "PDFs")

    arrange_files(files, ".txt", "Text Files")

    arrange_files(files, ".docx", "Word Files")

    arrange_files(files, ".xlsx", "Excel Files")

    arrange_files(files, ".pptx", "PowerPoint Files")

    arrange_files(files, ".py", "Python Files")

    arrange_files(files, ".mp3", "Music")

    arrange_files(files, ".mp4", "Videos")