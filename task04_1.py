"""
Все файлы, которые будут создаваться для задач должны начинаться с префикса "task04"
Все файлы отправить на github

1. Создать скрипт, который через параметр запуска получает имя исполняемого файла.
И запускает этот файл через библиотеку subprocess. Обработку ошибок (файл не существует, или не
может быть запущен и т.д.) сделать через исключения.
"""

from sys import argv

import subprocess
import os
import threading
import logging

script, Proggy_for_execute = argv
print('Proggy_for_execute = ', Proggy_for_execute)
try:
    subprocess.run([Proggy_for_execute])
except FileNotFoundError:
    print("Can't fined this proggy {0}!!!".format(Proggy_for_execute))
except OSError:
    print("{0} не является приложением Win32 !!!".format(Proggy_for_execute))
finally:
    print("be carefully!!!")






