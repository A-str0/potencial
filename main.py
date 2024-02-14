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

def main():
    f = open('songs.csv', encoding='UTF8')

    r = csv.reader(f, delimiter=';')
    songs_table = list(r)[1:]

    fill_gaps('01.01.2002', songs_table)

    res = get_songs_by_date('01.01.2002', songs_table)
    for i in res:
        print(i)

    f.close()


if __name__ == '__main__':
    main()

