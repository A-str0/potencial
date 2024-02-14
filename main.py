import csv


def calculate_streams(date, song):
    '''
    Функция, вычисляющая кол-во послушваний
    :param date: дата, необходимая для формулы кол-ва прослушиваний
    :param song: данные о песне
    :return: вычисленное кол-во прослушиваний
    '''

    date = date.split('.')
    dn = int(date[2]) - 1 * 365 + int(date[1]) * 30 + int(date[0])

    start_date = song[-1].split('.')
    di = int(start_date[2]) - 1 * 365 + int(start_date[1]) * 30 + int(start_date[0])

    divido = 1 if len(song[1]) - len(song[2]) == 0 else len(song[1]) - len(song[2])

    return (dn - di) // divido


def fill_gaps(date, table):
    '''
    Функция заполняет пробелы прослушиваний в таблице
    :param date: дата, необходимая для формулы кол-ва прослушиваний
    :param table: таблица для замены
    :return: None
    '''

    for song in table:
        if song[0] == '0':
            song[0] = str(abs(calculate_streams(date, song)))


def get_songs_by_date(date, table):
    '''
    Функция находит в таблице все песни, созданные до введенной даты
    :param date: дата, не позже которой должны выйти искомые песни
    :param table: таблица для поиска
    :return: список массивов, содержащих данные о найденных песнях
    '''

    date = date.split('.')
    result = []
    for song in table:
        full_date = song[-1].split('.')
        if int(full_date[2]) <= int(date[2]):
            if int(full_date[1]) <= int(date[1]):
                if int(full_date[0]) <= int(date[0]):
                    result.append(song)
    return result


def sort_songs_by_date(table):
    new_table = table.copy()
    while True:
        cnt = 0
        for i in range(len(table) - 1):
            if new_table[i][3] > new_table[i + 1][3]:
                new_table[i], new_table[i + 1] = new_table[i + 1], new_table[i]
                cnt += 1
        if cnt == 0: break
    return new_table


def print_top5(table):
    songs_table = sort_songs_by_date(table)
    for i in range(5):
        print(f'№{i} {songs_table[i][2]}, {songs_table[i][1]}, {songs_table[i][3]}')


def task1(songs_table):
    fill_gaps('01.01.2002', songs_table)

    res = get_songs_by_date('01.01.2002', songs_table)
    for i in res:
        print(f'{i[2]} - {i[1]} - {i[0]}')


def task2(songs_table):
    print_top5(songs_table)


def find_song_by_artist(artist, table):
    for song in table:
        if artist == song[1]:
            return f'У {artist} найдена песня: {song[2]}'
    return 'К сожалению, ничего не удалось найти'


def main():
    f = open('songs.csv', encoding='UTF8')

    r = csv.reader(f, delimiter=';')
    songs_table = list(r)[1:]

    print('Task 1')
    task1(songs_table)

    print('Task 2')
    task2(songs_table)

    print('Task 3')
    print('Введите имя артиста для поиска:')
    artist = input()
    result = find_song_by_artist(artist, songs_table)
    print(result)

    f.close()


if __name__ == '__main__':
    main()

