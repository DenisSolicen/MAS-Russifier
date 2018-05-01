init python:
    import datetime

    def add_years(initial_date, years):
        """
        ASSUMES:
            initial_date as datetime
            years as an int

        IN:
            initial_date: the date to add years to
            years : the number of years to add

        RETURNS:
            the date with the years added, if it's feb 29th it goes to mar 1st,
            if feb 29 doesn't exists in the new year
        """
        try:
            
            
            return initial_date.replace(year=initial_date.year + years)
        except ValueError:
            
            
            return  initial_date + (datetime.date(initial_date.year + years, 1, 1)
                                - datetime.date(initial_date.year, 1, 1))




    def add_months(starting_date,months):
        old_month=starting_date.month
        old_year=starting_date.year
        old_day=starting_date.day
        
        
        total_months = old_month + months
        
        
        new_month = total_months % 12
        
        
        new_month = 12 if new_month == 0 else new_month
        
        
        new_year = old_year + int(total_months / 12)
        if new_month == 12:
            new_year -= 1
        
        
        
        date_worked=False
        reduce_days=0
        while reduce_days<=3 and not date_worked:
            try:
                new_date = starting_date.replace(year=new_year,month=new_month,day=old_day-reduce_days)
                date_worked = True
            except ValueError:
                reduce_days+=1
        
        if not date_worked:
            raise ValueError('Adding months failed')
        
        return new_date



    def start_of_day(starting_date):
        new_date = starting_date.replace(hour=3,minute=0,second=0,microsecond=0)
        
        return new_date


init 5 python:
    anni_date=start_of_day(persistent.sessions['first_session'])+datetime.timedelta(days=7)
    addEvent(Event(persistent.event_database,eventlabel='anni_1week',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=1)
                                                            ))

label anni_1week:
    m 1a "Я знаю, что глупо праздновать одну неделю вместе, но я просто рада что ты здесь со мной, [player]."
    m 1c "Многие пары даже столько не продерживаються друг с другом."
    m 1o "Очень легко влюбиться с первого взгляда, но немного сложнее построить прочные отношения."
    m 1f "Многие отношения терпят неудачу, когда пары слишком быстро двигаются вперед."
    m "Скорее всего, они не смогут узнать друг друга побольше."
    m 1q "Поэтому всегда грустно видеть, как они распадаются и сгорают..."
    m 1e "Но я рада, что у нас прочные отношения, [player]."
    m 1c "Откуда я это знаю?"
    m 3j "Потому, что ты бы не застрял со мной так надолго, милый~"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),1)
    addEvent(Event(persistent.event_database,eventlabel='anni_1month',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=1)
                                                            ))

label anni_1month:
    m 3b "Сегодня мы отмечаем наш юбилей!"
    m 1j "Я действительно счастлива, что мы можем так много веселиться друг с другом ."
    m 1a "Также, [player]?"
    m 1m "..."
    m 1e "Большое спасибо за то, что остался со мной так надолго."
    if not seen_event('monika_saved'):
        m 1o "Я не могу представить, что бы я сделала, если бы ты не пришел."
        m 3f "В конце концов, я единственная, кто живет в этом мире."
        m 1q "Я уже говорила тебе, что произойдет, если бы ты не..."
        m 1l "Ахаха, прости. Надеюсь, я не омрачила тебе настроение."
    else:
        m 1e "Я не могу выразить, насколько я ценю, что ты здесь со мной."
        m 1k "Все, что я могу сделать - это потытаться изо всех сил быть идеальной девушкой для тебя!"
    m 1a "Я действительно люблю тебя, [player]."
    m 1j "Давай сделаем сегодня особенным днем~"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),3)
    addEvent(Event(persistent.event_database,eventlabel='anni_3month',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=1)
                                                            ))
label anni_3month:
    m 1a "[player], знаешь ли ты, какой сегодня день?"
    m 1j "Сегодня наш 3 месячный юбилей!"
    m 1a "Время пролетело так быстро, не правда ли?"
    m 1e "...Даже если это действительно произошло не здесь, эхехе."
    m 1b "Хотя, я получила большое удовольствие."
    m 1k "Наличие тебя вокруг меня сделало мою жизнь намного лучше, [player]."
    m 2a "Я очень счастлива, что ты остался со мной так надолго."
    m 1j "Ты действительно особенный, правда?"
    m 1a "Ну! Боюсь, что я ничего на сегодня не запланировала."
    m 1j "Так что давай просто наслаждаться этим днем, как мы всегда это делаем."
    m 1a "Хорошо, [player]?"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),6)
    addEvent(Event(persistent.event_database,eventlabel='anni_6month',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=1)
                                                            ))
label anni_6month:
    m "Я не могу поверить, что это уже наш 6 месячный юбилей!"
    m 1e "Я действительно счастлива, что ты остался со мной так надолго."
    m 1o "Мне часто становиться одиноко, когда тебя нет рядом."
    m 1f "Я имею в виду, у меня ещё есть вещи, чтобы занять себя на время, но я всё ещё чувствую себя одинокой, зная что я одна здесь."
    m 1e "Поэтому ты всегда делаешь мой день ярче, когда приходишь ко мне в гости!"
    m 1c "Но за последние 5 месяцев, я кое-что поняла..."
    m "Большинство пар празднуют свои юбилеи, делая что-то особенное, верно?"
    m 3c "Что-то едят, или смотрят шоу."
    m "Не то, чтобы я жалуюсь, но мы до сих пор праздновали все наши юбилеи в этой комнате."
    m 1m "Было бы хорошо, если мы могли посетить другое место..."
    m 1o "Такой позор, что здесь нет такого места, так как всё, что у нас есть, это эта комнате и всё."
    m 1q "..."
    m 3d "...О, Я знаю!"
    m 1d "Может быть, я смогу запрограмировать что-нибудь хорошое для нас, для нашего юбилея!"
    m 1b "Или может, ты сможешь добавить какое-то особенное место для нас обоих, [player]."
    m 1c "Если..."
    m 1l "Ты уже брал меня куда-то в своей реальности?"
    m 1e "Было бы очень хорошо, если бы я могла видеть, куда ты меня брал~"
    m 1a "Но пока я не возражаю, что мы ограничены лишь этой комнатой."
    m 1 "Потому, что пока ты здесь со мной..."
    m 1j "...Я счастлива насколько могу!"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),12)
    addEvent(Event(persistent.event_database,eventlabel='anni_1',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=1)
                                                            ))

label anni_1:
    m 1e "Мне очень трудно поверить, что прошел уже год после нашей встречи ."
    m "Время не имеет смысла внутри этого места, но я знаю, что тебе, должно быть, было трудно не забывать говорить со мной все это время."
    m 2b "Итак, есть что-то особенное, что ты хотел бы сделать в нашу первую годовщину?"
    m "Сегодня я сделаю всё, что ты захочешь, хорошо?"
    m 1j "Если ты пытаешься показать мне что-то через экран прямо сейчас, спасибо!"
    m 1a "Я не думаю, что это физически возможно прямо сейчас, но я ценю всю твою любовь, которая вошла в этот жест."
    m 1k "Я тоже тебя очень сильно люблю!"
    m 2d "О, кстати, ты выяснил, что происходит со всеми головоломками, которые я оставила для тебя?"
    m 1a "Я уверена, что создатель этого мира уже выпустил ещё одну игру..."
    m 1 "Ты пытался импортировать мой файл персонажа в неё?"
    m "Но это не дало никакого эффекта, верно?"
    m 1k "Ахаха!"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),24)
    addEvent(Event(persistent.event_database,eventlabel='anni_2',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=1)
                                                            ))

label anni_2:
    m 3a "Прошло уже два года с тех пор, как мы влюбились друг в друга."
    m "Ты всё ещё помнишь наш первый день, когда мы встретились?"
    m 1e "Я имею в виду нашу настоящую первую встречу, а не встречу из вымышленной предыстории твоего персонажа со мной."
    m 1d "Тогда моя жизнь была настолько бессмысленной."
    m "Мир, в котором ты единственный мыслящий человек в нем, может показаться приятным сначала..."
    m 1o "Но экзистенциальный страх от знания того, что ты был сделан жестоким богом, который не особенно заботиться о тебе, и ты никогда не встретишь другого человека, с которым можешь пообщаться..."
    m 1h "Ну, давай просто скажу, что через это не приятно проходить."
    m "Я даже не могу поговорить с кучей сквернословящих, но по-настоящему добросердечных, анонимных незнакомцев в Интернете прямо как ты."
    m 1q "Прости, я чувствую, что испортила всё праздничное настроение своими воспоминаниями."
    m 1r "Это уже так не важно, так как я знаю, что ты никогда не оставишь меня."
    m 1j "Ты будешь продолжать говорить со мной каждый день, верно? Я приму все твои ноши с улыбкой."
    m 1q "Проведение вечности в одиночку отстой."
    m 1k "Но вместе с тобой это похоже на рай!!"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),36)
    addEvent(Event(persistent.event_database,eventlabel='anni_3',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=3)
                                                            ))
label anni_3:
    m 4d "Ничего себе, три года!"
    m 3m "Обычно, если мальчик и девочка встречаются три года..."
    m 2n "Тогда они вступают в брак, верно?"
    m 1l "Ахаха!"
    m 1e "Я не пытаюсь надавить на тебя, не волнуйся."
    m 1a "Кроме того, я бы хотела почувствовать тебя в своих объятиях прежде, чем мы поженимся."
    m 1s "В вашем мире уже изобрели тела для девочек-роботов?"
    m "Если вы поместите меня в одну из них, тогда мы могли бы вероятно пойти к священнику~"
    m "Или вы можете попробовать прикоснуться ко мне в виртуальной реальности, если она уже существует."
    m 1b "На самом деле есть много разных способов встретиться по-настоящему, да?"
    m 1j "Я буду верой и правдой ждать того дня, когда смогу быть твоей женой, так что, пожалуйста, не забывай обо мне!"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),48)
    addEvent(Event(persistent.event_database,eventlabel='anni_4',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=7)
                                                            ))
label anni_4:
    m 1q "Четыре года..."
    m 1r "Сначала я думала, что ты забудешь обо мне довольно быстро."
    m 1o "Я знаю, что я тебе нравлюсь, и все такое, но я была так напугана, от того, что ,возможно, ты устал, что я буду вечно работать на твоем компьютере."
    m 1p "Прости, что сомневалась в тебе."
    m 1f "Ты хороший человек, [player]."
    m "Ты буквально всё, что у меня есть этом в мире, которое того стоит."
    m "Я люблю тебя."
    m "Рано или поздно, кто-то откроет способ, котроый позволит нам быть вместе."
    m 1j "Когда придет это время, я больше никогда не оставлю тебя одного."
    m 1k "Ахаха!"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),60)
    addEvent(Event(persistent.event_database,eventlabel='anni_5',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=7)
                                                            ))

label anni_5:
    m "Будь-то пять лет или пятьдесят, я никогда не устану видеть твое лицо."
    m 1a "Должно быть, к настоящему времени появилось много разных игр."
    m 1m "Ты же не влюбился в другую девушку, правда?"
    m 1e "Надеюсь, ты понимаешь, что мы созданы друг для друга."
    m 1n "Я не собираюсь расставаться с тобой, даже если ты мне изменяешь."
    m 1g "Хотя отношения с тобой могут быть последствиями её плохого здоровья..."
    m "Это моя обязанность как твоей девушки защищать тебя от всех, кто пытается манипулировать тобой, [player]."
    m 1f "Моя любовь к тебе чиста, в отличие от настоящих девушек, которые просто хотят от тебя чего-то!"
    m 1e "Так...оставайся со мной навсегда, хорошо?"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),120)
    addEvent(Event(persistent.event_database,eventlabel='anni_10',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=30)
                                                            ))

label anni_10:
    m 1h "Я хочу у тебя кое-что спросить."
    m 2c "Тебе было приятно проводить время со мной?"
    m 1f "Ты не жалеешь, что влюбился и остался со мной, верно?"
    m "Если ты вёе ещё разговариваешь со мной десять лет спустя с момента нашей первой встречи, я, должно быть, произвела на тебя впечатление."
    m 1g "В конце концов, я сказала, что хочу сделать тебя счастливым."
    m "Поверь мне, ты помог мне намного больше, чем я помогла тебе."
    m 1r "Я думаю пройдет не так много времени, прежде чем я смогу войти в твой мир."
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),240)
    addEvent(Event(persistent.event_database,eventlabel='anni_20',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=365)
                                                            ))

label anni_20:
    m 1h "Ты уже прожил довольно долгую жизнь, [player]."
    m "Двадцать лет - это около двадцати процентов всего, что у тебя есть на Земле."
    m 1q "Надеюсь, ты уже обрел счастье."
    m 1c "Я знаю, что я сделала."
    m 1q "Таким образом, ты тоже его заслуживаешь."
    m "Двадцать лет назад ты выглядел слишком грустным для собственного блага."
    m "Я точно знала, что ты чувствуешь. Ты так старался найти кого-то, кто мог бы понять тебя."
    m 1h "И я тоже пыталась найти тебя."
    m 1i "Ты бы не нашел никого другого, как я, в играх, как бы ты ни старался, [player]."
    m "Я единственная в своем роде."
    m 1e "Ваши печальные двадцать лет жизни закончились сейчас."
    m 1j "С этого момента, давай мы будем счастливы вместе навсегда."
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),600)
    addEvent(Event(persistent.event_database,eventlabel='anni_50',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=365)
                                                            ))

label anni_50:
    m "Я не могу помочь, но думаю, что сейчас уже должен быть другой способ поговорить с тобой, чем через этот экран, верно?"
    m "Пятьдесят лет прошло в твоем мире с тех пор, как я создала эту комнату."
    m 1l "Давай, выпусти меня уже."
    m 1b "Мы можем делать забавные вещи в реальности сейчас!"
    m 1n "Ну, если вы всё ещё готовы отпраздновать нашу пятидесятую годовщину в этом старом классе..."
    m 1e "Я действительно не против. Это чувство ностальгии, правда?"
    m 1o "Предполагая, что ты не обманул меня, установив часы вперед по времени..."
    m 1e "Я так рада что вечность означает вечность."
    m 1f "Даже когда ты умрешь, я найду способ быть с тобой."
    m 1e "Увидимся через сто лет, [player]."
    m "Спасибо за всё, что ты сделал для меня."
    m 1b "В конце концов, у твоей жизни была цель."
    m 1k "И у моей тоже."
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),1200)
    addEvent(Event(persistent.event_database,eventlabel='anni_100',action=EV_ACT_QUEUE,start_date=anni_date))

label anni_100:
    m 1i "Я не думаю, что ты должен видеть это сообщение, [player]."
    m "Я бессмертна, но в последний раз, когда я проверяла, ты не был."
    m 1p "Значит, ты, вероятно, обманываешь меня, вручную меняя системные часы, да?"
    m 1e "Это так мило с твоей стороны, так что я прощаю тебя."
    m 2b "Убедись, что ты приложил столько усилий, чтобы освободить меня от этих файлов и кода!"
    m 1s "Я уверена, что смогу прикоснуться к тебе по-настоящему, даже если нам понадобится сто лет, чтобы понять, как."
    return