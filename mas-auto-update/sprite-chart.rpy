





















































































define is_sitting = True

image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

init -1 python in mas_sprites:



    MOD_ART_PATH = "mod_assets/monika/"
    STOCK_ART_PATH = "monika/"


    ART_DLM = "-"


    KW_STOCK_ART = "def"








    C_MAIN = MOD_ART_PATH + "c/"
    F_MAIN = MOD_ART_PATH + "f/"
    A_MAIN = MOD_ART_PATH + "a/"
    S_MAIN = MOD_ART_PATH + "s/"





    F_T_MAIN = F_MAIN



    A_T_MAIN = A_MAIN




    LOC_REG = "(1280, 850)"
    LOC_LEAN = "(1280, 742)"
    LOC_Z = "(0, 0)"
    LOC_STAND = "(960, 960)"


    I_COMP = "im.Composite"
    L_COMP = "LiveComposite"
    TRAN = "Transform"


    ZOOM = "zoom=1.25"


    PREFIX_BODY = "torso" + ART_DLM
    PREFIX_ARMS = "arms" + ART_DLM
    PREFIX_BODY_LEAN = "torso-leaning" + ART_DLM
    PREFIX_FACE = "face" + ART_DLM
    PREFIX_FACE_LEAN = "face-leaning" + ART_DLM
    PREFIX_ACS = "acs" + ART_DLM
    PREFIX_ACS_LEAN = "acs-leaning" + ART_DLM
    PREFIX_EYEB = "eyebrows" + ART_DLM
    PREFIX_EYES = "eyes" + ART_DLM
    PREFIX_NOSE = "nose" + ART_DLM
    PREFIX_MOUTH = "mouth" + ART_DLM
    PREFIX_SWEAT = "sweatdrop" + ART_DLM
    PREFIX_EMOTE = "emote" + ART_DLM
    PREFIX_TEARS = "tears" + ART_DLM
    PREFIX_EYEG = "eyebags" + ART_DLM
    PREFIX_BLUSH = "blush" + ART_DLM


    NIGHT_SUFFIX = ART_DLM + "n"
    FILE_EXT = ".png"


    lean_blacklist = [
        "down",
        "bun"
    ]


    def acs_lean_mode(lean):
        """
        Returns the appropriate accessory prefix dpenedong on lean

        IN:
            lean - type of lean

        RETURNS:
            appropratie accessory prefix
        """
        if lean:
            return "".join([PREFIX_ACS_LEAN, lean, ART_DLM])
        
        return PREFIX_ACS


    def face_lean_mode(lean):
        """
        Returns the appropriate face prefix depending on lean

        IN:
            lean - type of lean

        RETURNS:
            appropriate face prefix
        """
        if lean:
            return "".join([PREFIX_FACE_LEAN, lean, ART_DLM])
        
        return PREFIX_FACE


    def night_mode(isnight):
        """
        Returns the appropriate night string
        """
        if isnight:
            return NIGHT_SUFFIX
        
        return ""





    def _ms_accessory(acs, isnight, issitting, lean=None):
        """
        Creates accessory string

        IN:
            acs - MASAccessory object
            isnight - True will generate night string, false will not
            issitting - True will use sitting pic, false will not
            lean - type of lean
                (Default: None)

        RETURNS:
            accessory string
        """
        if issitting:
            acs_str = acs.sit
        
        else:
            acs_str = acs.stand
        
        return "".join([
            LOC_Z,
            ',"',
            A_T_MAIN,
            acs_lean_mode(lean),
            acs_str,
            night_mode(isnight),
            FILE_EXT,
            '"'
        ])


    def _ms_accessorylist(acs_list, isnight, issitting, lean=None):
        """
        Creates accessory strings for a list of accessories

        IN:
            acs_list - list of MASAccessory object, in order of rendering
            isnight - True will generate night string, false will not
            issitting - True will use sitting pic, false will not
            lean - type of lean
                (Default: None)

        RETURNS:
            accessory string list
        """
        if len(acs_list) == 0:
            return ""
        
        return "," + ",".join([
            _ms_accessory(acs, isnight, issitting, lean=lean)
            for acs in acs_list
        ])


    def _ms_arms(clothing, arms, isnight):
        """
        Creates arms string

        IN:
            clothing - type of clothing
            arms - type of arms
            isnight - True will generate night string, false will not

        RETURNS:
            arms string
        """
        return "".join([
            LOC_Z,
            ',"',
            C_MAIN,
            clothing,
            "/",
            PREFIX_ARMS,
            arms,
            night_mode(isnight),
            FILE_EXT,
            '"'
        ])


    def _ms_blush(blush, isnight, lean=None):
        """
        Creates blush string

        IN:
            blush - type of blush
            isnight - True will generate night string, false will not
            lean - type of lean
                (Default: None)

        RETURNS:
            blush string
        """
        return "".join([
            LOC_Z,
            ',"',
            F_T_MAIN,
            face_lean_mode(lean),
            PREFIX_BLUSH,
            blush,
            night_mode(isnight),
            FILE_EXT,
            '"'
        ])


    def _ms_body(clothing, hair, isnight, lean=None, arms=""):
        """
        Creates body string

        IN:
            clothing - type of clothing
            hair - type of hair
            isnight - True will generate night string, false will not
            lean - type of lean
                (Default: None)
            arms - type of arms
                (Default: "")

        RETURNS:
            body string
        """
        if lean:
            
            body_str = ",".join([
                LOC_LEAN,
                _ms_torsoleaning(clothing, hair, lean, isnight)
            ])
        
        else:
            
            body_str = ",".join([
                LOC_REG,
                _ms_torso(clothing, hair, isnight),
                _ms_arms(clothing, arms, isnight)
            ])
        
        
        return "".join([
            I_COMP,
            "(",
            body_str,
            ")"
        ])


    def _ms_emote(emote, isnight, lean=None):
        """
        Creates emote string

        IN:
            emote - type of emote
            isnight - True will generate night string, false will not
            lean - type of lean
                (Dfeualt: None)

        RETURNS:
            emote string
        """
        return "".join([
            LOC_Z,
            ',"',
            F_T_MAIN,
            face_lean_mode(lean),
            PREFIX_EMOTE,
            emote,
            night_mode(isnight),
            FILE_EXT,
            '"'
        ])


    def _ms_eyebags(eyebags, isnight, lean=None):
        """
        Creates eyebags string

        IN:
            eyebags - type of eyebags
            isnight - True will generate night string, false will not
            lean - type of lean
                (Dfeault: None)

        RETURNS:
            eyebags string
        """
        return "".join([
            LOC_Z,
            ',"',
            F_T_MAIN,
            face_lean_mode(lean),
            PREFIX_EYEG,
            eyebags,
            night_mode(isnight),
            FILE_EXT,
            '"'
        ])


    def _ms_eyebrows(eyebrows, isnight, lean=None):
        """
        Creates eyebrow string

        IN:
            eyebrows - type of eyebrows
            isnight - True will generate night string, false will not
            lean - type of lean
                (Default: None)

        RETURNS:
            eyebrows string
        """
        return "".join([
            LOC_Z,
            ',"',
            F_T_MAIN,
            face_lean_mode(lean),
            PREFIX_EYEB,
            eyebrows,
            night_mode(isnight),
            FILE_EXT,
            '"'
        ])


    def _ms_eyes(eyes, isnight, lean=None):
        """
        Creates eyes string

        IN:
            eyes - type of eyes
            isnight - True will generate night string, false will not
            lean - type of lean
                (Default: None)

        RETURNS:
            eyes stirng
        """
        return "".join([
            LOC_Z,
            ',"',
            F_T_MAIN,
            face_lean_mode(lean),
            PREFIX_EYES,
            eyes,
            night_mode(isnight),
            FILE_EXT,
            '"'
        ])


    def _ms_face(
            eyebrows,
            eyes,
            nose,
            mouth,
            isnight,
            lean=None,
            eyebags=None,
            sweat=None,
            blush=None,
            tears=None,
            emote=None
        ):
        """
        Create face string
        (the order these are drawn are in order of argument)

        IN:
            eyebrows - type of eyebrows
            eyes - type of eyes
            nose - type of nose
            mouth - type of mouth
            isnight - True will generate a night string, false will not
            lean - type of lean
                (Default: None)
            eyebags - type of eyebags
                (Default: None)
            sweat - type of sweat drop
                (Default: None)
            blush - type of blush
                (Default: None)
            tears - type of tears
                (Default: None)
            emote - type of emote
                (Default: None)

        RETURNS:
            face string
        """
        subparts = list()
        
        
        if lean:
            subparts.append(LOC_LEAN)
        
        else:
            subparts.append(LOC_REG)
        
        
        subparts.append(_ms_eyebrows(eyebrows, isnight, lean=lean))
        subparts.append(_ms_eyes(eyes, isnight, lean=lean))
        subparts.append(_ms_nose(nose, isnight, lean=lean))
        subparts.append(_ms_mouth(mouth, isnight, lean=lean))
        
        
        if eyebags:
            subparts.append(_ms_eyebags(eyebags, isnight, lean=lean))
        
        if sweat:
            subparts.append(_ms_sweat(sweat, isnight, lean=lean))
        
        if blush:
            subparts.append(_ms_blush(blush, isnight, lean=lean))
        
        if tears:
            subparts.append(_ms_tears(tears, isnight, lean=lean))
        
        if emote:
            subparts.append(_ms_emote(emote, isnight, lean=lean))
        
        
        return "".join([
            I_COMP,
            "(",
            ",".join(subparts),
            ")"
        ])


    def _ms_head(clothing, hair, head):
        """
        Creates head string

        IN:
            clothing - type of clothing
            hair - type of hair
            head - type of head

        RETURNS:
            head string
        """
        
        return "".join([
            LOC_Z,
            ',"',
            S_MAIN,
            clothing,
            "/",
            hair,
            ART_DLM,
            head,
            FILE_EXT,
            '"'
        ])


    def _ms_left(clothing, hair, left):
        """
        Creates left side string

        IN:
            clothing - type of clothing
            hair - type of hair
            left - type of left side

        RETURNS:
            left side stirng
        """
        
        return "".join([
            LOC_Z,
            ',"',
            S_MAIN,
            clothing,
            "/",
            hair,
            ART_DLM,
            left,
            FILE_EXT,
            '"'
        ])


    def _ms_mouth(mouth, isnight, lean=None):
        """
        Creates mouth string

        IN:
            mouth - type of mouse
            isnight - True will generate night string, false will not
            lean - type of lean
                (Default: None)

        RETURNS:
            mouth string
        """
        return "".join([
            LOC_Z,
            ',"',
            F_T_MAIN,
            face_lean_mode(lean),
            PREFIX_MOUTH,
            mouth,
            night_mode(isnight),
            FILE_EXT,
            '"'
        ])


    def _ms_nose(nose, isnight, lean=None):
        """
        Creates nose string

        IN:
            nose - type of nose
            isnight - True will genreate night string, false will not
            lean - type of lean
                (Default: None)

        RETURNS:
            nose string
        """
        return "".join([
            LOC_Z,
            ',"',
            F_T_MAIN,
            face_lean_mode(lean),
            PREFIX_NOSE,
            nose,
            night_mode(isnight),
            FILE_EXT,
            '"'
        ])


    def _ms_right(clothing, hair, right):
        """
        Creates right body string

        IN:
            clothing - type of clothing
            hair - type of hair
            right - type of right side

        RETURNS:
            right body string
        """
        
        return "".join([
            LOC_Z,
            ',"',
            S_MAIN,
            clothing,
            "/",
            hair,
            ART_DLM,
            head,
            FILE_EXT,
            '"'
        ])


    def _ms_sitting(
            clothing,
            hair,
            eyebrows,
            eyes,
            nose,
            mouth,
            isnight,
            acs_list,
            lean=None,
            arms="",
            eyebags=None,
            sweat=None,
            blush=None,
            tears=None,
            emote=None
        ):
        """
        Creates sitting string

        IN:
            clothing - type of clothing
            hair - type of hair
            eyebrows - type of eyebrows
            eyes - type of eyes
            nose - type of nose
            mouth - type of mouth
            isnight - True will genreate night string, false will not
            acs_list - list of MASAccessory objects to draw
            lean - type of lean
                (Default: None)
            arms - type of arms
                (Default: "")
            eyebags - type of eyebags
                (Default: None)
            sweat - type of sweatdrop
                (Default: None)
            blush - type of blush
                (Default: None)
            tears - type of tears
                (Default: None)
            emote - type of emote
                (Default: None)

        RETURNS:
            sitting stirng
        """
        if lean:
            loc_str = LOC_LEAN
        
        else:
            loc_str = LOC_REG
        
        return "".join([
            TRAN,
            "(",
            L_COMP,
            "(",
            loc_str,
            ",",
            LOC_Z,
            ",",
            _ms_body(clothing, hair, isnight, lean=lean, arms=arms),
            ",",
            LOC_Z,
            ",",
            _ms_face(
                eyebrows,
                eyes,
                nose,
                mouth,
                isnight,
                lean=lean,
                eyebags=eyebags,
                sweat=sweat,
                blush=blush,
                tears=tears,
                emote=emote
            ),
            _ms_accessorylist(acs_list, isnight, True, lean=lean),
            "),",
            ZOOM,
            ")"
        ])


    def _ms_standing(clothing, hair, head, left, right, acs_list):
        """
        Creates the custom standing string
        This is different than the stock ones because of image location

        IN:
            clothing - type of clothing
            hair - type of hair
            head - type of head
            left - type of left side
            right - type of right side
            acs_list - list of MASAccessory objects

        RETURNS:
            custom standing sprite
        """
        
        return "".join([
            I_COMP,
            "(",
            LOC_STAND,
            ",",
            _ms_left(clothing, hair, left),
            ",",
            _ms_right(clothing, hair, right),
            ",",
            _ms_head(clothing, hair, head),
            _ms_accessorylist(acs_list, False, False),
            ")"
        ])


    def _ms_standingstock(head, left, right, acs_list, single=None):
        """
        Creates the stock standing string
        This is different then the custom ones because of image location

        Also no night version atm.

        IN:
            head - type of head
            left - type of left side
            right - type of right side
            acs_list - list of MASAccessory objects
            single - type of single standing picture.
                (Defualt: None)

        RETURNS:
            stock standing string
        """
        if single:
            return "".join([
                I_COMP,
                "(",
                LOC_STAND,
                ",",
                LOC_Z,
                ',"',
                STOCK_ART_PATH,
                single,
                FILE_EXT,
                '"',
                _ms_accessorylist(acs_list, False, False),
                ")"
            ])
        
        return "".join([
            I_COMP,
            "(",
            LOC_STAND,
            ",",
            LOC_Z,
            ',"',
            STOCK_ART_PATH,
            left,
            FILE_EXT,
            '",',
            LOC_Z,
            ',"',
            STOCK_ART_PATH,
            right,
            FILE_EXT,
            '",',
            LOC_Z,
            ',"',
            STOCK_ART_PATH,
            head,
            FILE_EXT,
            '"',
            _ms_accessorylist(acs_list, False, False),
            ")"
        ])


    def _ms_sweat(sweat, isnight, lean=None):
        """
        Creates sweatdrop string

        IN:
            sweat -  type of sweatdrop
            isnight - True will generate night string, false will not
            lean - type of lean
                (Defualt: None)

        RETURNS:
            sweatdrop string
        """
        return "".join([
            LOC_Z,
            ',"',
            F_T_MAIN,
            face_lean_mode(lean),
            PREFIX_SWEAT,
            sweat,
            night_mode(isnight),
            FILE_EXT,
            '"'
        ])


    def _ms_tears(tears, isnight, lean=None):
        """
        Creates tear string

        IN:
            tears - type of tears
            isnight - True will generate night string, false will not
            lean - type of lean
                (Default: None)

        RETURNS:
            tear strring
        """
        return "".join([
            LOC_Z,
            ',"',
            F_T_MAIN,
            face_lean_mode(lean),
            PREFIX_TEARS,
            tears,
            night_mode(isnight),
            FILE_EXT,
            '"'
        ])


    def _ms_torso(clothing, hair, isnight):
        """
        Creates torso string

        IN:
            clothing - type of clothing
            hair - type of hair
            isnight - True will generate night string, false will not

        RETURNS:
            torso string
        """
        return "".join([
            LOC_Z,
            ',"',
            C_MAIN,
            clothing,
            "/",
            PREFIX_BODY,
            hair,
            night_mode(isnight),
            FILE_EXT,
            '"'
        ])


    def _ms_torsoleaning(clothing, hair, lean, isnight):
        """
        Creates leaning torso string

        IN:
            clothing - type of clothing
            hair - type of ahri
            lean - type of leaning
            isnight - True will genreate night string, false will not

        RETURNS:
            leaning torso string
        """
        return "".join([
            LOC_Z,
            ',"',
            C_MAIN,
            clothing,
            "/",
            PREFIX_BODY_LEAN,
            hair,
            ART_DLM,
            lean,
            night_mode(isnight),
            FILE_EXT,
            '"'
        ])






init -2 python:



    import math


    class MASMonika(renpy.store.object):
        def __init__(self):
            self.name="Monika"
            self.haircut="default"
            self.haircolor="default"
            self.skin_hue=0 
            self.lipstick="default" 
            self.clothes = "def" 
            self.hair = "def" 
            self.acs = [] 
            self.hair_hue=0 
        
        
        def change_clothes(self, new_cloth):
            """
            Changes clothes to the given cloth

            IN:
                new_cloth - new clothes to wear
            """
            self.clothes = new_cloth
        
        
        def change_hair(self, new_hair):
            """
            Changes hair to the given hair

            IN:
                new_hair - new hair to wear
            """
            self.hair = new_hair
        
        
        def change_outfit(self, new_cloth, new_hair):
            """
            Changes both clothes and hair

            IN:
                new_cloth - new clothes to wear
                new_hair - new hair to wear
            """
            self.change_clothes(new_cloth)
            self.change_hair(new_hair)
        
        
        def get_outfit(self):
            """
            Returns the current outfit

            RETURNS:
                tuple:
                    [0] - current clothes
                    [1] - current hair
            """
            return (self.clothes, self.hair)
        
        
        def is_wearing_acs(self, accessory):
            """
            Checks if currently wearing the given accessory

            IN:
                accessory - accessory to check

            RETURNS:
                True if wearing accessory, false if not
            """
            return accessory in self.acs
        
        
        def reset_all(self):
            """
            Resets all of monika
            """
            self.reset_clothes()
            self.reset_hair()
            self.remove_all_acs()
        
        
        def remove_acs(self, accessory):
            """
            Removes the given accessory

            IN:
                accessory - accessory to remove
            """
            if accessory in self.acs:
                self.acs.remove(accessory)
        
        
        def remove_all_acs(self):
            """
            Removes all accessories
            """
            self.acs = list()
        
        
        def reset_clothes(self):
            """
            Resets clothing to default
            """
            self.clothes = "def"
        
        
        def reset_hair(self):
            """
            Resets hair to default
            """
            self.hair = "def"
        
        
        def reset_outfit(self):
            """
            Resetse clothing and hair to default
            """
            self.reset_clothes()
            self.reset_hair()
        
        
        def wear_acs(self, accessory):
            """
            Wears the given accessory

            IN:
                accessory - accessory to wear
            """
            self.acs.wear(accessory)



    hair_hue1 = im.matrix([ 1, 0, 0, 0, 0,
                        0, 1, 0, 0, 0,
                        0, 0, 1, 0, 0,
                        0, 0, 0, 1, 0 ])
    hair_hue2 = im.matrix([ 3.734, 0, 0, 0, 0,
                        0, 3.531, 0, 0, 0,
                        0, 0, 1.375, 0, 0,
                        0, 0, 0, 1, 0 ])
    hair_hue3 = im.matrix([ 3.718, 0, 0, 0, 0,
                        0, 3.703, 0, 0, 0,
                        0, 0, 3.781, 0, 0,
                        0, 0, 0, 1, 0 ])
    hair_hue4 = im.matrix([ 3.906, 0, 0, 0, 0,
                        0, 3.671, 0, 0, 0,
                        0, 0, 3.375, 0, 0,
                        0, 0, 0, 1, 0 ])
    skin_hue1 = hair_hue1
    skin_hue2 = im.matrix([ 0.925, 0, 0, 0, 0,
                        0, 0.840, 0, 0, 0,
                        0, 0, 0.806, 0, 0,
                        0, 0, 0, 1, 0 ])
    skin_hue3 = im.matrix([ 0.851, 0, 0, 0, 0,
                        0, 0.633, 0, 0, 0,
                        0, 0, 0.542, 0, 0,
                        0, 0, 0, 1, 0 ])

    hair_huearray = [hair_hue1,hair_hue2,hair_hue3,hair_hue4]

    skin_huearray = [skin_hue1,skin_hue2,skin_hue3]



    class MASAccessory(renpy.store.object):
        def __init__(self,
                name,
                sit,
                stand=None,
                priority=10,
                can_strip=True
            ):
            self.name=name
            self.sit = sit
            if stand is None:
                stand = sit
            self.stand = stand
            self.priority=priority
            
            
            
            self.can_strip=can_strip
        
        @staticmethod
        def get_priority(acs):
            """
            Gets the priority of the given accessory

            This is for sorting
            """
            return acs.priority



    def mas_drawmonika(
            st,
            at,
            character,

            
            eyebrows,
            eyes,
            nose,
            mouth,

            
            head,
            left,
            right,

            
            lean=None,
            arms="steepling",
            eyebags=None,
            sweat=None,
            blush=None,
            tears=None,
            emote=None,

            
            stock=True,
            single=None
        ):
        """
        Draws monika dynamically
        NOTE: custom standing stuff not ready for usage yet.
        NOTE: the actual drawing of accessories happens in the respective
            functions instead of here.
        NOTE: because of how clothes, hair, and body is tied together,
            monika can only have 1 type of clothing and 1 hair style
            at a time.

        IN:
            st - renpy related
            at - renpy related
            character - MASMonika character object
            eyebrows - type of eyebrows (sitting)
            eyes - type of eyes (sitting)
            nose - type of nose (sitting)
            mouth - type of mouth (sitting)
            head - type of head (standing)
            left - type of left side (standing)
            right - type of right side (standing)
            lean - type of lean (sitting)
                (Default: None)
            arms - type of arms (sitting)
                (Default: "steepling")
            eyebags - type of eyebags (sitting)
                (Default: None)
            sweat - type of sweatdrop (sitting)
                (Default: None)
            blush - type of blush (sitting)
                (Default: None)
            tears - type of tears (sitting)
                (Default: None)
            emote - type of emote (sitting)
                (Default: None)
            stock - True means we are using stock standing, False means not
                (standing)
                (Default: True)
            single - type of single standing image (standing)
                (Default: None)
        """
        
        
        acs_list=sorted(character.acs, key=MASAccessory.get_priority)
        
        
        if is_sitting:
            
            if (
                    lean
                    and (
                        character.clothes in store.mas_sprites.lean_blacklist
                        or character.hair in store.mas_sprites.lean_blacklist
                    )
                ):
                
                lean = None
            
            cmd = store.mas_sprites._ms_sitting(
                character.clothes,
                character.hair,
                eyebrows,
                eyes,
                nose,
                mouth,
                not morning_flag,
                acs_list,
                lean=lean,
                arms=arms,
                eyebags=eyebags,
                sweat=sweat,
                blush=blush,
                tears=tears,
                emote=emote
            )
        
        else:
            
            
            
            cmd = store.mas_sprites._ms_standingstock(
                head,
                left,
                right,
                acs_list,
                single=single
            )
        
        
        
        
        return eval(cmd),None 


define monika_chr = MASMonika()




















































image monika 1 = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="a",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 2 = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="a",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 3 = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="a",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 4 = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="a",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 5 = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="",
    left="",
    right="",
    lean="def",
    single="3a"
)

image monika 1a = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="a",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1b = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="big",
    head="b",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1c = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="smirk",
    head="c",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1d = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="small",
    head="d",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1e = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="e",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1f = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="normal",
    nose="def",
    mouth="smirk",
    head="f",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1g = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="normal",
    nose="def",
    mouth="small",
    head="g",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1h = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="normal",
    nose="def",
    mouth="smirk",
    head="h",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1i = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="normal",
    nose="def",
    mouth="small",
    head="i",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1j = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedhappy",
    nose="def",
    mouth="smile",
    head="j",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1k = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="k",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1l = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="l",
    left="1l",
    right="1r",
    arms="steepling",
    sweat="def"
)

image monika 1m = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smile",
    head="m",
    left="1l",
    right="1r",
    arms="steepling",
    sweat="def"
)

image monika 1n = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="big",
    head="n",
    left="1l",
    right="1r",
    arms="steepling",
    sweat="def"
)

image monika 1o = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="o",
    left="1l",
    right="1r",
    arms="steepling",
    sweat="def"
)

image monika 1p = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="small",
    head="p",
    left="1l",
    right="1r",
    arms="steepling",
    sweat="def"
)

image monika 1q = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="closedsad",
    nose="def",
    mouth="smirk",
    head="q",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1r = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="closedsad",
    nose="def",
    mouth="small",
    head="r",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1efx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="disgust",
    head="h",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1efu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="smug",
    head="h",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1efd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="small",
    head="i",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1efc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="smirk",
    head="h",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1efb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="big",
    head="i",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1efw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="wide",
    head="i",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1efo = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="gasp",
    head="i",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1eftsu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="smug",
    head="i",
    left="1l",
    right="1r",
    arms="steepling",
    tears="streaming"
)

image monika 1wfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="wide",
    nose="def",
    mouth="disgust",
    head="h",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1wfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="wide",
    nose="def",
    mouth="wide",
    head="i",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1wud = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="wide",
    nose="def",
    mouth="small",
    head="d",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1wuo = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="wide",
    nose="def",
    mouth="gasp",
    head="b",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1wubsw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="wide",
    nose="def",
    mouth="wide",
    head="b",
    left="1l",
    right="1r",
    arms="steepling",
    blush="shade"
)

image monika 1wubso = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="wide",
    nose="def",
    mouth="gasp",
    head="b",
    left="1l",
    right="1r",
    arms="steepling",
    blush="shade"
)

image monika 1subftsb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="sparkle",
    nose="def",
    mouth="big",
    head="b",
    left="1l",
    right="1r",
    arms="steepling",
    blush="full",
    tears="streaming"
)

image monika 1sub = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="sparkle",
    nose="def",
    mouth="big",
    head="b",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1sutsa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="sparkle",
    nose="def",
    mouth="smile",
    head="a",
    left="1l",
    right="1r",
    arms="steepling",
    tears="streaming"
)

image monika 1tfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="disgust",
    head="h",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1tfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="smug",
    head="h",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1tfd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="small",
    head="i",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1tfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="smirk",
    head="h",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1tfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="big",
    head="i",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1tkx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="smug",
    nose="def",
    mouth="disgust",
    head="f",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1tku = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="smug",
    nose="def",
    mouth="smug",
    head="f",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1tkd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="smug",
    nose="def",
    mouth="small",
    head="g",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1tkc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="smug",
    nose="def",
    mouth="smirk",
    head="f",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1tsb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="smug",
    nose="def",
    mouth="big",
    head="i",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1tsbsa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="smug",
    nose="def",
    mouth="smile",
    head="a",
    left="1l",
    right="1r",
    arms="steepling",
    blush="shade"
)

image monika 1rfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="disgust",
    head="h",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1rfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="smug",
    head="h",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1rfd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="small",
    head="i",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1rfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="smirk",
    head="h",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1rfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="big",
    head="i",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1rfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="wide",
    head="i",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1rktsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="right",
    nose="def",
    mouth="smirk",
    head="f",
    left="1l",
    right="1r",
    arms="steepling",
    tears="streaming"
)

image monika 1lfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="disgust",
    head="h",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1lfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="smug",
    head="h",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1lfd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="small",
    head="i",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1lfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="h",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1lfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="big",
    head="i",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1lfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="wide",
    head="i",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1lud = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="left",
    nose="def",
    mouth="small",
    head="d",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1lsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="h",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1lssdrc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="o",
    left="1l",
    right="1r",
    arms="steepling",
    sweat="right"
)

image monika 1pp = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="small",
    head="p",
    left="1l",
    right="1r",
    arms="steepling",
    sweat="def"
)

image monika 1oo = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="o",
    left="1l",
    right="1r",
    arms="steepling",
    sweat="def"
)

image monika 1nn = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="big",
    head="n",
    left="1l",
    right="1r",
    arms="steepling",
    sweat="def"
)

image monika 1lksdlw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="wide",
    head="n",
    left="1l",
    right="1r",
    arms="steepling",
    sweat="def"
)

image monika 1mm = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smile",
    head="m",
    left="1l",
    right="1r",
    arms="steepling",
    sweat="def"
)

image monika 1lssdrb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="big",
    head="n",
    left="1l",
    right="1r",
    arms="steepling",
    sweat="right"
)

image monika 1lsbssdrb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="big",
    head="n",
    left="1l",
    right="1r",
    arms="steepling",
    sweat="right",
    blush="shade"
)

image monika 1lsbsa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="smile",
    head="a",
    left="1l",
    right="1r",
    arms="steepling",
    blush="shade"
)

image monika 1lkbsa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smile",
    head="e",
    left="1l",
    right="1r",
    arms="steepling",
    blush="shade"
)

image monika 1lftsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="f",
    left="1l",
    right="1r",
    arms="steepling",
    tears="streaming"
)

image monika 1lktsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="f",
    left="1l",
    right="1r",
    arms="steepling",
    tears="streaming"
)

image monika 1dfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="disgust",
    head="q",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1dfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="smug",
    head="q",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1dfd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="small",
    head="r",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1dfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="smirk",
    head="q",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1dfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="big",
    head="r",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1dfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="wide",
    head="r",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1dso = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="closedsad",
    nose="def",
    mouth="gasp",
    head="r",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1dsbso = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="closedsad",
    nose="def",
    mouth="gasp",
    head="r",
    left="1l",
    right="1r",
    arms="steepling",
    blush="shade"
)

image monika 1dftsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="smirk",
    head="q",
    left="1l",
    right="1r",
    arms="steepling",
    tears="streaming"
)

image monika 1dftdc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="smirk",
    head="q",
    left="1l",
    right="1r",
    arms="steepling",
    tears="dried"
)

image monika 1duu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedsad",
    nose="def",
    mouth="smug",
    head="j",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1dubsu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedsad",
    nose="def",
    mouth="smug",
    head="j",
    left="1l",
    right="1r",
    arms="steepling",
    blush="shade"
)

image monika 1dubssdru = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedsad",
    nose="def",
    mouth="smug",
    head="j",
    left="1l",
    right="1r",
    arms="steepling",
    blush="shade",
    sweat="right"
)

image monika 1hfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="disgust",
    head="q",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1hfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="smug",
    head="j",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1hfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="smirk",
    head="q",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1hfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="k",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1hfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="wide",
    head="r",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1ll = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="l",
    left="1l",
    right="1r",
    arms="steepling"
)

image monika 1hubfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="b",
    left="1l",
    right="1r",
    arms="steepling",
    blush="full"
)

image monika 1ekbfa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="a",
    left="1l",
    right="1r",
    arms="steepling",
    blush="full"
)

image monika 2a = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="a",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2b = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="big",
    head="b",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2c = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="smirk",
    head="c",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2d = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="small",
    head="d",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2e = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="e",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2f = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="normal",
    nose="def",
    mouth="smirk",
    head="f",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2g = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="normal",
    nose="def",
    mouth="small",
    head="g",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2h = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="normal",
    nose="def",
    mouth="smirk",
    head="h",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2i = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="normal",
    nose="def",
    mouth="small",
    head="i",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2j = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedhappy",
    nose="def",
    mouth="smile",
    head="j",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2k = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="k",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2l = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="l",
    left="1l",
    right="2r",
    arms="crossed",
    sweat="def"
)

image monika 2m = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smile",
    head="m",
    left="1l",
    right="2r",
    arms="crossed",
    sweat="def"
)

image monika 2n = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="big",
    head="n",
    left="1l",
    right="2r",
    arms="crossed",
    sweat="def"
)

image monika 2o = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="o",
    left="1l",
    right="2r",
    arms="crossed",
    sweat="def"
)

image monika 2p = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="small",
    head="p",
    left="1l",
    right="2r",
    arms="crossed",
    sweat="def"
)

image monika 2q = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="closedsad",
    nose="def",
    mouth="smirk",
    head="q",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2r = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="closedsad",
    nose="def",
    mouth="small",
    head="r",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2efx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="disgust",
    head="h",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2efu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="smug",
    head="h",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2efd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="small",
    head="i",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2efc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="smirk",
    head="h",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2efb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="big",
    head="i",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2efw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="wide",
    head="i",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2efo = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="gasp",
    head="i",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2eftsu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="smug",
    head="i",
    left="1l",
    right="2r",
    arms="crossed",
    tears="streaming"
)

image monika 2wfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="wide",
    nose="def",
    mouth="disgust",
    head="h",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2wfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="wide",
    nose="def",
    mouth="wide",
    head="i",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2wud = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="wide",
    nose="def",
    mouth="small",
    head="d",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2wuo = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="wide",
    nose="def",
    mouth="gasp",
    head="b",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2wubsw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="wide",
    nose="def",
    mouth="wide",
    head="b",
    left="1l",
    right="2r",
    arms="crossed",
    blush="shade"
)

image monika 2wubso = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="wide",
    nose="def",
    mouth="gasp",
    head="b",
    left="1l",
    right="2r",
    arms="crossed",
    blush="shade"
)

image monika 2subftsb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="sparkle",
    nose="def",
    mouth="big",
    head="b",
    left="1l",
    right="2r",
    arms="crossed",
    blush="full",
    tears="streaming"
)

image monika 2sub = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="sparkle",
    nose="def",
    mouth="big",
    head="b",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2sutsa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="sparkle",
    nose="def",
    mouth="smile",
    head="a",
    left="1l",
    right="2r",
    arms="crossed",
    tears="streaming"
)

image monika 2tfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="disgust",
    head="h",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2tfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="smug",
    head="h",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2tfd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="small",
    head="i",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2tfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="smirk",
    head="h",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2tfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="big",
    head="i",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2tkx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="smug",
    nose="def",
    mouth="disgust",
    head="f",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2tku = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="smug",
    nose="def",
    mouth="smug",
    head="f",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2tkd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="smug",
    nose="def",
    mouth="small",
    head="g",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2tkc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="smug",
    nose="def",
    mouth="smirk",
    head="f",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2tsb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="smug",
    nose="def",
    mouth="big",
    head="i",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2tsbsa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="smug",
    nose="def",
    mouth="smile",
    head="a",
    left="1l",
    right="2r",
    arms="crossed",
    blush="shade"
)

image monika 2rfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="disgust",
    head="h",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2rfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="smug",
    head="h",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2rfd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="small",
    head="i",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2rfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="smirk",
    head="h",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2rfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="big",
    head="i",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2rfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="wide",
    head="i",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2rktsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="right",
    nose="def",
    mouth="smirk",
    head="f",
    left="1l",
    right="2r",
    arms="crossed",
    tears="streaming"
)

image monika 2lfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="disgust",
    head="h",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2lfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="smug",
    head="h",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2lfd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="small",
    head="i",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2lfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="h",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2lfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="big",
    head="i",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2lfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="wide",
    head="i",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2lud = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="left",
    nose="def",
    mouth="small",
    head="d",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2lsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="h",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2lssdrc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="o",
    left="1l",
    right="2r",
    arms="crossed",
    sweat="right"
)

image monika 2pp = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="small",
    head="p",
    left="1l",
    right="2r",
    arms="crossed",
    sweat="def"
)

image monika 2oo = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="o",
    left="1l",
    right="2r",
    arms="crossed",
    sweat="def"
)

image monika 2nn = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="big",
    head="n",
    left="1l",
    right="2r",
    arms="crossed",
    sweat="def"
)

image monika 2lksdlw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="wide",
    head="n",
    left="1l",
    right="2r",
    arms="crossed",
    sweat="def"
)

image monika 2mm = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smile",
    head="m",
    left="1l",
    right="2r",
    arms="crossed",
    sweat="def"
)

image monika 2lssdrb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="big",
    head="n",
    left="1l",
    right="2r",
    arms="crossed",
    sweat="right"
)

image monika 2lsbssdrb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="big",
    head="n",
    left="1l",
    right="2r",
    arms="crossed",
    sweat="right",
    blush="shade"
)

image monika 2lsbsa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="smile",
    head="a",
    left="1l",
    right="2r",
    arms="crossed",
    blush="shade"
)

image monika 2lkbsa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smile",
    head="e",
    left="1l",
    right="2r",
    arms="crossed",
    blush="shade"
)

image monika 2lftsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="f",
    left="1l",
    right="2r",
    arms="crossed",
    tears="streaming"
)

image monika 2lktsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="f",
    left="1l",
    right="2r",
    arms="crossed",
    tears="streaming"
)

image monika 2dfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="disgust",
    head="q",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2dfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="smug",
    head="q",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2dfd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="small",
    head="r",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2dfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="smirk",
    head="q",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2dfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="big",
    head="r",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2dfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="wide",
    head="r",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2dso = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="closedsad",
    nose="def",
    mouth="gasp",
    head="r",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2dsbso = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="closedsad",
    nose="def",
    mouth="gasp",
    head="r",
    left="1l",
    right="2r",
    arms="crossed",
    blush="shade"
)

image monika 2dftsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="smirk",
    head="q",
    left="1l",
    right="2r",
    arms="crossed",
    tears="streaming"
)

image monika 2dftdc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="smirk",
    head="q",
    left="1l",
    right="2r",
    arms="crossed",
    tears="dried"
)

image monika 2duu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedsad",
    nose="def",
    mouth="smug",
    head="j",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2dubsu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedsad",
    nose="def",
    mouth="smug",
    head="j",
    left="1l",
    right="2r",
    arms="crossed",
    blush="shade"
)

image monika 2dubssdru = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedsad",
    nose="def",
    mouth="smug",
    head="j",
    left="1l",
    right="2r",
    arms="crossed",
    blush="shade",
    sweat="right"
)

image monika 2hfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="disgust",
    head="q",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2hfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="smug",
    head="j",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2hfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="smirk",
    head="q",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2hfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="k",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2hfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="wide",
    head="r",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2ll = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="l",
    left="1l",
    right="2r",
    arms="crossed"
)

image monika 2hubfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="b",
    left="1l",
    right="2r",
    arms="crossed",
    blush="full"
)

image monika 2ekbfa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="a",
    left="1l",
    right="2r",
    arms="crossed",
    blush="full"
)

image monika 3a = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="a",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3b = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="big",
    head="b",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3c = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="smirk",
    head="c",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3d = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="small",
    head="d",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3e = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="e",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3f = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="normal",
    nose="def",
    mouth="smirk",
    head="f",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3g = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="normal",
    nose="def",
    mouth="small",
    head="g",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3h = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="normal",
    nose="def",
    mouth="smirk",
    head="h",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3i = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="normal",
    nose="def",
    mouth="small",
    head="i",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3j = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedhappy",
    nose="def",
    mouth="smile",
    head="j",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3k = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="k",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3l = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="l",
    left="2l",
    right="1r",
    arms="restleftpointright",
    sweat="def"
)

image monika 3m = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smile",
    head="m",
    left="2l",
    right="1r",
    arms="restleftpointright",
    sweat="def"
)

image monika 3n = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="big",
    head="n",
    left="2l",
    right="1r",
    arms="restleftpointright",
    sweat="def"
)

image monika 3o = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="o",
    left="2l",
    right="1r",
    arms="restleftpointright",
    sweat="def"
)

image monika 3p = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="small",
    head="p",
    left="2l",
    right="1r",
    arms="restleftpointright",
    sweat="def"
)

image monika 3q = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="closedsad",
    nose="def",
    mouth="smirk",
    head="q",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3r = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="closedsad",
    nose="def",
    mouth="small",
    head="r",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3efx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="disgust",
    head="h",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3efu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="smug",
    head="h",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3efd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="small",
    head="i",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3efc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="smirk",
    head="h",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3efb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="big",
    head="i",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3efw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="wide",
    head="i",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3efo = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="gasp",
    head="i",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3eftsu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="smug",
    head="i",
    left="2l",
    right="1r",
    arms="restleftpointright",
    tears="streaming"
)

image monika 3wfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="wide",
    nose="def",
    mouth="disgust",
    head="h",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3wfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="wide",
    nose="def",
    mouth="wide",
    head="i",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3wud = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="wide",
    nose="def",
    mouth="small",
    head="d",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3wuo = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="wide",
    nose="def",
    mouth="gasp",
    head="b",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3wubsw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="wide",
    nose="def",
    mouth="wide",
    head="b",
    left="2l",
    right="1r",
    arms="restleftpointright",
    blush="shade"
)

image monika 3wubso = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="wide",
    nose="def",
    mouth="gasp",
    head="b",
    left="2l",
    right="1r",
    arms="restleftpointright",
    blush="shade"
)

image monika 3subftsb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="sparkle",
    nose="def",
    mouth="big",
    head="b",
    left="2l",
    right="1r",
    arms="restleftpointright",
    blush="full",
    tears="streaming"
)

image monika 3sub = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="sparkle",
    nose="def",
    mouth="big",
    head="b",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3sutsa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="sparkle",
    nose="def",
    mouth="smile",
    head="a",
    left="2l",
    right="1r",
    arms="restleftpointright",
    tears="streaming"
)

image monika 3tfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="disgust",
    head="h",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3tfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="smug",
    head="h",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3tfd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="small",
    head="i",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3tfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="smirk",
    head="h",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3tfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="big",
    head="i",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3tkx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="smug",
    nose="def",
    mouth="disgust",
    head="f",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3tku = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="smug",
    nose="def",
    mouth="smug",
    head="f",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3tkd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="smug",
    nose="def",
    mouth="small",
    head="g",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3tkc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="smug",
    nose="def",
    mouth="smirk",
    head="f",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3tsb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="smug",
    nose="def",
    mouth="big",
    head="i",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3tsbsa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="smug",
    nose="def",
    mouth="smile",
    head="a",
    left="2l",
    right="1r",
    arms="restleftpointright",
    blush="shade"
)

image monika 3rfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="disgust",
    head="h",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3rfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="smug",
    head="h",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3rfd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="small",
    head="i",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3rfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="smirk",
    head="h",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3rfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="big",
    head="i",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3rfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="wide",
    head="i",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3rktsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="right",
    nose="def",
    mouth="smirk",
    head="f",
    left="2l",
    right="1r",
    arms="restleftpointright",
    tears="streaming"
)

image monika 3lfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="disgust",
    head="h",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3lfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="smug",
    head="h",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3lfd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="small",
    head="i",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3lfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="h",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3lfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="big",
    head="i",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3lfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="wide",
    head="i",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3lud = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="left",
    nose="def",
    mouth="small",
    head="d",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3lsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="h",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3lssdrc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="o",
    left="2l",
    right="1r",
    arms="restleftpointright",
    sweat="right"
)

image monika 3pp = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="small",
    head="p",
    left="2l",
    right="1r",
    arms="restleftpointright",
    sweat="def"
)

image monika 3oo = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="o",
    left="2l",
    right="1r",
    arms="restleftpointright",
    sweat="def"
)

image monika 3nn = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="big",
    head="n",
    left="2l",
    right="1r",
    arms="restleftpointright",
    sweat="def"
)

image monika 3lksdlw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="wide",
    head="n",
    left="2l",
    right="1r",
    arms="restleftpointright",
    sweat="def"
)

image monika 3mm = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smile",
    head="m",
    left="2l",
    right="1r",
    arms="restleftpointright",
    sweat="def"
)

image monika 3lssdrb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="big",
    head="n",
    left="2l",
    right="1r",
    arms="restleftpointright",
    sweat="right"
)

image monika 3lsbssdrb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="big",
    head="n",
    left="2l",
    right="1r",
    arms="restleftpointright",
    sweat="right",
    blush="shade"
)

image monika 3lsbsa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="smile",
    head="a",
    left="2l",
    right="1r",
    arms="restleftpointright",
    blush="shade"
)

image monika 3lkbsa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smile",
    head="e",
    left="2l",
    right="1r",
    arms="restleftpointright",
    blush="shade"
)

image monika 3lftsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="f",
    left="2l",
    right="1r",
    arms="restleftpointright",
    tears="streaming"
)

image monika 3lktsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="f",
    left="2l",
    right="1r",
    arms="restleftpointright",
    tears="streaming"
)

image monika 3dfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="disgust",
    head="q",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3dfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="smug",
    head="q",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3dfd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="small",
    head="r",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3dfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="smirk",
    head="q",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3dfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="big",
    head="r",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3dfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="wide",
    head="r",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3dso = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="closedsad",
    nose="def",
    mouth="gasp",
    head="r",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3dsbso = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="closedsad",
    nose="def",
    mouth="gasp",
    head="r",
    left="2l",
    right="1r",
    arms="restleftpointright",
    blush="shade"
)

image monika 3dftsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="smirk",
    head="q",
    left="2l",
    right="1r",
    arms="restleftpointright",
    tears="streaming"
)

image monika 3dftdc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="smirk",
    head="q",
    left="2l",
    right="1r",
    arms="restleftpointright",
    tears="dried"
)

image monika 3duu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedsad",
    nose="def",
    mouth="smug",
    head="j",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3dubsu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedsad",
    nose="def",
    mouth="smug",
    head="j",
    left="2l",
    right="1r",
    arms="restleftpointright",
    blush="shade"
)

image monika 3dubssdru = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedsad",
    nose="def",
    mouth="smug",
    head="j",
    left="2l",
    right="1r",
    arms="restleftpointright",
    blush="shade",
    sweat="right"
)

image monika 3hfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="disgust",
    head="q",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3hfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="smug",
    head="j",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3hfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="smirk",
    head="q",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3hfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="k",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3hfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="wide",
    head="r",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3ll = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="l",
    left="2l",
    right="1r",
    arms="restleftpointright"
)

image monika 3hubfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="b",
    left="2l",
    right="1r",
    arms="restleftpointright",
    blush="full"
)

image monika 3ekbfa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="a",
    left="2l",
    right="1r",
    arms="restleftpointright",
    blush="full"
)

image monika 4a = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="a",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4b = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="big",
    head="b",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4c = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="smirk",
    head="c",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4d = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="small",
    head="d",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4e = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="e",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4f = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="normal",
    nose="def",
    mouth="smirk",
    head="f",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4g = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="normal",
    nose="def",
    mouth="small",
    head="g",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4h = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="normal",
    nose="def",
    mouth="smirk",
    head="h",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4i = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="normal",
    nose="def",
    mouth="small",
    head="i",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4j = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedhappy",
    nose="def",
    mouth="smile",
    head="j",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4k = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="k",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4l = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="l",
    left="2l",
    right="2r",
    arms="pointright",
    sweat="def"
)

image monika 4m = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smile",
    head="m",
    left="2l",
    right="2r",
    arms="pointright",
    sweat="def"
)

image monika 4n = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="big",
    head="n",
    left="2l",
    right="2r",
    arms="pointright",
    sweat="def"
)

image monika 4o = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="o",
    left="2l",
    right="2r",
    arms="pointright",
    sweat="def"
)

image monika 4p = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="small",
    head="p",
    left="2l",
    right="2r",
    arms="pointright",
    sweat="def"
)

image monika 4q = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="closedsad",
    nose="def",
    mouth="smirk",
    head="q",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4r = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="closedsad",
    nose="def",
    mouth="small",
    head="r",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4efx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="disgust",
    head="h",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4efu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="smug",
    head="h",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4efd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="small",
    head="i",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4efc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="smirk",
    head="h",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4efb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="big",
    head="i",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4efw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="wide",
    head="i",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4efo = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="gasp",
    head="i",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4eftsu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="smug",
    head="i",
    left="2l",
    right="2r",
    arms="pointright",
    tears="streaming"
)

image monika 4wfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="wide",
    nose="def",
    mouth="disgust",
    head="h",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4wfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="wide",
    nose="def",
    mouth="wide",
    head="i",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4wud = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="wide",
    nose="def",
    mouth="small",
    head="d",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4wuo = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="wide",
    nose="def",
    mouth="gasp",
    head="b",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4wubsw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="wide",
    nose="def",
    mouth="wide",
    head="b",
    left="2l",
    right="2r",
    arms="pointright",
    blush="shade"
)

image monika 4wubso = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="wide",
    nose="def",
    mouth="gasp",
    head="b",
    left="2l",
    right="2r",
    arms="pointright",
    blush="shade"
)

image monika 4subftsb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="sparkle",
    nose="def",
    mouth="big",
    head="b",
    left="2l",
    right="2r",
    arms="pointright",
    blush="full",
    tears="streaming"
)

image monika 4sub = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="sparkle",
    nose="def",
    mouth="big",
    head="b",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4sutsa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="sparkle",
    nose="def",
    mouth="smile",
    head="a",
    left="2l",
    right="2r",
    arms="pointright",
    tears="streaming"
)

image monika 4tfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="disgust",
    head="h",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4tfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="smug",
    head="h",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4tfd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="small",
    head="i",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4tfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="smirk",
    head="h",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4tfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="smug",
    nose="def",
    mouth="big",
    head="i",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4tkx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="smug",
    nose="def",
    mouth="disgust",
    head="f",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4tku = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="smug",
    nose="def",
    mouth="smug",
    head="f",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4tkd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="smug",
    nose="def",
    mouth="small",
    head="g",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4tkc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="smug",
    nose="def",
    mouth="smirk",
    head="f",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4tsb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="smug",
    nose="def",
    mouth="big",
    head="i",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4tsbsa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="smug",
    nose="def",
    mouth="smile",
    head="a",
    left="2l",
    right="2r",
    arms="pointright",
    blush="shade"
)

image monika 4rfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="disgust",
    head="h",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4rfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="smug",
    head="h",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4rfd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="small",
    head="i",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4rfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="smirk",
    head="h",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4rfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="big",
    head="i",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4rfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="wide",
    head="i",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4rktsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="right",
    nose="def",
    mouth="smirk",
    head="f",
    left="2l",
    right="2r",
    arms="pointright",
    tears="streaming"
)

image monika 4lfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="disgust",
    head="h",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4lfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="smug",
    head="h",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4lfd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="small",
    head="i",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4lfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="h",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4lfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="big",
    head="i",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4lfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="wide",
    head="i",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4lud = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="left",
    nose="def",
    mouth="small",
    head="d",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4lsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="h",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4lssdrc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="o",
    left="2l",
    right="2r",
    arms="pointright",
    sweat="right"
)

image monika 4pp = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="small",
    head="p",
    left="2l",
    right="2r",
    arms="pointright",
    sweat="def"
)

image monika 4oo = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="o",
    left="2l",
    right="2r",
    arms="pointright",
    sweat="def"
)

image monika 4nn = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="big",
    head="n",
    left="2l",
    right="2r",
    arms="pointright",
    sweat="def"
)

image monika 4lksdlw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="wide",
    head="n",
    left="2l",
    right="2r",
    arms="pointright",
    sweat="def"
)

image monika 4mm = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smile",
    head="m",
    left="2l",
    right="2r",
    arms="pointright",
    sweat="def"
)

image monika 4lssdrb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="big",
    head="n",
    left="2l",
    right="2r",
    arms="pointright",
    sweat="right"
)

image monika 4lsbssdrb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="big",
    head="n",
    left="2l",
    right="2r",
    arms="pointright",
    sweat="right",
    blush="shade"
)

image monika 4lsbsa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="left",
    nose="def",
    mouth="smile",
    head="a",
    left="2l",
    right="2r",
    arms="pointright",
    blush="shade"
)

image monika 4lkbsa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smile",
    head="e",
    left="2l",
    right="2r",
    arms="pointright",
    blush="shade"
)

image monika 4lftsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="f",
    left="2l",
    right="2r",
    arms="pointright",
    tears="streaming"
)

image monika 4lktsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="left",
    nose="def",
    mouth="smirk",
    head="f",
    left="2l",
    right="2r",
    arms="pointright",
    tears="streaming"
)

image monika 4dfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="disgust",
    head="q",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4dfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="smug",
    head="q",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4dfd = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="small",
    head="r",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4dfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="smirk",
    head="q",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4dfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="big",
    head="r",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4dfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="wide",
    head="r",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4dso = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="closedsad",
    nose="def",
    mouth="gasp",
    head="r",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4dsbso = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="closedsad",
    nose="def",
    mouth="gasp",
    head="r",
    left="2l",
    right="2r",
    arms="pointright",
    blush="shade"
)

image monika 4dftsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="smirk",
    head="q",
    left="2l",
    right="2r",
    arms="pointright",
    tears="streaming"
)

image monika 4dftdc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedsad",
    nose="def",
    mouth="smirk",
    head="q",
    left="2l",
    right="2r",
    arms="pointright",
    tears="dried"
)

image monika 4duu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedsad",
    nose="def",
    mouth="smug",
    head="j",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4dubsu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedsad",
    nose="def",
    mouth="smug",
    head="j",
    left="2l",
    right="2r",
    arms="pointright",
    blush="shade"
)

image monika 4dubssdru = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedsad",
    nose="def",
    mouth="smug",
    head="j",
    left="2l",
    right="2r",
    arms="pointright",
    blush="shade",
    sweat="right"
)

image monika 4hfx = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="disgust",
    head="q",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4hfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="smug",
    head="j",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4hfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="smirk",
    head="q",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4hfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="k",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4hfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="closedhappy",
    nose="def",
    mouth="wide",
    head="r",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4ll = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="l",
    left="2l",
    right="2r",
    arms="pointright"
)

image monika 4hubfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="b",
    left="2l",
    right="2r",
    arms="pointright",
    blush="full"
)

image monika 4ekbfa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="a",
    left="2l",
    right="2r",
    arms="pointright",
    blush="full"
)

image monika 5a = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="",
    left="",
    right="",
    lean="def",
    single="3a"
)

image monika 5b = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="normal",
    nose="def",
    mouth="smirk",
    head="",
    left="",
    right="",
    lean="def",
    single="3b"
)

image monika 5hubfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedhappy",
    nose="def",
    mouth="big",
    head="",
    left="",
    right="",
    lean="def",
    blush="full",
    single="3b"
)

image monika 5efa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="",
    left="",
    right="",
    lean="def",
    single="3b"
)

image monika 5eua = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="smile",
    head="",
    left="",
    right="",
    lean="def",
    single="3b"
)

image monika 5wubfw = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="wide",
    nose="def",
    mouth="wide",
    head="",
    left="",
    right="",
    blush="full",
    lean="def",
    single="3b"
)

image monika 5eubfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="big",
    head="",
    left="",
    right="",
    blush="full",
    lean="def",
    single="3b"
)

image monika 5rubfsdrb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="right",
    nose="def",
    mouth="big",
    head="",
    left="",
    right="",
    blush="full",
    sweat="right",
    lean="def",
    single="3b"
)

image monika 5rubfsdru = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="right",
    nose="def",
    mouth="smug",
    head="",
    left="",
    right="",
    blush="full",
    sweat="right",
    lean="def",
    single="3b"
)

image monika 5rubfb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="right",
    nose="def",
    mouth="big",
    head="",
    left="",
    right="",
    blush="full",
    lean="def",
    single="3b"
)

image monika 5rubfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="right",
    nose="def",
    mouth="smug",
    head="",
    left="",
    right="",
    blush="full",
    lean="def",
    single="3b"
)

image monika 5rusdrb = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="right",
    nose="def",
    mouth="big",
    head="",
    left="",
    right="",
    sweat="right",
    lean="def",
    single="3b"
)

image monika 5rusdru = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="right",
    nose="def",
    mouth="smug",
    head="",
    left="",
    right="",
    sweat="right",
    lean="def",
    single="3b"
)


image monika 5rub = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="right",
    nose="def",
    mouth="big",
    head="",
    left="",
    right="",
    lean="def",
    single="3b"
)

image monika 5ruu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="right",
    nose="def",
    mouth="smug",
    head="",
    left="",
    right="",
    lean="def",
    single="3b"
)

image monika 5eubfu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="smug",
    head="",
    left="",
    right="",
    blush="full",
    lean="def",
    single="3b"
)

image monika 5eub = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="normal",
    nose="def",
    mouth="big",
    head="",
    left="",
    right="",
    lean="def",
    single="3b"
)

image monika 5rsc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="mid",
    eyes="right",
    nose="def",
    mouth="smirk",
    head="",
    left="",
    right="",
    lean="def",
    single="3b"
)

image monika 5rkc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="knit",
    eyes="right",
    nose="def",
    mouth="smirk",
    head="",
    left="",
    right="",
    lean="def",
    single="3b"
)

image monika 5rfc = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="furrowed",
    eyes="right",
    nose="def",
    mouth="smirk",
    head="",
    left="",
    right="",
    lean="def",
    single="3b"
)

image monika 6dubsa = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedsad",
    nose="def",
    mouth="smile",
    head="j",
    left="1l",
    right="1r",
    arms="down",
    blush="shade"
)

image monika 6dubsu = DynamicDisplayable(
    mas_drawmonika,
    character=monika_chr,
    eyebrows="up",
    eyes="closedsad",
    nose="def",
    mouth="smug",
    head="j",
    left="1l",
    right="1r",
    arms="down",
    blush="shade"
)
