# Цифровой поток
import random, shutil, sys, time


def stream():
    # Задаем константы:
    min_stream_length = 20  # (!) Попробуйте заменить это значение на 1 или 50.
    max_stream_length = 22  # (!) Попробуйте заменить это значение на 100.
    pause = 0.08  # (!) Попробуйте заменить это значение на 0.0 или 2.0.
    stream_chars = ['1', '0']  # (!) Попробуйте заменить их на другие символы.

    # Плотность может варьироваться от 0.0 до 1.0:
    density = 0.30  # (!) Попробуйте заменить это значение на 0.10 или 0.30.

    # Получаем размер окна терминала:
    width = shutil.get_terminal_size()[0]
    # В Windows нельзя вывести что-либо в последнем столбце без добавления
    # автоматически символа новой строки, поэтому уменьшаем ширину на 1:
    width -= 1

    print('Digital Stream')
    print('Press Ctrl+C to quit')
    time.sleep(2)

    try:
        # Если для столбца счетчик равен 0, поток не отображается.
        # В противном случае он показывает, сколько раз должны отображаться
        # в этом столбце 1 или 0.
        columns = [0] * width
        while True:
            # Задаем счетчики для каждого столбцов:
            for i in range(width):
                if columns[i] == 0:
                    if random.random() <= density:
                        # Перезапускаем поток для этого столбца
                        columns[i] = random.randint(min_stream_length, max_stream_length)

                # выводим пробел и символ 1/0
                if columns[i] > 0:
                    print(random.choice(stream_chars), end='')
                    columns[i] -= 1
                else:
                    print('', end='')
            print()  # Выводим символ новой строки в конце строки столбцов.
            sys.stdout.flush()  # Обеспечиваем появление текста на экране.
            time.sleep(pause)
    except KeyboardInterrupt:
        sys.exit()  # Если нажато сочетание клавиш Ctrl+C — завершаем программу.


if __name__ == '__main__':
    stream()
