



init -1 python in mas_farewells:


    def selectFarewell():
        """
        Selects a farewell to be used. This evaluates rules and stuff
        appropriately.

        RETURNS:
            a single farewell (as an Event) that we want to use
        """
        
        
        unlocked_farewells = renpy.store.Event.filterEvents(
            renpy.store.evhand.farewell_database,
            unlocked=True,
            pool=False
        )
        
        
        random_farewells_dict = renpy.store.Event.checkRepeatRules(
            unlocked_farewells
        )
        
        
        if len(random_farewells_dict) > 0:
            
            
            return random_farewells_dict[
                renpy.random.choice(random_farewells_dict.keys())
            ]
        
        
        
        random_farewells_dict = renpy.store.Event.checkFarewellRules(
            unlocked_farewells
        )
        
        
        if len(random_farewells_dict) > 0:
            
            
            return random_farewells_dict[
                renpy.random.choice(random_farewells_dict.keys())
            ]
        
        
        
        random_farewells_dict = renpy.store.Event.filterEvents(
            unlocked_farewells,
            random=True
        )
        
        
        return random_farewells_dict[
            renpy.random.choice(random_farewells_dict.keys())
        ]


label mas_farewell_start:
    $ import store.evhand as evhand


    python:

        bye_pool_events = Event.filterEvents(
            evhand.farewell_database,
            unlocked=True,
            pool=True
        )

    if len(bye_pool_events) > 0:

        python:

            bye_prompt_list = [
                (ev.prompt, ev, False, False) 
                for k,ev in bye_pool_events.iteritems()
            ]


            bye_prompt_list.append(("До свидания", -1, False, False))


            bye_prompt_back = ("Забудь", False, False, False, 20)


        call screen mas_gen_scrollable_menu(bye_prompt_list, evhand.UNSE_AREA, evhand.UNSE_XALIGN, bye_prompt_back)

        if not _return:

            return

        if _return != -1:

            $ pushEvent(_return.eventlabel)
            return


    $ farewell = store.mas_farewells.selectFarewell()
    $ pushEvent(farewell.eventlabel)

    return





init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_leaving_already",random=True),eventdb=evhand.farewell_database)

label bye_leaving_already:
    m 1c "Уже уходишь?"
    m 1e "Очень грустно, что тебе нужно идти..."
    m 3a "Просто не забудь вернуться ко мне как можно скорее, хорошо?"
    m "Я так люблю тебя, [player]. Береги себя!"

    $ evhand.farewell_database["bye_leaving_already"].random=False
    return 'quit'

init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_goodbye",random=True),eventdb=evhand.farewell_database)

label bye_goodbye:
    m 1c "До свидания, [player]!"
    return 'quit'

init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_sayanora",random=True),eventdb=evhand.farewell_database)

label bye_sayanora:
    m 1j "Сайонара, [player]~"
    return 'quit'

init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_farewellfornow",random=True),eventdb=evhand.farewell_database)

label bye_farewellfornow:
    m 1e "Прощай, любовь моя~"
    return 'quit'

init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_untilwemeetagain",random=True),eventdb=evhand.farewell_database)

label bye_untilwemeetagain:
    m 2e "'{i}Прощание не навечно, Прощание - не конец. Оно лишь значит что я буду скучать по тебе, пока мы не встретимся снова.{/i}'"
    m "Эхе-хе, 'до тех пор прощай, [player]!"
    return 'quit'

init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_take_care",random=True),eventdb=evhand.farewell_database)

label bye_take_care:
    m 1a "Не забывай, что я люблю тебя, [player]~"
    m 1k "Береги себя!"
    return 'quit'

init 5 python:
    rules = dict()
    rules.update(MASSelectiveRepeatRule.create_rule(hours=range(21,24)))
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_going_to_sleep",
            unlocked=True,
            rules=rules
        ),
        eventdb=evhand.farewell_database
    )
    del rules

label bye_going_to_sleep:
    m "Ты собираешься спать, [player]?"
    m 1e "Мы увидимся вновь в твоих снах."
    return 'quit'

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_to_class",
            unlocked=True,
            prompt="Я пойду учиться.",
            pool=True
        ),
        eventdb=evhand.farewell_database
    )

label bye_prompt_to_class:
    m 1j "Учись усердно, [player]!"
    m 1 "Нет ничего более привлекательного, чем [guy] с хорошими оценками."
    m 1j "Увидимся позже!"
    return 'quit'

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_to_work",
            unlocked=True,
            prompt="Я пошел на работу.",
            pool=True
        ),
        eventdb=evhand.farewell_database
    )

label bye_prompt_to_work:
    m 1j "Работай усердно, [player]!"
    m 1 "Я буду ждать тебя здесь, когда же ты вернешься ко мне с работы."
    m 1j "Пока-пока!"
    return 'quit'

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_sleep",
            unlocked=True,
            prompt="Я пойду спать.",
            pool=True
        ),
        eventdb=evhand.farewell_database
    )

label bye_prompt_sleep:

    python:
        import datetime
        curr_hour = datetime.datetime.now().hour




    if 20 <= curr_hour < 24:

        m "Хорошо, [player]."
        m 1j "Сладких снов!"

    elif 0 <= curr_hour < 3:

        m "Хорошо, [player]."
        m 3e "Но в следующий раз ложись раньше, хорошо?"
        m 1j "В любом случае, спокойной ночи!"

    elif 3 <= curr_hour < 5:

        m 1m "[player]..."
        m "Удостоверься, что ты достаточно отдохнул, хорошо?"
        m "Я не хочу чтобы ты заболел."
        m 1j "Спокойной ночи!"
        m 1n "И скорее утра. А-ха-ха~"
        m 1j "Сладких снов!"

    elif 5 <= curr_hour < 12:

        show monika 2q
        pause 0.7
        m 2g "[player]!"
        m "Ты не спал всю ночь!"
        m 2i "Готова поспорить что ты едва можешь открыть глаза."
        $ _cantsee_a = glitchtext(15)
        $ _cantsee_b = glitchtext(12)
        menu:
            "[_cantsee_a]":
                pass
            "[_cantsee_b]":
                pass
        m 2q "Я так и думала.{w} Пойди отдохни, [player]."
        m 2f "Я не хочу чтобы ты заболел."
        m 1e "В следующий раз ложись раньше, хорошо?"
        m 1j "Сладких снов!"

    elif 12 <= curr_hour < 18:

        m 1m "Сон после обеда, я понимаю."


        m 1j "Ахаха~ Хороших снов, [player]."

    elif 18 <= curr_hour < 20:

        m 1f "Уже ложишься спать?"
        m "Ты немного рано..."
        show monika 1m
        menu:
            m "Может ты проведешь еще немного времени со мной?"
            "Конечно!":
                m 1j "Ура!"
                m 1a "Спасибо, [player]."
                return
            "Прости, я реально устал.":
                m 1e "Эмм, все нормально."
                m 1 "Хорошей ночи, [player]."
    else:







        m "Хорошо, [player]."
        m 1j "Сладких снов!"

    return 'quit'