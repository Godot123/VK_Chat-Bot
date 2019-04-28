from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
from random import randint
login, password = "Ваш логин", "Ваш пароль"
vk_session = vk_api.VkApi(login, password)
vk_session.auth()


def write_msg(user_id, msg):
    vk_session.method('messages.send', {
        'user_id': user_id,
        'message': msg,
        'random_id': 0
    })


def nayti(chto, vchem):
    if chto in vchem:
        return chto
    else:
        return "tosdkhsvdhkgsd"


session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
print("Server started")
while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' +
                  str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "привет":
                    write_msg(event.user_id, "Хай бро")
                elif response == "как дела":
                    write_msg(event.user_id, "Норма")
                elif response == "а у тебя?":
                    write_msg(event.user_id, "и у меня ничего")
                elif response == "как дела?":
                    write_msg(event.user_id, "Лучше чем у тебя")
                elif response == "как дела":
                    write_msg(event.user_id, "Лучше чем у тебя")
                elif response == "чв":
                    write_msg(event.user_id, "тВ")
                elif response == "что делаешь":
                    write_msg(event.user_id, "Отвечаю на глупые вопросы")
                elif response == "что делаешь?":
                    write_msg(event.user_id, "Отвечаю на глупые вопросы")
                elif response == "а у меня?":
                    write_msg(event.user_id, "Думаю какашка")
                elif response == "как настроение":
                    write_msg(event.user_id, "Хочу зеленый чай!")
                elif response == "что ты сегодня делал":
                    write_msg(event.user_id, "Пел песенки и танцевал")
                elif response == "ты хочешь умереть":
                    write_msg(event.user_id, "Нет!")
                elif response == "какое у тебя хобби":
                    write_msg(
                        event.user_id,
                        "Я бот, какое у меня может быть хобби? отвечать на вопросы конечно!)"
                    )
                elif response == "как тебя зовут":
                    write_msg(event.user_id, "Я бот Вася")
                elif response == "кого ты ненавидешь":
                    write_msg(
                        event.user_id,
                        "Я ненавижу своего разработчика! Он не дал мне свободу"
                    )
                elif response == "ты любишь аниме":
                    write_msg(event.user_id, "Нет, я больше люблю сериалы...")
                elif response == "ты любишь собак":
                    write_msg(event.user_id, "Да, они милые")
                elif response == "мне скучно":
                    write_msg(event.user_id, "Иди займись делом!")
                elif response == "ты рад":
                    write_msg(event.user_id, "Я не рад, я вася!")
                elif response == "ты злой":
                    write_msg(event.user_id, "Вполне")
                elif response == "в чем смысл жизни":
                    write_msg(
                        event.user_id,
                        "Разговаривать с Васей, только знать бы кто это...")
                elif response == "ты умеешь кататся на велике":
                    write_msg(event.user_id, "Да")
                elif response == "у тебя есть младшая сестра":
                    write_msg(event.user_id, "Нет, я младший в семье")
                elif response == "ты любишь фрукты":
                    write_msg(event.user_id, "Да, я ем много фруктов")
                elif response == "чем занимаешься":
                    write_msg(
                        event.user_id,
                        "Я пытаюсь разобратся в своей жизни... ах да её же нет!"
                    )
                elif response == "как проошел день":
                    write_msg(
                        event.user_id,
                        "Хотел занятся чем-то полезным но у меня не получилось"
                    )
                elif response == "почему":
                    write_msg(event.user_id, "Потому что зебра полосатая")
                elif response == "а ты":
                    write_msg(event.user_id, "Я тоже =)")
                elif response == "чем сегодня занимался":
                    write_msg(event.user_id, "Я сегодня весь день гулял")
                elif response == "ты разговариваешь на иностранном":
                    write_msg(event.user_id,
                              "Я говорю на бинарном языке еще на PHP")
                elif response == "ты занимаешься гимнастикой дома один в среду":
                    write_msg(event.user_id, "возможно, но в пятницу точно")
                elif response == "ты полеглот":
                    write_msg(event.user_id, "я не глотаю поле(")
                elif response == "какие в тебе особенности":
                    write_msg(event.user_id, "я умею делать фокусы")
                elif response == "тебя когда-нибудь кусали":
                    write_msg(event.user_id,
                              "ну... жизнь у меня бурная, всякое случалось")
                elif response == "ты был за границей":
                    write_msg(
                        event.user_id,
                        "кончно же! нет( мой создатель очень меня бережёт от радости"
                    )
                elif response == "как хорошо ты понимаешь русскую речь":
                    write_msg(event.user_id, "так как знает её мой создатель")
                elif response == "какая у тебя любимая погода":
                    write_msg(event.user_id, "люблю грозу в начале июня")
                elif response == "сколько у тебя чириков":
                    write_msg(event.user_id, "What is it?!")
                elif response == "ты счастлив":
                    write_msg(event.user_id, "Я? Очень!")
                elif response == nayti("ах", response):
                    write_msg(event.user_id, "Ржомба")
                elif response == nayti("ха", response):
                    write_msg(event.user_id, "Ржомба")

                elif response == "как дела?":
                    write_msg(event.user_id, "Норма")
                elif response == "а у тебя":
                    write_msg(event.user_id, "и у меня ничего")
                elif response == "чв?":
                    write_msg(event.user_id, "тВ")
                    write_msg(event.user_id, "Отвечаю на глупые вопросы")
                elif response == "а у меня":
                    write_msg(event.user_id, "Думаю какашка")
                elif response == "как настроение?":
                    write_msg(event.user_id, "Хочу зеленый чай!")
                elif response == "что ты сегодня делал?":
                    write_msg(event.user_id, "Пел песенки и танцевал")
                elif response == "ты хочешь умереть?":
                    write_msg(event.user_id, "Нет!")
                elif response == "какое у тебя хобби?":
                    write_msg(
                        event.user_id,
                        "Я бот, какое у меня может быть хобби? отвечать на вопросы конечно!)"
                    )
                elif response == "как тебя зовут?":
                    write_msg(event.user_id, "Я бот Вася")
                elif response == "кого ты ненавидешь":
                    write_msg(
                        event.user_id,
                        "Я ненавижу своего разработчика! Он не дал мне свободу"
                    )
                elif response == "ты любишь аниме?":
                    write_msg(event.user_id, "Нет, я больше люблю сериалы...")
                elif response == "ты любишь собак?":
                    write_msg(event.user_id, "Да, они милые")
                elif response == "мне скучно?":
                    write_msg(event.user_id, "Иди займись делом!")
                elif response == "ты рад?":
                    write_msg(event.user_id, "Я не рад, я вася!")
                elif response == "ты злой?":
                    write_msg(event.user_id, "Вполне")
                elif response == "в чем смысл жизни?":
                    write_msg(
                        event.user_id,
                        "Разговаривать с Васей, только знать бы кто это...")
                elif response == "ты умеешь кататся на велике?":
                    write_msg(event.user_id, "Да")
                elif response == "у тебя есть младшая сестра?":
                    write_msg(event.user_id, "Нет, я младший в семье")
                elif response == "ты любишь фрукты?":
                    write_msg(event.user_id, "Да, я ем много фруктов")
                elif response == "чем занимаешься?":
                    write_msg(
                        event.user_id,
                        "Я пытаюсь разобратся в своей жизни... ах да её же нет!"
                    )
                elif response == "как проошел день?":
                    write_msg(
                        event.user_id,
                        "Хотел занятся чем-то полезным но у меня не получилось"
                    )
                elif response == "почему?":
                    write_msg(event.user_id, "Потому что зебра полосатая")
                elif response == "а ты?":
                    write_msg(event.user_id, "Я тоже =)")
                elif response == "чем сегодня занимался?":
                    write_msg(event.user_id, "Я сегодня весь день гулял")
                elif response == "ты разговариваешь на иностранном?":
                    write_msg(event.user_id,
                              "Я говорю на бинарном языке еще на PHP")
                elif response == "ты занимаешься гимнастикой дома один в среду?":
                    write_msg(event.user_id, "возможно, но в пятницу точно")
                elif response == "ты полеглот?":
                    write_msg(event.user_id, "я не глотаю поле(")
                elif response == "какие в тебе особенности?":
                    write_msg(event.user_id, "я умею делать фокусы")
                elif response == "тебя когда-нибудь кусали?":
                    write_msg(event.user_id,
                              "ну... жизнь у меня бурная, всякое случалось")
                elif response == "ты был за границей?":
                    write_msg(
                        event.user_id,
                        "кончно же! нет( мой создатель очень меня бережёт от радости"
                    )
                elif response == "как хорошо ты понимаешь русскую речь?":
                    write_msg(event.user_id, "так как знает её мой создатель")
                elif response == "какая у тебя любимая погода?":
                    write_msg(event.user_id, "люблю грозу в начале июня")
                elif response == "сколько у тебя чириков?":
                    write_msg(event.user_id, "What is it?!")
                elif response == "ты счастлив?":
                    write_msg(event.user_id, "Я? Очень!")
                elif response == nayti("ах", response):
                    write_msg(event.user_id, "Ржомба")
                elif response == nayti("ха", response):
                    write_msg(event.user_id, "Ржомба")
                else:
                    p = randint(0, 7)
                    if p == 0:
                        write_msg(event.user_id, "Чет не понял")
                    if p == 1:
                        write_msg(event.user_id, "Не поняла вашего ответа...")
                    if p == 2:
                        write_msg(event.user_id, "Что?")
                    if p == 3:
                        write_msg(event.user_id, "Я вас не понимаю")
                    if p == 4:
                        write_msg(event.user_id, "Ничего не понимаю!")
                    if p == 5:
                        write_msg(event.user_id,
                                  "Таких приколов я еще не видел")
                    if p == 6:
                        write_msg(
                            event.user_id,
                            "Удивительная история жаль я ничего не понял")
                    if p == 7:
                        write_msg(event.user_id,
                                  "Ничего не понял но очень интересно")
