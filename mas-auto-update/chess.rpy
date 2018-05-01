

default persistent._mas_chess_stats = {"wins": 0, "losses": 0, "draws": 0}
define mas_chess.CHESS_SAVE_PATH = "/chess_games/"
define mas_chess.CHESS_SAVE_EXT = ".pgn"
define mas_chess.CHESS_SAVE_NAME = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ-_0123456789"
define mas_chess.CHESS_PROMPT_FORMAT = "{0} | {1} | Turn: {2} | You: {3}"


init 1 python in mas_chess:
    import os
    import chess.pgn


    quit_game = False


    REL_DIR = "chess_games/"


    CHESS_MENU_X = 680
    CHESS_MENU_Y = 40
    CHESS_MENU_W = 560
    CHESS_MENU_H = 640
    CHESS_MENU_XALIGN = -0.05
    CHESS_MENU_AREA = (CHESS_MENU_X, CHESS_MENU_Y, CHESS_MENU_W, CHESS_MENU_H)

    CHESS_MENU_NEW_GAME_VALUE = "NEWGAME"
    CHESS_MENU_NEW_GAME_ITEM = (
        "Play New Game",
        CHESS_MENU_NEW_GAME_VALUE,
        True,
        False
    )

    CHESS_MENU_FINAL_VALUE = "NONE"
    CHESS_MENU_FINAL_ITEM = (
        "Nevermind",
        CHESS_MENU_FINAL_VALUE,
        False,
        False,
        20
    )

    def isInProgressGame(filename, mth):
        """
        Checks if the pgn game with the given filename is valid and
        in progress.

        IN:
            filename - filename of the pgn game
            mth - monika twitter handle. pass it in since I'm too lazy to
                find context from a store

        RETURNS:
            tuple of the following format:
                [0]: Text to display on button
                [1]: chess.pgn.Game of the game
            OR NONE if this is not a valid pgn game
        """
        if filename[-4:] != CHESS_SAVE_EXT:
            return None
        
        pgn_game = None
        with open(
            os.path.normcase(CHESS_SAVE_PATH + filename),
            "r"
        ) as loaded_game:
            pgn_game = chess.pgn.read_game(loaded_game)
        
        if pgn_game is None:
            return None
        
        if pgn_game.headers["Result"] != "*":
            return None
        
        
        if pgn_game.headers["White"] == mth:
            the_player = "Black"
        elif pgn_game.headers["Black"] == mth:
            the_player = "White"
        else: 
            return None
        
        
        
        
        board = pgn_game.board()
        for move in pgn_game.main_line():
            board.push(move)
        
        return (
            CHESS_PROMPT_FORMAT.format(
                pgn_game.headers["Date"].replace(".","-"),
                pgn_game.headers["Event"],
                board.fullmove_number,
                the_player
            ),
            pgn_game
        )


init:
    python:
        import chess
        import chess.pgn
        import subprocess
        import platform
        import random
        import pygame
        import threading
        import collections
        import os

        ON_POSIX = 'posix' in sys.builtin_module_names

        def enqueue_output(out, queue, lock):
            for line in iter(out.readline, b''):
                lock.acquire()
                queue.appendleft(line)
                lock.release()
            out.close()

        def is_morning():
            return (datetime.datetime.now().time().hour > 6 and datetime.datetime.now().time().hour < 18)

        class ArchitectureError(RuntimeError):
            pass

        def is_platform_good_for_chess():
            import platform
            import sys
            if sys.maxsize > 2**32:
                return platform.system() == 'Windows' or platform.system() == 'Linux' or platform.system() == 'Darwin'
            else:
                return platform.system() == 'Windows'

        def get_mouse_pos():
            vw = config.screen_width * 10000
            vh = config.screen_height * 10000
            pw, ph = renpy.get_physical_size()
            dw, dh = pygame.display.get_surface().get_size()
            mx, my = pygame.mouse.get_pos()
            
            
            
            mx = (mx * pw) / dw
            my = (my * ph) / dh
            
            r = None
            
            
            if vw / (vh / 10000) > pw * 10000 / ph:
                r = vw / pw
                my -= (ph - vh / r) / 2
            else:
                r = vh / ph
                mx -= (pw - vw / r) / 2
            
            newx = (mx * r) / 10000
            newy = (my * r) / 10000
            
            return (newx, newy)


        class ChessException(Exception):
            def __init__(self, msg):
                self.msg = msg
            def __str__(self):
                return self.msg


        if is_platform_good_for_chess():
            
            try: 
                file_path = os.path.normcase(
                    config.basedir + mas_chess.CHESS_SAVE_PATH
                )
                if not os.access(file_path, os.F_OK):
                    os.mkdir(file_path)
                mas_chess.CHESS_SAVE_PATH = file_path
            except: 
                raise ChessException(
                    "Chess game folder could not be created '{0}'".format(
                        file_path
                    )
                )

        class ChessDisplayable(renpy.Displayable):
            COLOR_WHITE = True
            COLOR_BLACK = False
            MONIKA_WAITTIME = 1500
            MONIKA_OPTIMISM = 33
            MONIKA_THREADS = 1
            
            MOUSE_EVENTS = (
                pygame.MOUSEMOTION,
                pygame.MOUSEBUTTONUP,
                pygame.MOUSEBUTTONDOWN
            )
            
            def __init__(self, player_color, pgn_game=None):
                """
                player_color - player color obvi
                pgn_game - previous game to load (chess.pgn.Game)
                """
                import sys
                
                renpy.Displayable.__init__(self)
                
                
                self.pieces_image = Image("mod_assets/chess_pieces.png")
                self.board_image = Image("mod_assets/chess_board.png")
                self.piece_highlight_red_image = Image("mod_assets/piece_highlight_red.png")
                self.piece_highlight_green_image = Image("mod_assets/piece_highlight_green.png")
                self.piece_highlight_yellow_image = Image("mod_assets/piece_highlight_yellow.png")
                self.piece_highlight_magenta_image = Image("mod_assets/piece_highlight_magenta.png")
                self.move_indicator_player = Image("mod_assets/move_indicator_player.png")
                self.move_indicator_monika = Image("mod_assets/move_indicator_monika.png")
                self.player_move_prompt = Text(_("It's your turn, [player]!"), size=36)
                self.num_turns = 0
                self.surrendered = False           
                
                
                self.VECTOR_PIECE_POS = {
                    'K': 0,
                    'Q': 1,
                    'R': 2,
                    'B': 3,
                    'N': 4,
                    'P': 5
                }
                self.BOARD_BORDER_WIDTH = 15
                self.BOARD_BORDER_HEIGHT = 15
                self.PIECE_WIDTH = 57
                self.PIECE_HEIGHT = 57
                self.BOARD_WIDTH = self.BOARD_BORDER_WIDTH * 2 + self.PIECE_WIDTH * 8
                self.BOARD_HEIGHT = self.BOARD_BORDER_HEIGHT * 2 + self.PIECE_HEIGHT * 8
                self.INDICATOR_WIDTH = 60
                self.INDICATOR_HEIGHT = 96
                self.BUTTON_WIDTH = 120
                self.BUTTON_HEIGHT = 35
                self.BUTTON_X_SPACING = 10
                self.BUTTON_Y_SPACING = 10
                
                
                button_idle = Image("mod_assets/hkb_idle_background.png")
                button_hover = Image("mod_assets/hkb_hover_background.png")
                button_no = Image("mod_assets/hkb_disabled_background.png")
                
                
                
                button_text_save_idle = Text(
                    "Save",
                    font=gui.default_font,
                    size=gui.text_size,
                    color="#000",
                    outlines=[]
                )
                button_text_giveup_idle = Text(
                    "Give Up",
                    font=gui.default_font,
                    size=gui.text_size,
                    color="#000",
                    outlines=[]
                )
                button_text_done_idle = Text(
                    "Done",
                    font=gui.default_font,
                    size=gui.text_size,
                    color="#000",
                    outlines=[]
                )
                
                
                button_text_save_hover = Text(
                    "Save",
                    font=gui.default_font,
                    size=gui.text_size,
                    color="#fa9",
                    outlines=[]
                )
                button_text_giveup_hover = Text(
                    "Give Up",
                    font=gui.default_font,
                    size=gui.text_size,
                    color="#fa9",
                    outlines=[]
                )
                button_text_done_hover = Text(
                    "Done",
                    font=gui.default_font,
                    size=gui.text_size,
                    color="#fa9",
                    outlines=[]
                )
                
                
                self.drawn_board_x = int((1280 - self.BOARD_WIDTH) / 2)
                self.drawn_board_y=  int((720 - self.BOARD_HEIGHT) / 2)
                drawn_button_x = (
                    1280 - self.drawn_board_x + self.BUTTON_X_SPACING
                )
                drawn_button_y_top = (
                    720 - (
                        (self.BUTTON_HEIGHT * 2) + 
                        self.BUTTON_Y_SPACING +
                        self.drawn_board_y
                    )
                )
                drawn_button_y_bot = (
                    720 - (self.BUTTON_HEIGHT + self.drawn_board_y)
                )
                
                
                self._button_save = MASButtonDisplayable(
                    button_text_save_idle,
                    button_text_save_hover,
                    button_text_save_idle,
                    button_idle,
                    button_hover,
                    button_no,
                    drawn_button_x,
                    drawn_button_y_top,
                    self.BUTTON_WIDTH,
                    self.BUTTON_HEIGHT,
                    hover_sound=gui.hover_sound,
                    activate_sound=gui.activate_sound
                )
                self._button_giveup = MASButtonDisplayable(
                    button_text_giveup_idle,
                    button_text_giveup_hover,
                    button_text_giveup_idle,
                    button_idle,
                    button_hover,
                    button_no,
                    drawn_button_x,
                    drawn_button_y_bot,
                    self.BUTTON_WIDTH,
                    self.BUTTON_HEIGHT,
                    hover_sound=gui.hover_sound,
                    activate_sound=gui.activate_sound
                )
                self._button_done = MASButtonDisplayable(
                    button_text_done_idle,
                    button_text_done_hover,
                    button_text_done_idle,
                    button_idle,
                    button_hover,
                    button_no,
                    drawn_button_x,
                    drawn_button_y_bot,
                    self.BUTTON_WIDTH,
                    self.BUTTON_HEIGHT,
                    hover_sound=gui.activate_sound,
                    activate_sound=gui.activate_sound
                )
                
                
                self._visible_buttons = [
                    self._button_save,
                    self._button_giveup
                ]
                self._visible_buttons_winner = [
                    self._button_save,
                    self._button_done
                ]
                
                
                
                if not is_platform_good_for_chess():
                    
                    raise ArchitectureError('Your operating system does not support the chess game.')
                
                def open_stockfish(path,startupinfo=None):
                    return subprocess.Popen([renpy.loader.transfn(path)], stdin=subprocess.PIPE, stdout=subprocess.PIPE,startupinfo=startupinfo)
                
                is_64_bit = sys.maxsize > 2**32
                if platform.system() == 'Windows':
                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    if is_64_bit:
                        self.stockfish = open_stockfish('mod_assets/stockfish_8_windows_x64.exe',startupinfo)
                    else:
                        self.stockfish = open_stockfish('mod_assets/stockfish_8_windows_x32.exe',startupinfo)
                elif platform.system() == 'Linux' and is_64_bit:
                    os.chmod(config.basedir + '/game/mod_assets/stockfish_8_linux_x64',0755)
                    self.stockfish = open_stockfish('mod_assets/stockfish_8_linux_x64')
                elif platform.system() == 'Darwin' and is_64_bit:
                    os.chmod(config.basedir + '/game/mod_assets/stockfish_8_macosx_x64',0755)
                    self.stockfish = open_stockfish('mod_assets/stockfish_8_macosx_x64')
                
                
                self.stockfish.stdin.write("setoption name Skill Level value %d\n" % (persistent.chess_strength))
                self.stockfish.stdin.write("setoption name Contempt value %d\n" % (self.MONIKA_OPTIMISM))
                
                
                self.queue = collections.deque()
                self.lock = threading.Lock()
                thrd = threading.Thread(target=enqueue_output, args=(self.stockfish.stdout, self.queue, self.lock))
                thrd.daemon = True
                thrd.start()
                
                
                
                
                
                
                self.promolist = ["q","r","n","b","r","k"]
                
                
                
                self.music_menu_open = False
                
                
                
                
                
                
                
                self.board = None
                
                
                if pgn_game:
                    
                    self.board = pgn_game.board()
                    for move in pgn_game.main_line():
                        self.board.push(move)
                    
                    
                    if self.board.turn == chess.WHITE:
                        self.current_turn = self.COLOR_WHITE
                    else:
                        self.current_turn = self.COLOR_BLACK
                    
                    
                    if pgn_game.headers["White"] == mas_monika_twitter_handle:
                        self.player_color = self.COLOR_BLACK
                    else:
                        self.player_color = self.COLOR_WHITE
                    
                    
                    last_move = self.board.peek().uci()
                    self.last_move_src = (
                        ord(last_move[0]) - ord('a'), 
                        ord(last_move[1]) - ord('1')
                    )
                    self.last_move_dst = (
                        ord(last_move[2]) - ord('a'),
                        ord(last_move[3]) - ord('1')
                    )
                
                else:
                    
                    self.board = chess.Board()
                    
                    
                    self.today_date = datetime.date.today().strftime("%Y.%m.%d")
                    self.start_fen = self.board.fen()
                    
                    
                    self.current_turn = self.COLOR_WHITE
                    
                    
                    self.player_color = player_color
                    
                    
                    self.last_move_src = None
                    self.last_move_dst = None
                
                self.selected_piece = None
                self.possible_moves = set([])
                self.winner = None
                self.last_clicked_king = 0.0
                
                
                self.drawn_button_x = 0
                self.drawn_button_y_top = 0
                self.drawn_button_y_bot = 0
                
                
                
                self.pgn_game = pgn_game
                
                
                if player_color != self.current_turn:
                    self.start_monika_analysis()
                    self._button_save.disable()
                    self._button_giveup.disable()
                elif self.board.fullmove_number <= 4:
                    self._button_save.disable()
            
            def start_monika_analysis(self):
                self.stockfish.stdin.write("position fen %s" % (self.board.fen()) + '\n')
                self.stockfish.stdin.write("go movetime %d" % self.MONIKA_WAITTIME + '\n')
            
            def poll_monika_move(self):
                self.lock.acquire()
                res = None
                while self.queue:
                    line = self.queue.pop()
                    match = re.match(r"^bestmove (\w+)", line)
                    if match:
                        res = match.group(1)
                self.lock.release()
                return res
            
            def __del__(self):
                self.stockfish.stdin.close()
                self.stockfish.wait()
            
            @staticmethod
            def coords_to_uci(x, y):
                x = chr(x + ord('a'))
                y += 1
                return str(x) + str(y)
            
            def check_winner(self, current_move):
                if self.board.is_game_over():
                    if self.board.result() == '1/2-1/2':
                        self.winner = 'none'
                    else:
                        self.winner = current_move
            
            def _quitPGN(self, giveup):
                """
                Generates a pgn of the board, and depending on if we are
                doing previous game or not, does appropriate header
                setting

                IN:
                    giveup - True if the player surrendered, False otherwise

                RETURNS: tuple of the following format:
                    [0]: chess.pgn.Game object of this game
                    [1]: True if monika won, False if not
                    [2]: True if player gaveup, False otherwise
                    [3]: number of turns of this game
                """
                new_pgn = chess.pgn.Game.from_board(self.board)
                
                if giveup:
                    if self.player_color == self.COLOR_WHITE:
                        new_pgn.headers["Result"] = "0-1"
                    else:
                        new_pgn.headers["Result"] = "1-0"
                
                if self.pgn_game:
                    
                    new_pgn.headers["Site"] = self.pgn_game.headers["Site"]
                    new_pgn.headers["Date"] = self.pgn_game.headers["Date"]
                    new_pgn.headers["White"] = self.pgn_game.headers["White"]
                    new_pgn.headers["Black"] = self.pgn_game.headers["Black"]
                    
                    old_fen = self.pgn_game.headers.get("FEN", None)
                    if old_fen:
                        new_pgn.headers["FEN"] = old_fen
                        new_pgn.headers["SetUp"] = "1"
                
                else:
                    
                    
                    if player_color == self.COLOR_WHITE:
                        new_pgn.headers["White"] = persistent.playername
                        new_pgn.headers["Black"] = mas_monika_twitter_handle
                    else:
                        new_pgn.headers["White"] = mas_monika_twitter_handle
                        new_pgn.headers["Black"] = persistent.playername
                    
                    
                    
                    new_pgn.headers["Site"] = "MAS" 
                    new_pgn.headers["Date"] = self.today_date
                    new_pgn.headers["FEN"] = self.start_fen
                    new_pgn.headers["SetUp"] = "1"
                
                return (
                    new_pgn,
                    (
                        (
                            new_pgn.headers["Result"] == "1-0"
                            and new_pgn.headers["White"] == mas_monika_twitter_handle
                        ) or (
                            new_pgn.headers["Result"] == "0-1"
                            and new_pgn.headers["Black"] == mas_monika_twitter_handle
                        )
                    ),
                    giveup,
                    self.board.fullmove_number
                )
            
            
            def _inButton(self, x, y, button_x, button_y):
                """
                Checks if the given mouse coordinates is in the given button's
                area.

                IN:
                    x - x coordinate
                    y - y coordinate
                    button_x - x coordinate of the button
                    button_y - y coordinate of the button

                RETURNS:
                    True if the mouse coords are in the button,
                    False otherwise
                """
                return (
                    button_x <= x <= button_x + self.BUTTON_WIDTH
                    and button_y <= y <= button_y + self.BUTTON_HEIGHT
                )
            
            
            def render(self, width, height, st, at):
                
                
                if self.current_turn != self.player_color and not self.winner:
                    monika_move = self.poll_monika_move()
                    if monika_move is not None:
                        self.last_move_src = (ord(monika_move[0]) - ord('a'), ord(monika_move[1]) - ord('1'))
                        self.last_move_dst = (ord(monika_move[2]) - ord('a'), ord(monika_move[3]) - ord('1'))
                        self.board.push_uci(monika_move)
                        if self.current_turn == self.COLOR_BLACK:
                            self.num_turns += 1
                        self.current_turn = self.player_color
                        self.winner = self.board.is_game_over()
                        
                        
                        
                        if not self.winner:
                            self._button_giveup.enable()
                            
                            
                            if self.num_turns > 4:
                                self._button_save.enable()
                
                
                r = renpy.Render(width, height)
                
                
                board = renpy.render(self.board_image, 1280, 720, st, at)
                
                
                pieces = renpy.render(self.pieces_image, 1280, 720, st, at)
                
                
                highlight_red = renpy.render(self.piece_highlight_red_image, 1280, 720, st, at)
                highlight_green = renpy.render(self.piece_highlight_green_image, 1280, 720, st, at)
                highlight_yellow = renpy.render(self.piece_highlight_yellow_image, 1280, 720, st, at)
                highlight_magenta = renpy.render(self.piece_highlight_magenta_image, 1280, 720, st, at)
                
                
                mx, my = get_mouse_pos()
                
                
                
                
                
                visible_buttons = list()
                if self.winner:
                    
                    
                    visible_buttons = [
                        (b.render(width, height, st, at), b.xpos, b.ypos)
                        for b in self._visible_buttons_winner
                    ]
                
                else:
                    
                    
                    visible_buttons = [
                        (b.render(width, height, st, at), b.xpos, b.ypos)
                        for b in self._visible_buttons
                    ]
                
                
                r.blit(board, (self.drawn_board_x, self.drawn_board_y))
                indicator_position = (int((width - self.INDICATOR_WIDTH) / 2 + self.BOARD_WIDTH / 2 + 50),
                                      int((height - self.INDICATOR_HEIGHT) / 2))
                
                
                if self.current_turn == self.player_color:
                    r.blit(renpy.render(self.move_indicator_player, 1280, 720, st, at), indicator_position)
                else:
                    r.blit(renpy.render(self.move_indicator_monika, 1280, 720, st, at), indicator_position)
                
                
                for b in visible_buttons:
                    r.blit(b[0], (b[1], b[2]))
                
                def get_piece_render_for_letter(letter):
                    jy = 0 if letter.islower() else 1
                    jx = self.VECTOR_PIECE_POS[letter.upper()]
                    return pieces.subsurface((jx * self.PIECE_WIDTH, jy * self.PIECE_HEIGHT,
                                              self.PIECE_WIDTH, self.PIECE_HEIGHT))
                
                
                for ix in range(8):
                    for iy in range(8):
                        iy_orig = iy
                        ix_orig = ix
                        if self.player_color == self.COLOR_WHITE:
                            iy = 7 - iy
                        else: 
                            ix = 7 - ix
                        x = int((width - (self.BOARD_WIDTH - self.BOARD_BORDER_WIDTH * 2)) / 2  + ix * self.PIECE_WIDTH)
                        y = int((height - (self.BOARD_HEIGHT - self.BOARD_BORDER_HEIGHT * 2)) / 2 + iy * self.PIECE_HEIGHT)
                        
                        def render_move(move):
                            if move is not None and ix_orig == move[0] and iy_orig == move[1]:
                                if self.player_color == self.current_turn:
                                    r.blit(highlight_magenta, (x, y))
                                else:
                                    r.blit(highlight_green, (x, y))
                        
                        render_move(self.last_move_src)
                        render_move(self.last_move_dst)
                        
                        
                        if (self.selected_piece is not None and
                            ix_orig == self.selected_piece[0] and
                            iy_orig == self.selected_piece[1]):
                            r.blit(highlight_green, (x, y))
                            continue
                        
                        piece = self.board.piece_at(iy_orig * 8 + ix_orig)
                        
                        possible_move_str = None
                        blit_rendered = False
                        if self.possible_moves:
                            possible_move_str = (ChessDisplayable.coords_to_uci(self.selected_piece[0], self.selected_piece[1]) +
                                                 ChessDisplayable.coords_to_uci(ix_orig, iy_orig))
                            if chess.Move.from_uci(possible_move_str) in self.possible_moves:
                                r.blit(highlight_yellow, (x, y))
                                blit_rendered = True
                            
                            
                            if not blit_rendered and (iy == 0 or iy == 7):
                                index = 0
                                while (not blit_rendered
                                        and index < len(self.promolist)):
                                    
                                    if (chess.Move.from_uci(
                                        possible_move_str + self.promolist[index])
                                        in self.possible_moves):
                                        r.blit(highlight_yellow, (x, y))
                                        blit_rendered = True
                                    
                                    index += 1
                        
                        if piece is None:
                            continue
                        
                        if (mx >= x and mx < x + self.PIECE_WIDTH and
                            my >= y and my < y + self.PIECE_HEIGHT and
                            bool(str(piece).isupper()) == (self.player_color == self.COLOR_WHITE) and
                            self.current_turn == self.player_color and
                            self.selected_piece is None and
                            not self.winner):
                            r.blit(highlight_green, (x, y))
                        
                        if self.winner:
                            result = self.board.result()
                            
                            
                            if str(piece) == "k" and result == "0-1":
                                r.blit(highlight_red, (x, y))
                            
                            
                            elif str(piece) == "K" and result == "1-0":
                                r.blit(highlight_red, (x, y))
                        
                        r.blit(get_piece_render_for_letter(str(piece)), (x, y))
                
                
                if self.current_turn == self.player_color and not self.winner:
                    
                    prompt = renpy.render(self.player_move_prompt, 1280, 720, st, at)
                    pw, ph = prompt.get_size()
                    bh = (height - self.BOARD_HEIGHT) / 2
                    r.blit(prompt, (int((width - pw) / 2), int(self.BOARD_HEIGHT + bh + (bh - ph) / 2)))
                
                if self.selected_piece is not None:
                    
                    piece = self.board.piece_at(self.selected_piece[1] * 8 + self.selected_piece[0])
                    assert piece is not None
                    px, py = get_mouse_pos()
                    px -= self.PIECE_WIDTH / 2
                    py -= self.PIECE_HEIGHT / 2
                    r.blit(get_piece_render_for_letter(str(piece)), (px, py))
                
                
                renpy.redraw(self, 0)
                
                
                
                return r
            
            
            def event(self, ev, x, y, st):
                
                
                if ev.type in self.MOUSE_EVENTS:
                    
                    
                    
                    if self.winner:
                        
                        if self._button_done.event(ev, x, y, st):
                            
                            return self._quitPGN(False)
                    
                    
                    elif self.current_turn == self.player_color:
                        
                        if self._button_save.event(ev, x, y, st):
                            
                            return self._quitPGN(False)
                        
                        elif self._button_giveup.event(ev, x, y, st):
                            renpy.call_in_new_context("mas_chess_confirm_context")
                            if mas_chess.quit_game:
                                
                                return self._quitPGN(True)
                
                def get_piece_pos():
                    mx, my = get_mouse_pos()
                    mx -= (1280 - (self.BOARD_WIDTH - self.BOARD_BORDER_WIDTH * 2)) / 2
                    my -= (720 - (self.BOARD_HEIGHT - self.BOARD_BORDER_HEIGHT * 2)) / 2
                    px = mx / self.PIECE_WIDTH
                    py = my / self.PIECE_HEIGHT
                    if self.player_color == self.COLOR_WHITE:
                        py = 7 - py
                    else: 
                        px = 7 - px
                    if py >= 0 and py < 8 and px >= 0 and px < 8:
                        return (px, py)
                    return (None, None)
                
                
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    px, py = get_piece_pos()
                    if (
                            px is not None 
                            and py is not None 
                            and self.board.piece_at(py * 8 + px) is not None 
                            and bool(str(self.board.piece_at(py * 8 + px)).isupper()) 
                                == (self.player_color == self.COLOR_WHITE) 
                            and self.current_turn == self.player_color
                        ):
                        
                        piece = str(self.board.piece_at(py * 8 + px))
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        self.possible_moves = self.board.legal_moves
                        self.selected_piece = (px, py)
                
                
                if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                    px, py = get_piece_pos()
                    if px is not None and py is not None and self.selected_piece is not None:
                        move_str = self.coords_to_uci(self.selected_piece[0], self.selected_piece[1]) + self.coords_to_uci(px, py)
                        
                        piece = str(
                            self.board.piece_at(
                                self.selected_piece[1] * 8 +
                                self.selected_piece[0]
                            )
                        )
                        
                        if piece.lower() == 'p' and (py == 0 or py == 7):
                            move_str += "q"
                        if chess.Move.from_uci(move_str) in self.possible_moves:
                            self.last_move_src = self.selected_piece
                            self.last_move_dst = (px, py)
                            self.board.push_uci(move_str)
                            
                            self.winner = self.board.is_game_over()
                            if self.current_turn == self.COLOR_BLACK:
                                self.num_turns += 1
                            self.current_turn = not self.current_turn
                            if not self.winner:
                                self.start_monika_analysis()
                            
                            
                            self._button_save.disable()
                            self._button_giveup.disable()
                    
                    self.selected_piece = None
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    self.possible_moves = set([])
                
                
                if ev.type == pygame.KEYUP:
                    
                    
                    if ev.key == pygame.K_m:
                        
                        
                        if ev.mod & pygame.KMOD_SHIFT:
                            mute_music()
                        elif not self.music_menu_open:
                            self.music_menu_open = True
                            select_music()
                        else: 
                            self.music_menu_open = False
                    
                    
                    if (ev.key == pygame.K_PLUS
                            or ev.key == pygame.K_EQUALS
                            or ev.key == pygame.K_KP_PLUS):
                        inc_musicvol()
                    
                    
                    if (ev.key == pygame.K_MINUS
                            or ev.key == pygame.K_UNDERSCORE
                            or ev.key == pygame.K_KP_MINUS):
                        dec_musicvol()
                
                raise renpy.IgnoreEvent()


label game_chess:
    hide screen keylistener
    m 1b "Ты хочешь поиграть в шахматы? Хорошо~"

    m 1a "Приготовся!"
    call demo_minigame_chess from _call_demo_minigame_chess
    return

label demo_minigame_chess:
    $ import chess.pgn
    $ import os





    $ pgn_files = os.listdir(mas_chess.CHESS_SAVE_PATH)
    $ loaded_game = None
    if pgn_files:
        python:

            pgn_games = list()
            for filename in pgn_files:
                in_prog_game = mas_chess.isInProgressGame(
                    filename,
                    mas_monika_twitter_handle
                )
                
                if in_prog_game:
                    pgn_games.append((
                        in_prog_game[0],
                        in_prog_game[1],
                        False,
                        False
                    ))


        if len(pgn_games) > 0:
            if len(pgn_games) == 1:
                $ game_s_dialog = "игра"
            else:
                $ game_s_dialog = "несколько игр"

            python:

                pgn_games.sort()
                pgn_games.reverse()


            $ pgn_games.append(mas_chess.CHESS_MENU_NEW_GAME_ITEM)

            m 1a "У нас все еще [game_s_dialog] в прогрессе."
            show monika at t21
            $ renpy.say(m, "Выбери игру, в которую ты хочешь играть.", interact=False)

            call screen mas_gen_scrollable_menu(pgn_games, mas_chess.CHESS_MENU_AREA, mas_chess.CHESS_MENU_XALIGN, mas_chess.CHESS_MENU_FINAL_ITEM)

            show monika at t11
            $ loaded_game = _return


            if loaded_game == mas_chess.CHESS_MENU_FINAL_VALUE:
                m "Хорошо, может позже?"
                return


            if loaded_game != mas_chess.CHESS_MENU_NEW_GAME_VALUE:


                if loaded_game.headers["White"] == mas_monika_twitter_handle:
                    $ player_color = ChessDisplayable.COLOR_BLACK
                else:
                    $ player_color = ChessDisplayable.COLOR_WHITE
                jump mas_chess_game_start


    $ loaded_game = None
    menu:
        m "Какой цвет ты выберешь?"
        "Белый":

            $ player_color = ChessDisplayable.COLOR_WHITE
        "Черный":
            $ player_color = ChessDisplayable.COLOR_BLACK
        "Давай тянуть жребий!":
            $ choice = random.randint(0, 1) == 0
            if choice:
                $ player_color = ChessDisplayable.COLOR_WHITE
                m 2a "О смотри, Я хожу черными! Давай начнем!"
            else:
                $ player_color = ChessDisplayable.COLOR_BLACK
                m 2a "О смотри, Я хожу белыми! Давай начнем!"

label mas_chess_game_start:
    window hide None

    python:
        ui.add(ChessDisplayable(player_color, pgn_game=loaded_game))
        results = ui.interact(suppress_underlay=True)


        new_pgn_game, is_monika_winner, is_surrender, num_turns = results


        game_result = new_pgn_game.headers["Result"]






    if game_result == "*":


        jump mas_chess_savegame

    elif game_result == "1/2-1/2":

        m 3h "Ничья? Как скучно..."
        $ persistent._mas_chess_stats["draws"] += 1

    elif is_monika_winner:
        $ persistent._mas_chess_stats["losses"] += 1
        if is_surrender and num_turns <= 4:
            m 1e "Да ладно, не сдавайся так легко."
        else:
            m 1b "Я выиграла!"

        if persistent.chess_strength>0:
            m 1j "I'll go a little easier on you next time."
            $ persistent.chess_strength += -1
        else:
            m 1l "Действительно было легко с тобой!"
    else:

        $ persistent._mas_chess_stats["wins"] += 1

        if not persistent.ever_won['chess']:
            $ persistent.ever_won['chess'] = True
            $ grant_xp(xp.WIN_GAME)

        m 2a "Ты выиграл! Поздравляю."
        if persistent.chess_strength<20:
            m 2 "I'll get you next time for sure!"
            $ persistent.chess_strength += 1
        else:
            m 2b "Ты действительно потрясяюще играешь!"
            m 3l "Ты уверен что не читеришь?"


    if num_turns > 4:
        menu:
            m "Ты хочешь сохранить эту игру?"
            "Да":
                label mas_chess_savegame:
                    python:
                        if loaded_game: 
                            new_pgn_game.headers["Event"] = (
                                loaded_game.headers["Event"]
                            )


                        else:
                            
                            save_name = ""
                            while len(save_name) == 0:
                                save_name = renpy.input(
                                    "Enter a name for this game:",
                                    allow=mas_chess.CHESS_SAVE_NAME,
                                    length=15
                                )
                            new_pgn_game.headers["Event"] = save_name


                        save_filename = (
                            new_pgn_game.headers["Event"] + 
                            mas_chess.CHESS_SAVE_EXT
                        )


                        file_path = mas_chess.CHESS_SAVE_PATH + save_filename


                        is_file_exist = os.access(
                            os.path.normcase(file_path),
                            os.F_OK
                        )


                    if is_file_exist:
                        m 1e "У нас уже есть игра под названием '[save_name]'."
                        menu:
                            m "Я должна её перезаписать?"
                            "Да":
                                pass
                            "Нет":
                                jump mas_chess_savegame

                    python:
                        with open(file_path, "w") as pgn_file:
                            pgn_file.write(str(new_pgn_game))


                        display_file_path = mas_chess.REL_DIR + save_filename

                    m 1q ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"
                    m 1j "I've saved our game in '[display_file_path]'!"

                    if not renpy.seen_label("mas_chess_pgn_explain"):

                        label mas_chess_pgn_explain:
                            m 1a "Она в формате называемом Portable Game Notation."
                            m "Этот файл можно открыть в программе просмотра PGN."

                            if game_result == "*":
                                m 1n "Можно отредактировать этот файл и изменить исход игры,{w} но я уверена, что ты этого не сделаешь."
                                m 1e "Правда, [player]?"
                                menu:
                                    "Конечно нет":
                                        m 1j "Ура~"

                    if game_result == "*":
                        jump mas_chess_end
            "Нет":

                pass

label mas_chess_playagain:
    menu:
        m "Ты хочешь сыграть снова?"
        "Да":

            jump demo_minigame_chess
        "Да":
            pass

label mas_chess_end:
    if is_monika_winner:
        m 2d "Несмотря на свои простые правила, шахматы - действительно сложная игра."
        m 1a "Все в порядке, если ты время от времени борешься."
        m 1j "Помни, что важно уметь учиться на своих ошибках."
    elif game_result == "*":

        m 1a "Ладно, [player], давай продолжим эту игру позже."
    else:
        m 2b "Удивительно, сколько еще я должна учиться даже сейчас."
        m 2a "Я действительно не против проиграть ведь столькому надо еще учиться."
        m 1j "В конце концов, я в хорошей компании."

    return



label mas_chess_confirm_context:
    call screen mas_chess_confirm 
    $ store.mas_chess.quit_game = _return
    return


screen mas_chess_confirm():


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _("Ты уверен что хочешь сдаться?"):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Да") action Return(True)
            textbutton _("Нет") action Return(False)
