import webbrowser
import speech_recognition
import pyttsx3
import os
from bs4 import BeautifulSoup
import requests
import random
from past.builtins import execfile
import base
from pydub import AudioSegment
from pydub.playback import play


def play_voice_assistant_speech(text_to_speech):
    """
    Проигрывание речи ответов голосового ассистента (без сохранения аудио)
    :param text_to_speech: текст, который нужно преобразовать в речь
    """
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()


def record_and_recognize_audio(*args: tuple):
    """
    Запись и распознавание аудио
    """

    with microphone:
        recognized_data = ""

        # регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=0.5)
        recognizer.pause_threshold = 0.5
        try:
            # звук на включении
            sound = AudioSegment.from_mp3('start.wav')
            play(sound)
            audio = recognizer.listen(microphone, 5, 5)
            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())
        except RuntimeWarning:
            print('ffmpeg')

        except speech_recognition.WaitTimeoutError:
            play_voice_assistant_speech('Проверьте свой микрофон пожалуйста, я вас не слышу')
            print('Проверьте свой микрофон пожалуйста, я вас не слышу')
            return

        # использование online-распознавания через Google
        # (высокое качество распознавания)
        try:
            print("Подождите, я думаю...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        return recognized_data


def game_for_drink():
    """
    Запуск локальной игры из папки проекта "Пиккало"
    :return: запускает исполняемый файл игры из папки проекта
    """
    execfile('game.py')


def parser(url):
    """
    Основной парсер
    :param url: ссылка на ресурс с которого нужно запарсить
    :return: разметка страницы с помощю BeautifulSoup(r.text, 'html.parser')
    """
    # общий парсер
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(r.status_code)
    return soup


def games(soup):
    """
    Парсинг игр
    :param soup: основной парсер
    :return: рандомная игра из источника
    """
    game = soup.find_all('a', class_='name')
    clear_games = [g.text for g in game]
    game_for_human = random.choice(clear_games)
    return game_for_human


def films(soup):
    """
    Парсинг фильмов из источника
    :param soup: основной парсер
    :return: рандомный фильм из источника
    """
    film = soup.find_all('div', class_='nbl-slimPosterBlock__title')
    clear_films = [f.text for f in film]
    film_for_human = random.choice(clear_films)
    return film_for_human


def jokes(soup):
    """
    Парсинг шутки из источника
    :param soup: основной парсер
    :return: рандомная шутка из источника
    """
    joke = soup.find_all('div', class_='text')
    joke_clear = [f.text for f in joke]
    joke_for_human = random.choice(joke_clear)
    return joke_for_human


def find(soup):
    """
    Функция поиска определенной информации в Wikipedia
    :param soup: основной парсер
    :return: вывод запроса в википедии (голосовой)
    """
    impo = soup.find_all('p')
    impo_clear = [i.text for i in impo]
    return impo_clear[0]


def weather(soup, command):
    """
    Функция парсинга актуальной погоды в городе на неделю
    :param soup: основной парсер
    :param command: речь человека для распознания дня недели
    :return: запрос пользователя по погоде
    """
    weather = soup.find_all('div', class_='day-temperature')
    days = soup.find_all('div', class_='day-week')
    today = soup.find_all('span', {'class': 'dw-into'})
    today_clear = [t.text for t in today]
    only_days = [d.text.lower() for d in days]
    only_int = [w.text for w in weather]
    w_week = {}

    for i in range(len(only_days)):
        w_week.update({only_days[i]: only_int[i]})
        for key, value in w_week.copy().items():
            bufer = w_week.pop(key)
            if key in ["среда", "пятница", "суббота"]:
                w_week[key[:-1] + "у"] = bufer
            else:
                w_week[key] = bufer

    for human in command.lower().split():
        if human == 'сегодня':
            return human, only_int[0]
        elif human == 'завтра':
            return human, only_int[1]
        elif human == 'неделю':
            return human, w_week
        elif human in base.today_weather:
            return today_clear
        elif human in w_week:
            print(human)
            print(command.lower().split())
            return human, w_week[human]


def dollar():
    """
    Функция для вывода курса доллара
    :return:
    """
    URL_DOLLAR = (
        'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=rehc&aqs=chrome.1.69i57j0i10i131i433l5j0i10j0i10i131i433l2j0i10.2126j1j7&sourceid=chrome&ie=UTF-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }

    full_page = requests.get(URL_DOLLAR, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    print(full_page.status_code)
    convert = soup.findAll('span', {'class': 'DFlfde SwHCTb', 'data-precision': 2})
    return convert[0].text


def euro():
    """
    Функция для вывода актуального курса евро
    :return:
    """
    URL_EURO = (
        'https://www.google.com/search?q=rehc+tdhj&oq=rehc+tdhj+&aqs=chrome..69i57j0i10l9.1528j0j7&sourceid=chrome&ie=UTF-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    full_page = requests.get(URL_EURO, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    print(full_page.status_code)
    euro = soup.findAll('span', {'class': 'DFlfde SwHCTb', 'data-precision': 2})
    return euro[0].text


def index_mass():
    """
    Функция для расчета индекса массы тела
    :return:
    """
    while True:
        try:
            play_voice_assistant_speech('скажите свою массу только в цифрах после сигнала')
            mass = record_and_recognize_audio()
            play_voice_assistant_speech('скажите свой рост только в цифрах после сигнала')
            height = record_and_recognize_audio()
            mass = int(mass)
            height = int(height)
            height = height / 100
            index = mass // (height ** 2)
            print(mass, height, index)
            if index <= 16:
                return play_voice_assistant_speech(
                    f'у вас выраженный дефицит массы, ваш индекс равен {index}')

            elif 16 < index <= 18.5:
                return play_voice_assistant_speech(
                    f'у вас дефицит массы, ваш индекс равен {index}')

            elif 18.5 <= index <= 25:
                return play_voice_assistant_speech(
                    f'у вас все в порядке с массой, индекс равен {index}')

            elif 25 <= index <= 30:
                return play_voice_assistant_speech(
                    f'у вас есть избыточная масса, индекс равен {index}')

            elif 30 < index <= 35:
                return play_voice_assistant_speech(f'у вас первая степень ожирения, индекс равен {index}')

            elif 35 <= index <= 40:
                return play_voice_assistant_speech(
                    f'у вас вторая степень ожирения, индекс равен {index}')
            elif index > 40:
                return play_voice_assistant_speech(
                    f'у вас ожирение третьей степени, индекс равен {index}')

        except TypeError:
            play_voice_assistant_speech('Простите, я вас не расслышала, попробуйте еще раз')
        except ValueError:
            play_voice_assistant_speech('Простите, я вас не расслышала, попробуйте еще раз')


def main():
    while True:
        # отделение комманд от дополнительной информации (аргументов)
        # старт записи речи с последующим выводом распознанной речи
        # и удалением записанного в микрофон аудио
        voice_input = record_and_recognize_audio()
        os.remove("microphone-results.wav")
        print(voice_input)
        command = voice_input

        if command in base.byby:
            play_voice_assistant_speech(str(random.choice(base.byby_answer)))
            break
        for human in command.lower().split():
            if human in base.hi_human:
                play_voice_assistant_speech(str(random.choice(base.hi_bot)))
            elif human in base.say:
                play_voice_assistant_speech('что вы хотите чтобы я сказала ?')
                user = record_and_recognize_audio()
                play_voice_assistant_speech(user)
            elif human == 'пикколо':
                game_for_drink()
            elif human in base.zina:
                play_voice_assistant_speech(str(random.choice(base.zina_answer)))
            elif human in base.god:
                play_voice_assistant_speech(str(random.choice(base.god_answer)))
                break
            elif human in base.go:
                play_voice_assistant_speech(str(random.choice(base.go_answer)))
                break
            elif human in base.function:
                play_voice_assistant_speech(
                    'Я функциональный голосовой ассистент по имени Зина, могу подсказать погоду на неделю, актуальный курс доллара или евро, рассказать анекдот, посоветовать фильм или игру, так-же расчитать ваш индекс массы тела и провести ненавязчивую беседу')
            elif human in base.human_gratitude:
                play_voice_assistant_speech(f'{str(random.choice(base.bot_gratitude))}')
            elif human in base.question:
                play_voice_assistant_speech(str(random.choice(base.answer)))
            elif human in base.answer_human_question_g:
                play_voice_assistant_speech(str(random.choice(base.answer_bot_g)))
            elif human in base.answer_human_question_b:
                play_voice_assistant_speech(str(random.choice(base.answer_bot_b)))
            elif human in base.youtube:
                webbrowser.open('https://www.youtube.com/watch?v=SGt-ZWeiokk')
            elif human in base.find:
                URL = f'https://www.google.com/search?q={command}'
                webbrowser.open(URL)
                break
            elif human in base.info:
                play_voice_assistant_speech('что вы хотите знать?')
                user = record_and_recognize_audio()
                fiNd = parser(url=f'https://ru.m.wikipedia.org/wiki/{user}')
                play_voice_assistant_speech(str(find(fiNd)))
            elif human in base.human_dollar:
                play_voice_assistant_speech(f'за 1 доллар нынче просят, {dollar()} рублей')
            elif human in base.euro:
                play_voice_assistant_speech(f'нынче за 1 Евро просят, {euro()} рублей')
            elif human in base.human_weather:
                # погода
                weaTher = parser(url='https://world-weather.ru/pogoda/russia/fryazino/')
                play_voice_assistant_speech(f'погода на {str(weather(weaTher, command=voice_input))}')
                break
            elif human in base.game:
                # игры
                game = parser(url='https://metarankings.ru/new-games/')
                play_voice_assistant_speech(f'сегодня можно поиграть в {games(game)}')
            elif human in base.human_film:
                # фильмы
                film = parser(url='https://www.ivi.ru/collections/best-movies/page9')
                play_voice_assistant_speech(f'сегодня можно посмотреть фильм под названием: {films(film)}')
            elif human in base.joke:
                # шутки
                joke = parser(url='https://www.anekdot.ru/')
                play_voice_assistant_speech(jokes(joke))
            elif human in base.mass:
                index_mass()
                break


if __name__ == '__main__':
    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    # инициализация инструмента синтеза речи
    ttsEngine = pyttsx3.init()
    voices = ttsEngine.getProperty('voices')
    rate = ttsEngine.getProperty('rate')
    # noinspection PyTypeChecker
    ttsEngine.setProperty('rate', rate - 25)
    ttsEngine.setProperty('voice', 'ru')
    # noinspection PyTypeChecker
    for voice in voices:
        if voice.name == 'Anna':
            ttsEngine.setProperty('voice', voice.id)
    main()
