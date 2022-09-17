"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('file.txt', 'r', encoding='utf-8') as file:
        print(f'Длина файла {len(file.read())}')

    with open('file.txt', 'r', encoding='utf-8') as file:
        count_strings = file.read().split()
        print(f'Количество слов в файле - {len(count_strings)}')

    with open('file.txt', 'r', encoding='utf-8') as file:
        read_file = file.read().replace('.', '!')
        with open ('regerat2.txt', 'w', encoding='utf-8') as file_write:
            file_write.write(read_file)

if __name__ == "__main__":
    main()
