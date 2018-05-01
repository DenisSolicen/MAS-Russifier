


label sayori_name_scare:
    python:
        from store.songs import FP_SAYO_NARA, initMusicChoices
        initMusicChoices(sayori=True)
        play_song(FP_SAYO_NARA)
        persistent.current_track = FP_SAYO_NARA
        store.songs.selected_track = FP_SAYO_NARA
        store.songs.current_track = FP_SAYO_NARA
    return


label yuri_name_scare:


    $ HKBHideButtons()
    $ disable_esc()


    scene black
    show yuri eyes zorder 2 at t11
    play music hb
    show layer master at heartbeat
    show dark zorder 200
    pause 4.0
    hide yuri
    hide dark
    show layer master
    stop music


    $ HKBShowButtons()
    $ enable_esc()
    return


label natsuki_name_scare(playing_okayev=False):


    $ HKBHideButtons()
    $ disable_esc()
    $ store.songs.enabled = False
    $ quick_menu = False
    $ scary_t5c = "bgm/5_ghost.ogg"
    $ curr_vol = store.songs.getVolume("music")
    $ renpy.music.set_volume(1.0, channel="music")


    if playing_okayev:
        $ currentpos = get_pos(channel="music")
        $ adjusted_t5c = "<from " + str(currentpos) + " loop 4.444>" + scary_t5c
        stop music fadeout 2.0
        $ renpy.music.play(adjusted_t5c, fadein=2.0, tight=True)
    else:
        stop music
        $ play_song("<from 11>" + scary_t5c)


    scene black
    show darkred zorder 5
    show natsuki ghost1 zorder 2 at t11
    show n_rects_ghost1_instant zorder 4
    show n_rects_ghost2_instant zorder 4
    show n_rects_ghost3_instant zorder 4
    show natsuki_ghost_blood zorder 3




    pause 5



    play sound "sfx/crack.ogg"
    hide natsuki_ghost_blood
    hide n_rects_ghost1_instant
    hide n_rects_ghost2_instant
    hide n_rects_ghost3_instant
    show natsuki ghost3
    show n_rects_ghost4 onlayer front zorder 4
    show n_rects_ghost5 onlayer front zorder 4
    pause 0.5


    hide natsuki
    play sound "sfx/run.ogg"
    show natsuki ghost4 on layer front at i11
    pause 0.25


    window hide(None)
    hide natsuki onlayer front
    hide n_rects_ghost4 onlayer front
    hide n_rects_ghost5 onlayer front
    scene black
    with None
    window auto
    scene black


    python:
        HKBShowButtons()
        enable_esc()
        store.songs.enabled = True
        quick_menu = True
        renpy.music.set_volume(curr_vol, channel="music")



    if playing_okayev:
        $ currentpos = get_pos(channel="music")
        $ adjusted_okayev = "<from " + str(currentpos) + " loop 4.444>bgm/5_monika.ogg"
        stop music fadeout 2.0
        $ renpy.music.play(adjusted_okayev, fadein=2.0, tight=True)
    else:
        stop music
        $ play_song(store.songs.current_track)

    return


image n_rects_ghost1_instant:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (580, 270)
    size (20, 25)

image n_rects_ghost2_instant:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (652, 264)
    size (20, 25)

image n_rects_ghost3_instant:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (616, 310)
    size (25, 15)