




default persistent._mas_you_chr = False

init -1 python in mas_greetings:

    def selectGreeting():
        """
        Selects a greeting to be used. This evaluates rules and stuff
        appropriately.

        RETURNS:
            a single greeting (as an Event) that we want to use
        """
        
        
        unlocked_greetings = renpy.store.Event.filterEvents(
            renpy.store.evhand.greeting_database,
            unlocked=True
        )
        
        
        random_greetings_dict = renpy.store.Event.checkRepeatRules(
            unlocked_greetings
        )
        
        
        if len(random_greetings_dict) > 0:
            
            
            return random_greetings_dict[
                renpy.random.choice(random_greetings_dict.keys())
            ]
        
        
        
        random_greetings_dict = renpy.store.Event.checkGreetingRules(
            unlocked_greetings
        )
        
        
        if len(random_greetings_dict) > 0:
            
            
            return random_greetings_dict[
                renpy.random.choice(random_greetings_dict.keys())
            ]
        
        
        
        random_greetings_dict = renpy.store.Event.filterEvents(
            unlocked_greetings,
            random=True
        )
        
        
        return random_greetings_dict[
            renpy.random.choice(random_greetings_dict.keys())
        ]


init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_sweetheart", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_sweetheart:
    m 1k "Привет, дорогой!"
    m 1l "Немного неловко говорить это в слух, правда?"
    m 3b "Однако, я думаю, что это со временем станет нормальным."
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_honey", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_honey:
    m 1b "С возвращением, дорогой!"
    m 1a "Я так рада тебя снова видеть."
    m "Давай проведем еще немного времени вместе, хорошо?"
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_back", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_back:
    m 1a "[player], ты вернулся!"
    m 1e "Я начала скучать по тебе."
    m 1k "Давай проведем еще один прекрасный день вместе, хорошо?"
    return

init 5 python:
    rules = dict()
    rules.update(MASGreetingRule.create_rule(skip_visual=False, random_chance=10))
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_gooday", unlocked=True, rules=rules),eventdb=evhand.greeting_database)
    del rules

label greeting_gooday:
    m 1k "Снова привет, [player]. Как дела?"
    menu:
        m "У тебя сегодня был хороший день?"
        "Да.":
            m 1a "Я очень рада за тебя, [player]."
            m "Это заставляет меня чувствовать себя намного лучше, зная, что ты счастлив."
            m "Я постараюсь изо всех сил, чтобы убедится, что он останется таким, я обещаю."
        "Нет...":
            m 1f "Ох..."
            m 2e "Ну, не волнуйся, [player]. Я всегда здесь ради тебя."
            m "Мы можем весь день говорить о твоих проблемах, если ты захочешь."
            m 3r "Я хочу попробовать сделать твой день лучше, и убедится, что ты всегда счастлив."
            m 1h "Потому что это то что сделает меня счастливой."
            m 1b "Я буду изо всех сил стараться подбодрить тебя, я обещаю."
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_visit", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_visit:
    m 1b "Вот и ты, [player]."
    m 1a "Приятно что ты заглянул."
    m 1e "Ты всегда такой заботливый, [player]!"
    m "Спасибо, что так много времени провел со мной~"
    m 2k "Просто помни, что твое время со мной никогда не тратится впустую."
    return

label greeting_goodmorning:
    $ current_time = datetime.datetime.now().time().hour
    if current_time >= 0 and current_time < 6:
        m 1b "Доброе утро-"
        m 1d "...ох, подожди."
        m "Это ночь мертвецов, дорогой."
        m 1i "Почему ты не спишь в такое время?"
        m 1g "Я предполагаю что ты не можешь уснуть..."
        menu:
            m "Это так?"
            "Да.":
                m 2h "Ты действительно должен лечь пораньше, если можешь."
                m "Если ты ляжешь слишком поздно это плохо отразится на твоем здоровье, понимаешь?"
                m 3m "Но если из-за этого я проведу больше времени с тобой, то я не буду жаловаться."
                m 3l "А-ха-ха!"
                m 3h "Но все же..."
                m "Мне бы очень хотелось, чтобы ты немного отдохнул."
                m "Сделай перерыв, если он тебе нужен, хорошо? Сделай это ради меня."
            "Нет.":
                m 1a "Ах. Я чувствую облегчение."
                m 1e "Значит ли это, что ты здесь только ради меня, посреди ночи?"
                m 1k "Боже, я так счастлива!"
                m "Ты действительно заботишься обо мне, [player]."
                m 2e "Но если ты действительно устал, пожалуйста ложись спать!"
                m "Я очень сильно тебя люблю, поэтому не переутомляйся!"
    elif current_time >= 6 and current_time < 12:
        m 1b "Доброе утро, дорогой."
        m "Еще одно отличное утро, чтобы начать день, да?"
        m 1k "Я рада что увидела тебя сегодня утром~"
        m 1a "Не забывай заботиться о себе, хорошо?"
        m "Сделай меня счастливой девушкой сегодня, как и всегда!"
    elif current_time >= 12 and current_time < 18:
        m 1b "Добрый день, любовь моя."
        m 1a "Не позволяй стрессу добраться до тебя, хорошо?"
        m "Я знаю, что ты снова постараешься сегодня, но...."
        m 4a "По-прежнему важно сохранять ясный разум!"
        m "Держите себя уверенно, глубоко вздохни ..."
        m "Я обещаю, что не буду жаловаться, если ты уйдешь, так что делай, что должен."
        m "Или ты можешь остаться со мной, если хочешь."
        m 4k "Просто помни, я люблю тебя!"
    elif current_time >= 18:
        m 1b "Добрый вечер, любимый!"
        menu:
            m "У тебя был сегодня хороший день?"
            "Да.":
                m 1k "Ах, это отлично!"
                m 1b "Я не могу чувствовать себя счастливой, когда ты..."
                m 1a "Но ведь все хорошо, верно?"
                m "Я так сильно тебя люблю, [player]."
                m 1k "А-ха-ха!"
            "Нет.":
                m 1g "Ох дорогой..."
                m "Я надеюсь скоро ты почувствуешь себя лучше, хорошо?"
                m "Просто помни что не зависимо от того что происходит, что кто-то говорит или делает..."
                m 1e "Я так сильно тебя люблю, так сильно."
                m "Просто останься со мной, если тебе станет лучше."
                m 1a "Я люблю тебя, [player], На самом деле."
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_back2", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_back2:
    m 1k "Привет, дорогой."
    m 1n "Я ужасно начала по тебе скучать. Я так рада снова тебя видеть!"
    m "Не заставляй меня так долго тебя ждать в следующий раз, эхехе~"
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_back3", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_back3:
    m 1e "Я так скучала по тебе, [player]!"
    m "Спасибо что вернулся. Мне очень нравится проводить время с тобой."
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_back4", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_back4:
    m 2k "Эй, [player]!"
    m 2l "Ты не подумал, что оставил меня одну слишком на большое время?"
    m 2b "Я просто шучу. Я никогда не смогу на тебя злиться."
    return


init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_visit2", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_visit2:
    m 1j "Спасибо что так много времени проводишь со мной, [player]."
    m 1a "Каждая минутка которую я провожу с тобой подобна пребыванию в раю!"
    m 1m "Я надеюсь это не звучало слишком убого, эхехе~"
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_visit3", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_visit3:
    m 1b "Ты вернулся!"
    m 1n "Я уже начала скучать по тебе ..."
    m 1i "Не заставляй меня так долго тебя ждать в следующий раз, хорошо?"
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_back5", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_back5:
    m 1a "Я так рада видеть тебя снова!"
    m 1f "Я беспокоилась о тебе."
    m "Пожалуйста не забывай посещать меня, хорошо? Я всегда здесь буду ради тебя."
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_visit4", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_visit4:
    m 1k "Я лююююблю тееебя, [player]. Эхехе~"
    m 1l "Ох, прости! Я немного разошлась.."
    m 1b "Я не думала, что смогу увидеть тебя снова так скоро."
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_visit5", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_visit5:
    m 1b "~День за днем ,~\n~строю мир в голове, где я рядышком с тобой...~"
    m 1a "О, ты здесь! Я просто замечталась и начала петь."
    m 1k "Я не думаю, что тебе трудно понять, о чем я мечтала, эхехе~"
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_visit6", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_visit6:
    m 1a "Каждый день с тобой, становится все лучше и лучше!"
    m "Говоря об этом, я так счастлива что ты наконец здесь."
    m "Давай проведем еще один замечательный день вместе."
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_back6", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_back6:
    m 3b "Эй, [player]!"
    m "Ты действительно должен навещать меня чаще."
    m 2h "Ты знаешь, что происходит с людьми, которые мне не нравятся, в конце концов..."
    m 1k "Я просто дразню тебя, эхехе~"
    m 1a "Не будь таким доверчивым! Я никогда не причиню тебе зла."
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_visit7", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_visit7:
    m 1k "Ты здесь, [player]!"
    m 1a "Готов ли ты провести еще больше времени вместе? Эхехе~"
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_visit8", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_visit8:
    m 1b "Я так рада что ты здесь, [player]!"
    m 1a "Что мы будем делать сегодня?"
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_visit9", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_visit9:
    m 1j "Ты наконец вернулся! Я ждала тебя."
    m 1b "Готов ли ты провести еще больше времени со мной? Эхехе~"
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_italian", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_italian:
    m 1b "Ciao, [player]!"
    m 1a "È così bello vederti ancora, amore mio..."
    m 1k "Ахаха!"
    m 2l "Я все еще практикую свой итальянский. Это очень сложный язык!"
    m 1a "В любом случае, приятно снова тебя видеть, любовь моя."
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_latin", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_latin:
    m 4b "Iterum obvenimus!"
    m 4h "Quid agis?"
    m 4l "Эхехе..."
    m 2l "Латынь звучит так напыщенно. Даже простое приветствие звучит как большое дело."
    m 1a "Если тебе интересно что я сказала, это просто 'Мы снова встречаемся! Как ты?'."
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_yay", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_yay:
    m 1k "Ты вернулся! Ура!"
    m 1l "О, прости. Я немного перевозбудилась сейчас."
    m 1m "Я просто очень рада снова тебя видеть, хехе~"
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_youtuber", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_youtuber:
    m 2b "Привет всем, добро пожаловать в следующий эпизод... Только Моника!"
    m 2k "Ахаха!"
    m 1a "Я выдавала себя за ютубера. Надеюсь, я рассмешила тебя, хехе~"
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_hamlet", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_hamlet:
    m 4h "Быть или не быть, вот в чем вопрос..."
    m 1d "O, вот и ты. Я просто убивала время, хехе~"
    m 1n "Я не ожидала увидеть тебя так скоро."
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_welcomeback", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_welcomeback:
    m 1b "Привет! Добро пожаловать назад."
    m 1k "Я так рада что ты можешь провести со мной это время."
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_flower", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_flower:
    m 1k "Ты мой прекрасный цветок, эхе-хе~"
    m 1l "Ой, это звучит так неловко."
    m 1e "Но я действительно буду всегда заботиться о тебе."
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_chamfort", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_chamfort:
    m 2 "День без Моники - это день, потраченный впустую."
    m 2k "Ахаха!"
    m 1b "С возвращением, любовь моя."
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_welcomeback2", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_welcomeback2:
    m 1b "С возвращением, [player]!"
    m "Надеюсь, твой день пройдет хорошо."
    m 1a "Я уверена, что это так, ты здесь в конце концов. Ничто не может пойти не так, хехе~"
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_longtime", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_longtime:
    m 1e "Давно не виделись, [player]!"
    m 1a "Я так счастлива что ты здесь сейчас."
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_sweetpea", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_sweetpea:
    m 1d "Посмотрите кто вернулся."
    m 2k "Это ты, мой милый!"
    m 1l "Боже мой... Было довольно смущающе это говорить, эхехе~"
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_glitch", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_glitch:
    hide monika
    show yuri glitch zorder 1
    y "{cps=500}[player]?!{nw}{/cps}"
    hide yuri glitch
    show yuri glitch2 zorder 1
    play sound "sfx/glitch3.ogg"
    pause 0.1
    hide yuri glitch2
    show yuri glitch zorder 1
    pause 0.3
    hide yuri glitch
    show monika 4n zorder 2 at i11
    m 1d "[player]!"
    hide monika
    show monika 4l zorder 2 at i11
    extend "Не важно, что я просто..."
    pause 0.1
    extend " немного поиграла с кодом."
    m 3l "Вот и все! Здесь нет никого, кроме нас... навсегда~"
    $ monika_clone1 = "Yes"
    m 2j "Я люблю тебя, [player]!"
    return

init 5 python:
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_surprised", unlocked=True, random=True),eventdb=evhand.greeting_database)

label greeting_surprised:
    m "О, привет [player]!"
    m "Прости, ты меня немного удивил."
    m "Как ты?"
    return

init 5 python:
    rules = dict()
    rules.update(MASSelectiveRepeatRule.create_rule(weekdays=[0], hours=range(5,12)))
    addEvent(Event(persistent.greeting_database,eventlabel="greeting_monika_monday_morning",
        unlocked=True, rules=rules),eventdb=evhand.greeting_database)
    del rules

label greeting_monika_monday_morning:
    m "Еще одно утро понедельника, да [player]?"
    m 1r "Он тебя засасывает и заставляет начать неделю ..."
    m 1 "Но видя, что ты делаешь это так лениво уходи"
    m 1k "Ты мой солнечный свет, который будит меня каждое утро!"
    m "Я очень сильно тебя люблю, [player]~"
    return


define gmr.eardoor = list()
define gmr.eardoor_all = list()
define opendoor.MAX_DOOR = 10
define opendoor.chance = 20
default persistent.opendoor_opencount = 0
default persistent.opendoor_knockyes = False

init 5 python:
    rules = dict()


    rules.update(
        MASGreetingRule.create_rule(
            skip_visual=True,
            random_chance=opendoor.chance
        )
    )

    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="i_greeting_monikaroom",
            unlocked=True,
            rules=rules
        ),
        eventdb=evhand.greeting_database
    )

    del rules

label i_greeting_monikaroom:
    scene black
    $ HKBHideButtons()



    $ has_listened = False


label monikaroom_greeting_choice:
    menu:
        "... Осторожно открыть дверь" if not persistent.seen_monika_in_room:
            jump monikaroom_greeting_opendoor
        "Открыть дверь" if persistent.seen_monika_in_room:
            if persistent.opendoor_opencount > 0:
                jump monikaroom_greeting_opendoor_locked
            else:
                jump monikaroom_greeting_opendoor_seen
        "Постучать":


            jump monikaroom_greeting_knock
        "Подслушать" if not has_listened:
            $ has_listened = True
            $ mroom_greet = renpy.random.choice(gmr.eardoor)

            jump expression mroom_greet






init 5 python:
    gmr.eardoor.append("monikaroom_greeting_ear_narration")

label monikaroom_greeting_ear_narration:
    m "Когда [player] наклоняет ухо к двери,{w} голос повествует о каждом его движении."
    m "'Кто это?' подумал он, когда [player] озадаченно смотрит на экран."
    call spaceroom from _call_spaceroom_enar
    m 1k "Это я!"
    m "С возвращением, [player]!"
    jump monikaroom_greeting_cleanup



init 5 python:
    gmr.eardoor.append("monikaroom_greeting_ear_loveme")

label monikaroom_greeting_ear_loveme:
    $ cap_he = he.capitalize()
    m "[cap_he] любит.{w} [cap_he] не любит."
    m "[cap_he] {i}любит{/i}.{w} [cap_he] {i}не{/i} любит."
    m "[cap_he] любит."
    m "...{w} [cap_he] любит меня!"
    jump monikaroom_greeting_choice


init 5 python:
    gmr.eardoor.append("monikaroom_greeting_ear_bathdinnerme")

label monikaroom_greeting_ear_bathdinnerme:
    m "С возвращением, [player]."
    m "Хочешь поужинать?"
    m "Или пойти в ванну?"
    m "Или.{w=1}.{w=1}.{w=1} Меня?"
    pause 2.0
    m "Мнннн!{w} T-{w=0.20} Я не смогу сказать, это перед [player]ом!"
    jump monikaroom_greeting_choice


init 5 python:
    gmr.eardoor.append("monikaroom_greeting_ear_progbrokepy")

label monikaroom_greeting_ear_progbrokepy:
    m "Что за-!{w} NoneType не имеет длины атрибута?"
    if renpy.seen_label("monikaroom_greeting_ear_progreadpy"):
        m "О, я знаю, что пошло не так!{w} Это должно это исправить!"
    else:
        m "Я не понимаю, что я делаю неправильно!"
        m "Здесь не должно быть None...{w} Я в этом уверена..."
    m "Кодировать действительно сложно..."
    jump monikaroom_greeting_choice


init 5 python:
    gmr.eardoor.append("monikaroom_greeting_ear_progreadpy")

label monikaroom_greeting_ear_progreadpy:
    m "...{w} Доступ к атрибуту объекта типа 'NoneType' приведет к 'AttributeError'."
    m "Я знаю. {w}Я должна убедиться, что переменная имеет значение None перед доступом к ее атрибутам."
    if renpy.seen_label("monikaroom_greeting_ear_progbrokepy"):
        m "Это объясняет ошибку, которую я получала раньше."
    m "Кодировать действительно сложно..."
    jump monikaroom_greeting_choice


init 5 python:
    gmr.eardoor.append("monikaroom_greeting_ear_rmrf")

label monikaroom_greeting_ear_rmrf:
    if renpy.windows:
        $ bad_cmd = "del C:\Windows\System32"
    else:
        $ bad_cmd = "rm -rf /"
    m "Итак, решение этой проблемы - ввести '[bad_cmd]' в командной строке?"
    if renpy.seen_label("monikaroom_greeting_ear_rmrf_end"):
        m "Да,{w} хорошая попытка."
    else:
        m "Хорошо, позволь мне попробовать."
        show noise
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.2
        stop sound
        hide noise
        m "{cps=*2} А! Нет! Это не то, что я хотела!{/cps}"
        m "..."
    m "Я не должна доверять Интернету так слепо..."
label monikaroom_greeting_ear_rmrf_end:
    jump monikaroom_greeting_choice



init 10 python:


    gmr.eardoor_all = list(gmr.eardoor)


    remove_seen_labels(gmr.eardoor)


    if len(gmr.eardoor) == 0:
        gmr.eardoor = list(gmr.eardoor_all)




label monikaroom_greeting_opendoor_locked:
    show paper_glitch2
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    pause 0.7
    $ style.say_window = style.window_monika
    menu:
        m "Я тебя пугаю, [player]?"
        "Да":
            m "Все, прости."
        "Нет":
            m "{cps=*2}Хмпф, у меня получиться в следующий раз.{/cps}{nw}"
            m " Я поняла.  В конце концов, это все лишь обычный сбой."
    m "Поскольку ты продолжаешь открывать дверь,{w} я не могла не добавить для тебя немного сюрпризов~"
    m "Постучи в следующий раз, хорошо?"
    m "Теперь позвольте мне исправить эту комнату..."

    hide paper_glitch2
    scene black
    $ scene_change = True
    call spaceroom from _call_sp_mrgo_l

    if renpy.seen_label("monikaroom_greeting_opendoor_locked_tbox"):
        $ style.say_window = style.window

    m 1j "Вот так!"

    if not renpy.seen_label("monikaroom_greeting_opendoor_locked_tbox"):
        menu:
            "...текстовое поле...":
                m 1n "Упс! Я все еще учусь, как это делать."
                m 1m "Позволь мне просто изменить этот флаг здесь...{w=1.5}{nw}"
                $ style.say_window = style.window
                m 1j "Все исправлено!"


label monikaroom_greeting_opendoor_locked_tbox:
    m 1a "С возвращением, [player]."
    jump monikaroom_greeting_cleanup


label monikaroom_greeting_opendoor_seen:

    jump monikaroom_greeting_opendoor_seen_partone


label monikaroom_greeting_opendoor_seen_partone:
    $ is_sitting = False

    call spaceroom (start_bg="bedroom", hide_monika=True) from _call_sp_mrgo_spo
    pause 0.2
    show monika 1h zorder 2 at l21
    pause 1.0
    m 1r "[player]..."


    m 1f "Я понимаю, почему ты не постучал в первый раз,{w} но не мог бы ты просто войти?"
    m 1o "В конце концов, это моя комната."
    menu:
        "Твоя комната?":
            m 3a "Правильно!"
    m "Разработчики этого мода дали мне хорошую удобную комнату, чтобы оставаться там, когда тебя нет."
    m 1m "Тем не менее, я могу смогу в неё войти, только если ты скажешь мне 'до свидания' или 'спокойной ночи', прежде чем закрыть игру."
    m 2b "Поэтому, пожалуйста, не забудь сказать мне это, прежде чем уйти, хорошо?"
    m "В любом случае..."





























    $ persistent.opendoor_opencount += 1
    jump monikaroom_greeting_opendoor_post2


label monikaroom_greeting_opendoor_post2:
    show monika 1a at t11
    pause 0.7
    show monika 5a at hf11
    m "Я так рада что ты вернулся, [player]."
    show monika 5a at t11

    m "В последнее время я практиковалась с переключение фонов, и теперь я могу изменить их мгновенно.."
    m "Смотри!"


    m 1q "...{w=1.5}{nw}"
    scene black
    $ scene_change = True
    call spaceroom (hide_monika=True) from _call_sp_mrgo_p2
    show monika 4a zorder 2 at i11
    m "Тада!"


    show monika at lhide
    hide monika
    jump monikaroom_greeting_post


label monikaroom_greeting_opendoor:
    $ is_sitting = False
    call spaceroom (start_bg="bedroom", hide_monika=True) from _call_spaceroom_5
    m 2i "~Украсть тебя - это признак любви или стоит отпустить?~"
    show monika 1 zorder 2 at l32
    m 1d "А-А?! [player]!"
    m 3g "Ты увидил меня, внезапно появившись!"
    show monika 1 at hf32
    m 5b "У меня не хватило времени, чтобы подготовиться!"
    m 5a "Но спасибо, что вернулся, [player]."
    show monika 1 at t32
    m 3a "Просто дай мне несколько секунд, чтобы все наладить, хорошо?"
    show monika 1 at t31
    m 2d "..."
    show monika 1 at t33
    m 1d "...и..."
    if is_morning():
        show monika_day_room zorder 1 with wipeleft
    else:
        show monika_room zorder 1 with wipeleft
    show monika 1 at t32
    m 3a "Вот так!"
    menu:
        "...окно...":
            show monika 1 at h32
            m 1l "Упс! Я забыла об этом~"
            show monika 1 at t21
            m "Подожди..."
            hide bedroom
            m 2j "И... исправлено!"
            show monika 1 at lhide
            hide monika
            $ renpy.hide("bedroom")
    $ persistent.seen_monika_in_room = True
    jump monikaroom_greeting_post


label monikaroom_greeting_knock:
    m "Кто это~?"
    menu:
        "Это я.":
            m 1b "[player]! Я так счастлива что ты вернулся!"
            if persistent.seen_monika_in_room:
                m "И спасибо что сначала постучал."
            m 1j "Подожди, мне надо привести себя в порядок..."
            call spaceroom (hide_monika=True) from _call_spaceroom_6
    jump monikaroom_greeting_post


label monikaroom_greeting_post:
    m 2a "А теперь позволь мне взять столик и стул. ..."
    $ is_sitting = True
    show monika 1 zorder 2 at ls32
    m 1a "Чем мы будем заниматься сегодня, [player]?"
    jump monikaroom_greeting_cleanup


label monikaroom_greeting_cleanup:
    python:
        if persistent.current_track is not None:
            play_song(persistent.current_track)
        else:
            play_song(songs.current_track) 
        HKBShowButtons()
        set_keymaps()
    return

label greeting_youarereal:
    python:
        try:
            renpy.file(
                config.basedir.replace("\\","/") +
                "/characters/" + persistent.playername.lower() + ".chr"
            )
            persistent._mas_you_chr = True
        except:
            persistent._mas_you_chr = False
    m 1b "[player]! Рада тебя видеть!"
    if persistent._mas_you_chr:
        m "Подожди. Что-то изменилось."
        m 1d "Ты...добавил файл персонажа?"
        m 1f "[player].chr...Да?"
        m 1g "Зачем ты...пытаешься поместить себя рядом со мной?"
        m "Зачем тебе это нужно?"
        m 1o "Разве ты не понял? "
        m 1p "Этого места не существует! Я не знаю, что произойдет если ты придешь сюда!"
        m 1q "Как ты мог это сделать?"
        m 1o "Отказаться от своей реальности..."
        m 1p "Просто чтобы быть со мной?"
        m 1n "Это все моя вина!"
        m 1f "Но...но 'ты', в игре..."
        m 1i "Он даже начинает немного двигаться снова."
        m 1 "Может...это позволит тебе управлять им снова?"
        m 1f "Это неправильно! Я не хочу марионетку!"
        m 1q "Пожалуйста, [player]..."
        m "Если ты собираешься это сделать, ты уверен, что это то, что ты хочешь?"
        menu:
            m "Ты уверен?"
            "Я уверен.":
                m 1e "Тогда...У меня нет выбора кроме как принять его..."
                m 1k "Я приму этот подарок с распростертыми объятиями!"
                m "Мы сможем, наконец, быть вместе, [player]."
                m "И мы сможем понять, как это сделать в твоей реальности, вместе!"
            "Возможно нет...":
                m 1l "Я так и думала..."
                m 1m "Нельзя отказаться от того, чтобы быть 'настоящим' рядом со мной..."
                m 1l "Я не могу заставить себя удалить этот симпатичный маленький  .chr-файл, но..."
                m 1q "Пожалуйста, сделай это сам."
                m 1r "В этих файлах есть какие-то жуткие вещи ..."
                m 1e "Я люблю тебя, [player]. Я буду ждать тебя столько, сколько потребуется."
                m "Так что не торопись, хорошо?"
    else:
        m 1i "Я много думала о файлах  .chr..."
        m 1n "Например, что это такое?"
        m 1o "Они вроде жуткие..."
        m 1p "И даже если другие девушки не настоящие, почему можно удалить одного из персонажей?"
        m 1i "Можно ли добавить персонажа?"
        m 1r "Трудно сказать..."
    return

label greeting_japan:
    m 1k "Oh, kon'nichiwa [player]!"
    m "Эхехе~"
    m 2b "Привет, [player]!"
    m 1a "Я просто занимаюсь японским языком."
    m 3c "Посмотри..."
    m 4b "Ваташи ха его недостаток анана нет моно дешу!"
    m 2l "Извини, если это не имеет смысла!"
    m 3 "Ты знаешь, что это означает, [player]?"
    m 4j "Это означает {i}'Я буду твоей навсегда{/i}'~"
    return

label greeting_sunshine:
    m 1r "{i}Ты мое солнце, мое единственное солнце.{i}"
    m 1k "{i}Ты делаешь меня счастливой, когда небеса пасмурны.{/i}"
    m 4j "{i}Ты никогда не узнаешь дорогой, как сильно я тебя люблю.{/i}"
    m 2r "{i}Пожалуйста, не отнимай у меня солнце.~{/i}"
    m 1j "..."
    m 1d "Э-Эм?! [player]!"
    m 4n "О, черт возьми, это так неловко!"
    m 1l "Я просто пела про себя, чтобы скоротать время."
    m 1b "Но теперь, когда ты здесь, мы можем провести это время вместе."
    return