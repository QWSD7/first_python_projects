#Заголовок программы
from random import *

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]


print('Приветствую тебя! Я магический шар, и я знаю ответ на любой твой вопрос!')
name = input('Как зовут тебя? ')
print('Привет ' + name.title())
while True:
    que = input('Какой вопрос хотел бы ты задать? \n')
    print(choice(answers))

    print(name.title() + ', у тебя ещё остались вопросы?')
    close=input().lower()

    if close == 'да':
        continue
    else:
        print('Возвращайся если возникнут вопросы!')
        break





