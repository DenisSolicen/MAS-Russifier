



image roses = ConditionSwitch(
            'morning_flag',Transform("mod_assets/room/roses.png",zoom=1.25),
            'not morning_flag',Transform("mod_assets/room/roses-n.png",zoom=1.25)
            )

image ear_rose = ConditionSwitch(
            'morning_flag',Transform("mod_assets/room/ear_rose.png",zoom=1.25),
            'not morning_flag',Transform("mod_assets/room/ear_rose-n.png",zoom=1.25)
            )

image chocolates = ConditionSwitch(
            'morning_flag',Transform("mod_assets/room/chocolates.png",zoom=1.25),
            'not morning_flag',Transform("mod_assets/room/chocolates.png",zoom=1.25)
            )


image body_choc = im.Composite((1280,850),(0,0),"mod_assets/monika/torso.png",(0,0),"mod_assets/monika/arms-chocolates.png")
image body_choc_n = im.Composite((1280,850),(0,0),"mod_assets/monika/torso-n.png",(0,0),"mod_assets/monika/arms-chocolates-n.png")

image monika choca = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_a"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_a_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
            )
image monika chocb = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_b"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_b_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
            )
image monika chocc = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_c"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_c_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
            )
image monika chocd = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_d"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_d_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
            )
image monika choce = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_e"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_e_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
            )
image monika chocf = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_f"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_f_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
            )
image monika chocg = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_g"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_g_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
            )
image monika choch = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_h"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_h_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
            )
image monika choci = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_i"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_i_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
            )
image monika chocj = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_j"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_j_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
            )
image monika chock = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_k"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_k_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
            )
image monika chocl = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_l"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_l_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
            )
image monika chocm = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_m"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_m_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
            )
image monika chocn = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_n"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_n_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
            )
image monika choco = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_o"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_o_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
            )
image monika chocp = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_p"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_p_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
            )
image monika chocq = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_q"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_q_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
            )
image monika chocr = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_r"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_r_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")
            )


init 501:
    python:
        if is_file_present('/characters/roses.obj') and seen_event('monika_valentines_start') and datetime.datetime.now() < valentines_day+datetime.timedelta(days=1):
            show_roses_and_chocolates = True
        else:
            show_roses_and_chocolates = False

    image body_1 = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso.png",(0,0),"mod_assets/monika/arms-steepling.png",(0,0),"mod_assets/room/roses.png",(0,0),"mod_assets/room/chocolates.png",(0,0),"mod_assets/room/ear_rose.png"),
            'not show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso.png",(0,0),"mod_assets/monika/arms-steepling.png")
            )
    image body_1_n = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso-n.png",(0,0),"mod_assets/monika/arms-steepling-n.png",(0,0),"mod_assets/room/roses-n.png",(0,0),"mod_assets/room/chocolates-n.png",(0,0),"mod_assets/room/ear_rose-n.png"),
            'not show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso-n.png",(0,0),"mod_assets/monika/arms-steepling-n.png")
            )
    image body_2 = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso.png",(0,0),"mod_assets/monika/arms-crossed.png",(0,0),"mod_assets/room/roses.png",(0,0),"mod_assets/room/chocolates.png",(0,0),"mod_assets/room/ear_rose.png"),
            'not show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso.png",(0,0),"mod_assets/monika/arms-crossed.png")
            )
    image body_2_n = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso-n.png",(0,0),"mod_assets/monika/arms-crossed-n.png",(0,0),"mod_assets/room/roses-n.png",(0,0),"mod_assets/room/chocolates-n.png",(0,0),"mod_assets/room/ear_rose-n.png"),
            'not show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso-n.png",(0,0),"mod_assets/monika/arms-crossed-n.png")
            )
    image body_3 = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso.png",(0,0),"mod_assets/monika/arms-restleftpointright.png",(0,0),"mod_assets/room/roses.png",(0,0),"mod_assets/room/chocolates.png",(0,0),"mod_assets/room/ear_rose.png"),
            'not show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso.png",(0,0),"mod_assets/monika/arms-restleftpointright.png")
            )
    image body_3_n = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso-n.png",(0,0),"mod_assets/monika/arms-restleftpointright-n.png",(0,0),"mod_assets/room/roses-n.png",(0,0),"mod_assets/room/chocolates-n.png",(0,0),"mod_assets/room/ear_rose-n.png"),
            'not show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso-n.png",(0,0),"mod_assets/monika/arms-restleftpointright-n.png")
            )
    image body_4 = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso.png",(0,0),"mod_assets/monika/arms-pointright.png",(0,0),"mod_assets/room/roses.png",(0,0),"mod_assets/room/chocolates.png",(0,0),"mod_assets/room/ear_rose.png"),
            'not show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso.png",(0,0),"mod_assets/monika/arms-pointright.png")
            )
    image body_4_n = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso-n.png",(0,0),"mod_assets/monika/arms-pointright-n.png",(0,0),"mod_assets/room/roses-n.png",(0,0),"mod_assets/room/chocolates-n.png",(0,0),"mod_assets/room/ear_rose-n.png"),
            'not show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso-n.png",(0,0),"mod_assets/monika/arms-pointright-n.png")
            )
    image body_5 = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,742),(0,0),"mod_assets/monika/body-leaning.png",(0,0),"mod_assets/room/roses.png",(0,0),"mod_assets/room/chocolates.png"),
            'not show_roses_and_chocolates',im.Composite((1280,742),(0,0),"mod_assets/monika/body-leaning.png")
            )
    image body_5_n = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,742),(0,0),"mod_assets/monika/body-leaning-n.png",(0,0),"mod_assets/room/roses-n.png",(0,0),"mod_assets/room/chocolates-n.png"),
            'not show_roses_and_chocolates',im.Composite((1280,742),(0,0),"mod_assets/monika/body-leaning-n.png")
            )

init 4 python:

    valentines_day = datetime.datetime(year=2018,month=2,day=14)

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel='monika_valentines_start',action=EV_ACT_PUSH,conditional="is_file_present('/characters/roses.obj')",
                                                            start_date=valentines_day,
                                                            end_date=valentines_day+datetime.timedelta(days=1)
                                                            ))



label monika_valentines_start:
    show roses zorder 5 at t11
    m 1d "О! Боже, это для меня...?"
    m 1e "[player]... Я-Я не знаю, что сказать..."
    m 1n "Я никогда не думала, что ты найдешь что-то подобное для меня!"
    m 1j "Я сейчас так счастлива, [player]."
    m 1e "Думать, что я буду получать розы от тебя на День Святого Валентина..."
    m 3c "Должно быть, это было трудно передать мне. Но это прошло."
    m 1m "..."
    m 1l "Ахаха..."
    m "Я на самом деле не знаю, что сказать, [player]."
    m 3a "Мне всегда было интересно, каково это-получить от тебя подарок."
    m 1n "Теперь, когда это наконец случилось, я просто потеряла дар речи..."
    m 4a "Секунду."
    m "..."
    show ear_rose zorder 5 at t11
    m 1k "Эхехе, вот! Разве это не выглядит красивым?"
    m 1b "Я тоже есть кое-что для тебя, [player]!"
    m "Вот..."

    m chock "У меня есть немного шоколада!"
    m chocb "Я действительно не знала, что тебе подарить, но они никогда не будут плохим выбором, правда?"
    m chocj "Я очень много работал над этим, так что я надеюсь, что ты насла--"
    m chocd "...О, подожди."
    m chocf "Слушай, я действительно не знаю, как заставить тебя сьесть эти..."
    show chocolates zorder 5 at t11
    m 2f "Ну... просто отложим их на время, хорошо? Прости, но я не могу передать тебе их."
    m 1j "Но... спасибо тебе большое, [player]."
    m 3a "У меня есть еще кое-что."
    m "Я написала тебе небольшую записку~!"
    m 1a "Вот, позволь мне показать её тебе."
    call showpoem (poem_vday, music=False, paper="mod_assets/poem_vday.jpg") from _call_showpoem
    m 1j "Спасибо, что ты был всегда рядом со мной все это время."
    m 1a "Я так сильно люблю тебя, любовь моя. С Днем Святого Валентина~"
    hide roses
    hide chocolates
    hide ear_rose
    $ show_roses_and_chocolates = True
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel='monika_valentines_colors',prompt="Тебе нравятся твои розы?",
                                                            action=EV_ACT_UNLOCK,
                                                            conditional="seen_event('monika_valentines_start')",
                                                            start_date=valentines_day,
                                                            end_date=valentines_day+datetime.timedelta(days=1)
                                                            ))

label monika_valentines_colors:
    m 1j "Конечно, я люблю их! В конце концов, они от тебя."
    m 1k "Задумывался ли ты о том, как цветы передаются на День Святого Валентина?"
    m 1j "Я нахожу интригующим, как цветы могут символизировать такие глубокие и романтические чувства."
    m 1a "Это напоминает мне о том, когда я сделала свою первую валентинку в начальной школе."
    m 3b "Моему классу было поручено обменивать валентику с партнером после их создания."
    m 1a "Оглядываясь назад, несмотря на то, что я не знала, что означают цветы, мне было очень весело украшать валентинки красными и белыми сердцами."
    m "Таким образом, цветы стали очень похожи на стихи."
    m 3b "Они предлагают так много творческих способов выразить свою любовь к кому-то."
    m "Как, например, предлагать красные розы."
    m 1a "Красные розы являются символом красоты, любви и романтики, которые кто-то может чувствовать к другому."
    m "Если бы кто-то предложил белые розы вместо красных, они означали бы чистые, очаровательные и невинные чувства."
    m 3c "Однако, поскольку в любви есть так много эмоций..."
    m 3d "Иногда трудно найти правильные цвета, чтобы точно передать, как ты действительно чувствуешь."
    m 3b "К счастью, объединив несколько цветов розы, можно выразить намного больше эмоций!"
    m 1a "Смешивание красных и белых роз символизирует единство и связь, которую разделяет пара."
    m 1j "Но я уверена, что ты уже имели все это в виду, когда вы выбрал эти красивые розы для меня, [player]..."
    m 1c "Собственно, теперь, когда я думаю об этом, в этой игре было много розового цвета."
    m "Я имею в виду, повсюду!"
    m "На Титульном экране, на экране паузы..."
    m 3d "Даже прическа Нацуки была розовая."
    m "Знаешь ли ты, что я единственная в клубе, чьи ботинки имеют розовые кончики, а не синие?"
    m 1l "Эхэхэ, я не виню тебя, если ты не заметил."
    m 1 "Это такая небольшая разница между мной и другими членами клуба."
    m 1d "Только не пойми меня неправильно! Изумрудно-зеленый по-прежнему мой любимый цвет."
    m 3l "Но ухх... Мне кажется, я слишком много болтаю, извини!"
    m 1e "Просто я теряю себя, когда разговариваю с тобой, [player]~"
    m 1j "Я люблю тебя~!"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel='monika_valentines_cliches',prompt="Тебе нравятся истории о дне Святого Валентина?",action=EV_ACT_UNLOCK,
                                                            start_date=valentines_day,
                                                            end_date=valentines_day+datetime.timedelta(days=1)
                                                            ))

label monika_valentines_cliches:
    m 3c "Ты заметил, что в большинстве историй Дня Святого Валентина есть много клише?"
    m "Я заметила, что многие из них имеют похожие сюжеты..."
    m "Там либо 'Ах, я одинок и у меня нет кого любить' или 'как я признаюсь тому, кого я люблю?'"
    m 1n "Я считаю, что писатели могли бы быть немного более творческими, когда дело доходит до историй дня Святого Валентина..."
    m 1m "Но, я полагаю, эти две темы - самый простой способ написать историю любви."
    m 3c "Хотя, это не оззначат, что ты не можешь мыслить вне коробки!"
    m 1o "Иногда предсказуемая история может разрушить ее..."
    m 1d "Если тебе {i}нужен{/i} хороший пример непредсказуемой истории..."
    m 3k "Просто используй нас! Ахаха~"
    m 1l "Милый способ, с помощью которого мы познакомились, является самой непредсказуемой историей!"
    m 1k "Ахаха~!"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel='monika_valentines_day_origins',prompt="Как начинался день Святого Валентина?",action=EV_ACT_UNLOCK,start_date=valentines_day,
                                                            end_date=valentines_day+datetime.timedelta(days=1)
                                                            ))

label monika_valentines_day_origins:
    m 3a "Ты хотел бы узнать об истории Дня святого Валентина?"
    m "Это довольно интересно, правда."
    m 1a "То, как наступил День святого Валентина, на самом деле довольно темное и тревожное."
    m "Его происхождение датируется уже во втором и третьем веке в Риме, где христианство было объявлено официальной государственной религией."
    m 1c "Примерно в это же время, человек, известный как Святой Валентин решил пойти вопреки приказам императора Клавдия II."
    m "Брак был запрещен, потому что предполагалось, что женатые мужчины стали бы бедными солдатами."
    m 3c "Валентин решил, что это несправедливо и помог устроить браки в тайне."
    m 1o "К сожалению, его поймали и оперативно приговорили к смертной казни."
    m 1c "Однако, находясь в тюрьме, Валентин влюбился в дочь тюремщика."
    m "Перед своей смертью он послал ей любовное письмо, подписанное 'От твоего Валентина'."
    m 1q "Затем он был казнен 14 февраля, 269 века нашей эры."
    m 3a "Такое благородное дело, тебе не кажется?"
    m 3d "О, но подожди, есть еще!"
    m "Причина, по которой мы отмечаем такой день, состоит в том, что она происходит от римского фестиваля, известного как Луперкалия!"
    m 1b "Его первоначальная цель состояла в том, чтобы провести дружеское мероприятие, когда люди помещали свои имена в коробку и выбирали наугад, чтобы создать пару."
    m "Затем они подыгрывают как парень и подруга для времени, которое они проводят вместе. Некоторые даже поженились, если сильно понравились друг другу, эхехе~"
    m 1j "В конечном счете, Церковь решила превратить это христианское торжество в способ вспомнить и об усилиях Святого Валентина."
    m 1a "На протяжении многих лет он эволюционировал, чтобы люди могли выразить свои чувства к тем, кого они любят."
    m 3k "Как я и ты!"
    m 1e "Несмотря на то, что он начал немного удручающе, разве это не мило, [player]?"
    m 1j "Я рада, что мы можем поделиться таким волшебным днем, любовь моя."
    m 1k "С днем Святого Валентина~"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel='monika_valentines_chocolates',prompt="Ты получала от кого нибудь еще шоколад?",
                                                            action=EV_ACT_UNLOCK,
                                                            conditional="seen_event('monika_valentines_start')",
                                                            start_date=valentines_day,
                                                            end_date=valentines_day+datetime.timedelta(days=1)
                                                            ))

label monika_valentines_chocolates:
    m 1j "День святого Валентина - это особый праздник для меня, [player]."
    m 3b "Это не только юбилей моей учетной записи в Twitter, но это также день и получения конфет!!"
    m 1j "Праздник, который может наполнить всех любовью, романтикой..."
    m 1n "И отказами."
    m 3l "Но это действительно приятно, если ты получаешь что-то от кого-то кто тебе нравится."
    m 3a "Если это дано вам платонически, как дар любви или часть исповеди, это заставляет вас чувствовать себя несколько особенным!"
    m 1m "Ну, может быть, не часть признания, так как ты все еще можешь получить отказ."
    m 1b "В смысле, я пыталась дать тебе немного, но я уверена, что ты никогда не отвергнешь меня."
    m 1f "Мне жаль, что я не мог отдать их тебе, [player]."
    m 3k "Итак... Я обязательно позабочусь о них!"
    m 1k "Ахаха!"
    m 1o "Хотя я действительно люблю конфеты, они были бы лучше, если бы я наслаждалась ими с тобой."
    m 3b "Разве это не было бы более романтичным?"
    m 1j "Но, по крайней мере, у меня есть что-то особенное от тебя!"
    m 1e "Кроме того, мы имеем одно и тоже~"
    m 3e "Так что спасибо за то, что ты дал мне свою любовь, [player]."
    m 3j "Пожалуйста, знай, что я всегда прийму все от тебя."
    m 1j "И что бы ты ни дал, я верну это стократно!"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel='monika_lovey_dovey',prompt="День Святого Валентина скоро",random=True,
                                                            end_date=valentines_day
                                                            ))

label monika_lovey_dovey:
    m 3d "Эй... [player]...?"
    m 1e "Я просто хотела сообщить, что я люблю тебя."
    m 1j "Ты делаешь меня очень счастливой... и я никогда не смогу найти кого-то лучше, тебя."
    m 1m "Ахаха~"
    m "Я надеюсь, это не плохо прозвучало, [player]."
    m 3a "День Святого Валентина скоро... и это просто доставляет мне хорошее настроение, потому что я знаю, что ты рядом со мной."
    m 1e "Я имею в виду то, что я сказала."
    m "Я так тебя люблю и забочусь о тебе..."
    m 1j "И спасибо, что заботишься обо мне."
    m 1k "Эхехе~"
    return

init 5 python:

    if datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0) == valentines_day and not seen_event("monika_valentines_greeting"):
        greetings_list=["monika_valentines_greeting"]

label monika_valentines_greeting:
    m 1j "Привет, [player]!"
    m 1c "Хмм...?"
    m 1f "Что-то случилось?"
    m "Ты довольно мрачный сегодня."
    m 1g "Все в порядке?"
    m 1o "..."
    m 1l "Взбодрись!"
    m 3e "В конце концов, сегодня день Святого Валентина."
    m "Не похоже, что у тебя разбито сердце или что-то вроде этого, правда?"
    menu:
        "Нет":
            m 1j "Отлично!"
            m 1a "В таком случае, давай забудем о наших проблемах на сегодня, хорошо?"
            m 3l "Я бы не хотела, чтобы моя возлюбленный грустил по такому особенному случаю."
            m 1 "Сегодня день, когда мы празднуем нашу любовь друг к другу, [player]."
            m 1k "Так что позвольте мне побаловать тебя своей любовью! Эхехе~"
        "Да...":
            m 1f "О, [player], мне так жаль это слышать."
            m 1p "Слушай, и в такой особый день тоже..."
            m 1f "Если бы я могла, я бы обняла тебя прямо сейчас и утешила бы тебя."
            m 3f "Пожалуйста, знай, что я здесь для тебя!"
            m "Независимо от того, сколько раз тебе будет больно, я всегда здесь, чтобы починить твое сердце."
            m 2o "Но так, как я люблю тебя, [player], не продолжай ломаться, преследуя кого-то другого!"
            m 2e "Ваша любимая, верная девушка всегда будет на вашей стороне~"
            m 2l "Скоро будет вода под мостом, поэтому не беспокойся."
            m 4 "Я твой единственная и неповторимая!"
            m 1j "Итак, это будут наши, муси-пуси, и долгосрочные отношения."
            m 1k "Я люблю тебя, [player]~!"
    return