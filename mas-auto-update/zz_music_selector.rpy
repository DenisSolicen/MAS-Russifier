




init -1 python in songs:



    PIANO_COVER = "Your Reality (Piano Cover)"
    JUST_MONIKA = "Just Monika"
    YOURE_REAL = "Your Reality"
    STILL_LOVE = "I Still Love You"
    OKAY_EV_MON = "Okay, Everyone! (Monika)"
    DDLC_MT_80 = "Doki Doki Theme (80s ver.)"
    SAYO_NARA = "Сюрприз!"
    PLAYWITHME_VAR6 = "Play With Me (Variant 6)"
    NO_SONG = "Ничего"


    FP_PIANO_COVER = "mod_assets/bgm/runereality.ogg"
    FP_JUST_MONIKA = "bgm/m1.ogg"
    FP_YOURE_REAL = "bgm/credits.ogg"
    FP_STILL_LOVE = "bgm/monika-end.ogg"
    FP_OKAY_EV_MON = "<loop 4.444>bgm/5_monika.ogg"
    FP_DDLC_MT_80 = (
        "<loop 17.451 to 119.999>mod_assets/bgm/ddlc_maintheme_80s.ogg"
    )
    FP_SAYO_NARA = "<loop 36.782>bgm/d.ogg"
    FP_PLAYWITHME_VAR6 = "<loop 43.572>bgm/6s.ogg"
    FP_NO_SONG = None



    def adjustVolume(channel="music",up=True):
        
        
        
        
        
        
        
        
        direct = 1
        if not up:
            direct = -1
        
        
        new_vol = getVolume(channel)+(direct*vol_bump)
        if new_vol < 0.0:
            new_vol = 0.0
        elif new_vol > 1.0:
            new_vol = 1.0
        
        renpy.music.set_volume(new_vol, channel=channel)

    def getVolume(channel):
        
        
        
        
        
        
        
        
        return renpy.audio.audio.get_channel(channel).context.secondary_volume

    def getPlayingMusicName():
        
        
        
        
        
        
        
        
        
        
        
        
        curr_filename = renpy.music.get_playing()
        
        
        if curr_filename:
            bracket_endex = curr_filename.find(">")
            
            if bracket_endex >= 0:
                curr_filename = curr_filename[bracket_endex:]
            
            
            for name,song in music_choices:
                
                
                if song: 
                    bracket_endex = song.find(">")
                    
                    if bracket_endex >= 0:
                        check_song = song[bracket_endex:]
                    else:
                        check_song = song
                else:
                    check_song = song
                
                if curr_filename == check_song:
                    return name
        return None

    def initMusicChoices(sayori=False):
        
        
        
        
        
        
        
        global music_choices
        music_choices = list()
        
        
        
        
        if not sayori:
            music_choices.append((JUST_MONIKA, FP_JUST_MONIKA))
            music_choices.append((YOURE_REAL, FP_YOURE_REAL))
            
            
            music_choices.append((PIANO_COVER, FP_PIANO_COVER))
            
            music_choices.append((STILL_LOVE, FP_STILL_LOVE))
            music_choices.append((OKAY_EV_MON, FP_OKAY_EV_MON))
            music_choices.append((PLAYWITHME_VAR6, FP_PLAYWITHME_VAR6))
            
            
            music_choices.append((DDLC_MT_80, FP_DDLC_MT_80))
        
        
        music_choices.append((SAYO_NARA, FP_SAYO_NARA))
        
        if not sayori:
            
            music_choices.append((NO_SONG, FP_NO_SONG))



    current_track = "bgm/m1.ogg"
    selected_track = current_track
    menu_open = False
    enabled = True
    vol_bump = 0.1 


    music_choices = list()


init 10 python in songs:


    music_volume = getVolume("music")


init 10 python:


    if persistent.playername.lower() == "sayori":
        store.songs.current_track = store.songs.FP_SAYO_NARA
        store.songs.selected_track = store.songs.FP_SAYO_NARA
        persistent.current_track = store.songs.FP_SAYO_NARA
    else:
        store.songs.current_track = persistent.current_track
        store.songs.selected_track = store.songs.current_track


    store.songs.initMusicChoices(
        sayori=persistent.playername.lower() == "sayori"
    )


















style music_menu_return_button_text is navigation_button_text

style music_menu_outer_frame is game_menu_outer_frame
style music_menu_navigation_frame is game_menu_navigation_frame
style music_menu_content_frame is game_menu_content_frame
style music_menu_viewport is game_menu_viewport
style music_menu_side is game_menu_side
style music_menu_label is game_menu_label
style music_menu_label_text is game_menu_label_text

style music_menu_return_button is return_button

style music_menu_outer_frame:
    background "mod_assets/music_menu.png"

screen music_menu():
    modal True


    key "noshift_M" action Return()
    key "noshift_m" action Return()

    zorder 200

    style_prefix "music_menu"

    frame:
        style "music_menu_outer_frame"

        has hbox

        frame:
            style "music_menu_navigation_frame"

        frame:
            style "music_menu_content_frame"

            transclude


    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.8
        spacing gui.navigation_spacing


        $ import store.songs as songs
        for name,song in songs.music_choices:
            textbutton _(name) action [SetField(songs,"selected_track",song), Return()]

    textbutton _("Вернуться"):
        style "music_menu_return_button"
        action Return()

    label "Music Menu"


label display_music_menu:

    python:
        import store.songs as songs
        songs.menu_open = True
        prev_dialogue = allow_dialogue
        allow_dialogue = False

    call screen music_menu

    $ songs.menu_open = False
    $ allow_dialogue = prev_dialogue
    return