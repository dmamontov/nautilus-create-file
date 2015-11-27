# coding=utf-8

# Script Name : nautilus-create-file.py
# Author : Dmitry Mamontov
# Created : 27 November 2015
# Last Modified :
# Version : 1.0.0
# Modifications : 
# Description : Adds a context menu item Nautilus 'Create new file'

from os import popen
from os.path import join
from os.path import exists
from locale import getlocale
from gi.repository import GObject, Nautilus

class Slobel(GObject.GObject, Nautilus.MenuProvider):
    # Window titles and context menu
    TITLE = {
        'en_GB': 'Create new file',
        'en_US': 'Create new file',
        'en_AU': 'Create new file',
        'es_ES': 'Crear nuevo archivo',
        'es_MX': 'Crear nuevo archivo',
        'es_AR': 'Crear nuevo archivo',
        'es_CO': 'Crear nuevo archivo',
        'pt_PT': 'Criar novo arquivo',
        'pt_BR': 'Criar novo arquivo',
        'zh_CN': '创建新的文件。',
        'zh_TW': 'สร้างไฟล์ใหม่',
        'zh_HK': '創建新的文件。',
        'ru_RU': 'Создать новый файл',
        'ru_UA': 'Создать новый файл',
        'uk_UA': 'Створити новий файл'
    }

    # The name of the file
    FILENAME = {
        'en_GB': 'Filename',
        'en_US': 'Filename',
        'en_AU': 'Filename',
        'es_ES': 'Nombre del archivo',
        'es_MX': 'Nombre del archivo',
        'es_AR': 'Nombre del archivo',
        'es_CO': 'Nombre del archivo',
        'pt_PT': 'Nome do arquivo',
        'pt_BR': 'Nome do arquivo',
        'zh_CN': '文件名',
        'zh_TW': 'ชื่อแฟ้ม',
        'zh_HK': '文件名',
        'ru_RU': 'Имя файла',
        'ru_UA': 'Имя файла',
        'uk_UA': "Ім'я файлу"
    }

    # The name of the new file
    NEW_FILE = {
        'en_GB': 'new file',
        'en_US': 'new file',
        'en_AU': 'new file',
        'es_ES': 'archivo nuevo',
        'es_MX': 'archivo nuevo',
        'es_AR': 'archivo nuevo',
        'es_CO': 'archivo nuevo',
        'pt_PT': 'novo arquivo',
        'pt_BR': 'novo arquivo',
        'zh_CN': '新文件',
        'zh_TW': 'ไฟล์ใหม่',
        'zh_HK': '新文件',
        'ru_RU': 'новый файл',
        'ru_UA': 'новый файл',
        'uk_UA': "новий файл"
    }

    # Invalid characters in the file name
    INVALID_CHARS = ('/',)

    def __init__(self):
        pass

    # The pop-up error messages
    def alert(self, msg):
        dialog = popen("zenity --error --text '%s' --width=320" % msg)

        return dialog.read()

    # It gets the name of the new file
    def get_file_name(self, filename, folder):
        new_file = join(folder.get_uri().replace("file://", ""), filename)
        if exists(new_file):
            count = 1;
            while 1:
                new_file = join(folder.get_uri().replace("file://", ""), "%s (%d)" % (filename, count))
                if not exists(new_file):
                    return "%s (%d)" % (filename, count)
                count = count + 1

        return filename

    # Creates a new file
    def create_new_file(self, menu, folder):
        response = popen("zenity --entry --title '%s' --text '%s:' --width=320" % (self.TITLE[getlocale()[0]], self.FILENAME[getlocale()[0]]))
        filename = response.read()

        returncode = response.close()
        if returncode == 256:
            return

        filename = filename.split('\n')[0]

        if not filename:
            filename = self.get_file_name(self.NEW_FILE[getlocale()[0]], folder)
        elif exists(join(folder.get_uri().replace("file://", ""), filename)):
            filename = self.get_file_name(filename, folder)

        for invalid_char in self.INVALID_CHARS:
            if invalid_char in filename:
                self.alert("The filename cannot contain '%s' characteres" % invalid_char)
                return self.create_new_file(menu, folder)

        with open(join(folder.get_uri().replace("file://", ""), filename), 'w') as f:
            f.write('')

        return

    def get_background_items(self, window, current_folder):
        SlobelMenuItem = Nautilus.MenuItem(
            name = "Slobel::CreateFile",
            label = self.TITLE[getlocale()[0]],
            tip = self.TITLE[getlocale()[0]]
        )

        SlobelMenuItem.connect('activate', self.create_new_file, current_folder)

        return [SlobelMenuItem]