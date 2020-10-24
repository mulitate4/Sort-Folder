import os
import datetime
import shutil

# ===== #
# Input #
# ===== #

#Takes INPUT as a FULL FILE PATH for the BASE FOLDER
base_path = input("Path: ")

# ========= #
# Variables #
# ========= #
base_folder = os.listdir(base_path)
file_dict = {}

# ===================================== #
# Getting ALL File's Time modified info #
# ===================================== #
for file_ in base_folder:
    #Skip iteration if File is a Folder
    if os.path.splitext(file_)[1] == "":
        continue


    file_path = f"{base_path}/{file_}"

    #Get's the time of modification of file in SECONDS (since Unix Epoch)
    time_modified_seconds = os.path.getctime(file_path)
    time_modified_seconds = float(round(time_modified_seconds))

    #Convert SECONDS into Date-Time in format of DAY-MONTH-YEAR
    date_time = datetime.datetime.fromtimestamp(time_modified_seconds)
    date_modified = date_time.strftime('%m-%d-%Y')

    #Adds File Name as KEY and Date of Modification as VALUE - {FILE_NAME: DATE_MODIFIED}
    file_dict[file_] = date_modified

# ========================= #
# Actually Moving the Files #
# ========================= #
for file_ in file_dict:
    #Accessing Values
    date_modified = file_dict[file_]
    file_name = file_

    #Checks if Folder ALREADY exists
    #If Folder exists, doesn't exist, create a NEW one
    if not os.path.exists(f"{base_path}/{date_modified}"):
        os.mkdir(f"{base_path}/{date_modified}")


    #Actually MOVING the file to the newly created folder
    shutil.move(f"{base_path}/{file_name}", f"{base_path}/{date_modified}/{file_name}")