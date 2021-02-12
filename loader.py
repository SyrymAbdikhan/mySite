
import os, csv

def getSchedule(foldername):
    global WeekTimetable
    localTimetable = {}
    
    tmp_path = os.path.join(foldername, 'timetable.csv')
    if os.path.exists(tmp_path):
        with open(tmp_path, 'r', encoding='utf-8') as f:
            cont = csv.DictReader(f)
            for line in cont:
                if line['time']:
                    localTimetable[line['day']] = eval(line['time'])
                else:
                    localTimetable[line['day']] = DayTimetable
    else:
        localTimetable = WeekTimetable
    
    links = []
    with open(os.path.join(foldername, 'links.csv'), 'r', encoding='utf-8') as f:
        cont = csv.DictReader(f)
        for line in cont:
            links.append(line.copy())

    schedule = {}
    with open(os.path.join(foldername, 'schedule.csv'), 'r', encoding='utf-8') as f:
        cont = csv.DictReader(f)
        for line in cont:
            schedule[line['day']] = eval(line['lessons'])

    return [schedule, links, localTimetable]

def getFullSchedule():
    root = 'static/schedules/'
    classes = os.listdir(root)
    schedules = {}
    for _class in classes:
        schedules[_class] = getSchedule(os.path.join(root, _class))

    return schedules

DayTimetable = [
    '08:00 - 08:30',
    '08:35 - 09:05',
    '09:10 - 09:40',
    '09:45 - 10:15',
    '10:20 - 10:50',
    '10:55 - 11:25',
    '11:30 - 12:00'
]

SAUTimetable = [
    '08:30 - 08:50',
    '09:00 - 10:00',
    '10:10 - 11:10',
    '11:20 - 12:20',
    '12:30 - 13:30'
]

addSAUTimetable = [
    '08:30 - 09:30',
    '09:40 - 10:40',
    '10:50 - 11:50',
    '12:00 - 13:00'
]

WeekTimetable = {
    'Monday':    DayTimetable,
    'Tuesday':   DayTimetable,
    'Wednesday': DayTimetable,
    'Thursday':  DayTimetable,
    'Friday':    DayTimetable
}

TRANSLATION = {
    'Monday':    {'eng': 'Monday',    'ru': 'Понедельник', 'kz': 'Дүйсенбі'},
    'Tuesday':   {'eng': 'Tuesday',   'ru': 'Вторник',     'kz': 'Сейсенбі'},
    'Wednesday': {'eng': 'Wednesday', 'ru': 'Среда',       'kz': 'Сәрсенбі'},
    'Thursday':  {'eng': 'Thursday',  'ru': 'Четверг',     'kz': 'Бейсенбі'},
    'Friday':    {'eng': 'Friday',    'ru': 'Пятница',     'kz': 'Жұма'},
    'empty' :    {'eng': 'No lessons for this day', 'ru': 'На этот день нет уроков', 'kz': 'Бұл күнге сабақ жоқ'},
    
    'Select grade':      {'eng': 'Select grade', 'ru': 'Выберите класс', 'kz': 'Сыныпты таңданыз'},
    'technical support': {'eng': 'technical support', 'ru': 'техническая поддержка', 'kz': 'техникалық көмек'},
    'attendance':        {'eng': 'attendance', 'ru': 'посещаемость', 'kz': 'қатысушылар саны'},
    'Grades':            {'eng': 'Grades', 'ru': 'Классы', 'kz': 'Сыныптар'},
    'reload alert':      {'eng': 'don\'t forget to reload the page', 'ru': 'не забывайте перезагружать страницу', 'kz': 'парақты қайта жүктеуді ұмытпаңыз'},

    '11A':   {'eng': '11 A',  'ru': '11 А',  'kz': '11 А'},
    "11G'":  {'eng': "11 G'", 'ru': "11 Г'", 'kz': '11 Ғ'},
    '11-1':  {'eng': '11/1',  'ru': '11/1',  'kz': '11/1'},
    
    'class time': {'eng': 'Class time', 'ru': 'Кл час', 'kz': 'Сын сағ'},
    'english 1':  {'eng': 'Eng 1', 'ru': 'Англ яз 1', 'kz': 'Ағылшын т. 1'},
    'english 2':  {'eng': 'Eng 2', 'ru': 'Англ яз 2', 'kz': 'Ағылшын т. 2'},
    'algebra':    {'eng': 'Algebra', 'ru': 'Алгебра', 'kz': 'Алгебра'},
    'geometry':   {'eng': 'Geometry', 'ru': 'Геометрия', 'kz': 'Геометрия'},
    'cs 1':       {'eng': 'CS 1', 'ru': 'Информатика 1', 'kz': 'Информатика 1'},
    'cs 2':       {'eng': 'CS 2', 'ru': 'Информатика 2', 'kz': 'Информатика 2'},
    'geography':  {'eng': 'Geography', 'ru': 'География', 'kz': 'География'},
    'kaz lang':   {'eng': 'Kaz lang', 'ru': 'Каз яз', 'kz': 'Қазақ т.'},
    'kaz lit':    {'eng': 'Kaz lit', 'ru': 'Каз литра', 'kz': 'Қазақ әдеб.'},
    'rus lang 1': {'eng': 'Rus lang 1', 'ru': 'Рус яз 1', 'kz': 'Орыс т. 1'},
    'rus lang 2': {'eng': 'Rus lang 2', 'ru': 'Рус яз 2', 'kz': 'Орыс т. 2'},
    'physics':    {'eng': 'Physics', 'ru': 'Физика', 'kz': 'Физика'},
    'chemestry':  {'eng': 'Chemestry', 'ru': 'Химия', 'kz': 'Химия'},
    'biology':    {'eng': 'Biology', 'ru': 'Биология', 'kz': 'Биология'},
    'kaz hist':   {'eng': 'Kaz hist', 'ru': 'Ист. К.', 'kz': 'Қаз. тарихы'},
    'world hist': {'eng': 'World hist', 'ru': 'Всемирка', 'kz': 'Дж. тарихы'},
    '': {}
}