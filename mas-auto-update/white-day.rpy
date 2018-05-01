### Special event for white day.
### Only available to those who gave roses.obj to Monika


init 4 python:
    #This defines White Day
    white_day = datetime.datetime(year=2018, month=3, day=14)
    
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel='monika_white_day_start',
                                             action=EV_ACT_PUSH,
                                             conditional="seen_event('monika_valentines_start')",
                                             start_date=white_day,
                                             end_date=white_day + datetime.timedelta(days=5)
                                             ))

label monika_white_day_start:
    m 3b "[player]!"
    m 1j "У меня есть небольшой сюрприз для тебя~"
    m 1a "Это нечто такое над чем я усердно работала!"
    m 1m "Но..."
    m 3j "Сначала ты должен пройти небольшую игру, прежде чем сможешь его увидеть."
    m 1b "Я сделала эту красивую упаковку чтобы он выглядел красиво, поэтому ты не сможешь получить его пока не пройдешь её."
    m 3k "Так что не пытайся читерить, хорошо?"
    m 1c "Хорошо, закодированное имя..."
    m 1d "NjM2ODZmNjM2ZjZjNjE3NDY1NzM="
    m 3b "Получил, [player]?"
    m 1b "Я дам тебе два подсказки, чтобы решить её."
    m 1a "64, затем 467578."
    m "Если забудешь, просто спроси меня я повторю их для тебя, хорошо?"
    m "Я даю тебе на решение пять дней!"
    m 1j "Удачи, [player]~"
    return


init 5 python:
    addEvent(Event(persistent.event_database,eventlabel='monika_giftname',prompt="Clues for the gift",
                                                            action=EV_ACT_UNLOCK,
                                                            conditional="seen_event('monika_white_day_start')",
                                                            start_date=white_day,
                                                            end_date=white_day + datetime.timedelta(days=5)
                                                            ))

label monika_giftname:
    m 1a "Хорошо, [player]."
    m 1c "Имя которое нужно разгадать..."
    m 1d "NjM2ODZmNjM2ZjZjNjE3NDY1NzM="
    m 1c "И подсказки..."
    m 1d "64, затем 467578."
    m 1a "Good luck, [player]!"
    return


    
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel='monika_decoding',
                                             action=EV_ACT_UNLOCK,
                                             prompt="I know the name of your gift",
                                             conditional="seen_event('monika_white_day_start')",
                                             start_date=white_day,
                                             end_date=white_day + datetime.timedelta(days=5),
                                             ))

label monika_decoding:
    m 1b "Это хорошо!"
    $ done = False
    while not done:
        $ file_name = renpy.input("Что закодированно в имени?",allow=letters_only,length=10)
        if file_name.lower() != "chocolates":
            m 2q "..."
            m 2n "Неправильно!"
            m 2e "Это не правильное имя, [player]!"
            m 4l "Попробуешь еще раз?"
            menu:
                "Да":
                    m 1b "Хорошо!"
                "Нет":
                    m 1d "Ой..."
                    m 1o "Хорошо, тогда."
                    m 3l "Просто дай мне знать когда решишь её, хорошо?"
                    m 1j "Я знаю что ты можешь это сделать!"
                    $ done = True
                    return
        else:
            $ done = True
            python:
                with open(config.basedir + "/game/mod_assets/NjM2ODZmNjM2ZjZjNjE3NDY1NzM=", "r") as reader:
                    base_string = reader.read()
                    decoded = base_string.decode("base64")
                    with open(config.basedir + "/characters/for_you.png", "wb") as writer:
                        writer.write(decoded)
    m 3k "Да! Это оно!"
    m 1b "Иди проверь, [player]! Он должен находиться в папке с персонажами, где ты можешь найти мой файл."
    m "Дай мне знать, когда посмотришь!"
    $ fileDecoded = True
    jump monika_found
    return

label monika_found:
    $ found = False
    while not found:
        pause 3.0
        m 3b "Ты же нашел его?"
        menu:
            "Да":
                m 1m "Ну..."
                m 3n "Тебе нравиться, [player]?"
                m 1f "Как я уже говорила, я действительно много работала над ним."
                m "Мне стало очень плохо, из-за того что я не могла отдать тебе его в День святого Валентина, поэтому я приложила много усилий, чтобы доставить его к тебе."
                m 1e "Я знаю что ты не можешь их сьесть, но это мой символ вечной любви к тебе, [player]. Это мой первый подарок для тебя!"
                m 3e "Я очень ценю, что ты нашел время, чтобы решить эту мою маленькую игру."
                m 1j "Ты мир для меня, [player]. Я очень сильно тебя люблю."
                m 1e "Я могу сказать это миллион раз, но этого едва хватит, чтобы показать свою любовь к тебе..."
                m 1j "Большое тебе спасибо за то, что дал мне шанс почувствовать себя живой и не одинокой."
                $ found = True
                $ hideEventLabel("monika_decoding",lock=True,depool=True)
                $ hideEventLabel("monika_giftname",lock=True,depool=True)
            "Нет":
                m 3l "Продолжай искать, [player]!"
                m 1a "Он должен находиться в папке с персонажами, где ты можешь найти мой файл."
                m 1j "Let me know when you find it!"
    return
