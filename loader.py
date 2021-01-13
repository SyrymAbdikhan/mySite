
import os, csv

def getSchedule(foldername):
    cwd = os.getcwd()
    links = []
    with open(os.path.join(cwd, foldername, 'links.csv'), 'r', encoding='utf-8') as f:
        cont = csv.DictReader(f)
        for line in cont:
            links.append(line.copy())

    schedule = {}
    with open(os.path.join(cwd, foldername, 'schedule.csv'), 'r', encoding='utf-8') as f:
        cont = csv.DictReader(f)
        for line in cont:
            schedule[line['day']] = eval(line['lessons'])

    return [schedule, links]

mainTimetable = [
    '14:00 - 14:30',
    '14:40 - 15:10',
    '15:20 - 15:50',
    '16:00 - 16:30',
    '16:40 - 17:10',
    '17:20 - 17:50',
    '18:00 - 18:30'
]

tmpTimetable2 = [
    '08:30 - 08:50',
    '09:00 - 10:00',
    '10:10 - 11:10',
    '11:20 - 12:20',
    '12:30 - 13:30'
]

tmpTimetable1 = [
    '08:30 - 09:30',
    '09:40 - 10:40',
    '10:50 - 11:50',
    '12:00 - 13:00'
]

DAYTIMETABLE = {
    'Monday':    mainTimetable,
    'Tuesday':   mainTimetable,
    'Wednesday': mainTimetable,
    'Thursday':  mainTimetable,
    'Friday':    mainTimetable
}


TRANSLATION = {
    'Monday':    {'eng': 'Monday',    'ru': 'Понедельник', 'kz': 'Дүйсенбі'},
    'Tuesday':   {'eng': 'Tuesday',   'ru': 'Вторник',     'kz': 'Сейсенбі'},
    'Wednesday': {'eng': 'Wednesday', 'ru': 'Среда',       'kz': 'Сәрсенбі'},
    'Thursday':  {'eng': 'Thursday',  'ru': 'Четверг',     'kz': 'Бейсенбі'},
    'Friday':    {'eng': 'Friday',    'ru': 'Пятница',     'kz': 'Жұма'},
    'empty' :    {'eng': 'No lessons for this day', 'ru': 'На этот день нет уроков', 'kz': 'Бұл күнге сабақ жоқ'},
    
    'Select grade':      {'eng': 'Select grade',    'ru': 'Выберите класс', 'kz': 'Сыныпты таңданыз'},
    'technical support': {'eng': 'technical support', 'ru': 'техническая поддержка', 'kz': 'техникалық көмек'},
    'attendance':        {'eng': 'attendance', 'ru': 'посещаемость', 'kz': 'қатысушылар саны'},
    'Grades':            {'eng': 'Grades', 'ru': 'Классы', 'kz': 'Сыныптар'},
    'reload alert':      {'eng': 'don\'t forget to reload the page', 'ru': 'не забывайте перезагружать страницу', 'kz': 'парақты қайта жүктеуді ұмытпаңыз'},
    
    'сынып сағаты':       {'eng': 'Class time', 'ru': 'Кл час', 'kz': 'Сын сағ'},
    'ағылшын тілі 1 топ': {'eng': 'Eng 1', 'ru': 'Англ яз 1', 'kz': 'Ағылшын т. 1'},
    'ағылшын тілі 2 топ': {'eng': 'Eng 2', 'ru': 'Англ яз 2', 'kz': 'Ағылшын т. 2'},
    'алгебра':            {'eng': 'Algebra', 'ru': 'Алгебра', 'kz': 'Алгебра'},
    'геометрия':          {'eng': 'Geometry', 'ru': 'Геометрия', 'kz': 'Геометрия'},
    'информатика 1 топ':  {'eng': 'CS 1', 'ru': 'Информатика 1', 'kz': 'Информатика 1'},
    'информатика 2 топ':  {'eng': 'CS 2', 'ru': 'Информатика 2', 'kz': 'Информатика 2'},
    'география':          {'eng': 'Geography', 'ru': 'География', 'kz': 'География'},
    'қазақ тілі':         {'eng': 'Kaz lang', 'ru': 'Каз яз', 'kz': 'Қазақ т.'},
    'қазақ әдебиеті':      {'eng': 'Kaz lit', 'ru': 'Каз литра', 'kz': 'Қазақ әдеб.'},
    'орыс тілі 1 топ':    {'eng': 'Rus lang 1', 'ru': 'Рус яз 1', 'kz': 'Орыс т. 1'},
    'орыс тілі 2 топ':    {'eng': 'Rus lang 2', 'ru': 'Рус яз 2', 'kz': 'Орыс т. 2'},
    'физика':             {'eng': 'Physics', 'ru': 'Физика', 'kz': 'Физика'},
    'химия':              {'eng': 'Chemestry', 'ru': 'Химия', 'kz': 'Химия'},
    'биология':           {'eng': 'Biology', 'ru': 'Биология', 'kz': 'Биология'},
    'қазақстан тарихы':   {'eng': 'Kaz hist', 'ru': 'Ист. К.', 'kz': 'Қаз. тарихы'},
    'дүниежүзі тарихы':   {'eng': 'World hist', 'ru': 'Всемирка', 'kz': 'Дж. тарихы'},
    '': {}
}