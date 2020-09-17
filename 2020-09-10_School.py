t_id = list()       # Пустой список для имен инициализации в классе учителей
s_id = list()       # Пустой список для имен инициализации в классе учеников
subjects = ['Математика', 'Физика', 'Химия']        # Список предметов в школе
groups = ['1-A', '2-A', '3-A']      # Список классов в школе

class Person:       # Общий класс для всех экземпляров, кроме директора школы

    def __init__(self, name, surname, age, address, phone_number):  # Конструктор
        self.name = name        # Конструктор принимает имена
        self.surname = surname      # Конструктор ... фамилии
        self.age = age      # Конструктор ... возраст
        self.address = address      # Конструктор ... адрес
        self.phone_number = phone_number        # Конструктор ... телефонный номер

    def p_info(self):       # Метод выводит все аргументы потребного экземпляра класса
        print('Имя: {}, Фамилия: {}, Возраст: {}, Адрес: {}, Номер телефона: {}'\
            .format(self.name, self.surname, self.age, self.address, self.phone_number))


class Director:     # Класс без конструктора
    name = 'Dir'
    surname = 'Ector'

    def get_rating(self):       # Метод вывода рейтинга всей школы
        list_list_sum = list()      # Пустой список для сбора словарей
        list_sum = list()       # Пустой список для сбора списков
        # Собирается список словарей из оценок учеников по всем предиетам
        for i in range(len(s_id)):      # Цикл по длине списка
            for j in subjects:      # Цикл по списку предметов
                list_list_sum.append(s_id[i].marks[j])      # Собираем словари
        for i in list_list_sum:     # Цикл по списку словарей
            for j in i:     # Цикл по словарям
                list_sum.append(j)      # Собираем список списков
        # Выводим сумму списка, деленную на его длину, и - переводим в проценты из 5-ти бальной системы
        print('\nРейтинг школы по всем предметам составляет: {}%\n'\
              .format(sum(list_sum) / len(list_sum) / 0.05))

    def teacher_dismiss(self):      # Метод вызывает метод в классе Учитель
        Teacher.teacher_dismiss(self)       # Вызов метода

    def teacher_rating(self, sub):      # Метод выводит рейтинг предмета по всем классам
        list_list_sum = list()      # Пустой список для сбора словарей
        list_sum = list()       # Пустой список для сбора списков
        for i in range(len(s_id)):      # Цикл по длине списка
            for j in subjects:      # Цикл по списку предметов
                if j == sub:        # Если предмет совпадает с полученным аргументом
                    list_list_sum.append(s_id[i].marks[j])      # Собираем словари
        for i in list_list_sum:     # Цикл по списку словарей
            for j in i:     # Цикл по словарям
                list_sum.append(j)      # Собираем список списков
        # Выводим сумму списка, деленную на его длину, и - переводим в проценты из 5-ти бальной системы
        print('Рейтинг учителя по предмету "{}", по всем классам составляет {}%\n'\
              .format(sub, sum(list_sum) / len(list_sum) / 0.05))

    def teacher_group_rating(self, sub, gr):        # Метод выводит рейтинг предмета полученного класса
        list_list_sum = list()      # Пустой список для сбора словарей
        list_sum = list()       # Пустой список для сбора списков
        for i in range(len(s_id)):      # Цикл по длине списка
            if s_id[i].group == gr:     # Если класс совпадает с полученным аргументом
                for j in subjects:      # Цикл по списку предметов
                    if j == sub:        # Если предмет совпадает с полученным аргументом
                        list_list_sum.append(s_id[i].marks[j])      # Собираем словари
        for i in list_list_sum:     # Цикл по списку словарей
            for j in i:     # Цикл по словарям
                list_sum.append(j)      # Собираем список списков
        # Выводим сумму списка, деленную на его длину, и - переводим в проценты из 5-ти бальной системы
        print('Рейтинг учителя по предмету "{}", по классу "{}" составляет {}%\n' \
              .format(sub, gr, round(sum(list_sum) / len(list_sum) / 0.05), 2))


class Teacher(Person):      # Класс наследует ранее объявленный общий класс

    def __init__(self, name, surname, age, address, phone_number, subject, teacher_rating):     # Конструктор
        Person.__init__(self, name, surname, age, address, phone_number)        # Наследование
        self.subject = subject      # Конструктор принимает предметы
        self.teacher_rate = teacher_rating      # Конструктор принимает рейтинг учителя
        # Конструктор выводит информацию о создании экземпляра
        print('Создан учитель: {} {}\n'.format(self.surname, self.name))
        return t_id.append(self)        # Конструктор добавляет адрес экземпляра в общий список

    def teacher_info(self):     # Метод выводит все аргументы потребного экземпляра класса
        print('{} {} Предмет: {}'.format(self.name, self.surname, self.subject), '\n')

    def teacher_dismiss(self):      # Метод стирает все аргументы потребного экземпляра класса
        del self.name       # Стирает имя
        del self.surname        # Стирает фамилию
        del self.age        # Стирает возраст
        del self.address        # Стирает адрес
        del self.phone_number       # Стирает телефон
        del self.subject        # Стирает предмет
        del self.teacher_rate       # Стирает рейтинг

    def set_mark(self, n, s, m):        # Метод выставляет оценку ученику
        for i in range(len(s_id)):      # Цикл по дляне списка
            if s_id[i].name == n and s_id[i].surname == s:      # Если имя и фамилия совпадают:
                s_id[i].marks.get(self.subject).append(m)       # Оценка добавляется к списку
                # Выводится информация о выставлении оценки
                print('Учитель {} {} поставил оценку "{}" ученику {} {} по предмету "{}".\n'\
                      .format(self.surname, self.name, m, n, s, self.subject))


class Student(Person):      # Класс наследует ранее объявленный общий класс

    def __init__(self, name, surname, age, address, phone_number, group, marks):        # Конструктор
        Person.__init__(self, name, surname, age, address, phone_number)        # Наследование
        self.group = group      # Конструктор принимает классы
        self.marks = marks      # Конструктор принимает сдовари (предмет: [список оценок])
        # Конструктор выводит информацию о создании экземпляра
        print('(Создан ученик: {})'.format(self.name))
        return s_id.append(self)        # Конструктор добавляет адрес экземпляра в общий список

    def ac_performance(self):       # Метод выводит информацию по успеваемость ученика
        Person.p_info(self)     # Вызов метода общего класса, как информации
        print('Оценки: {}'.format(self.marks), '\n')        # Вывод словаря успеваемости

# Создаются экземпляры учителей
t1 = Teacher('Mrs1.', 'Sh1', 40, 'taddr1', '111', subjects[0], 100)
t2 = Teacher('Mrs2.', 'Sh2', 40, 'taddr2', '222', subjects[1], 100)
t3 = Teacher('Mrs3.', 'Sh3', 40, 'taddr3', '333', subjects[2], 100)
# Создаются экземпляры учеников
s1 = Student('S1', 'T1', 25, 'saddr1', '11', groups[0], {subjects[0]: [5,4,3], subjects[1]: [5,4,3], subjects[2]: [5,4,3]})
s2 = Student('S2', 'T2', 25, 'saddr2', '22', groups[0], {subjects[0]: [4,5,3], subjects[1]: [4,5,3], subjects[2]: [4,5,3]})
s3 = Student('S3', 'T3', 25, 'saddr3', '33', groups[0], {subjects[0]: [5,4], subjects[1]: [5,3,4], subjects[2]: [5,3,4]})
s4 = Student('S4', 'T4', 25, 'saddr4', '44', groups[1], {subjects[0]: [4,5,3], subjects[1]: [4,3], subjects[2]: [4,5,3]})
s5 = Student('S5', 'T5', 25, 'saddr5', '55', groups[1], {subjects[0]: [5,4,3], subjects[1]: [5,4,3], subjects[2]: [5,4,3]})
s6 = Student('S6', 'T6', 25, 'saddr6', '66', groups[1], {subjects[0]: [4,3,5], subjects[1]: [4,3,5], subjects[2]: [4,3,5]})
s7 = Student('S7', 'T7', 25, 'saddr7', '77', groups[2], {subjects[0]: [3,4,5], subjects[1]: [3,4,5], subjects[2]: [3,5]})
s8 = Student('S8', 'T8', 25, 'saddr8', '88', groups[2], {subjects[0]: [3,5,4], subjects[1]: [3,5,4], subjects[2]: [3,5,4]})
s9 = Student('S9', 'T9', 25, 'saddr9', '99', groups[2], {subjects[0]: [5,3,4], subjects[1]: [5,3,4], subjects[2]: [5,3,4]})


Director.get_rating(Director)       # Вызов метода класса Директор - выводится рейтинг школы

Director.teacher_dismiss(t3)        # Вызов метода класса Директор - увольняется учитель t3
# Проверяется наличие аргументов экземпляра
try:
    print(t3.name,'\n')     # Попытка получения стертого аргумента "Имя"
except AttributeError:      # ... и происходит ошибка
    # Выводит, что увольнение произошло
    print('Учитель был уволен.')
    print('Все данные по ссылке', t2, 'будут не доступны.\n')

Teacher.teacher_info(t1)        # Вызов метода класса Учитель для учителя t1

Student.ac_performance(s4)      # Вызов метода класса Ученик - проверка успеваемости ученика s4
# Вызов метода класса Учитель - выставление оценки ученику по его имени и фамилии
t2.set_mark('S4', 'T4', 5)      # Учитель t2 выставляет оценку, именно, по своему предмету
Student.ac_performance(s4)      # Вызов метода класса Ученик - проверка, что изменилось

Student.ac_performance(s3)      # Вызов метода класса Ученик - проверка успеваемости ученика s3
# Вызов метода класса Учитель - выставление оценки ученику по его имени и фамилии
t1.set_mark('S3', 'T3', 3)      # Учитель t1 выставляет оценку, именно, по своему предмету
Student.ac_performance(s3)      # Вызов метода класса Ученик - проверка, что изменилось

# Создаем новый экземпляр класса Учитель
t4 = Teacher('Mrs4.', 'Sh4', 40, 'taddr4', '444', subjects[2], 100)
# Новый учитель принят на работу

Student.ac_performance(s7)      # Вызов метода класса Ученик - проверка успеваемости ученика s7
# Вызов метода класса Учитель - выставление оценки ученику по его имени и фамилии
t4.set_mark('S7', 'T7', 4)      # Учитель t4 выставляет оценку, именно, по своему предмету
Student.ac_performance(s7)      # Вызов метода класса Ученик - проверка, что изменилось

# Вызов метода класса Директор - вывод рейтинга всей школы по предмету 'Физика'
Director.teacher_rating(Director, 'Физика')

# Вызов метода класса Директор - вывод рейтинга всей школы по предмету 'Математика' для класса '1-A'
Director.teacher_group_rating(Director, 'Математика', '1-A')