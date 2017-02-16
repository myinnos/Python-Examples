import os

def rename_files():
    #(1) get file names from folder
    file_list = os.listdir(r"C:\Python27\examples\secret message\prank")
    #print(file_list)
    save_path = os.getcwd()
    print("Current working directory is " + save_path)
    os.chdir(r"C:\Python27\examples\secret message\prank")
    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(save_path)

rename_files()
