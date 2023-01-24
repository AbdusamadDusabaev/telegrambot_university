from telebot.types import ReplyKeyboardMarkup, KeyboardButton


class Markup:

    # Выбор города

    @staticmethod
    def cities_markup():
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        city_1 = KeyboardButton("Воронеж")
        city_2 = KeyboardButton("Орёл")
        city_3 = KeyboardButton("Мценск")
        city_4 = KeyboardButton("Ливны")
        city_5 = KeyboardButton("Карачев")
        city_6 = KeyboardButton("Борисоглебск")
        markup.row(city_1, city_2)
        markup.row(city_3, city_4)
        markup.row(city_5, city_6)
        return markup

    # Выбор университетов

    @staticmethod
    def universities_markup(city):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        if city == "Воронеж":
            university_1 = KeyboardButton("ВГУ")
            markup.row(university_1)
        elif city == "Орёл":
            university_1 = KeyboardButton("ОГУ им. И.С. Тургенева")
            university_2 = KeyboardButton("ОГИК")
            university_3 = KeyboardButton("ОГАУ имени Н.В. Парахина")
            markup.row(university_1)
            markup.row(university_2)
            markup.row(university_3)
        elif city == "Карачев":
            university_1 = KeyboardButton("Карачевский Филиал ОГУ им. И.С. Тургенева")
            markup.row(university_1)
        elif city == "Ливны":
            university_1 = KeyboardButton("Ливенский Филиал ОГУ им. И.С. Тургенева")
            markup.row(university_1)
        elif city == "Мценск":
            university_1 = KeyboardButton("Мценский Филиал ОГУ им. И.С. Тургенева")
            markup.row(university_1)
        elif city == "Борисоглебск":
            university_1 = KeyboardButton("Борисоглебский Филиал ВГУ")
            markup.row(university_1)
        all_city = KeyboardButton("Выбрать другой город")
        markup.row(all_city)
        return markup

    # Выбор раздела университета

    @staticmethod
    def sections_university_markup(university, city):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        if university != "ОГИК":
            section_direction = KeyboardButton(f"Направления {university}")
            markup.row(section_direction)
        else:
            section_direction = KeyboardButton(f"Учебный план в {university}")
            markup.row(section_direction)
        section_dormitories = KeyboardButton(f"Общежития в {university}")
        section_time_of_work_admission_committee = KeyboardButton(f"Приемная комиссия {university}")
        section_documents = KeyboardButton(f"Документы для поступления в {university}")
        section_points = KeyboardButton(f"Баллы для поступления в {university}")
        section_free_places = KeyboardButton(f"Количество бюджетных мест в {university}")
        section_price = KeyboardButton(f"Стоимость образования в {university}")
        section_exam = KeyboardButton(f"Вступительные испытания в {university}")
        markup.row(section_dormitories)
        markup.row(section_time_of_work_admission_committee)
        markup.row(section_documents)
        markup.row(section_points)
        markup.row(section_free_places)
        markup.row(section_price)
        markup.row(section_exam)
        if university in ["ОГАУ имени Н.В. Парахина", "ОГИК", "ВГУ", "Борисоглебский Филиал ВГУ"]:
            section_successful_list = KeyboardButton(f"Списки зачисленных в {university}")
            markup.row(section_successful_list)
        all_university = KeyboardButton(f"Все университеты в городе {city}")
        markup.row(all_university)
        return markup

    # Выбор формата обучения

    @staticmethod
    def choose_education_format(university):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        format_1 = KeyboardButton(f"Очная форма обучения в {university}")
        format_2 = KeyboardButton(f"Заочная форма обучения в {university}")
        format_3 = KeyboardButton(f"Очно-заочная форма обучения в {university}")
        other_direction = KeyboardButton(f"Все разделы {university}")
        markup.row(format_1)
        markup.row(format_2)
        markup.row(format_3)
        markup.row(other_direction)
        return markup

    @staticmethod
    def choose_education_price_format(university):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        format_1 = KeyboardButton(f"Списки зачисленных на бюджет в {university}")
        format_2 = KeyboardButton(f"Списки зачисленных на платное обучение в {university}")
        markup.row(format_1)
        markup.row(format_2)
        other_direction = KeyboardButton(f"Все разделы {university}")
        markup.row(other_direction)
        return markup

    @staticmethod
    def sections_direction_markup(university, direction_code):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        section_study_plan = KeyboardButton(f"Учебный план {direction_code}")
        markup.row(section_study_plan)
        if university in ["ОГУ им. И.С. Тургенева"]:
            section_information_about_enrollment = KeyboardButton(f"Списки зачисленных {direction_code}")
            markup.row(section_information_about_enrollment)
        other_direction = KeyboardButton(f"Все разделы {university}")
        markup.row(other_direction)
        return markup



