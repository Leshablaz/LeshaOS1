import os

while True:
    print("Добро пожалавать в LeshaOS")
    print("Чтоб посмотреть команды напишите HELP")
    command = input()
    if command == "help" or command == "HELP":
        print("open-после написания напишите путь к программе которую хотите открыть(главное чтоб в пути не было пробелов)")
        print("quit-закрытие программы")
        print("create file-создать файлы")
        print("edit file-изменить файл")
        print("create dir-создать папку")
        print("replace file-перемистить файл")
        print("rename file-переименовать файл")
        print("view file-просмтореть файл")
        print("delete file-удалить файл")
    if command == "open" or command == "OPEN":
        print("напишите путь к файлу который хотите открыть(главное чтоб в пути не было пробелов)")
        put = input()
        os.system(put)

    if command == "quit" or command == "QUIT":
        quit()

    if command == "create file" or command == "CRTEATE FILE":
        print("Введите путь к файлу")
        file = input()
        new_file = open(file, "w+")

    if command == "edit file" or command == "EDIT FILE":
        print("Введите путь к файлу")
        edit_file = input()
        file_for_editing = open(edit_file , "w")
        print("Введите то что хотите добавить в файл")
        editing_file = input()
        file_for_editing.write(editing_file)
        file_for_editing.close()

    if command == "create dir" or command == "CREATE DIR":
        print("Введите путь к папке")
        new_dir = input()
        os.mkdir(new_dir)

    if command == "replace file" or command == "REPLACE FILE":
        print("напишите путь к файлу и потом введите новый путь к файлу")
        old_put = input()
        new_put = input()
        os.replace(old_put, new_put)

    if command == "rename file" or command == "RENAME FILE":
        print("Введите путь со старым именем а потом путь с новым")
        print("старое")
        old_name = input()
        print("новое")
        new_name = input()
        os.rename(old_name, new_name)

    if command == "view file" or command == "VIEW FILE":
        print("Введите путь к файлу")
        file_for_view = input()
        view_file_settings = open(file_for_view, "r")
        view_file = view_file_settings.read()
        view_file_settings.close()
        print(view_file)

    if command == "delete file" or command == "DELETE FILE":
        print("Введите путь к файлу который хотите удалить")
        deleted_file_name = input()
        os.remove(deleted_file_name)
        print("Удалено!")
