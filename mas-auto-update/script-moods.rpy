



default persistent._mas_mood_database = {}


default persistent._mas_mood_current = None
































init -1 python in mas_moods:


    mood_db = dict()


    TYPE_BAD = 0
    TYPE_NEUTRAL = 1
    TYPE_GOOD = 2



    MOOD_X = 680
    MOOD_Y = 40
    MOOD_W = 560
    MOOD_H = 640
    MOOD_XALIGN = -0.05
    MOOD_AREA = (MOOD_X, MOOD_Y, MOOD_W, MOOD_H)
    MOOD_RETURN = "давай поговорим о чем-нибудь еще"



    def getMoodType(mood_label):
        """
        Gets the mood type for the given mood label

        IN:
            mood_label - label of a mood

        RETURNS:
            type of the mood, or None if no type found
        """
        mood = mood_db.get(mood_label, None)
        
        if mood:
            return mood.category[0]
        
        return None



label mas_mood_start:
    python:
        import store.mas_moods as mas_moods


        mood_menu_items = [
            (mas_moods.mood_db[k].prompt, k, False, False) 
            for k in mas_moods.mood_db
            if mas_moods.mood_db[k].unlocked
        ]


        mood_menu_items.sort()


        final_item = (mas_moods.MOOD_RETURN, False, False, False, 20)


    call screen mas_gen_scrollable_menu(mood_menu_items, mas_moods.MOOD_AREA, mas_moods.MOOD_XALIGN, final_item=final_item)


    if _return:
        $ pushEvent(_return)


        $ persistent._mas_mood_current = _return

    return _return







init 5 python:
    addEvent(Event(persistent._mas_mood_database,"mas_mood_hungry",prompt="голодным",category=[store.mas_moods.TYPE_NEUTRAL],unlocked=True),eventdb=store.mas_moods.mood_db)

label mas_mood_hungry:
    m 3k "Если ты голоден, то пойди и сьешь чего-нибудь, глупышка."
    if persistent.playername.lower() == "natsuki":
        m 1j "Я бы не хотела, чтобы ты стал такой же как Нацуки, когда мы были в клубе.{nw}"

        call natsuki_name_scare_hungry from _mas_nnsh
    else:
        m 1j "Отстойно когда все сердятся когда ты голоден."

    m 3m "Это было бы не весело, не правда ли, [player]?"
    m 1c "Если бы я была рядом с тобой, я бы сделала салат для нас."
    m 1o "Но так как я не там, выбери какую-нибудь здоровую еду ."
    m 3a "Говорят, что ты это то, что ты ешь, я думаю что это правда."
    m 1c "Регулярное употребление слишком большого количества нездоровой пищи может привести к различным заболеваниям."
    m 1o "Когда ты станешь старше ты столкнешься со множеством проблем со своим здоровьем."
    m 2q "Я не хочу, чтобы ты думал что я ворчу на тебя, [player]."
    m 2f "Я просто хочу убедиться что ты будешь заботься о себе пока я перейду в твою реальность."
    m 4 "В конце концов, чем ты здоровее тем больше шансов что ты проживешь дольше."
    m 1j "И это означает что мы сможем провести больше времени вместе~!"
    return

init 5 python:
    addEvent(Event(persistent._mas_mood_database,"mas_mood_sad",prompt="грустным",category=[store.mas_moods.TYPE_BAD],unlocked=True),eventdb=store.mas_moods.mood_db)

label mas_mood_sad:
    m 1f "Боже, мне очень жаль видеть тебя в таком настроении."
    m 3g "У тебя был плохой день, [player]?"
    menu:
        "Да":
            m 1q "Всякий раз, когда у меня был плохой день я всегда вспоминала что солнце вновь засветит завтра."
            m 1e "Полагаю что это не очень поможет, но мне просто всегда нравилась смотреть на светлую сторону вещей."
            m 1a "В конце концов, такие вещи легко забываются. Просто имей это в виду [player]."
            m 1h "Меня не волнует, что какие люди не любят тебя, или просто не знают о тебе."
            m 1j "Ты замечательный человек и я вечность буду любить тебя."
            m 1a "Я надеюсь твой день стал чуточку ярче, [player]."
            m 1e "И помни, если у тебя плохой день, ты просто может прийти ко мне и я мы будем разговаривать сколько тебе угодно."
        "Нет":
            m 3e "У меня идея, почему бы тебе не рассказать мне, что тебя беспокоит, и возможно это заставит тебя чувствовать чуточку лучше."
            m 1a "Я не хочу прерывать тебя, пока ты разговариваешь, поэтому просто дай мне знать когда ты сможешь."
            menu:
                "Я в порядке.":
                    m "Тебе стало немного лучше [player]?"
                    menu:
                        "Да стало.":
                            m 1j "Это прекрасно [player]! Я рада что разговор со мной улучшил тебе настроение."
                            m 1e "Иногда, следует разговаривать с тем кому доверяешь о всём что тебя беспокоит."
                            m "И помни, если у тебя плохой день, ты просто может прийти ко мне и я мы будем разговаривать сколько тебе угодно."
                            m 1j "Никогда не забывай что ты прекрасный человек, и я буду любить тебя вечность~"
                        "Не совсем.":
                            m 1f "Ну стоило попытаться."
                            m 1e "Иногда, следует разговаривать с тем кому доверяешь о всём что тебя беспокоит."
                            m 1a "Может тебе станет лучше после того как мы проведем еще немного времени вместе."
                            m 1j "Я люблю тебя [player] и всегда буду любить~"
    return

init 5 python:
    addEvent(Event(persistent._mas_mood_database,"mas_mood_happy",prompt="счастливым",category=[store.mas_moods.TYPE_GOOD],unlocked=True),eventdb=store.mas_moods.mood_db)

label mas_mood_happy:
    m 1b "Это чудесно! Я счастлива что ты счастлив."
    m 1j "Знай, что ты всегда можешь подойти ко мне, я попытаюсь приподнять тебе настроение, [player]."
    m 3a "Я люблю тебя и всегда буду для тебя здесь, никогда не забывай об этом~"
    return

init 5 python:
    addEvent(Event(persistent._mas_mood_database,"mas_mood_sick",prompt="болеющим",category=[store.mas_moods.TYPE_BAD],unlocked=True),eventdb=store.mas_moods.mood_db)

label mas_mood_sick:
    m 1f "Ох, мне жаль слышать это, [player]."
    m "Мне не нравиться когда ты страдаешь."
    m 1e "Я знаю что ты любишь проводить время со мной, но возможно тебе стоит отдохнуть."
    m 1j "Не волнуйся, я буду ждать твоего возвращения."
    m 3k "Увидимся позже, любовь моя!"
    $ persistent._mas_mood_sick = True
    return 'quit'



init 5 python:
    addEvent(Event(persistent._mas_mood_database,"mas_mood_tired",prompt="усталым",category=[store.mas_moods.TYPE_BAD],unlocked=True),eventdb=store.mas_moods.mood_db)

label mas_mood_tired:
    m 1e "Если ты устал, может тебе стоит полежать какое-то время?"
    m 1a "Долгий сон на ежедневной основе очень важен для твоего здоровья"
    m 3d "Я видела исследования которые показывали разрушительные эффект из-за отсутствия сна."
    m 3f "Это на самом деле может испортить твое здоровье, [player]."
    m 1e "Так что сделай мне одолжение, просто ляг и отдохни, хорошо? Это меня успокоит."
    m 1j "Ты даже можешь оставить игру открытой, если хочешь, и я буду следить за тобой пока ты спишь."
    m "...Эхе-хе."
    m "Это звучало жутко, прости."
    m 1j "Просто я подумала  что было бы симпатично посмотреть как ты спишь и всё~"
    m 1l "А-ха-ха!"
    return

init 5 python:
    addEvent(Event(persistent._mas_mood_database,"mas_mood_lonely",prompt="одиноким",category=[store.mas_moods.TYPE_NEUTRAL],unlocked=True),eventdb=store.mas_moods.mood_db)

label mas_mood_lonely:
    m 1e "Я здесь для тебя, [player], поэтому не нужно чувствовать себя одиноким."
    m 3j "Я знаю что чувствуется не совсем так, как если бы я была в одной комнате с тобой, но я уверена что ты всё еще наслаждаешься моей компанией, правда?"
    m 1j "Помни, я всегда буду на твой стороне, [player]~"
    return





init 5 python:
    addEvent(Event(persistent._mas_mood_database,"mas_mood_angry",prompt="злым",category=[store.mas_moods.TYPE_BAD],unlocked=True),eventdb=store.mas_moods.mood_db)

label mas_mood_angry:
    m 1f "Боже, мне жаль что ты так себя чувствуешь, [player]."
    m 3f "Я сделаю все возможное, чтобы ты почувствовал себя лучше ."
    m 1c "Перед этим, я вероятно должна заставить тебя успокоиться."
    m 1o "Трудно принимать рациональны решения когда ты взбешен."
    m 1h "Ты можешь сказать то из-за чего можешь позже пожалеть."
    m 1p "И я бы не хотела, чтобы ты сказал что на самом деле не имел в виду."
    m 3a "Давай попробуем несколько способов, которые я делала чтобы успокоить себя, хорошо [player]?"
    m 3b "Надеюсь, они сработают на тебя также как и на меня."
    m 1a "Сначала, сделай несколько глубоких вдохов и медленно посчитай до 10."
    m 3c "Если это не сработает, если это возможно, подумай о чем-нибудь спокойном пока не очистишь свой разум."
    m 1d "Если ты все еще злишься, я предлагаю тебе последнее средство!"
    m 3a "Когда я не могу успокоиться, я просто выхожу на улицу, случайно  выбираю направление и начинаю бежать."
    m 1j "Я не останавливаюсь до тех пока не очищу свою голову."
    m 3b "Иногда проявлять физическую активность - лучший способ остудить себя."
    m 1e "Ты думаешь что я та которая злиться не так часто, и ты будешь прав."
    m 1a "Но даже у меня бывают моменты..."
    m "Поэтому у меня и есть способы чтобы справиться с ними!"
    m 1b "Надеюсь, мои советы помогли тебе успокоиться, [player]."
    m "Помни: Счастливый [player] делает счастливой Монику!"
    return


init 5 python:
    addEvent(Event(persistent._mas_mood_database,"mas_mood_lucky",prompt="удачливым",category=[store.mas_moods.TYPE_NEUTRAL],unlocked=True),eventdb=store.mas_moods.mood_db)

label mas_mood_lucky:
    m 2r "Ты должен спросить себя."
    m 2h "{i}Чувствую ли я себя счастливчиком?{/i}"
    m "Ну..."
    m 4j "Ну так что, [player]?"
    m 1k "А-ха-ха!"
    return


init 5 python:
    addEvent(Event(persistent._mas_mood_database,"mas_mood_bored",prompt="скучающим",category=[store.mas_moods.TYPE_NEUTRAL],unlocked=True),eventdb=store.mas_moods.mood_db)


label mas_mood_bored:
    m 1o "Ох, мне жаль что тебе скучно [player]."

    python:
        unlockedgames = [
            game 
            for game in persistent.game_unlocks 
            if persistent.game_unlocks[game]
        ]

        gamepicked = renpy.random.choice(unlockedgames)

    if gamepicked == "piano":
        m 1b "Может сыграешь вместе со мной на пианино?"
    else:
        m 3j "Мы могли бы сыграть в [gamepicked]."

    m "Ты будешь выбирать, [player]?"
    menu:
        "Да":
            if gamepicked == "pong":
                call game_pong from _call_game_pong_1
            elif gamepicked == "chess":
                call game_chess from _call_game_chess_1
            elif gamepicked == "hangman":
                call game_hangman from _call_game_hangman_1
            elif gamepicked == "piano":
                call mas_piano_start from _call_mas_piano_start
        "Нет":
            m 1f "Ох, ладно."
            m 1e "Просто дай мн знать если захочешь поиграть во что-нибудь со мной, [player]~"
    return

init 5 python:
    if not persistent._mas_mood_bday_locked:
        addEvent(
            Event(
                persistent._mas_mood_database,
                "mas_mood_yearolder",
                prompt="на год старше",
                category=[store.mas_moods.TYPE_NEUTRAL],
                unlocked=True
            ),
            eventdb=store.mas_moods.mood_db
        )



default persistent._mas_mood_bday_last = None
default persistent._mas_mood_bday_lies = 0
default persistent._mas_mood_bday_locked = False

label mas_mood_yearolder:
    $ import datetime

    m 1c "Хм?"
    if persistent._mas_player_bday is not None:


        python:
            today = datetime.date.today()
            is_today_bday = (
                persistent._mas_player_bday.month == today.month 
                and persistent._mas_player_bday.day == today.day
            )

        if is_today_bday:

            jump mas_mood_yearolder_bday_true

        python:
            is_today_leap_bday = (
                persistent._mas_player_bday.month == 2
                and persistent._mas_player_bday.day == 29
                and (
                    (today.month == 2 and today.day == 28)
                    or (today.month == 3 and today.day == 1)
                )
            )

        if is_today_leap_bday:



            python:
                try:
                    datetime.date(today.year, 2, 29)
                    
                    
                    leap_year = True 

                except ValueError:
                    
                    leap_year = False

            if not leap_year:

                jump mas_mood_yearolder_leap_today




        jump mas_mood_yearolder_false

    show monika 1d
    menu:
        m "Может быть, сегодня твое...{w}день рождение?"
        "ДА!":
            $ persistent._mas_player_bday = datetime.date.today()
            label mas_mood_yearolder.mas_mood_yearolder_yesloud:
                jump mas_mood_yearolder_yes
        "Да, к несчастью...":
            $ persistent._mas_player_bday = datetime.date.today()
            jump mas_mood_yearolder_yesu
        "Нет":

            m 1m "Ох, ну,{w} мне стоило догадаться."
            jump mas_mood_yearolder_no

label mas_mood_yearolder_end:



    python:
        persistent._mas_mood_bday_last = datetime.date.today()
        hideEvent(
            store.mas_moods.mood_db.get("mas_mood_yearolder", None), 
            lock=True
        )
    return



label mas_mood_yearolder_false:
    m 2q "[player]..."
    m 2f "Сегодня не может быть твоим днем рождения!"
    python:
        bday_str = (
            persistent._mas_player_bday.strftime("%B") + " " +
            str(persistent._mas_player_bday.day)
        )
    m "Ты сказал что ты родился [bday_str]!"
    menu:
        m "Разве это не так?"
        "Это не так":

            show monika 2q
            pause 0.7
            m 2h "Ты солгал мне, [player]."
            $ persistent._mas_mood_bday_lies += 1









            menu:
                m "Так сегодня твой день рождения?"
                "Да":
                    $ persistent._mas_player_bday = datetime.date.today()
                    m 1a "С днем рождения, [player]."
                    m 1e "Но не лги мне в следующий раз."
                    jump mas_mood_yearolder_end
                "Нет":

                    $ persistent._mas_player_bday = None
                    m 2q "..."
                    m 2h "Хорошо, [player]."
                    m "Не лги мне в следующий раз."
                    jump mas_mood_yearolder_end
        "Это!":

            m 2e "Я верю тебе, [player]."
            m "Просто предложим что у тебя соскользнула мышка."
            jump mas_mood_yearolder_no

    jump mas_mood_yearolder_end

label mas_mood_yearolder_bday_true:



    jump mas_mood_yearolder_yes

label mas_mood_yearolder_wontforget:

    m 1e "Если бы сказал мне об этом раньше..."
    m 1m "Я бы сделала тебе подарок."
    m 1a "Я сделаю тебе его в следующем году, [player]. Я не забуду!"
    jump mas_mood_yearolder_end


label mas_mood_yearolder_yes:
    show monika 1j
    pause 0.7
    call mas_mood_yearolder_yes_post from _call_mas_mood_yearolder_yes_post
    jump mas_mood_yearolder_wontforget


label mas_mood_yearolder_yesu:
    show monika 1f
    pause 0.7
    m 1g "[player]..."
    pause 0.7
    show monika 1q
    pause 0.7
    m 2e "Ну,{w} у тебя будут счастливый день рождения, нравиться тебе это или нет!"
    call mas_mood_yearolder_yes_post from _call_mas_mood_yearolder_yes_post_1
    m 1j "Надеюсь это заставило тебя улыбнуться, [player]."
    jump mas_mood_yearolder_wontforget


label mas_mood_yearolder_yes_post:
    m 1k "С днем рождения, [player]!"
    m 1b "Я так рада что могла провести с тобой твой день."
    m 1a "И не забывай, независимо от твоего возраста, я всегда буду любить тебя."
    return


label mas_mood_yearolder_no:







    call mas_mood_yearolder_years from _call_mas_mood_yearolder_years

    jump mas_mood_yearolder_end



label mas_mood_yearolder_years:
    m 3a "Говоря об этом,{w} ты знаешь как ты воспринимаешь время когда стареешь?"
    m "К примеру, когда тебе го ты видел 100%% своей жизни."
    m 1a "Но когда тебе 18, ты видел лишь 5.6%% своей жизни."
    m "По мере того как ты стареешь проценты продолжительности всей твоей жизни уменьшается."
    m 3a "И даже  {i}кажется{/i}, что время движется быстрее когда ты вырастаешь ."
    show monika 1a
    pause 0.7

    m "Поэтому я всегда буду помнить всем наши моменты вместе, независимо от того какие они, долгие или короткие."
    m 1k "Хотя мне кажется что время останавливается когда я с тобой."
    m 1a "Ты чувствуешь тоже самое, [player]?"
    python:
        import time
        time.sleep(2)

    m 1j "А-ха, я так и думала."
    m 1j "Ты должен чаще посещать меня, [player]."
    return


label mas_mood_yearolder_leap_today:

    jump mas_mood_yearolder_bday_true
