
import os, json


def getShiftSchedule(foldername):

    classes = {}
    filenames = [os.path.join(foldername, filename) for filename in os.listdir(foldername) if filename.endswith(".json")]
    base_data_path = os.path.join(foldername, "base_timetable.json")
    filenames.remove(base_data_path)

    schedule_type = "SA_schedule"
    base_data = getJsonData(base_data_path)

    if schedule_type == "SA_schedule" and schedule_type not in base_data:
        schedule_type = "regular_schedule"

    for filename in filenames:
        _class = os.path.split(filename)[-1][:-5]
        data = getJsonData(filename)
        result = {}

        if not data[schedule_type]["base_timetable"]:
            data[schedule_type]["base_timetable"] = base_data[schedule_type]["base_timetable"]

        tmp_links = list(data["links"].items())
        for day, timetable in list(data[schedule_type]["timetable"].items()):

            for i, n in enumerate(data[schedule_type]["schedule"][day]):
                if type(n) == int:
                    data[schedule_type]["schedule"][day][i] = tmp_links[n][0]
                else:
                    data[schedule_type]["schedule"][day][i] = [tmp_links[n[0]][0], tmp_links[n[1]][0]]

            if not timetable:
                if not base_data[schedule_type]["timetable"][day]:
                    data[schedule_type]["timetable"][day] = data[schedule_type]["base_timetable"]
                else:
                    data[schedule_type]["timetable"][day] = base_data[schedule_type]["timetable"][day]

        result["links"] = data["links"]
        result["schedule"] = data[schedule_type]["schedule"]
        result["timetable"] = data[schedule_type]["timetable"]
        classes[_class] = result

    return classes


def getFullSchedule():
    path = "static/schedules/"
    filenames = os.listdir(path)
    schedules = {}
    for filename in filenames:
        filename = os.path.join(path, filename)
        if os.path.isdir(filename):
            schedules.update(getShiftSchedule(filename))

    return schedules


def getJsonData(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data


TRANSLATION = {
    "Monday":    {"eng": "Monday",    "ru": "Понедельник", "kz": "Дүйсенбі"},
    "Tuesday":   {"eng": "Tuesday",   "ru": "Вторник",     "kz": "Сейсенбі"},
    "Wednesday": {"eng": "Wednesday", "ru": "Среда",       "kz": "Сәрсенбі"},
    "Thursday":  {"eng": "Thursday",  "ru": "Четверг",     "kz": "Бейсенбі"},
    "Friday":    {"eng": "Friday",    "ru": "Пятница",     "kz": "Жұма"},
    "empty" :    {"eng": "No lessons for this day", "ru": "На этот день нет уроков", "kz": "Бұл күнге сабақ жоқ"},
    
    "Select grade":      {"eng": "Select grade", "ru": "Выберите класс", "kz": "Сыныпты таңданыз"},
    "technical support": {"eng": "technical support", "ru": "техническая поддержка", "kz": "техникалық көмек"},
    "attendance":        {"eng": "attendance", "ru": "посещаемость", "kz": "қатысушылар саны"},
    "Grades":            {"eng": "Grades", "ru": "Классы", "kz": "Сыныптар"},
    "reload alert":      {"eng": "don\'t forget to reload the page", "ru": "не забывайте перезагружать страницу", "kz": "парақты қайта жүктеуді ұмытпаңыз"},

    "11A":   {"eng": "11 A",  "ru": "11 А",  "kz": "11 А"},
    "11A'":  {"eng": "11 A'", "ru": "11 А'", "kz": "11 Ә"},
    "11G'":  {"eng": "11 G'", "ru": "11 Г'", "kz": "11 Ғ"},
    "11-1":  {"eng": "11/1",  "ru": "11/1",  "kz": "11/1"},
    "11-2":  {"eng": "11/2",  "ru": "11/2",  "kz": "11/2"},
    
    "class time": {"eng": "Class time", "ru": "Кл час", "kz": "Сын сағ"},
    "english 1":  {"eng": "Eng 1", "ru": "Англ яз 1", "kz": "Ағылшын т. 1"},
    "english 2":  {"eng": "Eng 2", "ru": "Англ яз 2", "kz": "Ағылшын т. 2"},
    "algebra":    {"eng": "Algebra", "ru": "Алгебра", "kz": "Алгебра"},
    "geometry":   {"eng": "Geometry", "ru": "Геометрия", "kz": "Геометрия"},
    "cs 1":       {"eng": "CS 1", "ru": "Информатика 1", "kz": "Информатика 1"},
    "cs 2":       {"eng": "CS 2", "ru": "Информатика 2", "kz": "Информатика 2"},
    "geography":  {"eng": "Geography", "ru": "География", "kz": "География"},
    "kaz lang":   {"eng": "Kaz lang", "ru": "Каз яз", "kz": "Қазақ т."},
    "kaz lit":    {"eng": "Kaz lit", "ru": "Каз литра", "kz": "Қазақ әдеб."},
    "rus lang 1": {"eng": "Rus lang 1", "ru": "Рус яз 1", "kz": "Орыс т. 1"},
    "rus lang 2": {"eng": "Rus lang 2", "ru": "Рус яз 2", "kz": "Орыс т. 2"},
    "physics":    {"eng": "Physics", "ru": "Физика", "kz": "Физика"},
    "chemestry":  {"eng": "Chemestry", "ru": "Химия", "kz": "Химия"},
    "biology":    {"eng": "Biology", "ru": "Биология", "kz": "Биология"},
    "kaz hist":   {"eng": "Kaz hist", "ru": "Ист. К.", "kz": "Қаз. тарихы"},
    "world hist": {"eng": "World hist", "ru": "Всемирка", "kz": "Дж. тарихы"},
    "": {}
}