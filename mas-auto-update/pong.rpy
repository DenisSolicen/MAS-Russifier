init:

    image bg pong field = "mod_assets/pong_field.png"

    python:
        import random
        import math

        def is_morning():
            return (datetime.datetime.now().time().hour > 6 and datetime.datetime.now().time().hour < 18)

        class PongDisplayable(renpy.Displayable):
            
            def __init__(self):
                
                renpy.Displayable.__init__(self)
                
                
                self.paddle = Image("mod_assets/pong.png")
                self.ball = Image("mod_assets/pong_ball.png")
                self.player = Text(_("[player]"), size=36)
                self.monika = Text(_("Monika"), size=36)
                self.ctb = Text(_("Click to Begin"), size=36)
                
                
                self.PADDLE_WIDTH = 8
                self.PADDLE_HEIGHT = 79
                self.PADDLE_RADIUS = self.PADDLE_HEIGHT / 2
                self.BALL_WIDTH = 15
                self.BALL_HEIGHT = 15
                self.COURT_TOP = 124
                self.COURT_BOTTOM = 654
                
                
                
                self.MAX_REFLECT_ANGLE = math.pi / 3
                
                
                self.stuck = True
                
                
                self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
                self.computery = self.playery
                
                
                
                
                self.ctargetoffset = self.get_random_offset()
                
                
                
                self.computerspeed = 1000.0
                
                
                init_angle = random.uniform(-self.MAX_REFLECT_ANGLE, self.MAX_REFLECT_ANGLE)
                
                
                self.bx = 110
                self.by = self.playery
                self.bdx = .5 * math.cos(init_angle)
                self.bdy = .5 * math.sin(init_angle)
                self.bspeed = 500.0
                
                
                self.ctargety = self.by + self.ctargetoffset
                
                
                self.oldst = None
                
                
                self.winner = None
            
            def get_random_offset(self):
                return random.uniform(-self.PADDLE_RADIUS, self.PADDLE_RADIUS)
            
            def visit(self):
                return [ self.paddle, self.ball, self.player, self.monika, self.ctb ]
            
            
            
            def render(self, width, height, st, at):
                
                
                r = renpy.Render(width, height)
                
                
                if self.oldst is None:
                    self.oldst = st
                
                dtime = st - self.oldst
                self.oldst = st
                
                
                speed = dtime * self.bspeed
                oldbx = self.bx
                
                if self.stuck:
                    self.by = self.playery
                else:
                    self.bx += self.bdx * speed
                    self.by += self.bdy * speed
                self.ctargety = self.by + self.ctargetoffset
                
                
                
                cspeed = self.computerspeed * dtime
                if abs(self.ctargety - self.computery) <= cspeed:
                    self.computery = self.ctargety
                elif self.ctargety - self.computery >= 0:
                    self.computery += cspeed
                else:
                    self.computery -= cspeed
                
                
                
                
                ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
                if self.by < ball_top:
                    self.by = ball_top + (ball_top - self.by)
                    self.bdy = -self.bdy
                    if not self.stuck:
                        renpy.sound.play("mod_assets/pong_beep.wav", channel=0)
                
                
                ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
                if self.by > ball_bot:
                    self.by = ball_bot - (self.by - ball_bot)
                    self.bdy = -self.bdy
                    if not self.stuck:
                        renpy.sound.play("mod_assets/pong_beep.wav", channel=0)
                
                
                def paddle(px, py, hotside, is_computer):
                    
                    
                    
                    
                    
                    
                    pi = renpy.render(self.paddle, 1280, 720, st, at)
                    
                    
                    
                    r.blit(pi, (int(px), int(py - self.PADDLE_RADIUS)))
                    
                    if py - self.PADDLE_RADIUS <= self.by <= py + self.PADDLE_RADIUS:
                        hit = True
                        if oldbx >= hotside >= self.bx:
                            self.bx = hotside + (hotside - self.bx)
                        elif oldbx <= hotside <= self.bx:
                            self.bx = hotside - (self.bx - hotside)
                        else:
                            hit = False
                        
                        if hit:
                            
                            
                            angle = (self.by - py) / self.PADDLE_RADIUS * self.MAX_REFLECT_ANGLE
                            self.bdy = .5 * math.sin(angle)
                            self.bdx = math.copysign(.5 * math.cos(angle), -self.bdx)
                            
                            
                            if is_computer:
                                self.ctargetoffset = self.get_random_offset()
                            
                            renpy.sound.play("mod_assets/pong_boop.wav", channel=1)
                            self.bspeed *= 1.20
                
                
                paddle(100, self.playery, 100 + self.PADDLE_WIDTH, False)
                paddle(1175, self.computery, 1175, True)
                
                
                ball = renpy.render(self.ball, 1280, 720, st, at)
                r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                              int(self.by - self.BALL_HEIGHT / 2)))
                
                
                player = renpy.render(self.player, 1280, 720, st, at)
                r.blit(player, (100, 25))
                
                
                monika = renpy.render(self.monika, 1280, 720, st, at)
                ew, eh = monika.get_size()
                r.blit(monika, (1150 - ew, 25))
                
                
                if self.stuck:
                    ctb = renpy.render(self.ctb, 1280, 720, st, at)
                    cw, ch = ctb.get_size()
                    r.blit(ctb, (640 - cw / 2, 30))
                
                
                
                if self.bx < -200:
                    self.winner = "monika"
                    
                    
                    
                    renpy.timeout(0)
                
                elif self.bx > 1280:
                    self.winner = "player"
                    renpy.timeout(0)
                
                
                
                renpy.redraw(self, 0)
                
                
                return r
            
            
            def event(self, ev, x, y, st):
                
                import pygame
                
                
                
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    self.stuck = False
                
                
                y = max(y, self.COURT_TOP)
                y = min(y, self.COURT_BOTTOM)
                self.playery = y
                
                
                
                if self.winner:
                    return self.winner
                else:
                    raise renpy.IgnoreEvent()


label game_pong:
    hide screen keylistener
    m 1a "Ты хочешь поиграть в Понг? Хорошо!"

    call demo_minigame_pong from _call_demo_minigame_pong
    return

label demo_minigame_pong:

    window hide None


    scene bg pong field


    if persistent.playername.lower() == "natsuki":
        $ playing_okayev = store.songs.getPlayingMusicName() == "Okay, Everyone! (Monika)"


        if playing_okayev:
            $ currentpos = get_pos(channel="music")
            $ adjusted_t5 = "<from " + str(currentpos) + " loop 4.444>bgm/5_natsuki.ogg"
            stop music fadeout 2.0
            $ renpy.music.play(adjusted_t5, fadein=2.0, tight=True)


    python:
        ui.add(PongDisplayable())
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)


    if persistent.playername.lower() == "natsuki":
        call natsuki_name_scare (playing_okayev=playing_okayev) from _call_natsuki_name_scare


    $ scene_change=True
    call spaceroom from _call_spaceroom_3

    if winner == "monika":
        $ inst_dialogue = store.mas_pong.DLG_WINNER
    else:


        if not persistent.ever_won['pong']:
            $ persistent.ever_won['pong'] = True
            $ grant_xp(xp.WIN_GAME)

        $ inst_dialogue = store.mas_pong.DLG_LOSER

    call expression inst_dialogue from _mas_pong_inst_dialogue

    menu:
        m "Ты хочешь сыграть снова?"
        "Да.":

            jump demo_minigame_pong
        "Нет.":

            if winner == "monika":
                if renpy.seen_label(store.mas_pong.DLG_WINNER_END):
                    $ end_dialogue = store.mas_pong.DLG_WINNER_FAST
                else:
                    $ end_dialogue = store.mas_pong.DLG_WINNER_END
            else:

                if renpy.seen_label(store.mas_pong.DLG_LOSER_END):
                    $ end_dialogue = store.mas_pong.DLG_LOSER_FAST
                else:
                    $ end_dialogue = store.mas_pong.DLG_LOSER_END

            call expression end_dialogue from _mas_pong_end_dialogue

    return




init -1 python in mas_pong:

    DLG_WINNER = "mas_pong_dlg_winner"
    DLG_WINNER_FAST = "mas_pong_dlg_winner_fast"
    DLG_LOSER = "mas_pong_dlg_loser"
    DLG_LOSER_FAST = "mas_pong_dlg_loser_fast"

    DLG_WINNER_END = "mas_pong_dlg_winner_end"
    DLG_LOSER_END = "mas_pong_dlg_loser_end"


    DLG_BLOCKS = (
        DLG_WINNER,
        DLG_WINNER_FAST,
        DLG_WINNER_END,
        DLG_LOSER,
        DLG_LOSER_FAST,
        DLG_LOSER_END
    )


label mas_pong_dlg_winner:
    m 1j "Я выиграла~!"
    return


label mas_pong_dlg_winner_end:
    m 4e "Я не могу радоваться такой просто победе..."
    m 1a "По крайней мере, мы все еще можем болтать друг с другом."
    m 1k "А-ха-ха!"
    m 1b "Спасибо, что позволил мне победить, [player]."
    m 1a "Только ученики начальных классов серьезно проигрывают в Понг, правда?"
    m 1j "Эхехе~"
    return


label mas_pong_dlg_winner_fast:

    return


label mas_pong_dlg_loser:
    m 1a "Ты выиграл! Поздравляю."
    return


label mas_pong_dlg_loser_end:
    m 1d "Вау, я действительно пыталась в тот раз."
    m 1a "Ты должно быть, действительно хорошо тренировался игре в Понг, чтобы так играть."
    m "Это то, чем ты можешь гордиться?"
    m 1j "Я думаю, что ты просто хотел произвести впечатление на меня, [player]~"
    return


label mas_pong_dlg_loser_fast:
    m 1e "Я побью тебя в следующий раз, [player]."
    return