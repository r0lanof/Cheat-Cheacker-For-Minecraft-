import os

def search_folders(directory, target_folders):
    found_folders = []

    # Просматриваем все подпапки в указанной директории
    for root, dirs, files in os.walk(directory):
        # Проверяем каждую папку в текущей подпапке
        for folder in dirs:
            # Если имя папки находится среди целевых, добавляем ее в список найденных
            if folder in target_folders:
                found_folders.append(os.path.join(root, folder))

    return found_folders

def search_entire_computer(target_folders):
    print("Проверка начата. Ожидайте...")
    found_folders = []

    # Получаем список доступных дисков
    drives = ['%s:' % d for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists('%s:' % d)]

    # Просматриваем все диски
    for drive in drives:
        # Ищем целевые папки на каждом диске
        found_folders.extend(search_folders(drive + '\\', target_folders))

    return found_folders

# Задаем целевые папки
target_folders = ["Nurik", "Celestial", "Matix", "Impact", "expensive", "arbuz", "wild", "baritone", "minced", "Trash", "excellent", "nova", "nmd", "Ricardo", "wissend"]

# Ищем папки и выводим результаты
found_folders = search_entire_computer(target_folders)
if found_folders:
    print("Найдены следующие папки:")
    for folder in found_folders:
        print(folder)
else:
    print("Целевые папки не найдены.")

print("made by r0lanoff")

input("Нажмите Enter для завершения программы...")
