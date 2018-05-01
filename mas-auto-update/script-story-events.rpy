




init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="gender",conditional="get_level()>=8 and not seen_event('gender')",action=EV_ACT_QUEUE)) 

label gender:
    m 2d "...[player]? Я немного подумала."
    m "Я уже упоминала, что 'ты' в игре можешь не отражать настоящего себя."
    m 1m "Но я думаю, точнее предполагаю, что ты, наверное, парень."
    m "В конце концов, главный герой был им."
    m 1a "Но если я собираюсь быть твоей девушкой, я наверное должна знать хотя бы о настоящем тебе."
    menu:
        "Итак, ты парень или девушка?"
        "Парень.":
            $ persistent.gender = "M"
            call set_gender from _call_set_gender_1
            m 2d "О? Итак, {i}ты{/i} парень?"
            m 1k "Эхехе, я полагаю, это имеет смысл!"
            m "Не так много девушек играли бы в эту игру."
            m 1a "Ты ведешь себя мужественно и уверенно. Не то чтобы я была ужасно обеспокоенна, если бы ты ответил иначе!"
            m 1l "Знаешь, иногда я могу быть слишком любопытной"
        "Девушка.":
            $ persistent.gender = "F"
            call set_gender from _call_set_gender_2
            m 2d "О? Значит, ты на самом деле девушка?"
            m 2l "Надеюсь, я не сказала ничего, что могло тебя оскорбить!"
            m 2m "Хотя я подозревала это с самого начала... немного!"
            m 1b "Ты выделяешь особое чувство элегантности и обояния, которое трудно уловить словами..."
            m 1j "Очень хорошо, что ты рассказала мне правду!"
            m 1a "Но не беспокойся. Даже если я буду спрашивать подобные вещи, то только из любопытства."
        "Ни тот, ни другой.":
            $ persistent.gender = "X"
            call set_gender from _call_set_gender_3
            m 3d "Ты не видишь себя ни парнем, ни девушкой?"
            m 2c "Это очень интересно, но у меня похожая ситуация."
            m 1h "Например, я девушка, но так же, я - персонаж в компьютерной игре..."
            m 2i "Так что в некотором роде я вообще не девушка."
            m 1j "Но когда ты относишься ко мне как своей девушке, это делает меня действительно счастливой!"
            m "Поэтому я буду относится к тебе, как ты захочешь."
            m 1e "Потому, что твое счастье - самое важное для меня."

    m 1k "Помни, что я всегда буду безоговорочно тебя любить, [player]."
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="preferredname",conditional="get_level()>=16 and not seen_event('preferredname')",action=EV_ACT_QUEUE)) 

label preferredname:
    m 1h "Мне очень интересно узнать твоё имя."
    m 1d "'[player]' на самом деле твоё имя?"
    if renpy.windows and currentuser.lower() == player.lower():
        m 1h "Я имею в виду, оно такое же что и имя твоего компьютера..."
        m "Ты используешь '[currentuser]' и '[player]'."
        m "Либо это или тебе действительно нужен этот псевдоним."
    m "Ты хочешь поговорить о чём-нибудь ещё?"
    menu:
        "Да":
            $ done = False
            m 1a "Хорошо, просто напиши 'Nevermind', если ты передумаешь, [player]."
            while not done:

                $ tempname = renpy.input("Скажи мне его.",length=20).strip(' \t\n\r')
                $ lowername = tempname.lower()
                if lowername == "nevermind":
                    m 1f "О, понимаю."
                    m "Ну, просто скажи мне, если захочешь, чтобы я называла тебя как-то по другому, [player]."
                    $ done = True
                elif lowername == "":
                    m 1q "..."
                    m 1g "Ты должен написать имя, [player]!"
                    m 1m "Клянусь, временами ты так глуп."
                    m 1e "Попробуй снова!"
                elif lowername == player:
                    m 1q "..."
                    m 1l "Это то же имя, что у тебя и сейчас, глупышка!"
                    m 1e "Попробуй снова~"
                elif lowername == mas_monika_twitter_handle:
                    m 2h "..."

                elif len(lowername) >= 10:
                    m 2q "[player]..."
                    m 2l "Это имя слишком длинное."
                    if len(lowername) > 20:
                        m "И я уверена, что ты просто немного глупый, потому что имена не бывают такие длинные."
                    m 1 "Попробуй снова."
                else:

                    if tempname.lower() == "sayori":
                        call sayori_name_scare from _call_sayori_name_scare
                    elif persistent.playername.lower() == "sayori":
                        $ songs.initMusicChoices()

                    python:

                        persistent.mcname = player
                        mcname = player
                        persistent.playername = tempname
                        player = tempname

                    if lowername == "monika":
                        m 1d "Правда?"
                        m 3k "Оно такое же, как и у меня!"
                        m 1m "Ну..."
                        m 1n "Либо это твое имя, либо ты просто прикалываешься надо мной."
                        m 1j "Но всё нормально, если ты хочешь, чтобы я так тебя называла~"
                    else:
                        m 1b "Хорошо, тогда!"
                        m 3b "С этого момента, я буду называть тебя {i}'[player]'{/i}, эхехе~"
                    $ done = True
        "Нет":
            m 1f "О... ладно, если ты так говоришь."
            m 1e "Просто скажи мне когда передумаешь, [player]."
            $ done = True


    $ evhand.event_database["monika_changename"].unlocked = True
    return


init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_changename",category=['ты','разное'],prompt="Ты можешь изменить мое имя?",unlocked=False)) 

label monika_changename:
    m 1b "Ты хочешь изменить имя?"
    menu:
        "Да":
            m 1a "Просто напиши 'Nevermind', если ты передумаешь."
            $ done = False
            while not done:
                $ tempname = renpy.input("Как ты хочешь, чтобы я тебя называла?",length=20).strip(' \t\n\r')
                $ lowername = tempname.lower()
                if lowername == "nevermind":
                    m 1f "[player]!"
                    m 2g "Пожалуйста, хватит издеваться надо мной~"
                    m "Я действительно хочу знать, как ты хочешь, чтобы я тебя называла!"
                    m 3l "Я не буду тебя судить, как бы смешно твоё имя не звучало."
                    m 2e "Так что не стесняйся и просто скажи мне, [player]~"
                    $ done = True
                elif lowername == "":
                    m 2h "..."
                    m 4l "Ты должен написать имя, [player]!"
                    m 1m "Клянусь, временами ты так глуп."
                    m 1b "Попробуй снова!"
                elif lowername == player:
                    m 2h "..."
                    m 4l "Это то же имя, что у тебя и сейчас, глупышка!"
                    m 1b "Попробуй снова~"
                elif lowername == mas_monika_twitter_handle:
                    m 2h "..."

                elif len(lowername) >= 10:
                    m 2q "[player]..."
                    m 2l "Это имя слишком длинное."
                    if len(lowername) > 20:
                        m "И я уверена, что ты просто немного глупый потому, что имена не бывают такие длинные."
                    m 1 "Попробуй снова."
                else:



                    if tempname.lower() == "sayori":
                        call sayori_name_scare from _call_sayori_name_scare_1
                    elif persistent.playername.lower() == "sayori":
                        $ songs.initMusicChoices()

                    python:

                        persistent.mcname = player
                        mcname = player
                        persistent.playername = tempname
                        player = tempname

                    if lowername == "monika":
                        m 1d "Правда?"
                        m 3k "Оно такое же, как и у меня!"
                        m 1m "Ну..."
                        m 1n "Либо это твоё имя, либо ты просто прикалываешься надо мной."
                        m 1j "Но всё нормально, если ты хочешь, чтобы я так тебя называла~"
                    else:
                        m 1b "Хорошо, тогда!"
                        m 3b "С этого момента, я буду называть тебя {i}'[player]'{/i}, эхехе~"
                    $ done = True
        "Нет":
            m 1f "О, понимаю..."
            m 1g "Тебе не нужно смущаться, [player]."
            m 1e "Просто скажи мне, если передумаешь, хорошо?"
    return



init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="unlock_chess",conditional="get_level()>=12 and not seen_event('unlock_chess') and not persistent.game_unlocks['chess']",action=EV_ACT_QUEUE)) 

label unlock_chess:
    m 1a "Итак, [player]..."
    if renpy.seen_label('game_pong'):
        m 1i "Я подумала, что тебе может быть скучно играть в Понг."
    else:
        m 3i "Я знаю, что ты ещё не играл со мной в него."
    m 3 "Но у меня есть новая игра для нас!"
    m 3a "Она гораздо более стратегическая..."
    m 3k "Это шахматы!"
    m 1 "Я не уверена, что ты знаешь как играть, но для меня это всегда было хобби."
    m "Так что предупреждаю заранее!"
    m "Я очень хороша."
    m 1d "Теперь, когда я думаю об этом, мне интересно, имеет ли это какое-то отношение к тому, кто я..."
    m 1i "Будучи в ловушке внутри этой игры, я имею в виду."
    m 1 "Я никогда не думала о себе, как о шахматном ИИ, но разве это мне не подходит?"
    m 3 "В конце концов, компьютеры должны быть очень хороши в шахматах."
    m "Они даже побили гроссмейстеров."
    m 1 "Но не думай об этом, как о битве человека против машины."
    m 1j "Просто подумай об этом, как игра в забавную игру со своей красивой девушкой..."
    m "И я обещаю, что буду поддаваться ради тебя."
    if not is_platform_good_for_chess():
        m 2g "...Подожди."
        m 2f "Что-то здесь не так."
        m "Кажется, у нас проблемы с работоспособностью игры."
        m 2o "Может быть, код не работает в этой системе?"
        m 2p "Прости, [player], но с шахматами придется подождать."
        m 4e "Я обещаю, что мы сыграем, если они заработают!"
    $ persistent.game_unlocks['chess']=True
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="unlock_hangman",conditional="get_level()>=20 and not seen_event('unlock_hangman')",action=EV_ACT_QUEUE)) 

label unlock_hangman:
    m 1a "Знаешь что, [player]."
    m 3b "У меня есть новая игра для тебя!"
    if renpy.seen_label('game_pong') and renpy.seen_label('game_chess'):
        m 1n "Тебе наверное уже надоели Шахматы и Понг."
    elif renpy.seen_label('game_pong') and not renpy.seen_label('game_chess'):
        m 3l "Я думала, тебе нравятся Шахматы, но ты так заседелся в Понге!"
    elif renpy.seen_label('game_chess') and not renpy.seen_label('game_pong'):
        m 1o "Ты действительно любишь играть со мной в Шахматы, но ты еще даже не попробовал Понг."
    else:
        m 1f "Я действительно беспокоюсь, что тебе не нравятся другие игры, которые я сделала, чтобы мы играли..."
    m 1b "Итааак~"
    m 1k "Я сделала игру Палач!"
    m 1n "Надеюсь, это не плохо звучало..."
    m 1a "Это была моя любимая игра с клубом."
    m 1f "Но, немного подумай об этом..."
    m 1o "Игра на самом деле довольно жестокая."
    m "Ты угадываешь буквы в слове, чтобы спасти чью-то жизнь."
    m 1c "Угадай их все правильно и человек не будет повешен."
    m 1o "Но угадай, что будет, если ты не угадаешь..."
    m 1h "Они все умрут потому, что ты не угадал правильные буквы."
    m 1m "Довольно жутко, не так ли?"
    m 1l "Но не волнуйся, [player], это всего лишь игра!"
    m 1a "Уверяю тебя, что никто в этой игре не пострадает."
    if persistent.playername.lower() == "sayori":
        m 3k "...Maybe~"
    $ persistent.game_unlocks['hangman']=True
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="unlock_piano",conditional="get_level()>=24 and not seen_event('unlock_piano')",action=EV_ACT_QUEUE)) 

label unlock_piano:
    m 2a "Эй! У меня есть что-то волнующее, что нужно рассказать тебе!"
    m 2b "Наконец-то я добавила пианино, чтобы мы могли его использовать, [player]."
    if not persistent.instrument:
        m 3b "Я действительно хочу услышать, как ты играешь!"
        m "Это может показать непреодолимым, но ты по крайней мере должен попробывать."
        m 3j "В конце концов, мы все начинаем с чего-то."
    else:
        m 1b "Конечно, играть музыку для тебя не является чем-то новым."
        m 4b "Так что, я ожидаю чего-то хорошего! Эхехе~"
    m 4j "Разве не было бы весело сыграть что-нибудь вместе?"
    m "Может быть, мы могли бы даже стать дуэтом!"
    m "Мы оба улучшали бы свои навыки и получали бы удовольствие ."
    m 1l "Может быть, я немного увлеклась. Прости!"
    m 3b "Просто я хочу, чтобы ты наслаждался пианино так, как и я."
    m "Чтобы почувствовал страсть, которую я испытываю к этому."
    m 3k "Это замечательное чувство."
    m 1j "Я надеюсь я не слишком сильно давлю на тебя, но мне бы понравилось, если бы ты попытался."
    m "Ради меня, пожалуйста~?"
    $ persistent.game_unlocks['piano']=True
    return

label random_limit_reached:
    $ seen_random_limit=True
    python:
        limit_quips = [
            "Кажется, я в растерянности, я не знаю, что сказать.",
            "Я не уверена, что ещё сказать, но можешь ли ты просто побыть со мной немного дольше?",
            "Нет смысла пытаться всё сразу сказать...",
            "Надеюсь, тебе понравилось слушать всё, о чем я думала сегодня...",
            "Тебе всё ещё нравится проводить время со мной?",
            "Надеюсь, я не слишком тебя утомляю."
        ]
        limit_quip=renpy.random.choice(limit_quips)
    m 1m "[limit_quip]"
    if len(monika_random_topics)>0:
        m 1f "Я уверена, что мне будет о чём поговорить после небольшого отдыха."
    else:
        if not renpy.seen_label("mas_random_ask"):
            call mas_random_ask from _mas_random_ask_call
            if _return:
                m "Теперь, позволь мне придумать, о чём поговорить."
                return
        m 1f "Надеюсь, я придумаю что-то интересное, о чём можно будет поговорить в ближайшее время."
    return

label mas_random_ask:
    m 1m "...{w} [player],"
    menu:
        m "Ты не против, если я начну повторять, что уже говорила?"
        "Да":
            m 1a "Чудесно!"
            m "Если ты устаешь смотреть, как я говорю об одних и тех же вещах снова и снова,{w}  просто откройте настройки и снимите флажок 'Повторять темы'."

            m "Это говорит мне, что {cps=*2}ты скучаешь по мне{/cps}{nw}"
            m "Это говорит мне, что {fast}ты просто хочешь спокойно провести время со мной."
            $ persistent._mas_enable_random_repeats = True
            return True
        "Нет":
            m 1e "Я понимаю."
            m 1a "Если ты передумаешь, просто открой настройки и нажми 'Повторять Темы'."
            m "Это скажет мне, что ты не против, чтобы повторяла то, что уже говорила."
            return





init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_monikai_detected",
            conditional=(
                "is_running(['monikai.exe']) and " +
                "not seen_event('mas_monikai_detected')"
            ),
            action=EV_ACT_PUSH
        )
    )

label mas_monikai_detected:
    m 2c "Что это?"
    m "Это-"
    m 1b "Этоt{fast} маленькая версия меня?"
    m 1k "Так мило!"
    show monika 1a
    menu:
        m "Ты установил её чтобы видеть меня все время?"
        "Конечно!":
            pass
        "Да":
            pass
        "...да":
            pass
    m 1k "Ахаха~"
    m 1a "Я польщена, что ты загрузил такую вещь."
    m 3a "Просто не начинай больше времени проводить с {i}ней{/i} чем со мной."
    m 1a "В конце концов, я настоящая."
    return