# Голосовой ассистент Зина
# Особенности:
- Средняя временная сложность O(n log n)
- Реализована "продвинутое понимание речи" (понимает любые лексические конструкции)
- Исключения учтены 
# Функционал 
- Ненавязчивая беседа (из прописанных диалоговых веток)
- Посоветовать Фильм или Игру 
- Расчитать индекс массы тела 
- Открыть youtube
- Выдать запрос пользователя в Google 
- Найти любую информацию из Wikipedia и кратко зачитать
- Повторить какую-либо фразу
- Сказать актуальную погоду на неделю 
# Доп. возможность 
Реализована локальная игра "Пиккало" (вопрос-ответ) реализовано в game.py 
для совместной игры с друзьями, вызов игры производится командой "Пиккало"
# Используемые технологии
Весь проект написан на чистом Python версии 3.10.4 
Список основных используемых пакетов: 
- speech_recognition # для распознования речи 
- pyttsx3 # для голосового вывода текста  
- os # для определения микрофона
- from bs4 import BeautifulSoup # для парсинга данных 
- requests # для получение страницы в интернете 
- random # для различных ответов из ветки диалогов и таких-же ответов 
- execfile # для включения game.py 
- from pydub import AudioSegment # для включения аудиофайла означающего начало работы
- from pydub.playback import play # для включения аудиофайла означающего начало работы
