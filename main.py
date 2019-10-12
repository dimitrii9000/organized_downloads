import os
import watchdog.events
import watchdog.observers
import os
import time

downloads_folder = 'C:/Downloads'

folder_names = ['Pictures',
                'Zips',
                'Documents']

# 1 block of extensions for every folder_name
extensions = [['jpeg', 'jpg', 'png'],
              ['zip', 'rar'],
              ['doc', 'docx', 'pdf']]


def move_f():
    for file in os.listdir(downloads_folder):
        filename, file_extension = os.path.splitext(file)
        file_extension = file_extension.replace(".", "")
        p_from = downloads_folder + "/" + file
        for i in range(len(extensions)):
            if file_extension in extensions[i]:
                p_to = downloads_folder + "/" + folder_names[i] + "/" + file
                try:
                    os.rename(p_from, p_to)
                except FileExistsError:
                    pass


def create_dirs_in_init():
    for name in folder_names:
        path = downloads_folder + "/" + name
        if not os.path.exists(path):
            os.makedirs(path)


try:
    while True:
        move_f()
        time.sleep(10)
except KeyboardInterrupt:
    exit(0)

