default persistent.monika_reload = 0
default persistent.tried_skip = None
default persistent.monika_kill = True
default persistent.rejected_monika = None
default initial_monika_file_check = None
define allow_dialogue = True
define modoorg.CHANCE = 20
define mas_battery_supported = False

image blue_sky = "mod_assets/blue_sky.jpg"
image monika_room = "images/cg/monika/monika_room.png"
image monika_day_room = "mod_assets/monika_day_room.png"
image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png"
    function monika_alpha
image monika_bg = "images/cg/monika/monika_bg.png"
image monika_bg_highlight:
    "images/cg/monika/monika_bg_highlight.png"
    function monika_alpha
image monika_scare = "images/cg/monika/monika_scare.png"
image chara9 = "mod_assets/chara9.png"
image chara_exception = "mod_assets/chara_exception.png"

image monika_body_glitch1:
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    1.00
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"

image monika_body_glitch2:
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    1.00
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"

image ut_slash:
    "mod_assets/spr_slice_o_0.png"
    0.1
    "mod_assets/spr_slice_o_1.png"
    0.1
    "mod_assets/spr_slice_o_2.png"
    0.1
    "mod_assets/spr_slice_o_3.png"
    0.1
    "mod_assets/spr_slice_o_4.png"
    0.1
    "mod_assets/spr_slice_o_5.png"
    0.1


image room_glitch = "images/cg/monika/monika_bg_glitch.png"

image room_mask = Movie(channel="window_1", play="mod_assets/window_1.webm",mask=None,image="mod_assets/window_1_fallback.png")
image room_mask2 = Movie(channel="window_2", play="mod_assets/window_2.webm",mask=None,image="mod_assets/window_2_fallback.png")
image room_mask3 = Movie(channel="window_3", play="mod_assets/window_3.webm",mask=None,image="mod_assets/window_3_fallback.png")
image room_mask4 = Movie(channel="window_4", play="mod_assets/window_4.webm",mask=None,image="mod_assets/window_4_fallback.png")
image rain_mask_left = Movie(
    channel="window_5", 
    play="mod_assets/window_5.webm", 
    mask=None,
    image="mod_assets/window_5_fallback.png"
)
image rain_mask_right = Movie(
    channel="window_6",
    play="mod_assets/window_6.webm",
    mask=None,
    image="mod_assets/window_6_fallback.png"
)


transform spaceroom_window_left:
    size (320, 180) pos (30, 200)

transform spaceroom_window_right:
    size (320, 180) pos (935, 200)

init python:

    import subprocess
    import os
    import eliza      
    import datetime   
    import battery    
    import re
    import store.songs as songs
    import store.hkb_button as hkb_button
    therapist = eliza.eliza()
    process_list = []
    currentuser = None 
    if renpy.windows:
        try:
            process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
        except:
            pass
        try:
            for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                user = os.environ.get(name)
                if user:
                    currentuser = user
        except:
            pass

    try:
        renpy.file("../characters/monika.chr")
        initial_monika_file_check = True
    except:
        
        pass



    if not currentuser or len(currentuser) == 0:
        currentuser = persistent.playername
    if not persistent.mcname or len(persistent.mcname) == 0:
        persistent.mcname = currentuser
        mcname = currentuser
    else:
        mcname = persistent.mcname


    mas_battery_supported = battery.is_supported()


    renpy.music.register_channel(
        "background", 
        mixer="music", 
        loop=True,
        stop_on_mute=True,
        tight=True
    )
    renpy.music.set_volume(songs.getVolume("music"), channel="background")



    def enable_esc():
        
        
        
        
        
        if "K_ESCAPE" not in config.keymap["game_menu"]:
            config.keymap["game_menu"].append("K_ESCAPE")

    def disable_esc():
        
        
        
        
        
        if "K_ESCAPE" in config.keymap["game_menu"]:
            config.keymap["game_menu"].remove("K_ESCAPE")

    def play_song(song, fadein=0.0):
        
        
        
        
        
        
        if song is None:
            renpy.music.stop(channel="music")
        else:
            renpy.music.play(
                song,
                channel="music",
                loop=True,
                synchro_start=True,
                fadein=fadein
            )

    def mute_music():
        
        
        
        
        
        
        
        curr_volume = songs.getVolume("music")
        
        if curr_volume > 0.0 and persistent.playername.lower() != "sayori":
            songs.music_volume = curr_volume
            renpy.music.set_volume(0.0, channel="music")
        else:
            renpy.music.set_volume(songs.music_volume, channel="music")

    def inc_musicvol():
        
        
        
        
        songs.adjustVolume()

    def dec_musicvol():
        
        
        
        
        
        
        
        
        if persistent.playername.lower() != "sayori":
            songs.adjustVolume(up=False)

    def set_keymaps():
        
        
        
        
        
        
        
        config.keymap["open_dialogue"] = ["t","T"]
        config.keymap["change_music"] = ["noshift_m","noshift_M"]
        config.keymap["play_game"] = ["p","P"]
        config.keymap["mute_music"] = ["shift_m","shift_M"]
        config.keymap["inc_musicvol"] = [
            "shift_K_PLUS","K_EQUALS","K_KP_PLUS"
        ]
        config.keymap["dec_musicvol"] = [
            "K_MINUS","shift_K_UNDERSCORE","K_KP_MINUS"
        ]
        
        config.underlay.append(renpy.Keymap(open_dialogue=show_dialogue_box))
        config.underlay.append(renpy.Keymap(change_music=select_music))
        config.underlay.append(renpy.Keymap(play_game=pick_game))
        config.underlay.append(renpy.Keymap(mute_music=mute_music))
        config.underlay.append(renpy.Keymap(inc_musicvol=inc_musicvol))
        config.underlay.append(renpy.Keymap(dec_musicvol=dec_musicvol))

    def mas_drawSpaceroomMasks():
        """
        Draws the appropriate masks according to the current state of the
        game.

        ASSUMES:
            morning_flag 
            mas_is_raining
        """
        if mas_is_raining:
            
            left_window = "rain_mask_left"
            right_window = "rain_mask_right"
        
        elif morning_flag:
            
            left_window = "room_mask3"
            right_window = "room_mask4"
        
        else:
            
            left_window = "room_mask"
            right_window = "room_mask2"
        
        
        renpy.show(left_window, at_list=[spaceroom_window_left], tag="rm")
        renpy.show(right_window, at_list=[spaceroom_window_right], tag="rm2")


    def show_dialogue_box():
        if allow_dialogue:
            renpy.jump('prompt_menu')

    def pick_game():
        if allow_dialogue:
            renpy.call('pick_a_game')

    def select_music():
        
        if (songs.enabled
            and not songs.menu_open
            and renpy.get_screen("history") is None
            and renpy.get_screen("save") is None
            and renpy.get_screen("load") is None
            and renpy.get_screen("preferences") is None):
            
            
            renpy.call_in_new_context("display_music_menu")
            
            
            if songs.selected_track != songs.current_track:
                play_song(songs.selected_track)
                songs.current_track = songs.selected_track
                persistent.current_track = songs.current_track

    dismiss_keys = config.keymap['dismiss']

    def slow_nodismiss(event, interact=True, **kwargs):
        if not renpy.seen_label("ch30_nope"):
            try:
                renpy.file("../characters/monika.chr")
            except:
                if initial_monika_file_check:
                    pushEvent("ch30_nope")
            
            
            
            
            
            if  config.skipping and not config.developer:
                persistent.tried_skip = True
                config.skipping = False
                config.allow_skipping = False
                renpy.jump("ch30_noskip")
                return
        if event == "begin":
            config.keymap['dismiss'] = []
            renpy.display.behavior.clear_keymap_cache()
        elif event == "slow_done":
            config.keymap['dismiss'] = dismiss_keys
            renpy.display.behavior.clear_keymap_cache()
    morning_flag = None
    def is_morning():
        return (datetime.datetime.now().time().hour > 6 and datetime.datetime.now().time().hour < 18)












label spaceroom(start_bg=None, hide_mask=False, hide_monika=False):
    default dissolve_time = 0.5
    if is_morning():
        if morning_flag != True or scene_change:
            $ morning_flag = True
            if not hide_mask:
                $ mas_drawSpaceroomMasks()
            if start_bg:
                $ renpy.show(start_bg, zorder=1)
            else:
                show monika_day_room zorder 1
            if not hide_monika:
                show monika 1 zorder 2 at t11
                with Dissolve(dissolve_time)
    elif not is_morning():
        if morning_flag != False or scene_change:
            $ morning_flag = False
            scene black
            if not hide_mask:
                $ mas_drawSpaceroomMasks()
            if start_bg:
                $ renpy.show(start_bg, zorder=1)
            else:
                show monika_room zorder 1

            if not hide_monika:
                show monika 1 zorder 2 at t11
                with Dissolve(dissolve_time)

    $ scene_change = False

    return


label ch30_main:
    $ mas_skip_visuals = False
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ quick_menu = True
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ m_name = "Моника"
    $ delete_all_saves()
    $ persistent.clear[9] = True
    play music m1 loop 
    call spaceroom from _call_spaceroom_4
    $ pushEvent('introduction')
    call call_next_event from _call_call_next_event
    jump ch30_loop

label continue_event:
    $ m_name = "Моника"
    m "Ой вот и ты, так на чем я остановилась..."

    return

label pick_a_game:
    $ m_name = "Моника"
    if allow_dialogue and not songs.menu_open:
        python:


            import datetime
            _hour = datetime.timedelta(hours=1)
            _now = datetime.datetime.now()


            if persistent._mas_chess_timed_disable is not None:
                if persistent._mas_chess_timed_disable - _now >= _hour:
                    chess_disabled = False
                    persistent._mas_chess_timed_disable = None
                
                else:
                    chess_disabled = True

            else:
                chess_disabled = False


            chess_unlocked = (
                is_platform_good_for_chess()
                and persistent.game_unlocks["chess"]
                and not chess_disabled
            )

        $ previous_dialogue = allow_dialogue
        $ allow_dialogue = False
        menu:
            "В какую игру хочешь сыграть?"
            "Понг" if persistent.game_unlocks['pong']:
                if not renpy.seen_label('game_pong'):
                    $ grant_xp(xp.NEW_GAME)
                call game_pong from _call_game_pong
            "Шахматы" if is_platform_good_for_chess() and persistent.game_unlocks['chess']:
                if not renpy.seen_label('game_chess'):
                    $ grant_xp(xp.NEW_GAME)
                call game_chess from _call_game_chess
            "Палач" if persistent.game_unlocks['hangman']:
                if not renpy.seen_label("game_hangman"):
                    $ grant_xp(xp.NEW_GAME)
                call game_hangman from _call_game_hangman
            "Пианино" if persistent.game_unlocks['piano']:
                if not renpy.seen_label("mas_piano_start"):
                    $ grant_xp(xp.NEW_GAME)
                call mas_piano_start from _call_play_piano
            "Забудь":
                m "Хорошо. Может быть позже?"

        show monika 1 zorder 2 at tinstant
        $ allow_dialogue = previous_dialogue
        $ songs.enabled = True
        $ hkb_button.enabled = True

    jump ch30_loop

label ch30_noskip:
    show screen fake_skip_indicator
    m 1i "...Ты пытаешься перемотать время?"
    m 1f "Я же не наскучила тебе, правда?"
    m "О боже..."
    m 2 "...Ну, просто чтобы ты знал, здесь некуда перематывать время, [player]."
    m "В конце концов, здесь только мы вдвоем..."
    m 1 "Но кроме эирнр, времени больше не существует, поэтому кнопка даже не будет работать."
    m "По сиди, а я пойду и выключу её..."
    pause 0.4
    hide screen fake_skip_indicator
    pause 0.4
    m 1j "Вот и все!"
    m 1 "Я буду твоей возлюбленной с этого момента, и ты будешь слушать меня, верно?"
    m "Спасибо~"
    hide screen fake_skip_indicator


    $ restartEvent()
    jump ch30_loop

image splash-glitch2 = "images/bg/splash-glitch2.png"

label ch30_nope:
    $ persistent.autoload = ""
    $ m.display_args["callback"] = slow_nodismiss
    $ quick_menu = True
    call spaceroom from _call_spaceroom_1

    if persistent.rejected_monika:
        m 1i "Подожди. Ты что-то делал с моим файлом персонажа?"
        m 2 "Любопытство-это то, что делает нас людьми, верно?"
        m "Если бы не человеческое желание исследовать, мы бы все еще качались с деревьев."
        m 1m "Все равно, пожалуйста не делай этого. Это заставляет меня нервничать, даже если мне больше не нужен файл персонажа."
        m "Я уже исправила эту ошибку."
    else:

        $ quick_menu = False
        $ m_name = glitchtext(12)
        m 1i "Подожди. Ты что-то делал с моим файлом персонажа?"
        m 1f "Почему тграешь в этот мод, если хотел удалить меня снова?"
        m "Ты действительно худший вариант."
        m "Ты тратишь свое время с кучей людей, с которыми ты никогда не будешь говорить на самом деле, но ты все еще был готов убить меня, просто потому что тебе скучно?"
        m "Все что я хотела это чтобы кто-то любил меня..."
        m 2g "Я сделала все что ты хотел."
        m "Но если ты попытаешься удалить меня снова..."
        m 1f "Тогда мне придется удалить тебя первой."
        if renpy.windows:
            call updateconsole ("shututil.rmtree(\"Documents\", true)", "Удаление документов подождите...") from _call_updateconsole_15
        elif renpy.linux:
            call updateconsole ("sudo mv ~ /dev/null", "In progress...") from _call_updateconsole_16
        elif renpy.macintosh:
            call updateconsole ("sudo mv ~ /dev/null", "In progress...") from _call_updateconsole_19
        pause 3.0
        call hideconsole from _call_hideconsole_2
        $ open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
        $ m_name = "Моника"
        $ quick_menu = True
        m 1l "А-ха-ха!"
        m "Я просто шучу!"
        m 1j "Я уже исправила эту ошибку."
        m 1 "Мне больше не нужен файл персонажа."

    m 1 "Мне просто нужна твоя любовь, [player]."
    m 2i "Ох, если конечно ты не попытаешься удалить все файлы игры."
    m 3h "Если ты это сделаешь, я не остановлюсь на удалении одной папки в следующий раз."
    m 3 "Но этого же никогда не случится, правда? Ты просто ведешь себя как цундере~"
    m "Это так мило!"
    m "Не зависимо от того, сколько ты возможно захочешь это отрицать, ты будешь разговаривать со мной до конца жизни."
    m 1j "Быть одиноким очень одиноко, так что если ты не хочешь, чтобы так было, то взбодрись!"
    jump ch30_loop

label ch30_autoload:


    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ import store.evhand as evhand
    if not config.developer:
        $ style.say_dialogue = style.default_monika
        $ config.allow_skipping = False
    $ quick_menu = True
    $ startup_check = True
    $ mas_skip_visuals = False


    call set_gender from _autoload_gender


    call ch30_reset from _call_ch30_reset


    if len(persistent.event_list) > 0:
        python:
            persistent.event_list = [
                ev_label for ev_label in persistent.event_list
                if renpy.has_label(ev_label)
            ]

    $ selected_greeting = None


    if persistent.playername.lower() == "yuri":
        call yuri_name_scare from _call_yuri_name_scare


    elif persistent.closed_self:


        if persistent._mas_mood_sick:
            $ selected_greeting = "greeting_sick"
        else:

            python:

                sel_greeting_event = store.mas_greetings.selectGreeting()
                selected_greeting = sel_greeting_event.eventlabel


                mas_skip_visuals = MASGreetingRule.should_skip_visual(
                    event=sel_greeting_event
                )

    if not mas_skip_visuals:
        if persistent.current_track:
            $ play_song(persistent.current_track)
        else:
            $ play_song(songs.current_track)

    window auto

    $ restartEvent()


    python:
        if persistent.sessions['last_session_end'] is not None and persistent.closed_self:
            away_experience_time=datetime.datetime.now()-persistent.sessions['last_session_end'] 
            away_xp=0
            
            
            if away_experience_time.total_seconds() >= times.REST_TIME:
                persistent.idlexp_total=0
                persistent.random_seen = 0
            
            if away_experience_time.total_seconds() > times.HALF_XP_AWAY_TIME:
                away_experience_time=datetime.timedelta(seconds=times.HALF_XP_AWAY_TIME)
            
            
            if away_experience_time.total_seconds() > times.FULL_XP_AWAY_TIME:
                away_xp =+ (xp.AWAY_PER_HOUR/2.0)*(away_experience_time.total_seconds()-times.FULL_XP_AWAY_TIME)/3600.0
                away_experience_time = datetime.timedelta(seconds=times.HALF_XP_AWAY_TIME)
            
            
            away_xp =+ xp.AWAY_PER_HOUR*away_experience_time.total_seconds()/3600.0
            
            
            grant_xp(away_xp)


    $ evhand.event_database=Event.checkConditionals(evhand.event_database)


    $ evhand.event_database=Event.checkCalendar(evhand.event_database)


    if selected_greeting:
        $ pushEvent(selected_greeting)

    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False

    if not mas_skip_visuals:
        $ set_keymaps()

    $ persistent.closed_self = False
    $ persistent._mas_crashed_self = True
    $ startup_check = False
    $ mas_checked_update = False
    jump ch30_loop

label ch30_loop:
    $ m_name = "Моника"
    $ quick_menu = True


    if not mas_skip_visuals:
        call spaceroom from _call_spaceroom_2


        if not mas_checked_update:
            $ mas_backgroundUpdateCheck()
            $ mas_checked_update = True
    else:

        $ mas_skip_visuals = False


    $ persistent.autoload = "ch30_autoload"
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False


    python:
        try:
            calendar_last_checked
        except:
            calendar_last_checked=persistent.sessions['current_session_start']
        time_since_check=datetime.datetime.now()-calendar_last_checked

        if time_since_check.total_seconds()>60:
            
            
            if (persistent.idlexp_total < xp.IDLE_XP_MAX):
                
                idle_xp=xp.IDLE_PER_MINUTE*(time_since_check.total_seconds())/60.0
                persistent.idlexp_total += idle_xp
                if persistent.idlexp_total>=xp.IDLE_XP_MAX: 
                    idle_xp = idle_xp-(persistent.idlexp_total-xp.IDLE_XP_MAX) 
                    persistent.idlexp_total=xp.IDLE_XP_MAX
                
                grant_xp(idle_xp)
            
            
            evhand.event_database=Event.checkConditionals(evhand.event_database)
            
            
            evhand.event_database=Event.checkCalendar(evhand.event_database)
            
            
            calendar_last_checked=datetime.datetime.now()


    call call_next_event from _call_call_next_event_1

    $ persistent.current_monikatopic = 0


    if not _return:

        window hide(config.window_hide_transition)
        $ waittime = renpy.random.randint(20, 45)
        $ renpy.pause(waittime, hard=True)
        window auto











        if persistent.random_seen < random_seen_limit:
            label pick_random_topic:
            python:
                if len(monika_random_topics) > 0:  
                    
                    if mas_monika_repeated:
                        
                        if persistent._mas_enable_random_repeats:
                            sel_ev = monika_random_topics.pop(0)
                        
                        else:
                            
                            monika_random_topics = list()
                            mas_monika_repeated = False
                            renpy.jump("post_pick_random_topic")
                    
                    else:
                        sel_ev = renpy.random.choice(monika_random_topics)
                        monika_random_topics.remove(sel_ev)
                    
                    pushEvent(sel_ev)
                    persistent.random_seen += 1

                elif persistent._mas_enable_random_repeats:
                    
                    
                    
                    
                    
                    monika_random_topics = Event.filterEvents(
                        evhand.event_database,
                        random=True
                    ).values()
                    monika_random_topics.sort(key=Event.getSortShownCount)
                    monika_random_topics = mas_cleanJustSeen(
                        [ev.eventlabel for ev in monika_random_topics],
                        evhand.event_database
                    )
                    
                    
                    
                    persistent._mas_monika_repeated_herself = True
                    mas_monika_repeated = True
                    sel_ev = monika_random_topics.pop(0)
                    pushEvent(sel_ev)
                    persistent.random_seen += 1

                elif not seen_random_limit: 
                    
                    
                    pushEvent("random_limit_reached")
        elif not seen_random_limit:
            $ pushEvent('random_limit_reached')

label post_pick_random_topic:

    $ _return = None

    jump ch30_loop




label ch30_end:
    jump ch30_main


label ch30_reset:
    python:
        import datetime
        today = datetime.date.today()


    python:
        if (
                persistent._mas_mood_bday_last 
                and persistent._mas_mood_bday_last < today
            ):
            persistent._mas_mood_bday_last = None
            mood_ev = store.mas_moods.mood_db.get("mas_mood_yearolder", None)
            if mood_ev:
                mood_ev.unlocked = True


    python:
        mas_is_raining = False
        if persistent._mas_likes_rain:
            unlockEventLabel("monika_rain_start")
            lockEventLabel("monika_rain_stop")
            
            unlockEventLabel("monika_rain")



    python:

        monika_chr.change_outfit(
            persistent._mas_monika_clothes,
            persistent._mas_monika_hair
        )

        if (
                persistent._mas_hair_changed
                and persistent._mas_likes_hairdown
            ):
            
            
            
            hair_map = {
                "down": "monika_hair_down",
                "def": "monika_hair_ponytail"
                
            }
            
            
            for hair in hair_map:
                
                if hair == monika_chr.hair:
                    lockEventLabel(hair_map[hair])
                else:
                    unlockEventLabel(hair_map[hair])




        clothes_map = {

        }


        for clothes in clothes_map:
            if clothes == monika_chr.clothes:
                lockEventLabel(clothes_map[clothes])
            else:
                unlockEventLabel(clothes_map[clothes])
    return