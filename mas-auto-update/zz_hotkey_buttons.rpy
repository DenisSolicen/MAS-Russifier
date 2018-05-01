


init python:


    def HKBHideButtons():
        
        
        
        config.overlay_screens.remove("hkb_overlay")
        renpy.hide_screen("hkb_overlay")


    def HKBShowButtons():
        
        
        
        config.overlay_screens.append("hkb_overlay")


    def MovieOverlayHideButtons():
        
        
        
        if "movie_overlay" in config.overlay_screens:
            config.overlay_screens.remove("movie_overlay")
            renpy.hide_screen("movie_overlay")


    def MovieOverlayShowButtons():
        
        
        
        config.overlay_screens.append("movie_overlay")

init -1 python in hkb_button:



    enabled = True
    movie_buttons_enabled = False







define gui.hkb_button_width = 120
define gui.hkb_button_height = None
define gui.hkb_button_tile = False
define gui.hkb_button_borders = Borders(100, 5, 100, 5)
define gui.hkb_button_text_font = gui.default_font
define gui.hkb_button_text_size = gui.text_size
define gui.hkb_button_text_xalign = 0.5
define gui.hkb_button_text_idle_color = "#000"
define gui.hkb_button_text_hover_color = "#fa9"



style hkb_vbox is vbox
style hkb_button is button
style hkb_button_text is button_text

style hkb_vbox:
    spacing 0

style hkb_button is default:
    properties gui.button_properties("hkb_button")
    idle_background "mod_assets/hkb_idle_background.png"
    hover_background "mod_assets/hkb_hover_background.png"

    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style hkb_button_text is default:
    properties gui.button_text_properties("hkb_button")
    outlines []


style hkbd_vbox is vbox
style hkbd_button is button
style hkbd_button_text is button_text

style hkbd_vbox:
    spacing 0

style hkbd_button is default:
    properties gui.button_properties("hkb_button")
    idle_background "mod_assets/hkb_disabled_background.png"
    hover_background "mod_assets/hkb_disabled_background.png"

style hkbd_button_text is default:

    font gui.default_font
    size gui.text_size
    xalign 0.5
    idle_color "#000"
    hover_color "#000"
    outlines []

screen hkb_overlay():

    zorder 50

    style_prefix "hkb"

    vbox:
        xalign 0.05
        yalign 0.95

        if allow_dialogue and store.hkb_button.enabled:
            textbutton _("{size=-6}Поговорить{/size}") action Jump("prompt_menu")
        else:
            textbutton _("{size=-6}Поговорить{/size}"):
                action NullAction()
                style "hkbd_button"

        if store.hkb_button.enabled:
            textbutton _("{size=-6}Музыка{/size}") action Function(select_music)
        else:
            textbutton _("{size=-6}Музыка{/size}"):
                action NullAction()
                style "hkbd_button"

        if allow_dialogue and store.hkb_button.enabled:
            textbutton _("{size=-6}Поиграть{/size}") action Jump("pick_a_game")
        else:
            textbutton _("{size=-6}Поиграть{/size}"):
                action NullAction()
                style "hkbd_button"


screen movie_overlay():

    zorder 50

    style_prefix "hkb"

    vbox:
        xalign 0.95
        yalign 0.95

        if watchingMovie:
            textbutton _("{size=-6}Пауза{/size}") action Jump("mm_movie_pausefilm")
        else:
            textbutton _("{size=-6}Пауза{/size}") action NullAction() style "hkbd_button"

        if watchingMovie:
            textbutton _("{size=-6}Время{/size}") action Jump("mm_movie_settime")
        else:
            textbutton _("{size=-6}Время{/size}"):
                action NullAction()
                style "hkbd_button"

init python:
    HKBShowButtons()