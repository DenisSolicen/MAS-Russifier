label ch30_monikamovie:
    init python:
        gamedir = os.path.normpath(config.gamedir)




        class AvaiableMovies:
            def __init__(self):
                self.listOfMovies = []
                self.checkMovies()
            
            def checkMovies(self):
                with open(os.path.join(gamedir, "movies-info.mms"),"r") as f: 
                    lines = f.readlines()
                listOfStrings = [x.strip() for x in lines]
                
                
                for line in listOfStrings:
                    if "#" in line:
                        continue
                    partialSplittedSentence = line.split(" ", 1)
                    firstWord = ""
                    if len(partialSplittedSentence) >= 2:
                        firstWord = partialSplittedSentence[0]
                        data = partialSplittedSentence[1]
                    if "movie" in firstWord:
                        self.listOfMovies.append(data)
            
            def searchMovies(self, movieName):
                foundMovies = []
                for xName in self.listOfMovies:
                    if movieName.lower() in xName.lower():
                        foundMovies.append(xName)
                return foundMovies

        class ParsedMovie:
            def __init__(self, movieName):
                self.descriptionList = []
                self.reactionList = []
                self.closureList = []
                self.currentReactionIndex = 0 
                self.retrieveMovie(movieName)
            
            def reactionsAreFinished(self):
                return self.currentReactionIndex >= len(self.reactionList)
            
            def stringReactionToTuple(self, string):
                emotion = None
                when = ""
                what = ""
                listOfInfo = []
                if not string[0] == "[": 
                    listOfInfo = string.split(" ", 2)
                    emotion = listOfInfo [0]
                    when = listOfInfo [1]
                    what = listOfInfo [2]
                else:
                    listOfInfo = string.split(" ", 1)
                    when = listOfInfo [0]
                    what = listOfInfo [1]
                return emotion,when,what
            
            def formattedTimeToSeconds(self, string):
                string = string.replace('[','')
                string = string.replace(']','')
                infoList = string.split(":")
                hours = int(infoList[0])
                minutes = int(infoList[1])
                seconds = int(infoList[2])
                return 3600*hours + 60*minutes + seconds
            
            def obtainCurrentReactionTuple(self):
                string = self.reactionList[self.currentReactionIndex]
                emotion, when, what = self.stringReactionToTuple(string)
                return emotion,when,what
            
            def popReaction(self):
                emotion, when, what = self.obtainCurrentReactionTuple()
                self.currentReactionIndex += 1
                return emotion,when,what
            
            
            def canReact(self, time):
                if(self.reactionsAreFinished()):
                    return False
                emotion, when, what = self.obtainCurrentReactionTuple()
                
                expectedToReact = self.formattedTimeToSeconds(when)
                return time > expectedToReact
            
            
            def popDescription(self):
                string = self.descriptionList.pop(0)
                stringArray = string.split(" ", 1)
                emotion = stringArray[0]
                line = stringArray[1]
                
                return emotion, line
            
            def hasDescription(self):
                return len(self.descriptionList) > 0
            
            def popClosure(self):
                string = self.closureList.pop(0)
                stringArray = string.split(" ", 1)
                emotion = stringArray[0]
                line = stringArray[1]
                
                return emotion, line
            
            def hasClosure(self):
                return len(self.closureList) > 0
            
            def formatData(self, data):
                return data.replace('"','')
            
            def retrieveMovie(self, movieName):
                with open(os.path.join(gamedir, "movies-info.mms"),"r") as f:
                    lines = f.readlines()
                listOfStrings = [x.strip() for x in lines]
                
                
                filmFound = False
                for line in listOfStrings:
                    if "#" in line:
                        continue
                    partialSplittedSentence = line.split(" ", 1)
                    firstWord = ""
                    if len(partialSplittedSentence) >= 2:
                        firstWord = partialSplittedSentence[0]
                        data = partialSplittedSentence[1]
                        data = self.formatData(data)
                    if "movie" in firstWord:
                        filmFound = movieName == partialSplittedSentence[1]
                    if filmFound:
                        if "description" == firstWord:
                            self.descriptionList.append(data)
                        if "m" == firstWord:
                            self.reactionList.append(data)
                        if "closure" == firstWord:
                            self.closureList.append(data)
            
            def resynchronizeIndex(self, timer):
                self.currentReactionIndex = 0
                while((not (self.reactionsAreFinished())) and self.canReact(timer.seconds)):
                    self.currentReactionIndex += 1


        class MovieTimer:
            def __init__(self):
                self.seconds = 0
            def seconds(self):
                return self.seconds
            def addSeconds(self, secondsAdded):
                self.seconds += secondsAdded
            def formattedTime(self):
                secondsPool = self.seconds
                hours = int(secondsPool / 3600)
                secondsPool -= hours * 3600
                minutes = int(secondsPool / 60)
                secondsPool -= minutes * 60
                secs = secondsPool
                return hours, minutes, secs
            def setFormattedTime(self,hours,minutes,seconds):
                self.seconds = int(hours)*3600 + int(minutes)*60 + int(seconds)



        def iterate_timer(st, at, timer):
            
            deltaTime = st - globals()['lastCountdownTime']
            globals()['lastCountdownTime'] = st
            if watchingMovie:
                timer.addSeconds(deltaTime)
            
            
            hours, minutes, secs = timer.formattedTime()
            d = Text("%02d:%02d:%02d" % (hours, minutes, secs))
            return d, 0.1
        def fastforward(timer,secondsAdded):
            timer.addSeconds(secondsAdded)

        def updateEmotionMonika(emotion):
            if emotion is not None:
                monika_reaction = "monika %s" % (emotion)
                renpy.show(monika_reaction)



        watchingMovie = False
        lastCountdownTime = 0 
        firstComment = False
        timer = MovieTimer()




    $ listMovies = AvaiableMovies()

    m 1b "Ты хочешь посмотреть фильм?"
    label mm_choose_movie:
        menu:
            "Можешь сказать название?"
            "Да":
                python:
                    player_dialogue = renpy.input('Какое оно? ',default='',pixel_width=720,length=50)
                    allFilms = listMovies.searchMovies(player_dialogue)
                    foundAnyFilm = len(allFilms) > 0
                if foundAnyFilm:
                    while (len(allFilms)>0):
                        $ renpy.say(eval("m"), "Я нашла фильм с названием %s" % (allFilms[0]) )
                        menu:
                            "Ты хотел посмотреть именно его?"
                            "Да":
                                m 1b "Клево! Давай посмотрим его вместе."
                                $ movieInformation = ParsedMovie(allFilms[0])
                                jump mm_found_movie
                            "Нет":
                                $ allFilms.pop(0)
                                m 1a "Я поищу заново."
                    m 1l "Прости, [player], я не могу найти фильм с таким названием."
                    show monika 1a
                else:
                    m 1f "Я не нашла фильм с таким названием, [player]. Прости."
                m "Может попробуешь что-нибудь другое"
                jump mm_choose_movie
            "Какой фильм я могу посмотреть?":

                m 1a "Давай посмотрим..."
                python:
                    LENGTH_RESTRICTION = 70
                    movieBuffer = ""
                    while(len(listMovies.listOfMovies) > 0):
                        movieBuffer += listMovies.listOfMovies.pop(0)
                        if len(movieBuffer) > LENGTH_RESTRICTION:
                            renpy.say(eval("m"), movieBuffer + "...")
                            movieBuffer = ""
                        else:
                            movieBuffer += ", "
                    if len(movieBuffer) > 0:
                        reemplacementBuffer = movieBuffer.rsplit(",",1)
                        movieBuffer = reemplacementBuffer[0] + "..."
                        renpy.say(eval("m"), movieBuffer)
                m 1a "И это всё."
                $ listMovies = AvaiableMovies()
                jump mm_choose_movie
            "Забудь":

                m 1j "Хорошо! Тогда, может быть позже."
                jump mm_movie_loop_end


    label mm_found_movie:
        $ MovieOverlayShowButtons()
        stop music fadeout 2.0
        image countdown = DynamicDisplayable(iterate_timer, timer)
        show countdown at topleft

        python:
            while(movieInformation.hasDescription()):
                emotion, what =  movieInformation.popDescription()
                updateEmotionMonika(emotion)
                renpy.say(eval("m"), what)
        m 3b "Давай синхронизируем начало фильма."
        m 1k "Приготовься начать просмотр, я начинаю обратный отчет!"

        menu:
            "Готов?"
            "Да":
                label mm_movie_resume:
                    $ allow_dialogue = False
                    m 1a "Три...{w=1}{nw}"
                    m "Да...{w=1}{nw}"
                    m "Один...{w=1}{nw}"

                    $ watchingMovie = True
                    label movie_loop:
                        pause 1.0
                        python:
                            if movieInformation.canReact(timer.seconds):
                                emotion, when, what = movieInformation.popReaction()
                                updateEmotionMonika(emotion)
                                
                                if not (what == "" or what is None):
                                    what += "{w=10}{nw}"
                                    renpy.say(eval("m"), what)

                        if movieInformation.reactionsAreFinished():
                            hide countdown
                            $ MovieOverlayHideButtons()
                            m 1a "Просто закончилось для меня! А тебе понравилось?"
                            jump mm_movie_closure

                        jump movie_loop
            "Нет":

                hide countdown
                $ MovieOverlayHideButtons()
                m 1a "Ох, ладно! Тогда просто буду ждать тебя~"
                jump mm_movie_loop_end

        label mm_movie_closure:

            python:
                while(movieInformation.hasClosure()):
                    emotion, what =  movieInformation.popClosure()
                    updateEmotionMonika(emotion)
                    renpy.say(eval("m"), what)



    label mm_movie_loop_end:
        hide countdown
        $ allow_dialogue = True
        $ watchingMovie = False
        $ timer.seconds = 0
        $ MovieOverlayHideButtons()
        $ play_song(store.songs.selected_track)
        show monika 1a
        jump ch30_loop

    label mm_movie_pausefilm:
        $ watchingMovie = False
        m 1b "Ох, ты поставил фильм на паузу, [player]."
        menu:
            "Хочешь продолжить?"
            "Да":
                m 1j "Отлично, [player]."
                jump mm_movie_resume
            "Нет":
                m 1a "Ох, тогда все нормально, [player]."
                jump mm_movie_loop_end

    label mm_movie_settime:
        $ watchingMovie = False
        m 1b "Ты хочешь синхронизировать время?"
        label mm_movie_repeattime:
            m 1b "Скажи мне его в формате HH:MM:SS, [player]."
            python:
                player_dialogue = renpy.input('Какое время я должна установить? ',default='',pixel_width=720,length=50)
                splittedTime = player_dialogue.split(":",2)
                bad_format = len(splittedTime) != 3
                if not bad_format:
                    hours = splittedTime[0]
                    minutes = splittedTime[1]
                    seconds = splittedTime[2]
                    bad_format = not (hours.isdigit() and minutes.isdigit() and seconds.isdigit())
                    if not bad_format:
                        bad_format = int(minutes) >= 60 or int(seconds) >= 60
            if bad_format:
                m 1o "Эмм..."
                m 1n "Прости,я не понимаю этого, [player]."
                m 1e "Помни время должно быть в формате HH:MM:SS."
                m 3a "Это 'Часы:Минуты:Секунды.'"
                m "Вот пример, [player]."
                m "01:05:32"
                m 1b "Это 1 час, 5 минут и 32 секунды."
                m 3j "Поэтому попробуй снова!"
                jump mm_movie_repeattime
            else:
                $ timer.setFormattedTime(splittedTime[0],splittedTime[1],splittedTime[2])
                $ movieInformation.resynchronizeIndex(timer)
        m 1a "Сделано! Давай смотреть!"
        jump mm_movie_resume