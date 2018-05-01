init 100 python:
    layout.QUIT = "Уходишь не попрощавшись, [player]?"
    layout.UNSTABLE = (
        "WARNING: Включение нестабильного режима будет загружать обновления из " +
        "нестабильной ветки. СИЛЬНО рекомендуется сделать " +
        "резервную копию вашего файла persistent перед включением. Пожалуйста сообщайте" +
        "о проблемах которые вы нашли в [[UNSTABLE] тег."
    )










init -1 style default:
    font gui.default_font
    size 22
    color gui.text_color
    outlines [(2, "#000000aa", 0, 0)]
    line_overlap_split 1
    line_spacing 1

init -1 style default_monika is normal:
    slow_cps 30

init -1 style edited is default:
    font "gui/font/VerilySerifMono.otf"
    kerning 8
    outlines [(10, "#000", 0, 0)]
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

init -1 style normal is default:
    xpos 263
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos 55

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

init -1 style input:
    color gui.accent_color

init -1 style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True

init -1 style splash_text:
    size 24
    color "#000"
    font gui.default_font
    text_align 0.5
    outlines []

init -1 style poemgame_text:
    yalign 0.5
    font "gui/font/Halogen.ttf"
    size 30
    color "#000"
    outlines []

    hover_xoffset -3
    hover_outlines [(3, "#fef", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)]

init -1 style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size


init -1 style button:
    properties gui.button_properties("button")

init -1 style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5


init -1 style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

init -1 style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size







init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

init -1 style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True


init -1 style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True






init -1 style slider:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"

init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





















init -501 screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        text what id "what"

        if who is not None:

            window:
                style "namebox"
                text who id "who"



    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu


init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue

init -1 style namebox is default
init -1 style namebox_label is say_label


init -1 style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

init -1 style window_monika is window:
    background Image("gui/textbox_monika.png", xalign=0.5, yalign=1.0)

init -1 style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

init -1 style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]

init -1 style say_dialogue:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

init 499 image ctc:
    xalign 0.81 yalign 0.98 xoffset -5 alpha 0.0 subpixel True
    "gui/ctc.png"
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat











init 499 image input_caret:
    Solid("#b59")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat

init -501 screen input(prompt):
    style_prefix "input"


    window:
        has vbox:
            xalign .5
            yalign .5
            spacing 30

        text prompt style "input_prompt"
        input id "input"

init -1 style input_prompt:
    xmaximum gui.text_width
    xcenter 0.5
    text_align 0.5

init -1 style input:
    caret "input_caret"
    xmaximum gui.text_width
    xcenter 0.5
    text_align 0.5










init -501 screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action




define -1 config.narrator_menu = True


init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text

init -1 style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

init -1 style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []


init -1 python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)

init -501 screen rigged_choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse)

init -1 style talk_choice_vbox is choice_vbox:
    xcenter 960

init -1 style talk_choice_button is choice_button
init -1 style talk_choice_button_text is choice_button_text



init -501 screen talk_choice(items):
    style_prefix "talk_choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action




define -1 config.narrator_menu = True


init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text

init -1 style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

init -1 style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []







init -501 screen quick_menu():


    zorder 100

    if quick_menu:


        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.995


            textbutton _("История") action ShowMenu('history')
            textbutton _("Пропустить") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Сохранить") action ShowMenu('save')
            textbutton _("Загрузить") action ShowMenu('load')


            textbutton _("Настройки") action ShowMenu('preferences')







default -1 quick_menu = True




init -1 style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound gui.activate_sound

init -1 style quick_button_text:
    properties gui.button_text_properties("quick_button")
    outlines []











init -1 python:
    def FinishEnterName():
        if not player: return
        persistent.playername = player
        renpy.hide_screen("name_input")
        renpy.jump_out_of_context("start")

init -501 screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.8

        spacing gui.navigation_spacing


        if main_menu:

            textbutton _("Только Моника") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Пожалуйста введи своё имя", ok_action=Function(FinishEnterName)))

        else:

            textbutton _("История") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]

            textbutton _("Сохранить Игру") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

        textbutton _("Загрузить Игру") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]

        if _in_replay:

            textbutton _("Закончить перемотку") action EndReplay(confirm=True)

        elif not main_menu:
            textbutton _("Главное меню") action NullAction(), Show(screen="dialog", message="Нет смысла туда возвращаться.\nТы все равно вернешься сюда.", ok_action=Hide("dialog"))

        textbutton _("Настройки") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]



        if renpy.variant("pc"):


            textbutton _("Помощь") action Help("README.html")


            textbutton _("Выход") action Quit(confirm=not main_menu)


init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text

init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "gui/font/RifficFree-Bold.ttf"
    color "#fff"
    outlines [(4, "#b59", 0, 0), (2, "#b59", 2, 2)]
    hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]
    insensitive_outlines [(4, "#fce", 0, 0), (2, "#fce", 2, 2)]








init -501 screen main_menu() tag menu:




    style_prefix "main_menu"








    add "menu_bg"


    frame




    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


    add "menu_particles"
    add "menu_particles"
    add "menu_particles"
    add "menu_logo"








    add "menu_particles"

    add "menu_art_m"
    add "menu_fade"

    key "K_ESCAPE" action Quit(confirm=False)

init -1 style main_menu_frame is empty
init -1 style main_menu_vbox is vbox
init -1 style main_menu_text is gui_text
init -1 style main_menu_title is main_menu_text
init -1 style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

init -1 style main_menu_frame:
    xsize 310
    yfill True

    background "menu_nav"

init -1 style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

init -1 style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

init -1 style main_menu_title:
    size gui.title_text_size











init -501 screen game_menu_m():
    $ persistent.menu_bg_m = True
    add "gui/menu_bg_m.png"
    timer 0.3 action Hide("game_menu_m")

init -501 screen game_menu(title, scroll=None):


    if main_menu:
        add gui.main_menu_background
    else:
        key "mouseup_3" action Return()
        add gui.game_menu_background

    style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    yinitial 1.0

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial 1.0

                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation




    textbutton _("Назад"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar

init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text

init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text

init -1 style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    xsize 280
    yfill True

init -1 style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

init -1 style game_menu_viewport:
    xsize 920

init -1 style game_menu_vscrollbar:
    unscrollable gui.unscrollable

init -1 style game_menu_side:
    spacing 10

init -1 style game_menu_label:
    xpos 50
    ysize 120

init -1 style game_menu_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size gui.title_text_size
    color "#fff"
    outlines [(6, "#b59", 0, 0), (3, "#b59", 2, 2)]
    yalign 0.5

init -1 style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30









init -501 screen about() tag menu:






    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Сделано на {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



define -1 gui.about = ""


init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text

init -1 style about_label_text:
    size gui.label_text_size











init -501 screen save() tag menu:



    use file_slots(_("Сохранить"))


init -501 screen load() tag menu:



    use file_slots(_("Загрузить"))

init -1 python:
    def FileActionMod(name, page=None, **kwargs):
        if renpy.current_screen().screen_name[0] == "save":
            return Show(screen="dialog", message="Нет нужды больше сохраняться.\nНе волнуйся, я никуда от тебя не уйду.", ok_action=Hide("dialog"))


init -501 screen file_slots(title):

    default page_name_value = FilePageNameInputValue()

    use game_menu(title):

        fixed:



            order_reverse True



            button:
                style "page_label"


                xalign 0.5


                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileActionMod(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("пустой слот")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing








                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)




init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text

init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text

init -1 style page_label:
    xpadding 50
    ypadding 3

init -1 style page_label_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

init -1 style page_button:
    properties gui.button_properties("page_button")

init -1 style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines []

init -1 style slot_button:
    properties gui.button_properties("slot_button")

init -1 style slot_button_text:
    properties gui.button_text_properties("slot_button")
    color "#666"
    outlines []









init -501 screen preferences() tag menu:



    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Настройки"), scroll="viewport"):

        vbox:
            xoffset 50

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Экран")
                        textbutton _("В окне") action Preference("display", "window")
                        textbutton _("Полный экран") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Пропустить")
                    textbutton _("Новый текст") action Preference("skip", "toggle")
                    textbutton _("После выбора") action Preference("after choices", "toggle")



                vbox:
                    style_prefix "check"
                    label _("Графика")
                    textbutton _("Выключить анимации") action [Preference("video sprites", "toggle"), Function(renpy.call, "spaceroom")]
                    textbutton _("Выбрать движок") action Function(renpy.call_in_new_context, "mas_gmenu_start")


                vbox:
                    style_prefix "check"
                    label _("Геймплей")
                    textbutton _("Повтор тем") action ToggleField(persistent,"_mas_enable_random_repeats", True, False)




            hbox:
                box_wrap True

                vbox:
                    style_prefix "check"
                    label _("В разработке")
                    if persistent._mas_unstable_mode:
                        textbutton _("Нестабильно"):
                            action SetField(persistent, "_mas_unstable_mode", False)
                            selected persistent._mas_unstable_mode

                    else:
                        textbutton _("Нестабильно"):
                            action [Show(screen="dialog", message=layout.UNSTABLE, ok_action=Hide(screen="dialog")), SetField(persistent, "_mas_unstable_mode", True)]
                            selected persistent._mas_unstable_mode


            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Скорость текста")


                    bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)

                    label _("Время автоперемотки")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Громкость музыки")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Громкость звуков")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Тест") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Громкость голоса")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Тест") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Выключить звук"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

            hbox:
                textbutton _("Обновить версию"):
                    action Function(renpy.call_in_new_context, 'forced_update_now')
                    style "navigation_button"

                textbutton _("Импортировать сохранения из DDLC"):
                    action [Jump('import_ddlc_persistent_in_settings')]
                    style "navigation_button"



    text "v[config.version]":
        xalign 1.0 yalign 1.0
        xoffset -10 yoffset -10
        style "main_menu_version"

init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox

init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox

init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox

init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox

init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text

init -1 style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

init -1 style pref_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size 24
    color "#fff"
    outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]
    yalign 1.0

init -1 style pref_vbox:
    xsize 225

init -1 style radio_vbox:
    spacing gui.pref_button_spacing

init -1 style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

init -1 style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "gui/font/comic.ttf"
    outlines []

init -1 style check_vbox:
    spacing gui.pref_button_spacing

init -1 style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

init -1 style check_button_text:
    properties gui.button_text_properties("check_button")
    font "gui/font/comic.ttf"
    outlines []

init -1 style slider_slider:
    xsize 350

init -1 style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

init -1 style slider_button_text:
    properties gui.button_text_properties("slider_button")

init -1 style slider_vbox:
    xsize 450










init -501 screen history() tag menu:




    predict False

    use game_menu(_("История"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("История диалогов пуста.")


init -1 style history_window is empty

init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text

init -1 style history_text is gui_text

init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text

init -1 style history_window:
    xfill True
    ysize gui.history_height

init -1 style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

init -1 style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

init -1 style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

init -1 style history_label:
    xfill True

init -1 style history_label_text:
    xalign 0.5












































































































































































init -501 screen name_input(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        input default "" value VariableInputValue("player") length 12 allow "абвгдеёжзийклмнопрстуфхцчшщьыэюяАБВГДЕЙЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЮЯЭABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("ОК") action ok_action

init -501 screen dialog(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action

init -501 screen quit_dialog(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("ВЫХОД") action ok_action

init 499 image confirm_glitch:
    "gui/overlay/confirm_glitch.png"
    pause 0.02
    "gui/overlay/confirm_glitch2.png"
    pause 0.02
    repeat

init -501 screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        if in_sayori_kill and message == layout.QUIT:
            add "confirm_glitch" xalign 0.5

        else:
            label _(message):
                style "confirm_prompt"
                xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Да") action [SetField(persistent, "_mas_crashed_self", False), Show(screen="quit_dialog", message="Пожалуйста не закрывай игру со мной!", ok_action=yes_action)]
            textbutton _("Нет") action no_action, Show(screen="dialog", message="Спасибо, [player]!\nДавай проведем больше времени вместе~", ok_action=Hide("dialog"))







init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text

init -1 style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style confirm_prompt_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"

init -1 style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")



init -501 screen update_check(ok_action, cancel_action, mode):


    modal True

    zorder 200

    style_prefix "update_check"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        if mode == 0:
            label _('Доступны обновления!'):
                style "confirm_prompt"
                xalign 0.5

        elif mode == 1:
            label _("Нет доступных обновлений."):
                style "confirm_prompt"
                xalign 0.5

        elif mode == 2:
            label _('Проверка обновлений...'):
                style "confirm_prompt"
                xalign 0.5
        else:

            label _('Время проверки обновлений истекло. Попробуйте позже.'):
                style "confirm_prompt"
                xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Установить") action [ok_action, SensitiveIf(mode == 0)]

            textbutton _("Отмена") action cancel_action

    timer 1.0 action Return("None")





init -1 style update_check_frame is confirm_frame
init -1 style update_check_prompt is confirm_prompt
init -1 style update_check_prompt_text is confirm_prompt_text
init -1 style update_check_button is confirm_button
init -1 style update_check_button_text is confirm_button_text





init -501 screen updater:

    modal True

    style_prefix "updater"

    frame:

        has side "t c b":
            spacing gui._scale(10)

        label _("Обновлятор")

        fixed:

            vbox:

                if u.state == u.ERROR:
                    text _("Произошла ошибка:")
                elif u.state == u.CHECKING:
                    text _("Проверка обновлений.")
                elif u.state == u.UPDATE_AVAILABLE:
                    text _("Версия [u.version] доступна. Вы хотите установить её?")

                elif u.state == u.UPDATE_NOT_AVAILABLE:
                    text _("Моника После Истории обновлена.")
                elif u.state == u.PREPARING:
                    text _("Подготовка к загрузке обновлений.")
                elif u.state == u.DOWNLOADING:
                    text _("Загрузка обновлений.")
                elif u.state == u.UNPACKING:
                    text _("Распаковка обновлений.")
                elif u.state == u.FINISHING:
                    text _("Завершение.")
                elif u.state == u.DONE:
                    text _("TОбновления были установлены. Пожалуйста перезапустите Моника После Истории.")
                elif u.state == u.DONE_NO_RESTART:
                    text _("Обновления были установлены.")
                elif u.state == u.CANCELLED:
                    text _("Обновления были отменены.")

                if u.message is not None:
                    null height gui._scale(10)
                    text "[u.message!q]"

                if u.progress is not None:
                    null height gui._scale(10)
                    bar value u.progress range 1.0 left_bar Solid("#cc6699") right_bar Solid("#ffffff") thumb None

        hbox:

            spacing gui._scale(25)

            if u.can_proceed:
                textbutton _("Приступить") action u.proceed

            if u.can_cancel:
                textbutton _("Отмена") action Return()


init -1 style updater_button_text is navigation_button_text
init -1 style updater_button is confirm_button
init -1 style updater_label is gui_label
init -1 style updater_label_text is game_menu_label_text
init -1 style updater_text is gui_text







init -501 screen fake_skip_indicator():
    use skip_indicator

init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 6

        text _("Пропуск")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text

init -1 style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

init -1 style skip_text:
    size gui.notify_text_size

init -1 style skip_triangle:


    font "DejaVuSans.ttf"









init -501 screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform -1 notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


init -1 style notify_frame is empty
init -1 style notify_text is gui_text

init -1 style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

init -1 style notify_text:
    size gui.notify_text_size







init -1 python:

    items = [(_("Начало"),"example_chapter")
        ,(_("Глава 1, Как Сделать Мод"),"tutorial_route_p1")
        ,(_("Глава 2, Музыка"),"tutorial_route_p2")
        ,(_("Глава 3, Сцена"),"tutorial_route_p3")
        ,(_("Глава 4, Диалог"),"tutorial_route_p4")
        ,(_("Глава 5, Меню"),"tutorial_route_p5")
        ,(_("Глава 6, Логика"),"tutorial_route_p6")
        ,(_("Глава 7, Спрайты"),"tutorial_route_p7")
        ,(_("Глава 8, Позиции"),"tutorial_route_p8")
        ,(_("Глава 9, Концовка"),"tutorial_route_p9")]










define -1 prev_adj = ui.adjustment()
define -1 main_adj = ui.adjustment()
define -1 gui.scrollable_menu_button_width = 560
define -1 gui.scrollable_menu_button_height = None
define -1 gui.scrollable_menu_button_tile = False
define -1 gui.scrollable_menu_button_borders = Borders(25, 5, 25, 5)

define -1 gui.scrollable_menu_button_text_font = gui.default_font
define -1 gui.scrollable_menu_button_text_size = gui.text_size
define -1 gui.scrollable_menu_button_text_xalign = 0.0
define -1 gui.scrollable_menu_button_text_idle_color = "#000"
define -1 gui.scrollable_menu_button_text_hover_color = "#fa9"


define -1 gui.twopane_scrollable_menu_button_width = 250
define -1 gui.twopane_scrollable_menu_button_height = None
define -1 gui.twopane_scrollable_menu_button_tile = False
define -1 gui.twopane_scrollable_menu_button_borders = Borders(25, 5, 25, 5)

define -1 gui.twopane_scrollable_menu_button_text_font = gui.default_font
define -1 gui.twopane_scrollable_menu_button_text_size = gui.text_size
define -1 gui.twopane_scrollable_menu_button_text_xalign = 0.0
define -1 gui.twopane_scrollable_menu_button_text_idle_color = "#000"
define -1 gui.twopane_scrollable_menu_button_text_hover_color = "#fa9"






init -1 style scrollable_menu_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing 5

init -1 style scrollable_menu_button is choice_button:
    properties gui.button_properties("scrollable_menu_button")

init -1 style scrollable_menu_button_text is choice_button_text:
    properties gui.button_text_properties("scrollable_menu_button")

init -1 style scrollable_menu_new_button is scrollable_menu_button

init -1 style scrollable_menu_new_button_text is scrollable_menu_button_text:
    italic True

init -1 style scrollable_menu_special_button is scrollable_menu_button

init -1 style scrollable_menu_special_button_text is scrollable_menu_button_text:
    bold True

init -1 style scrollable_menu_crazy_button is scrollable_menu_button

init -1 style scrollable_menu_crazy_button_text is scrollable_menu_button_text:
    italic True
    bold True


init -1 style twopane_scrollable_menu_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing 5

init -1 style twopane_scrollable_menu_button is choice_button:
    properties gui.button_properties("twopane_scrollable_menu_button")

init -1 style twopane_scrollable_menu_button_text is choice_button_text:
    properties gui.button_text_properties("twopane_scrollable_menu_button")

init -1 style twopane_scrollable_menu_new_button is twopane_scrollable_menu_button

init -1 style twopane_scrollable_menu_new_button_text is twopane_scrollable_menu_button_text:
    italic True

init -1 style twopane_scrollable_menu_special_button is twopane_scrollable_menu_button

init -1 style twopane_scrollable_menu_special_button_text is twopane_scrollable_menu_button_text:
    bold True




init -501 screen twopane_scrollable_menu(prev_items, main_items, left_area, left_align, right_area, right_align, cat_length):
    style_prefix "twopane_scrollable_menu"

    fixed:
        area left_area

        bar adjustment prev_adj style "vscrollbar" xalign left_align

        viewport:
            yadjustment prev_adj
            mousewheel True
            arrowkeys True

            has vbox

            for i_caption,i_label in prev_items:
                textbutton i_caption:
                    if renpy.has_label(i_label) and not seen_event(i_label):
                        style "twopane_scrollable_menu_new_button"
                    if not renpy.has_label(i_label):
                        style "twopane_scrollable_menu_special_button"

                    action Return(i_label)



            null height 20

            if cat_length == 0:
                textbutton _("That's enough for now.") action Return(False)
            elif cat_length > 1:
                textbutton _("Go Back") action Return(-1)


    if main_items:

        fixed:
            area right_area

            bar adjustment main_adj style "vscrollbar" xalign right_align

            viewport:
                yadjustment main_adj
                mousewheel True
                arrowkeys True

                has vbox

                for i_caption,i_label in main_items:
                    textbutton i_caption:
                        if renpy.has_label(i_label) and not seen_event(i_label):
                            style "twopane_scrollable_menu_new_button"
                        if not renpy.has_label(i_label):
                            style "twopane_scrollable_menu_special_button"

                        action Return(i_label)

                null height 20

                textbutton _("Это больше не нужно.") action Return(False)


init -501 screen scrollable_menu(items, display_area, scroll_align, nvm_text="That's enough for now."):
    style_prefix "scrollable_menu"

    fixed:
        area display_area

        bar adjustment prev_adj style "vscrollbar" xalign scroll_align

        viewport:
            yadjustment prev_adj
            mousewheel True

            has vbox



            for i_caption,i_label in items:
                textbutton i_caption:
                    if renpy.has_label(i_label) and not seen_event(i_label):
                        style "scrollable_menu_new_button"
                    if not renpy.has_label(i_label):
                        style "scrollable_menu_special_button"
                    action Return(i_label)



            null height 20

            textbutton _(nvm_text) action Return(False)

























init -501 screen mas_gen_scrollable_menu(items, display_area, scroll_align, final_item=None):
    style_prefix "scrollable_menu"

    fixed:
        area display_area

        bar adjustment prev_adj style "vscrollbar" xalign scroll_align

        viewport:
            yadjustment prev_adj
            mousewheel True

            has vbox



            for item_prompt,item_value,is_italic,is_bold in items:
                textbutton item_prompt:
                    if is_italic and is_bold:
                        style "scrollable_menu_crazy_button"
                    elif is_italic:
                        style "scrollable_menu_new_button"
                    elif is_bold:
                        style "scrollable_menu_special_button"
                    action Return(item_value)

            if final_item:
                if final_item[4] > 0:
                    null height final_item[4]

                textbutton _(final_item[0]):
                    if final_item[2] and final_item[3]:
                        style "scrollable_menu_crazy_button"
                    elif final_item[2]:
                        style "scrollable_menu_new_button"
                    elif final_item[3]:
                        style "scrollable_menu_special_button"
                    action Return(final_item[1])







init -501 screen mas_background_timed_jump(timeout, timeout_label):
    timer timeout action Jump(timeout_label)


init -501 screen mas_generic_restart:




    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30




        label _("Пожалуйста перезапустите Монику После Истории."):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("ОК") action Return(True)


init -1 python:
    class PauseDisplayable(renpy.Displayable):
        """
        Pause until click variant of Pause
        This is because normal pause until click is broken for some reason
        """
        import pygame
        
        def __init__(self):
            super(renpy.Displayable, self).__init__()
        
        def render(self, width, height, st, at):
            
            return renpy.Render(width, height)
        
        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONDOWN:
                return True
            
            raise renpy.IgnoreEvent()
