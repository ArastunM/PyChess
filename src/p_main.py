# Imports
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import random

# Global Variables
pawn_n = 0
count = 0
take_count = 0
taken_piece = None
allow = False
en_passant = 0
move_ord = 0
block = 0
touch_yp = 0
touch_xp = 0


# Screens
class Entry(Screen):
    b1 = ObjectProperty(None)

    def on_pre_enter(self, *args):
        Window.size = (800, 600)

    def on_touch_up(self, touch):
        self.b1.opacity = 1

    def p2_opacity(self):
        self.b1.opacity = 0.5


class Clicker(Screen):
    # Defining tiles
    tile1 = ObjectProperty(None)
    tile2 = ObjectProperty(None)
    tile3 = ObjectProperty(None)
    tile4 = ObjectProperty(None)
    tile5 = ObjectProperty(None)
    tile6 = ObjectProperty(None)
    tile7 = ObjectProperty(None)
    tile8 = ObjectProperty(None)
    tile9 = ObjectProperty(None)
    tile10 = ObjectProperty(None)
    tile11 = ObjectProperty(None)
    tile12 = ObjectProperty(None)

    def on_pre_enter(self, *args):
        Window.size = (800, 600)
        # All tiles in a list
        self.all_tiles = [self.tile1, self.tile2, self.tile3, self.tile4, self.tile5, self.tile6, self.tile7, self.tile8,
                         self.tile9, self.tile10, self.tile11, self.tile12]
        self.rem_time = 30
        self.score_p = 0

        f = open("starting_position.txt", "r")
        self.ids.best_score.text = f.readlines()[32]
        f.close()

        self.nullify_game()

    def start_on(self):
        if self.gamelock == 0:
            self.gamelock = 1
            self.score_p = 0
            self.ids.score.text = str(self.score_p)
            self.rem_time = 30
            self.ids.run_clock.color = 0, 0, 0, 1
            self.ids.run_clock.text = str(self.rem_time)

            # Random configuration with 4 - 7 tiles on
            for i in range(len(self.all_tiles)):
                self.all_tiles[i].background_color = 0, 0, 0, 1

            for i in range(9):
                self.all_tiles[random.randint(0, 11)].background_color = 1, 1, 1, 0
            self.update_time()

    def on_press(self):
        if self.gamelock == 1:
            self.score_p += 1
            self.ids.score.text = str(self.score_p)

    def on_touch_up(self, touch):
        if self.gamelock == 1 and touch.y > 140:
            # Each time approx two tiles reappear
            for i in range(random.randint(1, 2)):
                self.all_tiles[random.randint(0, 11)].background_color = 0, 0, 0, 1

    def nullify_game(self):
        # Game is set to be ready for next try
        for i in range(len(self.all_tiles)):
            self.all_tiles[i].background_color = 0, 0, 0, 1

        self.gamelock = 0

        # Score is saved (if it is a new record)
        if self.score_p != 0:
            f = open("starting_position.txt", "r")
            if int(f.readlines()[32]) < self.score_p:
                self.ids.best_score.text = str(self.score_p)

                f = open("starting_position.txt", "r")
                self.f_text = f.readlines()
                self.f_text[32] = str(self.score_p)
                f = open("starting_position.txt", "w")
                f.writelines(self.f_text)
                f.close()


    def update_time(self):
        if self.gamelock == 1:
            if self.rem_time <= 10:
                self.ids.run_clock.color = 1, 0, 0, 1
            if self.rem_time != 0:
                self.ids.run_clock.text = str(self.rem_time)
                self.rem_time -= 1
                Clock.schedule_once(lambda dt: self.update_time(), 1)
            else:
                self.ids.run_clock.text = str(self.rem_time)
                self.nullify_game()


class ChessBoard(Screen):
    # Defining figures
    pawn1 = ObjectProperty(None)
    pawn2 = ObjectProperty(None)
    pawn3 = ObjectProperty(None)
    pawn4 = ObjectProperty(None)
    pawn5 = ObjectProperty(None)
    pawn6 = ObjectProperty(None)
    pawn7 = ObjectProperty(None)
    pawn8 = ObjectProperty(None)

    pawn9 = ObjectProperty(None)
    pawn10 = ObjectProperty(None)
    pawn11 = ObjectProperty(None)
    pawn12 = ObjectProperty(None)
    pawn13 = ObjectProperty(None)
    pawn14 = ObjectProperty(None)
    pawn15 = ObjectProperty(None)
    pawn16 = ObjectProperty(None)

    rook17 = ObjectProperty(None)
    rook18 = ObjectProperty(None)
    bishop21 = ObjectProperty(None)
    bishop22 = ObjectProperty(None)
    queen25 = ObjectProperty(None)
    knight27 = ObjectProperty(None)
    knight28 = ObjectProperty(None)

    rook19 = ObjectProperty(None)
    rook20 = ObjectProperty(None)
    bishop23 = ObjectProperty(None)
    bishop24 = ObjectProperty(None)
    queen26 = ObjectProperty(None)
    knight29 = ObjectProperty(None)
    knight30 = ObjectProperty(None)

    king31 = ObjectProperty(None)
    king32 = ObjectProperty(None)

    def on_pre_enter(self, *args):
        Window.size = (1150, 800)
        # Listing figures
        # All involved figures
        self.all_figures = [self.pawn1, self.pawn2, self.pawn3, self.pawn4, self.pawn5, self.pawn6, self.pawn7,
                            self.pawn8, self.pawn9, self.pawn10, self.pawn11, self.pawn12, self.pawn13, self.pawn14,
                            self.pawn15, self.pawn16, self.rook17, self.rook18, self.rook19, self.rook20,
                            self.bishop21, self.bishop22, self.bishop23, self.bishop24, self.queen25, self.queen26,
                            self.knight27, self.knight28, self.knight29, self.knight30, self.king31, self.king32]
        # White
        self.white = [self.pawn1, self.pawn2, self.pawn3, self.pawn4, self.pawn5, self.pawn6, self.pawn7, self.pawn8,
                      self.rook17, self.rook18, self.bishop21, self.bishop22, self.queen25,
                      self.knight27, self.knight28, self.king31]

        # Black
        self.black = [self.pawn9, self.pawn10, self.pawn11, self.pawn12, self.pawn13, self.pawn14, self.pawn15,
                      self.pawn16, self.rook19, self.rook20, self.bishop23, self.bishop24,
                      self.queen26, self.knight29, self.knight30, self.king32]

        # Pawns
        self.pawns = [self.pawn1, self.pawn2, self.pawn3, self.pawn4, self.pawn5, self.pawn6, self.pawn7,
                      self.pawn8, self.pawn9, self.pawn10, self.pawn11, self.pawn12, self.pawn13,
                      self.pawn14, self.pawn15, self.pawn16]

        # Arrays
        self.cast_allow = [0] * 33
        self.q_to = [""] * 33
        self.current_opacity = [0] * len(self.all_figures)
        self.current_pos = [[0] * 2 for i in range(len(self.all_figures))]
        self.start_pos = [[0] * 2 for i in range(len(self.all_figures))]

        # Check
        self.king_spec = 0
        self.check = 0

        # Sound effects
        self.move_cl = SoundLoader.load('audio/move_sound.wav')
        self.check_sd = SoundLoader.load('audio/check_sound.wav')
        self.ts_on = SoundLoader.load('audio/turn_on.wav')
        self.sound_volume = 1
        self.ids.sound_cont.background_normal = "images/sound_on.png"
        self.ids.sound_cont.background_down = "images/sound_on.png"

    # Pawn functions
    def pawn_move(self, y, yp, xp, numb, name):
        global move_ord, block, en_passant
        # Checking move order
        if move_ord == 0:
            # Checking if pawn intends to move upward
            if y > yp + 90:
                # Checking if moving point is empty
                self.pawn_block("w", y, yp, xp)
                if block == 0:
                    if y < 310 and yp + 268 > y:
                        name.pos_hint = {"top": 233 / 600}
                        name.pos[1] = (0.38 * Window.size[1] - 96)
                        move_ord = 1
                    elif y < 399 and yp + 280 > y:
                        en_passant = numb
                        name.pos_hint = {"top": 299 / 600}
                        name.pos[1] = (0.49 * Window.size[1] - 96)
                        move_ord = 1
                    elif y < 486 and yp + 180 > y:
                        name.pos_hint = {"top": 365 / 600}
                        name.pos[1] = (0.608 * Window.size[1] - 96)
                        move_ord = 1
                    elif y < 575 and yp + 180 > y:
                        name.pos_hint = {"top": 431 / 600}
                        name.pos[1] = (0.718 * Window.size[1] - 96)
                        move_ord = 1
                    elif y < 662 and yp + 180 > y:
                        name.pos_hint = {"top": 497 / 600}
                        name.pos[1] = (0.828 * Window.size[1] - 96)
                        move_ord = 1
                    elif y < 749 and yp + 180 > y:
                        name.pos_hint = {"top": 563 / 600}
                        name.pos[1] = (0.938 * Window.size[1] - 96)
                        move_ord = 1

        else:
            if y < yp:
                self.pawn_block("b", y, yp, xp)
                if block == 0:
                    # Difference in numbers is because buttons pos is assigned from bottom (-110)
                    if y > 487 and yp - 158 < y:
                        name.pos_hint = {"top": 431 / 600}
                        name.pos[1] = (0.718 * Window.size[1] - 96)
                        move_ord = 0
                    elif y > 399 and yp - 170 < y:
                        en_passant = numb
                        name.pos_hint = {"top": 365 / 600}
                        name.pos[1] = (0.608 * Window.size[1] - 96)
                        move_ord = 0
                    elif y > 311 and yp - 70 < y:
                        name.pos_hint = {"top": 299 / 600}
                        name.pos[1] = (0.49 * Window.size[1] - 96)
                        move_ord = 0
                    elif y > 223 and yp - 70 < y:
                        name.pos_hint = {"top": 233 / 600}
                        name.pos[1] = (0.38 * Window.size[1] - 96)
                        move_ord = 0
                    elif y > 136 and yp - 70 < y:
                        name.pos_hint = {"top": 167 / 600}
                        name.pos[1] = (0.278 * Window.size[1] - 96)
                        move_ord = 0
                    elif y > 49 and yp - 70 < y:
                        name.pos_hint = {"top": 101 / 600}
                        name.pos[1] = (0.168 * Window.size[1] - 96)
                        move_ord = 0

    def pawn_block(self, col, y, yp, xp):
        # Pawn block is part of the Pawn move
        global block
        block = 0
        if col == "w":
            for i in range(0, len(self.all_figures)):
                # Super block / when pawn moves 2 squares
                if 310 < y < 390 and yp < 210:
                    if yp + 200 > self.all_figures[i].pos[1] > yp and \
                            (xp + 15 > self.all_figures[i].pos[0] > xp - 15) \
                            and self.all_figures[i].opacity != 0:
                        block = 1
                else:
                    # If they are 1 y apart and are on the same column / if pawn exists (has been taken?)
                    if yp + 100 > self.all_figures[i].pos[1] > yp and \
                            (xp + 15 > self.all_figures[i].pos[0] > xp - 15) \
                            and self.all_figures[i].opacity != 0:
                        block = 1

        elif col == "b":
            for i in range(0, len(self.all_figures)):
                if yp > 487 > y > 399:
                    if yp - 200 < self.all_figures[i].pos[1] < yp and \
                            (xp + 15 > self.all_figures[i].pos[0] > xp - 15) \
                            and self.all_figures[i].opacity != 0:
                        block = 1
                else:
                    if yp - 100 < self.all_figures[i].pos[1] < yp and \
                            (xp + 15 > self.all_figures[i].pos[0] > xp - 15) \
                            and self.all_figures[i].opacity != 0:
                        block = 1

    def pawn_passant(self, x, yp, xp, name):
        global move_ord, en_passant, take_count
        take_count = 0
        # Checking move order
        if move_ord == 0:
            for i in range(0, len(self.black)):
                # Inequalities must be true signifying en passant is possible
                # yp + 10 / yp - 10 is put as height of pawns can slightly vary after takes
                if yp + 10 > self.black[i].pos[1] > yp - 10 and en_passant == i + 9 and take_count == 0:
                    # Which side to take / first if is right
                    if x > xp:
                        if xp + 100 > self.black[i].pos[0] > xp + 70 and self.black[i].opacity != 0:
                            # Moving it sideways towards the taken pawn
                            name.pos_hint = {"x": self.black[i].pos[0] / Window.size[0],
                                             "y": (name.pos[1] + 88) / Window.size[1]}
                            name.pos = (self.black[i].pos[0], name.pos[1] + 88)
                            self.black[i].opacity = 0
                            self.black[i].size_hint = 0, 0
                            take_count = 1
                            en_passant = 0
                            move_ord = 1
                    else:
                        if xp - 100 < self.black[i].pos[0] < xp - 70 and self.black[i].opacity != 0:
                            name.pos_hint = {"x": self.black[i].pos[0] / Window.size[0],
                                             "y": (name.pos[1] + 88) / Window.size[1]}
                            name.pos = (self.black[i].pos[0], name.pos[1] + 88)
                            self.black[i].opacity = 0
                            self.black[i].size_hint = 0, 0
                            take_count = 1
                            en_passant = 0
                            move_ord = 1

        else:
            for i in range(0, len(self.white)):
                if yp + 10 > self.white[i].pos[1] > yp - 10 and en_passant == i + 1 and take_count == 0:
                    if x > xp:
                        if xp + 100 > self.white[i].pos[0] > xp + 70 and self.white[i].opacity != 0:
                            name.pos_hint = {"x": self.white[i].pos[0] / Window.size[0],
                                             "y": (name.pos[1] - 88) / Window.size[1]}
                            name.pos = (self.white[i].pos[0], name.pos[1] - 88)
                            self.white[i].opacity = 0
                            self.white[i].size_hint = 0, 0
                            take_count = 1
                            en_passant = 0
                            move_ord = 0
                    else:
                        if xp - 100 < self.white[i].pos[0] < xp - 70 and self.white[i].opacity != 0:
                            name.pos_hint = {"x": self.white[i].pos[0] / Window.size[0],
                                             "y": (name.pos[1] - 88) / Window.size[1]}
                            name.pos = (self.white[i].pos[0], name.pos[1] - 88)
                            self.white[i].opacity = 0
                            self.white[i].size_hint = 0, 0
                            take_count = 1
                            en_passant = 0
                            move_ord = 0

    # Too long?
    def pawn_takes(self, x, y, yp, xp, name):
        global move_ord, take_count, taken_piece
        take_count = 0
        # Checking move order
        if move_ord == 0:
            for i in range(0, len(self.black)):
                # If they are 1 y apart / avoid en passant possibility and taking backwards / avoid double executions
                # Checking if pressed y is on the figure
                if yp + 100 > self.black[i].pos[1] > yp + 15 and take_count == 0 and yp + 180 > y > yp + 95:
                    # Taking pawn on the right
                    if x > xp:
                        # If they are 1 x apart / ensuring they do not line on the same line (with and)
                        if xp + 100 > self.black[i].pos[0] > xp + 70 and self.black[i].opacity != 0:
                            # If a rook or a queen is taken
                            # Fixing slight change in position
                            if 7 < i < 10 or i == 12:
                                if self.king_spec == 0:
                                    name.pos_hint = {"x": self.black[i].pos[0] / Window.size[0],
                                                     "y": (self.black[i].pos[1] - 9) / Window.size[1]}
                                    name.pos = (self.black[i].pos[0], self.black[i].pos[1] - 9)
                                    self.black[i].opacity = 0
                                    self.black[i].size_hint = 0, 0
                                    take_count = 1
                                    move_ord = 1
                            # King is taken
                            elif i == 15:
                                self.check = 0
                                taken_piece = self.black[i]
                                move_ord = 1
                            # If pawn is taken
                            else:
                                if self.king_spec == 0:
                                    name.pos_hint = {"x": self.black[i].pos[0] / Window.size[0],
                                                     "y": self.black[i].pos[1] / Window.size[1]}
                                    name.pos = (self.black[i].pos[0], self.black[i].pos[1])
                                    self.black[i].opacity = 0
                                    self.black[i].size_hint = 0, 0
                                    take_count = 1
                                    move_ord = 1
                    # Taking pawn on the left
                    else:
                        if xp - 100 < self.black[i].pos[0] < xp - 70 and self.black[i].opacity != 0:
                            if 7 < i < 10 or i == 12:
                                if self.king_spec == 0:
                                    name.pos_hint = {"x": self.black[i].pos[0] / Window.size[0],
                                                     "y": (self.black[i].pos[1] - 9) / Window.size[1]}
                                    name.pos = (self.black[i].pos[0], self.black[i].pos[1] - 9)
                                    self.black[i].opacity = 0
                                    self.black[i].size_hint = 0, 0
                                    take_count = 1
                                    move_ord = 1
                            elif i == 15:
                                self.check = 0
                                taken_piece = self.black[i]
                                move_ord = 1
                            else:
                                if self.king_spec == 0:
                                    name.pos_hint = {"x": self.black[i].pos[0] / Window.size[0],
                                                     "y": self.black[i].pos[1] / Window.size[1]}
                                    name.pos = (self.black[i].pos[0], self.black[i].pos[1])
                                    self.black[i].opacity = 0
                                    self.black[i].size_hint = 0, 0
                                    take_count = 1
                                    move_ord = 1

        else:
            for i in range(0, len(self.white)):
                if yp - 100 < self.white[i].pos[1] < yp - 15 and take_count == 0 and yp - 70 < y < yp + 10:
                    if x > xp:
                        if xp + 100 > self.white[i].pos[0] > xp + 70 and self.white[i].opacity != 0:
                            if 7 < i < 10:
                                if self.king_spec == 0:
                                    name.pos_hint = {"x": self.white[i].pos[0] / Window.size[0],
                                                     "y": (self.white[i].pos[1] - 9) / Window.size[1]}
                                    name.pos = (self.white[i].pos[0], self.white[i].pos[1] - 9)
                                    self.white[i].opacity = 0
                                    self.white[i].size_hint = 0, 0
                                    take_count = 1
                                    move_ord = 0
                            elif i == 15:
                                self.check = 0
                                taken_piece = self.white[i]
                                move_ord = 0
                            else:
                                if self.king_spec == 0:
                                    name.pos_hint = {"x": self.white[i].pos[0] / Window.size[0],
                                                     "y": (self.white[i].pos[1] / Window.size[1])}
                                    name.pos = (self.white[i].pos[0], self.white[i].pos[1])
                                    self.white[i].opacity = 0
                                    self.white[i].size_hint = 0, 0
                                    take_count = 1
                                    move_ord = 0
                    else:
                        if xp - 100 < self.white[i].pos[0] < xp - 70 and self.white[i].opacity != 0:
                            if 7 < i < 10:
                                if self.king_spec == 0:
                                    name.pos_hint = {"x": self.white[i].pos[0] / Window.size[0],
                                                     "y": (self.white[i].pos[1] - 9) / Window.size[1]}
                                    name.pos = (self.white[i].pos[0], self.white[i].pos[1] - 9)
                                    self.white[i].opacity = 0
                                    self.white[i].size_hint = 0, 0
                                    take_count = 1
                                    move_ord = 0
                            elif i == 15:
                                self.check = 0
                                taken_piece = self.white[i]
                                move_ord = 0
                            else:
                                if self.king_spec == 0:
                                    name.pos_hint = {"x": self.white[i].pos[0] / Window.size[0],
                                                     "y": (self.white[i].pos[1] / Window.size[1])}
                                    name.pos = (self.white[i].pos[0], self.white[i].pos[1])
                                    self.white[i].opacity = 0
                                    self.white[i].size_hint = 0, 0
                                    take_count = 1
                                    move_ord = 0

    def on_queening(self, text):
        global move_ord
        # Note: function is executed twice each time called
        if self.queen_allow != 0 and self.ids.queen_opt.text != "":
            if text == "Queen":
                if move_ord == 0:
                    self.all_figures[self.queen_allow - 1].background_normal = "images/wqueen.png"
                    self.all_figures[self.queen_allow - 1].background_down = "images/wqueen.png"
                else:
                    self.all_figures[self.queen_allow - 1].background_normal = "images/bqueen.png"
                    self.all_figures[self.queen_allow - 1].background_down = "images/bqueen.png"
                self.q_to[self.queen_allow - 1] = "Queen"

            elif text == "Rook":
                if move_ord == 0:
                    self.all_figures[self.queen_allow - 1].background_normal = "images/wrook.png"
                    self.all_figures[self.queen_allow - 1].background_down = "images/wrook.png"
                    self.all_figures[self.queen_allow - 1].pos_hint = {"top": 0.95}
                else:
                    self.all_figures[self.queen_allow - 1].background_normal = "images/brook.png"
                    self.all_figures[self.queen_allow - 1].background_down = "images/brook.png"
                    self.all_figures[self.queen_allow - 1].pos_hint = {"top": 0.18}
                self.q_to[self.queen_allow - 1] = "Rook"

            elif text == "Bishop":
                if move_ord == 0:
                    self.all_figures[self.queen_allow - 1].background_normal = "images/wbishop.png"
                    self.all_figures[self.queen_allow - 1].background_down = "images/wbishop.png"
                    self.all_figures[self.queen_allow - 1].pos_hint = \
                        {"x": self.all_figures[self.queen_allow - 1].pos[0] / Window.size[0],
                         "y": 0.825}
                else:
                    self.all_figures[self.queen_allow - 1].background_normal = "images/bbishop.png"
                    self.all_figures[self.queen_allow - 1].background_down = "images/bbishop.png"
                    self.all_figures[self.queen_allow - 1].pos_hint = \
                        {"x": self.all_figures[self.queen_allow - 1].pos[0] / Window.size[0],
                         "y": 0.055}

                self.q_to[self.queen_allow - 1] = "Bishop"

            elif text == "Knight":
                if move_ord == 0:
                    self.all_figures[self.queen_allow - 1].background_normal = "images/wknight.png"
                    self.all_figures[self.queen_allow - 1].background_down = "images/wknight.png"
                    self.all_figures[self.queen_allow - 1].pos_hint = \
                        {"x": self.all_figures[self.queen_allow - 1].pos[0] / Window.size[0],
                         "y": 0.825}
                else:
                    self.all_figures[self.queen_allow - 1].background_normal = "images/bknight.png"
                    self.all_figures[self.queen_allow - 1].background_down = "images/bknight.png"
                    self.all_figures[self.queen_allow - 1].pos_hint = \
                        {"x": self.all_figures[self.queen_allow - 1].pos[0] / Window.size[0] - 0.003,
                         "y": 0.055}
                self.q_to[self.queen_allow - 1] = "Knight"

            self.ids.queen_opt.text = ""
            self.ids.queen_opt.opacity = 0
            self.ids.queen_opt.pos_hint = {"x": 1, "y": 1}
            self.queen_allow = 0
            self.fix_move_order()
            self.move_order_buttons(move_ord)

    def pawn_overall(self, x, y, yp, xp, numb):
        global count, move_ord
        # Confirming touched figure
        # Checking count / ensuring pawn is moved
        if count > 0 and numb != 0 and numb < 17 and self.q_to[numb - 1] == "":
            # Loop for all pawns
            for i in range(0, len(self.pawns)):
                # If white is to move
                if move_ord == 0:
                    # Assuming pawns are distributed equally
                    if i < (len(self.pawns) / 2) and numb == i + 1:
                        if xp + 4 < x < xp + 90:
                            self.pawn_move(y, yp, xp, numb, self.pawns[i])
                        elif x < xp + 4 or x > xp + 90:
                            self.pawn_passant(x, yp, xp, self.pawns[i])
                            self.pawn_takes(x, y, yp, xp, self.pawns[i])

                else:
                    if i >= (len(self.pawns) / 2) and numb == i + 1:
                        if xp + 4 < x < xp + 90:
                            self.pawn_move(y, yp, xp, numb, self.pawns[i])
                        elif x < xp + 4 or x > xp + 90:
                            self.pawn_passant(x, yp, xp, self.pawns[i])
                            self.pawn_takes(x, y, yp, xp, self.pawns[i])

            # Queening fix
            if self.all_figures[numb - 1].pos[1] > 645 or self.all_figures[numb - 1].pos[1] < 45:
                self.ids.queen_opt.opacity = 1
                if move_ord == 1:
                    self.ids.queen_opt.pos_hint = {"x": self.all_figures[numb - 1].pos[0] / Window.size[0],
                                                   "y": self.all_figures[numb - 1].pos[1] / Window.size[1]}
                else:
                    self.ids.queen_opt.pos_hint = {"x": self.all_figures[numb - 1].pos[0] / Window.size[0],
                                                   "y": (self.all_figures[numb - 1].pos[1] + 5) / Window.size[1]}

                self.queen_allow = numb
                self.fix_move_order()

                if move_ord == 0:
                    self.ids.queen_opt.background_normal = 'images/wqpawn.png'
                    self.ids.queen_opt.background_down = 'images/wqpawn.png'
                else:
                    self.ids.queen_opt.background_normal = 'images/bqpawn.png'
                    self.ids.queen_opt.background_down = 'images/bqpawn.png'

    # Rook functions
    def rook_move(self, x, y, xp, yp, name, numb):
        global move_ord, block
        # Same functions apply to both black and white (unlike pawns)
        # fixing move order / if rook has not been moved
        if count > 0 and (xp + 4 < x < xp + 90 and yp + 3 < y < yp + 85):
            pass

        # Moving vertically
        elif count > 0 and xp + 4 < x < xp + 90:
            self.rook_block(x, y, xp, yp, "v")
            if block == 0:
                if y < 136:
                    name.pos_hint = {"top": 0.18}
                    name.pos = (xp, 48)
                elif y < 222:
                    name.pos_hint = {"top": 0.29}
                    name.pos = (xp, 135)
                elif y < 310:
                    name.pos_hint = {"top": 0.4}
                    name.pos = (xp, 224)
                elif y < 399:
                    name.pos_hint = {"top": 0.51}
                    name.pos = (xp, 312)
                elif y < 486:
                    name.pos_hint = {"top": 0.62}
                    name.pos = (xp, 400)
                elif y < 575:
                    name.pos_hint = {"top": 0.73}
                    name.pos = (xp, 488)
                elif y < 662:
                    name.pos_hint = {"top": 0.84}
                    name.pos = (xp, 576)
                elif y < 749:
                    name.pos_hint = {"top": 0.95}
                    name.pos = (xp, 664)

                # Called to check if rook_takes is possible
                self.fig_takes(name.pos[0], name.pos[1])

                self.fix_move_order()
                # Castle not possible anymore
                self.cast_allow[numb] = 1

                # If check then
                if self.check == 1:
                    name.pos_hint = {"center_x": (xp + 49) / Window.size[0], "top": (yp + 96) / Window.size[1]}
                    name.pos = (xp, yp)

        # Moving horizontally
        elif count > 0 and yp + 3 < y < yp + 85:
            self.rook_block(x, y, xp, yp, "h")
            if block == 0:
                if x < 140:
                    name.pos_hint = {"center_x": 0.082}
                    name.pos = (45.4, yp)
                elif x < 231:
                    name.pos_hint = {"center_x": 0.162}
                    name.pos = (137.4, yp)
                elif x < 320:
                    name.pos_hint = {"center_x": 0.241}
                    name.pos = (228, yp)
                elif x < 411:
                    name.pos_hint = {"center_x": 0.319}
                    name.pos = (317.9, yp)
                elif x < 502:
                    name.pos_hint = {"center_x": 0.395}
                    name.pos = (405, yp)
                elif x < 593:
                    name.pos_hint = {"center_x": 0.477}
                    name.pos = (499, yp)
                elif x < 681:
                    name.pos_hint = {"center_x": 0.556}
                    name.pos = (590, yp)
                elif x < 770:
                    name.pos_hint = {"center_x": 0.636}
                    name.pos = (682, yp)

                self.fig_takes(name.pos[0], name.pos[1])

                self.fix_move_order()
                self.cast_allow[numb] = 1

                # If check then
                if self.check == 1:
                    name.pos_hint = {"center_x": (xp + 49) / Window.size[0], "top": (yp + 96) / Window.size[1]}
                    name.pos = (xp, yp)

    # Takes process of figures (except pawns) is similar
    def fig_takes(self, xp, yp):
        global move_ord, take_count, taken_piece
        take_count = 0
        taken_piece = None
        if move_ord == 0:
            for i in range(0, len(self.black)):
                # Inequality is used instead of equality since rooks size and pos slightly differs from pawns
                if xp - 10 < self.black[i].pos[0] < xp + 10 and yp - 10 < self.black[i].pos[1] < yp + 10 \
                        and take_count == 0 and self.black[i].opacity != 0:
                    taken_piece = self.black[i]
                    take_count = 1
                    # Unless takes is a check
                    if self.black[i] != self.king32:
                        self.black[i].opacity = 0
                        self.black[i].size_hint = 0, 0
                    else:
                        self.check = 1

        else:
            for i in range(0, len(self.white)):
                if xp - 10 < self.white[i].pos[0] < xp + 10 and yp - 10 < self.white[i].pos[1] < yp + 10 \
                        and take_count == 0 and self.white[i].opacity != 0:
                    taken_piece = self.white[i]
                    take_count = 1
                    if self.white[i] != self.king31:
                        self.white[i].opacity = 0
                        self.white[i].size_hint = 0, 0
                    else:
                        self.check = 1

    # Shorten
    def rook_block(self, x, y, xp, yp, d):
        global block, move_ord
        block = 0
        if d == "v":
            if block == 0:
                # Checking if the figure is within rooks vertical range / if it lies in rooks path
                if move_ord == 0:
                    # White block is different to white and black
                    for i in range(0, len(self.white)):
                        if xp - 4 < self.white[i].pos[0] < xp + 90 and \
                                (y - 100 < self.white[i].pos[1] < yp or yp < self.white[i].pos[1] < y) \
                                and self.white[i].opacity != 0:
                            block = 1

                    for i in range(0, len(self.black)):
                        if xp - 4 < self.black[i].pos[0] < xp + 90 and \
                                (y < self.black[i].pos[1] < yp or yp < self.black[i].pos[1] < y - 100) \
                                and self.black[i].opacity != 0:
                            block = 1

                else:
                    for i in range(0, len(self.black)):
                        if xp - 4 < self.black[i].pos[0] < xp + 90 and \
                                (y - 100 < self.black[i].pos[1] < yp or yp < self.black[i].pos[1] < y) \
                                and self.black[i].opacity != 0:
                            block = 1

                    for i in range(0, len(self.white)):
                        if xp - 4 < self.white[i].pos[0] < xp + 90 and \
                                (y < self.white[i].pos[1] < yp or yp < self.white[i].pos[1] < y - 100) \
                                and self.white[i].opacity != 0:
                            block = 1

        elif d == "h":
            if block == 0:
                if move_ord == 0:
                    # Similar application in horizontal movement
                    for i in range(0, len(self.white)):
                        if yp - 15 < self.white[i].pos[1] < yp + 70 and \
                            (x - 95 < self.white[i].pos[0] < xp or xp < self.white[i].pos[0] < x) \
                                and self.white[i].opacity != 0 and block == 0:
                            block = 1

                    for i in range(0, len(self.black)):
                        if yp - 15 < self.black[i].pos[1] < yp + 70 and \
                            (x < self.black[i].pos[0] < xp or xp < self.black[i].pos[0] < x - 90) \
                                and self.black[i].opacity != 0 and block == 0:
                            block = 1

                else:
                    for i in range(0, len(self.black)):
                        if yp - 15 < self.black[i].pos[1] < yp + 70 and \
                            (x - 95 < self.black[i].pos[0] < xp or xp < self.black[i].pos[0] < x) \
                                and self.black[i].opacity != 0 and block == 0:
                            block = 1

                    for i in range(0, len(self.white)):
                        if yp - 15 < self.white[i].pos[1] < yp + 70 and \
                            (x < self.white[i].pos[0] < xp or xp < self.white[i].pos[0] < x - 90) \
                                and self.white[i].opacity != 0 and block == 0:
                            block = 1

    def rook_overall(self, x, y, xp, yp, numb):
        global count, allow
        if count > 0 and (16 < numb < 21 or allow or self.q_to[numb - 1] == "Rook" or self.q_to[numb - 1] == "Queen"):
            self.rook_move(x, y, xp, yp, self.all_figures[numb - 1], numb)

    def bishop_move(self, x, y, xp, yp, name, numb):
        # "1" is put first for black squared bishops, "2" for white squared bishops
        # This function is also used by queens
        self.a = "1"
        self.b = "2"
        # Acting according to bishops position color
        if numb == 21 or numb == 24:
            pass
        elif numb == 22 or numb == 23:
            self.a, self.b = self.b, self.a

        # Detecting queens position color
        elif numb == 25 or numb == 26 or self.q_to[numb - 1] == "Bishop" or self.q_to[numb - 1] == "Queen":
            self.detect_cur_square(name.pos[1], name)
            if self.square_col == "w":
                self.a, self.b = self.b, self.a
            elif self.square_col == "b":
                pass

        if y < 136:
            self.bishop_move_row(x, xp, yp, 0.055, name, self.a)
        elif y < 222:
            self.bishop_move_row(x, xp, yp, 0.1649, name, self.b)
        elif y < 310:
            self.bishop_move_row(x, xp, yp, 0.275, name, self.a)
        elif y < 399:
            self.bishop_move_row(x, xp, yp, 0.385, name, self.b)
        elif y < 486:
            self.bishop_move_row(x, xp, yp, 0.495, name, self.a)
        elif y < 575:
            self.bishop_move_row(x, xp, yp, 0.605, name, self.b)
        elif y < 662:
            self.bishop_move_row(x, xp, yp, 0.715, name, self.a)
        elif y < 749:
            self.bishop_move_row(x, xp, yp, 0.825, name, self.b)

        self.bishop_block(xp, yp,
                          float(name.pos_hint["x"]) * Window.size[0], float(name.pos_hint["y"]) * Window.size[1])
        # If block exists bishop is set to its previous position
        if block == 1:
            name.pos_hint = {"x": xp / Window.size[0], "y": yp / Window.size[1]}
        else:
            self.move_based_block(xp, yp,
                                  float(name.pos_hint["x"]) * Window.size[0],
                                  float(name.pos_hint["y"]) * Window.size[1],
                                  name)
            if block == 1:
                name.pos_hint = {"x": xp / Window.size[0], "y": yp / Window.size[1]}

        if numb == 26:
            self.queen_pos = (name.pos_hint["x"] * Window.size[0], name.pos_hint["y"] * Window.size[1])
        elif numb == 25:
            self.queen_pos1 = (name.pos_hint["x"] * Window.size[0], name.pos_hint["y"] * Window.size[1])

        # Fixing move order
        if xp / Window.size[0] != name.pos_hint["x"] or yp / Window.size[1] != name.pos_hint["y"]:
            name.pos = (name.pos_hint["x"] * Window.size[0], name.pos_hint["y"] * Window.size[1])
            self.fix_move_order()
            # If check then
            if self.check == 1:
                name.pos_hint = {"x": xp / Window.size[0], "y": yp / Window.size[1]}
                name.pos = (xp, yp)

    def bishop_move_row(self, x, xp, yp, pre_y, name, row):
        # Bishop can move to only same colored squares
        if row == "1":
            if 52 < x < 143:
                name.pos_hint = {"x": 0.039, "y": pre_y}
            elif 232 < x < 323:
                name.pos_hint = {"x": 0.198, "y": pre_y}
            elif 412 < x < 504:
                name.pos_hint = {"x": 0.357, "y": pre_y}
            elif 594 < x < 685:
                name.pos_hint = {"x": 0.5135, "y": pre_y}

        elif row == "2":
            if 141 < x < 234:
                name.pos_hint = {"x": 0.119, "y": pre_y}
            elif 322 < x < 414:
                name.pos_hint = {"x": 0.276, "y": pre_y}
            elif 503 < x < 596:
                name.pos_hint = {"x": 0.434, "y": pre_y}
            elif 684 < x < 775:
                name.pos_hint = {"x": 0.593, "y": pre_y}

        # Eliminating all illegal moves using ratio
        # ratio of the change in position is always very similar in bishop moves (around 1.03 here)
        try:
            if 0.8 < (abs(float(name.pos_hint["x"]) * Window.size[0] - xp)) / \
                    (abs(float(name.pos_hint["y"]) * Window.size[1] - yp)) < 2:
                # Checking the possibility of bishop takes
                # Takes is only possible if move is legal
                self.fig_takes(float(name.pos_hint["x"]) * Window.size[0],
                               float(name.pos_hint["y"]) * Window.size[1])
            else:
                name.pos_hint = {"x": xp / Window.size[0], "y": yp / Window.size[1]}

        except ZeroDivisionError:
            name.pos_hint = {"x": xp / Window.size[0], "y": yp / Window.size[1]}

    def bishop_block(self, xp, yp, cur_x, cur_y):
        # Bishop_block function identifies any figures lying in bishops path
        # A rectangle is drawn with cur_x - xp, cur_y - yp as its lengths
        global block, move_ord, taken_piece
        block = 0
        # Moving up right
        if cur_y > yp and cur_x > xp:
            cur_y -= 10
            cur_x -= 10
            for i in range(0, len(self.all_figures)):
                # If Pieces lie in this rectangle considered as a bishop move block == 1
                if yp < self.all_figures[i].pos[1] < cur_y and xp < self.all_figures[i].pos[0] < cur_x:
                    try:
                        if 0.8 < (abs(self.all_figures[i].pos[0] - xp)) / (abs(self.all_figures[i].pos[1] - yp)) < 1.2 \
                                and self.all_figures[i].opacity != 0:
                            # In case of block takes is not possible
                            if taken_piece is not None:
                                taken_piece.size_hint = 0.085, 0.12
                                taken_piece.opacity = 1
                            block = 1
                    except ZeroDivisionError:
                        pass

        # Up left
        elif cur_y > yp and cur_x < xp:
            for i in range(0, len(self.all_figures)):
                if yp < self.all_figures[i].pos[1] < cur_y and cur_x < self.all_figures[i].pos[0] < xp:
                    try:
                        if 0.8 < (abs(self.all_figures[i].pos[0] - xp)) / (abs(self.all_figures[i].pos[1] - yp)) < 1.2 \
                                and self.all_figures[i].opacity != 0:
                            if taken_piece is not None:
                                taken_piece.size_hint = 0.085, 0.12
                                taken_piece.opacity = 1
                            block = 1
                    except ZeroDivisionError:
                        pass

        # Down right
        elif cur_y < yp and cur_x > xp:
            for i in range(0, len(self.all_figures)):
                if cur_y < self.all_figures[i].pos[1] < yp and xp < self.all_figures[i].pos[0] < cur_x:
                    try:
                        if 0.8 < (abs(self.all_figures[i].pos[0] - xp)) / (abs(self.all_figures[i].pos[1] - yp)) < 1.2 \
                                and self.all_figures[i].opacity != 0:
                            if taken_piece is not None:
                                taken_piece.size_hint = 0.085, 0.12
                                taken_piece.opacity = 1
                            block = 1
                    except ZeroDivisionError:
                        pass

        # Down left
        elif cur_y < yp and cur_x < xp:
            for i in range(0, len(self.all_figures)):
                if cur_y < self.all_figures[i].pos[1] < yp and cur_x < self.all_figures[i].pos[0] < xp:
                    try:
                        if 0.8 < (abs(self.all_figures[i].pos[0] - xp)) / (abs(self.all_figures[i].pos[1] - yp)) < 1.2 \
                                and self.all_figures[i].opacity != 0:
                            if taken_piece is not None:
                                taken_piece.size_hint = 0.085, 0.12
                                taken_piece.opacity = 1
                            block = 1
                    except ZeroDivisionError:
                        pass

    def bishop_overall(self, x, y, xp, yp, numb):
        global count, allow
        if count > 0 and (20 < numb < 25 or allow or self.q_to[numb - 1] == "Bishop" or self.q_to[numb - 1] == "Queen"):
            self.bishop_move(x, y, xp, yp, self.all_figures[numb - 1], numb)

    def detect_cur_square(self, yp, name):
        # Used for queens
        self.square_col = 0
        # For odd rows
        if 40 < yp < 120 or 200 < yp < 240 or 380 < yp < 420 or 556 < yp < 596:
            if 30 < name.pos[0] < 70:
                self.square_col = "b"
            elif 200 < name.pos[0] < 240:
                self.square_col = "b"
            elif 380 < name.pos[0] < 420:
                self.square_col = "b"
            elif 570 < name.pos[0] < 610:
                self.square_col = "b"
            elif 120 < name.pos[0] < 160:
                self.square_col = "w"
            elif 300 < name.pos[0] < 340:
                self.square_col = "w"
            elif 480 < name.pos[0] < 520:
                self.square_col = "w"
            elif 660 < name.pos[0] < 700:
                self.square_col = "w"

        # For even rows
        elif 120 < yp < 160 or 290 < yp < 430 or 468 < yp < 508 or 644 < yp < 684:
            if 30 < name.pos[0] < 70:
                self.square_col = "w"
            elif 200 < name.pos[0] < 240:
                self.square_col = "w"
            elif 380 < name.pos[0] < 420:
                self.square_col = "w"
            elif 570 < name.pos[0] < 610:
                self.square_col = "w"
            elif 120 < name.pos[0] < 160:
                self.square_col = "b"
            elif 300 < name.pos[0] < 340:
                self.square_col = "b"
            elif 480 < name.pos[0] < 520:
                self.square_col = "b"
            elif 660 < name.pos[0] < 700:
                self.square_col = "b"

    def queen_overall(self, x, y, xp, yp, numb):
        global move_ord, count, allow
        allow = True
        self.move_order = move_ord
        if count > 0 and (24 < numb < 27 or self.q_to[numb - 1] == "Queen"):
            self.rook_overall(x, y, xp, yp, numb)
            # If made move was not a rook move
            if self.move_order == move_ord:
                # Adjusting pos_hint assignment to those in bishops
                self.all_figures[numb - 1].pos_hint = {"x": xp / Window.size[0], "y": yp / Window.size[1]}
                self.bishop_overall(x, y, xp, yp, numb)

    def knight_move(self, x, y, xp, yp, name):
        # Moving up or down
        if yp + 180 < y < yp + 270:
            if xp - 86 < x < xp + 6:
                name.pos_hint = {"x": (xp - 90.5) / Window.size[0], "y": (yp + 176) / Window.size[1]}
            elif xp + 95 < x < xp + 187:
                name.pos_hint = {"x": (xp + 90.5) / Window.size[0], "y": (yp + 176) / Window.size[1]}
        elif yp - 172 < y < yp - 82:
            if xp - 86 < x < xp + 6:
                name.pos_hint = {"x": (xp - 90.5) / Window.size[0], "y": (yp - 176) / Window.size[1]}
            elif xp + 95 < x < xp + 187:
                name.pos_hint = {"x": (xp + 90.5) / Window.size[0], "y": (yp - 176) / Window.size[1]}
        # Left or right
        elif yp + 112 < y < yp + 202:
            # Right
            if xp + 184 < x < xp + 279:
                name.pos_hint = {"x": (xp + 181) / Window.size[0], "y": (yp + 88) / Window.size[1]}
            # Left
            elif xp - 177 < x < xp - 93:
                name.pos_hint = {"x": (xp - 181) / Window.size[0], "y": (yp + 88) / Window.size[1]}
        elif yp - 65 < y < yp + 28:
            if xp + 184 < x < xp + 279:
                name.pos_hint = {"x": (xp + 181) / Window.size[0], "y": (yp - 88) / Window.size[1]}
            elif xp - 177 < x < xp - 93:
                name.pos_hint = {"x": (xp - 181) / Window.size[0], "y": (yp - 88) / Window.size[1]}

        # Checking the possibility of takes
        self.fig_takes(name.pos_hint["x"] * Window.size[0], name.pos_hint["y"] * Window.size[1])
        # Checking the possibility of block
        self.move_based_block(xp, yp, name.pos_hint["x"] * Window.size[0], name.pos_hint["y"] * Window.size[1], name)
        if xp / Window.size[0] != name.pos_hint["x"] or yp / Window.size[1] != name.pos_hint["y"]:
            name.pos = (name.pos_hint["x"] * Window.size[0], name.pos_hint["y"] * Window.size[1])
            self.fix_move_order()
            # If check then
            if self.check == 1:
                name.pos_hint = {"x": xp / Window.size[0], "y": yp / Window.size[1]}
                name.pos = (xp, yp)

    # Applies to kings and knights
    def move_based_block(self, xp, yp, cur_x, cur_y, name):
        global block
        block = 0
        # Checking if there is a figure in the moved square
        if move_ord == 0:
            for i in range(0, len(self.white)):
                if cur_x - 10 < self.white[i].pos[0] < cur_x + 10:
                    if cur_y - 10 < self.white[i].pos[1] < cur_y + 10 and self.white[i].opacity != 0:
                        name.pos_hint = {"x": xp / Window.size[0], "y": yp / Window.size[1]}
                        block = 1

        elif move_ord == 1:
            for i in range(0, len(self.black)):
                if cur_x - 10 < self.black[i].pos[0] < cur_x + 10 and self.black[i].opacity != 0:
                    if cur_y - 10 < self.black[i].pos[1] < cur_y + 10:
                        name.pos_hint = {"x": xp / Window.size[0], "y": yp / Window.size[1]}
                        block = 1

    def knight_overall(self, x, y, xp, yp, numb):
        # Applies to knights only
        if 26 < numb < 31 or self.q_to[numb - 1] == "Knight":
            self.knight_move(x, y, xp, yp, self.all_figures[numb - 1])

    def king_move(self, x, y, xp, yp, name, numb):
        if pawn_n > 30:
            # Moving left or right
            if yp + 4 < y < yp + 94:
                # Same pos
                if xp + 2 < x < xp + 95:
                    pass
                elif xp - 90 < x <= xp + 2:
                    name.pos_hint = {"x": (xp - 90.5) / Window.size[0], "y": yp / Window.size[1]}
                elif xp + 93 < x < xp + 185:
                    name.pos_hint = {"x": (xp + 90.5) / Window.size[0], "y": yp / Window.size[1]}

            # Move up
            elif yp + 92 < y < yp + 181:
                # Just up
                if xp + 2 < x < xp + 95:
                    name.pos_hint = {"x": xp / Window.size[0], "y": (yp + 88) / Window.size[1]}
                # Up left
                elif xp - 90 < x <= xp + 2:
                    name.pos_hint = {"x": (xp - 90.5) / Window.size[0], "y": (yp + 88) / Window.size[1]}
                # Up right
                elif xp + 93 < x < xp + 185:
                    name.pos_hint = {"x": (xp + 90.5) / Window.size[0], "y": (yp + 88) / Window.size[1]}
            # Move down
            elif yp - 91 < y < yp:
                if xp + 2 < x < xp + 95:
                    name.pos_hint = {"x": xp / Window.size[0], "y": (yp - 88) / Window.size[1]}
                elif xp - 90 < x <= xp + 2:
                    name.pos_hint = {"x": (xp - 90.5) / Window.size[0], "y": (yp - 88) / Window.size[1]}
                elif xp + 93 < x < xp + 185:
                    name.pos_hint = {"x": (xp + 90.5) / Window.size[0], "y": (yp - 88) / Window.size[1]}

            # Check if castle is possible
            self.castle_check(x, y, name, numb)
            # Takes and block functions are similar to other pieces
            self.fig_takes(name.pos_hint["x"] * Window.size[0], name.pos_hint["y"] * Window.size[1])
            self.move_based_block(xp, yp, name.pos_hint["x"] * Window.size[0], name.pos_hint["y"] * Window.size[1], name)

            # Fixing move order
            if xp / Window.size[0] != name.pos_hint["x"] or yp / Window.size[1] != name.pos_hint["y"]:
                name.pos = (name.pos_hint["x"] * Window.size[0], name.pos_hint["y"] * Window.size[1])
                self.fix_move_order()
                # Castle not possible anymore
                self.cast_allow[numb] = 1

    def castle_check(self, x, y, name, numb):
        global move_ord, block
        if move_ord == 0:
            # Short Castle
            if 594 < x < 685 and 49 < y < 138:
                # Checking if king / rook has been moved
                if self.cast_allow[numb] + self.cast_allow[18] == 0:
                    # Checking if the line is empty / through a rook block
                    self.rook_block(507, 100, self.rook18.pos[0], self.rook18.pos[1], "h")
                    if block == 0:
                        name.pos_hint = {"x": 0.513, "y": 0.055}
                        self.rook18.pos_hint = {"center_x": 0.477, "top": 0.18}
                        self.rook18.pos = (0.477 * Window.size[0] - 49, 0.18 * Window.size[1] - 96)

            # Long Castle
            elif 232 < x < 323 and 49 < y < 138:
                if self.cast_allow[numb] + self.cast_allow[17] == 0:
                    self.rook_block(319, 92, self.rook17.pos[0], self.rook17.pos[1], "h")
                    if block == 0:
                        name.pos_hint = {"x": 0.198, "y": 0.055}
                        self.rook17.pos_hint = {"center_x": 0.319, "top": 0.18}
                        self.rook17.pos = (0.319 * Window.size[0] - 49, 0.18 * Window.size[1] - 96)
        else:
            # For black king
            if 594 < x < 685 and 662 < y < 752:
                if self.cast_allow[numb] + self.cast_allow[20] == 0:
                    self.rook_block(507, 100, self.rook20.pos[0], self.rook20.pos[1], "h")
                    if block == 0:
                        name.pos_hint = {"x": 0.513, "y": 0.825}
                        self.rook20.pos_hint = {"center_x": 0.477, "top": 0.95}
                        self.rook20.pos = (0.477 * Window.size[0] - 49, 0.95 * Window.size[1] - 96)

            elif 232 < x < 323 and 662 < y < 752:
                if self.cast_allow[numb] + self.cast_allow[19] == 0:
                    self.rook_block(319, 92, self.rook19.pos[0], self.rook19.pos[1], "h")
                    if block == 0:
                        name.pos_hint = {"x": 0.198, "y": 0.825}
                        self.rook19.pos_hint = {"center_x": 0.319, "top": 0.95}
                        self.rook19.pos = (0.319 * Window.size[0] - 49, 0.95 * Window.size[1] - 96)

    def check_assign(self, name):
        global block, taken_piece
        if taken_piece == name and block == 0:

            self.check = 1
            self.ids.check_col.opacity = 1
            self.ids.check_col.pos_hint = {"x": name.pos[0] / Window.size[0] - 0.017,
                                           "y": name.pos[1] / Window.size[1] - 0.02}
        else:
            self.check = 0
            taken_piece = None

    def check_detect(self, name):
        global move_ord, taken_piece, block
        taken_piece = None
        if move_ord == 0:
            name = self.king31
            self.x_cor = name.pos_hint["x"] * Window.size[0] + 34
            self.y_cor = name.pos_hint["y"] * Window.size[1] + 46
            self.fix_move_order()
            for i in range(len(self.black)):
                if self.black[i].opacity != 0:
                    # For pawns
                    if i < 8 and taken_piece != name:
                        if self.q_to[i + 8] == "":
                            self.king_spec = 1
                            block = 0
                            taken_piece = None
                            self.pawn_takes(self.x_cor, self.y_cor, self.black[i].pos[1],
                                            self.black[i].pos[0], self.black[i])

                            self.check_assign(name)
                            self.king_spec = 0

                        # Queened pawns
                        elif self.q_to[i + 8] == "Rook":
                            taken_piece = None
                            self.rook_move(self.x_cor, self.y_cor, self.black[i].pos[0], self.black[i].pos[1],
                                           self.black[i], i + 11)
                            self.check_assign(name)

                        elif self.q_to[i + 8] == "Bishop":
                            taken_piece = None
                            self.bishop_move(self.x_cor, self.y_cor, self.black[i].pos_hint["x"] * Window.size[0],
                                             self.black[i].pos_hint["y"] * Window.size[1], self.black[i], i + 13)

                            self.check_assign(name)

                        elif self.q_to[i + 8] == "Queen":
                            taken_piece = None
                            self.rook_move(self.x_cor, self.y_cor, self.black[i].pos[0], self.black[i].pos[1],
                                           self.black[i], i + 14)

                            if self.check == 0:
                                taken_piece = None
                                self.black[i].pos_hint = {"x": self.black[i].pos[0] / Window.size[0],
                                                          "y": self.black[i].pos[1] / Window.size[1]}
                                self.bishop_move(self.x_cor, self.y_cor, self.black[i].pos_hint["x"] * Window.size[0],
                                                 self.black[i].pos_hint["y"] * Window.size[1], self.black[i], i + 14)

                            self.check_assign(name)

                        elif self.q_to[i + 8] == "Knight":
                            block = 0
                            taken_piece = None
                            self.knight_move(self.x_cor, self.y_cor, self.black[i].pos_hint["x"] * Window.size[0],
                                             self.black[i].pos_hint["y"] * Window.size[1], self.black[i])

                            self.check_assign(name)

                    # For rooks
                    if 7 < i < 10 and taken_piece != name:
                        taken_piece = None
                        self.rook_move(self.x_cor, self.y_cor, self.black[i].pos[0], self.black[i].pos[1],
                                       self.black[i], i + 11)
                        self.check_assign(name)

                    # For bishops
                    if 9 < i < 12 and taken_piece != name:
                        taken_piece = None
                        self.bishop_move(self.x_cor, self.y_cor, self.black[i].pos_hint["x"] * Window.size[0],
                                         self.black[i].pos_hint["y"] * Window.size[1], self.black[i], i + 13)

                        self.check_assign(name)

                    # For queen
                    if i == 12 and taken_piece != name:
                        taken_piece = None
                        self.rook_move(self.x_cor, self.y_cor, self.black[i].pos[0], self.black[i].pos[1],
                                       self.black[i], i + 14)

                        if self.check == 0:
                            taken_piece = None
                            self.black[i].pos_hint = {"x": self.black[i].pos[0] / Window.size[0],
                                                      "y": self.black[i].pos[1] / Window.size[1]}
                            self.bishop_move(self.x_cor, self.y_cor, self.black[i].pos_hint["x"] * Window.size[0],
                                             self.black[i].pos_hint["y"] * Window.size[1], self.black[i], i + 14)

                        self.check_assign(name)

                    # For knights
                    if i > 12 and taken_piece != name:
                        block = 0
                        taken_piece = None
                        self.knight_move(self.x_cor, self.y_cor, self.black[i].pos_hint["x"] * Window.size[0],
                                         self.black[i].pos_hint["y"] * Window.size[1], self.black[i])

                        self.check_assign(name)

        elif move_ord == 1:
            name = self.king32
            self.x_cor = name.pos_hint["x"] * Window.size[0] + 34
            self.y_cor = name.pos_hint["y"] * Window.size[1] + 46
            self.fix_move_order()
            for i in range(len(self.white)):
                if self.white[i].opacity != 0:
                    if i < 8 and taken_piece != name:
                        if self.q_to[i] == "":
                            self.king_spec = 1
                            block = 0
                            taken_piece = None
                            self.pawn_takes(self.x_cor, self.y_cor, self.white[i].pos[1],
                                            self.white[i].pos[0], self.white[i])
                            self.check_assign(name)
                            self.king_spec = 0

                        # Queened pawns
                        elif self.q_to[i] == "Rook":
                            taken_piece = None
                            self.rook_move(self.x_cor, self.y_cor, self.white[i].pos[0], self.white[i].pos[1],
                                           self.white[i], i + 11)
                            self.check_assign(name)

                        elif self.q_to[i] == "Bishop":
                            taken_piece = None
                            self.bishop_move(self.x_cor, self.y_cor, self.white[i].pos_hint["x"] * Window.size[0],
                                             self.white[i].pos_hint["y"] * Window.size[1], self.white[i], i + 13)

                            self.check_assign(name)

                        elif self.q_to[i] == "Queen":
                            taken_piece = None
                            self.rook_move(self.x_cor, self.y_cor, self.white[i].pos[0], self.white[i].pos[1],
                                           self.white[i], i + 14)

                            if self.check == 0:
                                taken_piece = None
                                self.white[i].pos_hint = {"x": self.white[i].pos[0] / Window.size[0],
                                                          "y": self.white[i].pos[1] / Window.size[1]}
                                self.bishop_move(self.x_cor, self.y_cor, self.white[i].pos_hint["x"] * Window.size[0],
                                                 self.white[i].pos_hint["y"] * Window.size[1], self.white[i], i + 14)

                            self.check_assign(name)

                        elif self.q_to[i] == "Knight":
                            block = 0
                            taken_piece = None
                            self.knight_move(self.x_cor, self.y_cor, self.white[i].pos[0],
                                             self.white[i].pos[1], self.white[i])

                            self.check_assign(name)

                    if 7 < i < 10 and taken_piece != name:
                        taken_piece = None
                        self.rook_move(self.x_cor, self.y_cor, self.white[i].pos[0], self.white[i].pos[1],
                                       self.white[i], i + 9)

                        self.check_assign(name)

                    if 9 < i < 12 and taken_piece != name:
                        taken_piece = None
                        self.bishop_move(self.x_cor, self.y_cor, self.white[i].pos_hint["x"] * Window.size[0],
                                         self.white[i].pos_hint["y"] * Window.size[1], self.white[i], i + 11)

                        self.check_assign(name)

                    if i == 12 and taken_piece != name:
                        taken_piece = None
                        self.rook_move(self.x_cor, self.y_cor, self.white[i].pos[0], self.white[i].pos[1],
                                       self.white[i], i + 13)

                        if taken_piece != name:
                            taken_piece = None
                            self.white[i].pos_hint = {"x": self.white[i].pos[0] / Window.size[0],
                                                      "y": self.white[i].pos[1] / Window.size[1]}
                            self.bishop_move(self.x_cor, self.y_cor, self.white[i].pos_hint["x"] * Window.size[0],
                                             self.white[i].pos_hint["y"] * Window.size[1], self.white[i], i + 13)

                        self.check_assign(name)

                    if i > 12 and taken_piece != name:
                        block = 0
                        taken_piece = None
                        self.knight_move(self.x_cor, self.y_cor, self.white[i].pos_hint["x"] * Window.size[0],
                                         self.white[i].pos_hint["y"] * Window.size[1], self.white[i])

                        self.check_assign(name)

        if self.check == 0:
            self.ids.check_col.opacity = 0
            self.fix_move_order()

        name.size_hint = 0.08, 0.12

    def illegal_check(self):
        self.fix_move_order()

        self.check_detect(self.king32)
        if self.check == 1:
            self.act_current_pos("r")
            self.ids.check_col.opacity = 1
            if move_ord == 1:
                self.ids.check_col.pos_hint = {"x": self.king32.pos[0] / Window.size[0] - 0.017,
                                               "y": self.king32.pos[1] / Window.size[1] - 0.02}
            else:
                self.ids.check_col.pos_hint = {"x": self.king31.pos[0] / Window.size[0] - 0.017,
                                               "y": self.king31.pos[1] / Window.size[1] - 0.02}

            self.fix_move_order()

        else:
            self.check = 0

        self.fix_move_order()

    def act_current_pos(self, d):
        # Saving / Retrieving board positions
        if d == "s":
            for i in range(len(self.all_figures)):
                self.current_opacity[i] = self.all_figures[i].opacity
                self.current_pos[i][0] = self.all_figures[i].pos[0]
                self.current_pos[i][1] = self.all_figures[i].pos[1]

            for i in range(4):
                self.cast_allow[i] = self.cast_allow[i + 17]
            self.cast_allow[4] = self.cast_allow[31]
            self.cast_allow[5] = self.cast_allow[32]

        elif d == "r":
            for i in range(len(self.all_figures)):
                self.all_figures[i].opacity = self.current_opacity[i]
                if i < 30 and self.all_figures[i].opacity == 1 and self.all_figures[i].size_hint != (0.085, 0.12):
                    self.all_figures[i].size_hint = (0.085, 0.12)

                self.all_figures[i].pos = self.current_pos[i]
                self.all_figures[i].pos_hint = {"x": self.current_pos[i][0] / Window.size[0],
                                                "y": self.current_pos[i][1] / Window.size[1]}

            for i in range(4):
                self.cast_allow[i + 17] = self.cast_allow[i]
            self.cast_allow[31] = self.cast_allow[4]
            self.cast_allow[32] = self.cast_allow[5]

        # Loading starting position from txt.file
        elif d == "load_start":
            global move_ord
            f = open("starting_position.txt", "r")
            self.count = 0
            for line in f:
                if self.count < 32:
                    self.all_figures[self.count].pos = list(line.strip().split())
                    self.all_figures[self.count].pos_hint = {"x": self.all_figures[self.count].pos[0] / Window.size[0],
                                                             "y": self.all_figures[self.count].pos[1] / Window.size[1]}
                    self.all_figures[self.count].opacity = 1
                    if self.count < 30:
                        self.all_figures[self.count].size_hint = (0.085, 0.12)
                    self.count += 1

            move_ord = 0
            for i in range(33):
                self.cast_allow[i] = 0
            self.move_order_buttons(move_ord)
            self.ids.check_col.opacity = 0
            f.close()

    # Identify touched figure
    def detect_fig(self, fig_num, fig):
        global pawn_n, touch_yp, touch_xp, count, move_ord
        # If the piece exists
        if fig.opacity != 0:
            # Checking the move order
            if move_ord == 0 and (fig_num < 9 or 16 < fig_num < 19 or 20 < fig_num < 23
                                  or fig_num == 25 or 26 < fig_num < 29 or fig_num == 31):
                pawn_n = fig_num
                fig.opacity = 0.5
                count = 1
                touch_xp = fig.pos[0]
                touch_yp = fig.pos[1]
            elif move_ord == 1 and (8 < fig_num < 17 or 18 < fig_num < 21 or 22 < fig_num < 25
                                    or fig_num == 26 or 28 < fig_num < 31 or fig_num == 32):
                pawn_n = fig_num
                fig.opacity = 0.5
                count = 1
                touch_xp = fig.pos[0]
                touch_yp = fig.pos[1]

    def fix_move_order(self):
        global move_ord
        move_ord = abs(move_ord - 1)

    def move_order_buttons(self, mov):
        # Move order displaying buttons
        if mov == 0:
            self.ids.whitemove.opacity = 1
            self.ids.blackmove.opacity = 0.2
        else:
            self.ids.whitemove.opacity = 0.2
            self.ids.blackmove.opacity = 1

    # Main function
    def on_touch_up(self, touch):
        global count, touch_yp, touch_xp, pawn_n, move_ord, en_passant, taken_piece, allow
        self.act_current_pos("s")
        # Overall figure functions that execute all the necessary functions respectively
        if count > 0:
            # Ensuring pieces are moved within the board
            if 36 < touch.x < 789 and 37 < touch.y < 766:
                self.check = 0
                self.current_move = move_ord
                self.pawn_overall(touch.x, touch.y, touch_yp, touch_xp, pawn_n)
                self.rook_overall(touch.x, touch.y, touch_xp, touch_yp, pawn_n)
                self.bishop_overall(touch.x, touch.y, touch_xp, touch_yp, pawn_n)
                self.queen_overall(touch.x, touch.y, touch_xp, touch_yp, pawn_n)
                self.knight_overall(touch.x, touch.y, touch_xp, touch_yp, pawn_n)
                self.king_move(touch.x, touch.y, touch_xp, touch_yp, self.all_figures[pawn_n - 1], pawn_n)

                self.illegal_check()
                if self.check == 0:
                    self.check_detect(self.king31)
                    # Applying sound effects
                    if self.sound_volume == 1:
                        if self.check == 0 and move_ord != self.current_move:
                            self.move_cl.play()
                        elif self.check == 1 and move_ord != self.current_move:
                            self.check_sd.play()

        # Fixing opacity
        for i in range(len(self.all_figures)):
            if self.all_figures[i].opacity == 0.5:
                self.all_figures[i].opacity = 1
        self.move_order_buttons(move_ord)

        count = 0
        pawn_n = 0
        if block == 0 and count > 0:
            taken_piece = None
        allow = False
        # Fixing en passant rule
        if (en_passant < 9 and move_ord == 0) or (en_passant >= 9 and move_ord == 1):
            en_passant = 0
        self.ids.bmenu.opacity = 1

    def bmenu_opacity(self):
        self.ids.bmenu.opacity = 0.5

    def sound_control(self):
        self.sound_volume = abs(self.sound_volume - 1)
        if self.sound_volume == 1:
            self.ts_on.play()
            self.ids.sound_cont.background_normal = "images/sound_on.png"
            self.ids.sound_cont.background_down = "images/sound_on.png"
        else:
            self.ids.sound_cont.background_normal = "images/sound_off.png"
            self.ids.sound_cont.background_down = "images/sound_off.png"


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("kv")
screens = [Entry(name="Ent"), ChessBoard(name="CH"), Clicker(name="clk")]

wm = WindowManager()
for screen in screens:
    wm.add_widget(screen)


class ChessApp(App):
    def build(self):
        return wm


if __name__ == "__main__":
    ChessApp().run()
