#Скрипт слов честно позаимствован с порта DDLC на Android, перевод сделал Денис Солицен.
#Добавлены слова из мода MRM или True Route для DDLC. 
init python:
    import random


    class PoemWord:
        def __init__(self, word, sPoint, nPoint, yPoint, mPoint='0', glitch=False):
            self.word = word
            self.sPoint = sPoint
            self.nPoint = nPoint
            self.yPoint = yPoint
            self.mPoint = mPoint
            self.glitch = glitch


    POEM_DISLIKE_THRESHOLD = 29
    POEM_LIKE_THRESHOLD = 45


    poem_lines="""#File format: word,sPoint,nPoint,yPoint,mPoint

#Слова Саёри
счастье,3,2,1,0
грусть,3,2,1,0
смерть,3,1,2,0
трагедия,3,1,2,0
одиночество,3,1,2,0
любовь,3,2,1,0
приключение,3,2,1,0
сладкий,3,2,1,0
возбуждение,3,2,1,0
фейерверк,3,2,1,0
романтика,3,2,1,0
слёзы,3,1,2,0
депрессия,3,1,2,0
сердце,3,2,1,0
свадьба,3,2,1,0
страсть,3,2,1,0
детство,3,2,1,0
веселье,3,2,1,0
цвет,3,2,1,0
надежда,3,1,2,0
друзья,3,2,1,0
семья,3,2,1,0
вечеринка,3,2,1,0
каникулы,3,2,1,0
ленивая,3,2,1,0
мечта,3,1,2,0
боль,3,1,2,0
праздник,3,2,1,0
кровать,3,2,1,0
пух,3,2,1,0
стыд,3,1,2,0
страх,3,1,2,0
тепло,3,2,1,0
цветок,3,2,1,0
утешение,3,2,1,0
танцы,3,2,1,0
петь,3,2,1,0
плакать,3,1,2,0
смеяться,3,2,1,0
мрачный,3,1,2,0
солнечный,3,2,1,0
тучка,3,2,1,0
спокойный,3,1,2,0
глупый,3,2,1,0
летающий,3,2,1,0
замечательный,3,2,1,0
неразделённая,3,1,2,0
роза,3,1,2,0
вместе,3,2,1,0
обещаю,3,2,1,0
очарование,3,2,1,0
красота,3,2,1,0
ободрение,3,2,1,0
улыбка,3,2,1,0
разбитое,3,1,2,0
драгоценная,3,2,1,0
молитва,3,1,2,0
неуклюжий,3,2,1,0
прости,3,1,2,0
природа,3,2,1,0
океан,3,2,1,0
ослеплять,3,2,1,0
особенный,3,2,1,0
музыка,3,2,1,0
счастливчик,3,2,1,0
невезение,3,1,2,0
громко,3,2,1,0
безмятежно,3,1,2,0
восторг,3,1,2,0
закат,3,2,1,0
светлячки,3,2,1,0
радуга,3,2,1,0
ранить,3,1,2,0
игра,3,2,1,0
искорка,3,2,1,0
рубцы,3,1,2,0
пусто,3,1,2,0
невероятно,3,2,1,0
горе,3,1,2,0
обнимать,3,1,2,0
незаурядный,3,2,1,0
потрясающий,3,2,1,0
поражение,3,1,2,0
безнадёжно,3,1,2,0
страдание,3,1,2,0
сокровище,3,2,1,0
блаженство,3,2,1,0
воспоминания,3,2,1,0

#Слова Нацуки
милый,2,3,1,0
воздушный,2,3,1,0
чистый,1,3,2,0
конфета,2,3,1,0
шопинг,2,3,1,0
щеночек,2,3,1,0
котёнок,2,3,1,0
облака,2,3,1,0
помада,1,3,2,0
парфе,2,3,1,0
клубника,2,3,1,0
розовый,2,3,1,0
шоколад,2,3,1,0
сердцебиение,1,3,2,0
поцелуй,1,3,2,0
мелодия,2,3,1,0
лента,2,3,1,0
прыгучий,2,3,1,0
доки-доки,2,3,1,0
кавай,2,3,1,0
юбка,2,3,1,0
щёки,2,3,1,0
email,2,3,1,0
липучка,2,3,1,0
подвижная,2,3,1,0
яркий,2,3,1,0
кусь,2,3,1,0
фантазия,1,3,2,0
сахар,2,3,1,0
хихикать,2,3,1,0
зефир,2,3,1,0
подпрыгивать,2,3,1
прогуливать,2,3,1,0
покой,2,3,1,0
вертящийся,2,3,1,0
вращать,2,3,1,0
леденец,2,3,1,0
фу,2,3,1,0
пузырьки,2,3,1,0
шёпот,2,3,1,0
лето,2,3,1,0
водопад,1,3,2,0
купальник,2,3,1,0
ваниль,2,3,1,0
наушники,2,3,1,0
игры,2,3,1,0
носки,2,3,1,0
волосы,2,3,1,0
площадка,2,3,1,0
пеньюар,1,3,2,0
одеяло,1,3,2,0
молоко,2,3,1,0
надуться,2,3,1,0
ярость,2,3,1,0
папа,2,3,1,0
валентинка,2,3,1,0
мышь,1,3,2,0
свист,2,3,1,0
бип,2,3,1,0
зайчик,2,3,1,0
аниме,2,3,1,0
прыгать,2,3,1,0

#Слова Юри
решимость,1,1,3,0
суицид,2,1,3,0
воображение,2,1,3,0
скрытный,2,1,3,0
живучесть,1,1,3,0
существование,2,1,3,0
лучезарный,1,1,3,0
багряный,1,1,3,0
смерч,1,1,3,0
послеобраз,1,1,3,0
головокружение,1,1,3,0
дезориентированный,1,1,3,0
сущность,2,1,3,0
внешний,2,1,3,0
космос,2,1,3,0
смятение,1,1,3,0
загрязнение,1,1,3,0
интеллектуальный,1,1,3,0
анализ,1,1,3,0
энтропия,1,1,3,0
оживлённый,1,1,3,0
сверхъестественное,2,1,3,0
несовпадающий,1,1,3,0
гнев,2,1,3,0
ниспосланный,2,1,3,0
резня,2,1,3,0
философия,1,1,3,0
неустойчивый,1,1,3,0
упорный,1,1,3,0
аура,2,1,3,0
нестабильный,1,1,3,0
преисподняя,2,1,3,0
неспособный,2,1,3,0
судьба,2,1,3,0
непогрешимый,1,1,3,0
агонизирующий,2,1,3,0
противоречие,1,1,3,0
неконтролируемый,2,1,3,0
предельный,1,1,3,0
избегать,2,1,3,0
сон,2,2,3,0
катастрофа,2,1,3,0
отчётливый,2,1,3,0
трепещущий,1,2,3,0
вопрос,1,2,3,0
терзать,2,1,3,0
суждение,1,1,3,0
клетка,1,2,3,0
взрываться,1,2,3,0
удовольствие,1,2,3,0
вожделение,1,2,3,0
ощущение,1,2,3,0
кульминация,1,2,3,0
электричество,1,2,3,0
отречься,1,1,3,0
презирать,2,1,3,0
бесконечный,2,1,3,0
вечность,2,1,3,0
время,2,1,3,0
вселенная,2,1,3,0
нескончаемый,2,1,3,0
дождевые капли,2,1,3,0
домогаться,1,1,3,0
необузданный,1,1,3,0
пейзаж,2,1,3,0
портрет,2,1,3,0
поездка,2,1,3,0
скудный,1,1,3,0
беспокойство,2,1,3,0
пугающий,2,1,3,0
ужас,2,1,3,0
меланхолия,2,1,3,0
проницательность,2,1,3,0
искупить,2,1,3,0
дыхание,1,2,3,0
пленный,2,1,3,0
желание,1,2,3,0
кладбище,2,1,3,0

#Слова Моники
пианино,2,1,1,3
известно,2,1,2,3
сообщалось,1,2,2,3
разные,2,2,2,3
реальность,1,2,1,3
одержимость,1,1,2,3
удалить,1,1,1,3
мотив,2,1,2,3
зависть,2,2,1,3
подделка,1,2,1,3
одна,2,1,2,3
никто,1,1,1,3
выход за рамки,1,1,2,3
скрывать,2,2,2,3
поэзия,2,2,2,3
чувство,2,1,2,3
слова,1,1,2,3
пиксели,1,1,1,3
застрат,2,2,2,3
страсть,2,2,1,3
волна,2,2,1,3
визг,1,1,2,3
метафора,1,2,2,3
бежать,2,2,2,3
экран,1,1,1,3
прозрение,1,1,2,3
модифицировать,1,2,2,3
невозможно,1,1,2,3
виртуальность,1,1,1,3
недействительным,1,1,2,3
пространство,2,1,2,3
смысл,2,1,2,3
утерян,2,2,2,3
рифт,1,1,1,3
кроссовер,2,2,1,3
жертва,2,1,2,3
мир,1,2,2,3
ловушка,1,1,2,3
солнце,2,2,1,3
изготовлены,1,1,1,3
восприятие,2,2,2,3
копия,1,1,2,3
диссонанс,1,1,2,3
ноль,2,1,2,3
файлы,1,1,1,3
измерение,1,1,2,3
система,1,1,2,3
искусственный,1,1,2,3
бесконечен,2,1,2,3
мощность,1,1,2,3
монохромный,1,1,2,3
серый,1,1,2,3
живой,2,1,2,3
адаптироваться,1,1,2,3
ошибка,1,1,1,3"""
    full_wordlist = []

    for line in poem_lines.splitlines():

        line = line.strip()

        if line == '' or line[0] == '#': continue


        x = line.split(',')
        full_wordlist.append(PoemWord(x[0], float(x[1]), float(x[2]), float(x[3])))


default persistent._mas_hangman_playername = False
define hm_ltrs_only = "абвгдкёжзийклмнопрстуфхцчшщьыьэюя АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЬЭЮЯ?!-"



image hm_6 = "mod_assets/hangman/hm_6.png"
image hm_5 = "mod_assets/hangman/hm_5.png"
image hm_4 = "mod_assets/hangman/hm_4.png"
image hm_3 = "mod_assets/hangman/hm_3.png"
image hm_2 = "mod_assets/hangman/hm_2.png"
image hm_1 = "mod_assets/hangman/hm_1.png"
image hm_0 = "mod_assets/hangman/hm_0.png"


image hm_s:
    block:


        block:
            choice:
                "mod_assets/hangman/hm_s1.png"
            choice:
                "mod_assets/hangman/hm_s2.png"
        block:



            choice:
                0.075
            choice:
                0.09
            choice:
                0.05
        repeat



define hm.SAYORI_SCALE = 0.25
image hm_s_win_6 = im.FactorScale(im.Flip(getCharacterImage("sayori", "4r"), horizontal=True), hm.SAYORI_SCALE)
image hm_s_win_5 = im.FactorScale(im.Flip(getCharacterImage("sayori", "2a"), horizontal=True), hm.SAYORI_SCALE)
image hm_s_win_4 = im.FactorScale(im.Flip(getCharacterImage("sayori", "2i"), horizontal=True), hm.SAYORI_SCALE)
image hm_s_win_3 = im.FactorScale(im.Flip(getCharacterImage("sayori", "1f"), horizontal=True), hm.SAYORI_SCALE)
image hm_s_win_2 = im.FactorScale(im.Flip(getCharacterImage("sayori", "4u"), horizontal=True), hm.SAYORI_SCALE)
image hm_s_win_1 = im.FactorScale(im.Flip(getCharacterImage("sayori", "4w"), horizontal=True), hm.SAYORI_SCALE)
image hm_s_win_0 = im.FactorScale(im.Flip("images/sayori/end-glitch1.png", horizontal=True), hm.SAYORI_SCALE)
image hm_s_win_fail = im.FactorScale(im.Flip("images/sayori/3c.png", horizontal=True), hm.SAYORI_SCALE)
image hm_s_win_leave = im.FactorScale(getCharacterImage("sayori", "1a"), hm.SAYORI_SCALE)





image hm_frame = "mod_assets/hangman/hm_frame.png"


transform hangman_board:
    xanchor 0 yanchor 0 xpos 675 ypos 100 alpha 0.7

transform hangman_missed_label:
    xanchor 0 yanchor 0 xpos 680 ypos 105

transform hangman_missed_chars:
    xanchor 0 yanchor 0 xpos 780 ypos 105

transform hangman_display_word:
    xcenter 975 yanchor 0 ypos 475

transform hangman_hangman:
    xanchor 0 yanchor 0 xpos 880 ypos 125



transform hangman_sayori(z=1.0):
    xcenter -300 yoffset 0 yalign 0.47 zoom z*1.00 alpha 1.00 subpixel True
    easein 0.25 xcenter 90


transform hangman_sayori_i(z=1.0):
    xcenter 90 yoffset 0 yalign 0.47 zoom z*1.00 alpha 1.00 subpixel True


transform hangman_sayori_i3(z=1.0):
    xcenter 82 yoffset 0 yalign 0.47 zoom z*1.00 alpha 1.00 subpixel True


transform hangman_sayori_h(z=1.0):
    xcenter 90 yoffset 0 yalign 0.47 zoom z*1.00 alpha 1.00 subpixel True
    easein 0.1 yoffset -20
    easeout 0.1 yoffset 0


transform hangman_sayori_lh(z=1.0):
    subpixel True
    on hide:
        easeout 0.5 xcenter -300


transform hangman_monika(z=0.80):
    tcommon(330,z=z)

transform hangman_monika_i(z=0.80):
    tinstant(330,z=z)


style hangman_text:
    yalign 0.5
    font "gui/font/Halogen.ttf"
    size 30
    color "#000"
    outlines []
    kerning 10.0



















init -1 python in hangman:


    hm_words = list()


    all_hm_words = list()



    LETTER_SPACE = 10.0


    WORD_FONT = "gui/font/Halogen.ttf"
    WORD_SIZE = 30
    WORD_OUTLINE = []
    WORD_COLOR = "#fff"
    WORD_COLOR_GET = "#CC6699"
    WORD_COLOR_MISS = "#000"


    HM_IMG_NAME = "hm_"


    HM_HINT = "{0} понравилось бы это слово больше всего."


init 10 python:


    from store.hangman import hm_words, all_hm_words
    from copy import deepcopy



    for word in full_wordlist:
        
        winner = ""
        
        
        if word.sPoint > word.nPoint and word.sPoint > word.yPoint:
            winner = "Саёри" 
        
        elif word.nPoint > word.yPoint:
            winner = "Нацуки" 
        
        else:
            winner = "Юри" 
        
        hm_words.append((word.word, winner))

    all_hm_words = deepcopy(hm_words)

    if (
            not persistent._mas_hangman_playername
            and persistent.playername.lower() != "sayori"
            and persistent.playername.lower() != "yuri"
            and persistent.playername.lower() != "natsuki"
            and persistent.playername.lower() != "monika"
        ):
        hm_words.append(-1)


















label game_hangman:
    $ import store.hangman as hmg
    $ from copy import deepcopy
    $ is_sayori = persistent.playername.lower() == "sayori"
    $ is_window_sayori_visible = False
    m 2b "Ты хочешь сыграть в Палача? Хорошо!"

    show monika at hangman_monika
    show hm_frame zorder 5 at hangman_board

    python:

        missed_label = Text(
            "Мимо:",
            font=hmg.WORD_FONT,
            color=hmg.WORD_COLOR,
            size=hmg.WORD_SIZE,
            outlines=hmg.WORD_OUTLINE
        )


    show text missed_label as hmg_mis_label zorder 10 at hangman_missed_label




label hangman_game_loop:
    m 1a "Я думаю над словом..."
    pause 0.7

    python:
        player_word = False


        if len(hmg.hm_words) == 0:
            hmg.hm_words = deepcopy(hmg.all_hm_words)


        word = renpy.random.choice(hmg.hm_words)
        hmg.hm_words.remove(word)


        if (
                word == -1 
                and persistent.playername.isalpha()
                and len(persistent.playername) <= 15
            ):
            display_word = list("_" * len(persistent.playername.lower()))
            hm_hint = hmg.HM_HINT.format("Мне")
            word = persistent.playername.lower()
            player_word = True
            persistent._mas_hangman_playername = True

        else:
            if word == -1:
                word = renpy.random.choice(hmg.hm_words)
                hmg.hm_words.remove(word)
            display_word = list("_" * len(word[0]))
            hm_hint = hmg.HM_HINT.format(word[1])
            
            
            word = word[0]












    if is_sayori:
        if is_window_sayori_visible:
            show hm_s_win_6 as window_sayori at hangman_sayori_i
        else:
            show hm_s_win_6 as window_sayori at hangman_sayori
        $ is_window_sayori_visible = True

    m "Хорошо, я готова."
    m "[hm_hint]"


    $ done = False
    $ win = False
    $ chances = 6
    $ missed = ""
    $ avail_letters = list(hm_ltrs_only)
    $ dt_color = hmg.WORD_COLOR
    while not done:

        python:
            if chances == 0:
                dt_color = hmg.WORD_COLOR_MISS
            elif "_" not in display_word:
                dt_color = hmg.WORD_COLOR_GET

            display_text = Text(
                "".join(display_word),
                font=hmg.WORD_FONT,
                color=dt_color,
                size=hmg.WORD_SIZE,
                outlines=hmg.WORD_OUTLINE,
                kerning=hmg.LETTER_SPACE
            )

            missed_text = Text(
                missed,
                font=hmg.WORD_FONT,
                color=hmg.WORD_COLOR,
                size=hmg.WORD_SIZE,
                outlines=hmg.WORD_OUTLINE,
                kerning=hmg.LETTER_SPACE
            )


        show text display_text as hmg_dis_text zorder 10 at hangman_display_word
        show text missed_text as hmg_mis_text zorder 10 at hangman_missed_chars


        if is_sayori:


            if chances == 0:


                $ disable_esc()
                $ store.songs.enabled = False
                $ store.hkb_button.enabled = False


                $ hm_glitch_word = glitchtext(40) + "?"
                $ style.say_dialogue = style.edited


                show hm_s zorder 10 at hangman_hangman


                hide monika
                show monika_body_glitch1 as mbg zorder 2 at hangman_monika_i(z=1.0)


                show hm_s_win_0 as window_sayori


                show screen tear(20, 0.1, 0.1, 0, 40)
                play sound "sfx/s_kill_glitch1.ogg"
                pause 0.2
                stop sound
                hide screen tear


                m "{cps=*2}[hm_glitch_word]{/cps}{w=0.2}{nw}"


                show screen tear(20, 0.1, 0.1, 0, 40)
                play sound "sfx/s_kill_glitch1.ogg"
                pause 0.2
                stop sound
                hide screen tear


                hide mbg
                hide window_sayori
                hide hm_s
                show monika 1 zorder 2 at hangman_monika_i
                if config.developer:
                    $ style.say_dialogue = style.normal
                else:
                    $ style.say_dialogue = style.default_monika
                $ is_window_sayori_visible = False
                $ store.songs.enabled = True
                $ store.hkb_button.enabled = True
                $ enable_esc()
            else:


                $ next_window_sayori = "hm_s_win_" + str(chances)
                show expression next_window_sayori as window_sayori

        $ hm_display = hmg.HM_IMG_NAME + str(chances)

        show expression hm_display as hmg_hanging_man zorder 10 at hangman_hangman


        if chances == 0:
            $ done = True
            if player_word:
                m 1e "[player],..."
                m "Ты не смог угадать свое собственное имя?"
            m 1j "Повезет в следующий раз~"
        elif "_" not in display_word:
            $ done = True
            $ win = True
        else:
            python:


                bad_input = True
                while bad_input:
                    guess = renpy.input(
                        "\n" +
                        "Угадать букву: (Напиши '?' чтобы повторить подсказку, " +
                        "'!' чтобы сдаться)",
                        allow="".join(avail_letters),
                        length=1
                    )
                    
                    if len(guess) != 0:
                        bad_input = False


            if guess == "?":
                m "[hm_hint]"
            elif guess == "!":
                if is_window_sayori_visible:
                    show hm_s_win_fail as window_sayori at hangman_sayori_i3
                $ done = True


                m 1n "[player]..."
                if chances == 6:
                    m "Я думала что ты сказал что хочешь играть в Палача."
                    m 1o "Но ты даже не угадал ни одной буквы."
                    m "..."
                    m 1f "Знаешь, я действительно люблю с тобой играть."
                else:
                    m "Ты должен хотя бы доиграть до конца..."
                    m 1f "Такой легкий проигрыш признак слабой решемости."
                    if chances > 1:
                        m "Я имею в виду тебе придется пропустить больше [chances] букв, чтобы фактически проиграть."
                    else:
                        m "Я имею в виду тебе придется пропустить [chances] больше букв, чтобы фактически проиграть."
                m 1e "Можешь ли ты в следующий раз сыграть до конца, [player]? Ради меня?"
            else:
                python:
                    if guess in word:
                        for index in range(0,len(word)):
                            if guess == word[index]:
                                display_word[index] = guess
                    else:
                        chances -= 1
                        missed += guess
                        if chances == 0:
                            
                            display_word = word


                    avail_letters.remove(guess)


                hide text hmg_dis_text
                hide text hmg_mis_text
                hide hmg_hanging_man


    if win:
        if is_window_sayori_visible:
            show hm_s_win_6 as window_sayori at hangman_sayori_h

        if player_word:
            $ the_word = "твое имя"
        else:
            $ the_word = "твое слово"

        m 1j "Ого, ты угадал [the_word] правильно!"
        m "Хорошая работа, [player]!"
        if not persistent.ever_won['hangman']:
            $ persistent.ever_won['hangman']=True
            $ grant_xp(xp.WIN_GAME)


    menu:
        m "Может быть ты хочешь сыграть еще раз?"
        "Да":
            jump hangman_game_loop
        "Нет":
            jump hangman_game_end




label hangman_game_end:

    hide hmg_hanging_man
    hide hmg_mis_label
    hide hmg_dis_text
    hide hmg_mis_text
    hide hm_frame
    show monika at t32
    if is_window_sayori_visible:
        show hm_s_win_leave as window_sayori at hangman_sayori_lh
        pause 0.1
        hide window_sayori

    m 1d "Палач на самом деле довольно сложная игра."
    m "У тебя должен быть толстый словарь, чтобы угадывать слова."
    m 1j "Лучший способ улучшить свои навыки это больше читать!"
    m 1a "Я бы очень обрадовалась если бы ты сделал это ради меня, [player]."
    return