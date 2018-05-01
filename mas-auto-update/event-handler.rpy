






image monika_waiting_img:
    "monika 1a"
    1.0
    "monika 1c"
    1.0
    "monika 1h"
    1.0
    "monika 1o"
    1.0
    "monika 1g"
    1.0
    repeat


transform prompt_monika:
    tcommon(950,z=0.8)

init -500 python:



    mas_init_lockdb_template = (
        True, 
        False, 
        False, 
        False, 
        True, 
        True, 
        True, 
        True, 
        True, 
        True, 
        True, 
        True, 
        True, 
        False, 
        False, 
        True 
    )


    if (
            persistent._mas_event_init_lockdb_template is not None
            and len(persistent._mas_event_init_lockdb_template)
                != len(mas_init_lockdb_template)
        ):
        
        
        for ev_key in persistent._mas_event_init_lockdb:
            stored_lock_row = persistent._mas_event_init_lockdb[ev_key]
            
            
            lock_row = list(mas_init_lockdb_template)
            lock_row[0:len(stored_lock_row)] = list(stored_lock_row)
            persistent._mas_event_init_lockdb[ev_key] = tuple(lock_row)


    persistent._mas_event_init_lockdb_template = mas_init_lockdb_template


    if persistent._mas_event_init_lockdb is None:
        persistent._mas_event_init_lockdb = dict()


    Event.INIT_LOCKDB = persistent._mas_event_init_lockdb


init -1 python in evhand:


    event_database = dict()
    farewell_database = dict()
    greeting_database = dict()


    from collections import namedtuple




    _NT_CAT_PANE = namedtuple("_NT_CAT_PANE", "menu cats")



    RIGHT_X = 1020

    RIGHT_Y = 40

    RIGHT_W = 250
    RIGHT_H = 640

    RIGHT_XALIGN = -0.10
    RIGHT_AREA = (RIGHT_X, RIGHT_Y, RIGHT_W, RIGHT_H)



    LEFT_X = 735

    LEFT_Y = RIGHT_Y

    LEFT_W = RIGHT_W
    LEFT_H = RIGHT_H

    LEFT_XALIGN = -0.10
    LEFT_AREA = (LEFT_X, LEFT_Y, LEFT_W, LEFT_H)

    UNSE_X = 680
    UNSE_Y = 40
    UNSE_W = 560
    UNSE_H = 640
    UNSE_XALIGN = -0.05
    UNSE_AREA = (UNSE_X, UNSE_Y, UNSE_W, UNSE_H)


    import datetime
    LAST_SEEN_DELTA = datetime.timedelta(hours=2)


    def addIfNew(items, pool):
        
        
        
        
        
        
        
        
        
        
        
        for item in items:
            if item not in pool:
                pool.append(item)
        return pool

    def tuplizeEventLabelList(key_list, db):
        
        
        
        
        
        
        
        
        
        
        
        
        return [(db[x].prompt, x) for x in key_list]

init python:
    import store.evhand as evhand

    def addEvent(event, eventdb=evhand.event_database):
        
        
        
        
        
        
        
        
        
        
        if type(eventdb) is not dict:
            raise EventException("Given db is not of type dict")
        if type(event) is not Event:
            raise EventException("'" + str(event) + "' is not an Event object")
        if not renpy.has_label(event.eventlabel):
            raise EventException("'" + event.eventlabel + "' does NOT exist")
        if event.conditional is not None:
            eval(event.conditional)
        
        
        
        
        
        
        
        eventdb.setdefault(event.eventlabel, event)


    def hideEventLabel(
            eventlabel,
            lock=False,
            derandom=False,
            depool=False,
            decond=False,
            eventdb=evhand.event_database
        ):
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ev = eventdb.get(eventlabel, None)
        
        hideEvent(
            ev,
            lock=lock,
            derandom=derandom,
            depool=depool,
            decond=decond
        )


    def hideEvent(
            event,
            lock=False,
            derandom=False,
            depool=False,
            decond=False
        ):
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if event:
            
            if lock:
                event.unlocked = False
            
            if derandom:
                event.random = False
            
            if depool:
                event.pool = False
            
            if decond:
                event.conditional = None


    def lockEvent(ev):
        """
        Locks the given event object

        IN:
            ev - the event object to lock
        """
        hideEvent(ev, lock=True)


    def lockEventLabel(evlabel, eventdb=evhand.event_database):
        """
        Locks the given event label

        IN:
            evlabel - event label of the event to lock
            eventdb - Event database to find this label
        """
        hideEventLabel(evlabel, lock=True, eventdb=eventdb)


    def pushEvent(event_label):
        
        
        
        
        
        
        
        
        
        
        persistent.event_list.append(event_label)
        return

    def queueEvent(event_label):
        
        
        
        
        
        
        
        
        
        
        persistent.event_list.insert(0,event_label)
        return


    def unlockEvent(ev):
        """
        Unlocks the given evnet object

        IN:
            ev - the event object to unlock
        """
        if ev:
            ev.unlocked = True


    def unlockEventLabel(evlabel, eventdb=evhand.event_database):
        """
        Unlocks the given event label

        IN:
            evlabel - event label of the event to lock
            eventdb - Event database to find this label
        """
        unlockEvent(eventdb.get(evlabel, None))


    def isFuture(ev, date=None):
        """
        Checks if the start_date of the given event happens after the
        given time.

        IN:
            ev - Event to check the start_time
            date - a datetime object used to check against
                If None is passed it will check against current time
                (Default: None)

        RETURNS:
            True if the Event's start_date is in the future, False otherwise
        """
        
        
        if ev is None:
            return False
        
        
        if date is None:
            date = datetime.datetime.now()
        
        start_date = ev.start_date
        
        
        if start_date is None:
            return False
        
        return date < start_date


    def isPast(ev, date=None):
        """
        Checks if the end_date of the given event happens before the
        given time.

        IN:
            ev - Event to check the start_time
            date - a datetime object used to check against
                If None is passed it will check against current time
                (Default: None)

        RETURNS:
            True if the Event's end_date is in the past, False otherwise
        """
        
        
        if ev is None:
            return False
        
        
        if date is None:
            date = datetime.datetime.now()
        
        end_date = ev.end_date
        
        
        if end_date is None:
            return False
        
        return end_date < date


    def isPresent(ev):
        """
        Checks if current date falls within the given event's start/end date
        range

        IN:
            ev - Event to check the start_time and end_time

        RETURNS:
            True if current time is inside the  Event's start_date/end_date
            interval, False otherwise
        """
        
        if ev is None:
            return False
        
        start_date = ev.start_date
        end_date = ev.end_date
        
        current = datetime.datetime.now()
        
        
        if start_date is None or end_date is None:
            return False
        
        return start_date <= current <= end_date


    def popEvent(remove=True):
        
        
        
        
        
        
        
        
        
        
        
        
        if len(persistent.event_list) == 0:
            return None
        elif remove:
            event_label = persistent.event_list.pop()
            persistent.current_monikatopic = event_label
        else:
            event_label = persistent.event_list[-1]
        
        return event_label

    def seen_event(event_label):
        
        
        
        
        
        
        
        
        
        if renpy.seen_label(event_label) or event_label in persistent.event_list:
            return True
        else:
            return False


    def restartEvent():
        
        
        
        
        
        
        if persistent.current_monikatopic:
            
            if (not persistent.current_monikatopic.startswith('greeting_')
                    and not persistent.current_monikatopic.startswith('i_greeting')
                    and not persistent.current_monikatopic.startswith('bye')
                    and not persistent.current_monikatopic.startswith('ch30_reload')
                ):
                pushEvent(persistent.current_monikatopic)
                pushEvent('continue_event')
                persistent.current_monikatopic = 0
        return


    def mas_cleanJustSeen(eventlist, db):
        """
        Cleans the given event list of just seen items (withitn the THRESHOLD)
        retunrs not just seen items

        IN:
            eventlist - list of event labels to pick from
            db - database these events are tied to

        RETURNS:
            cleaned list of events (stuff not in the time THREASHOLD)
        """
        import datetime
        now = datetime.datetime.now()
        cleanlist = list()
        
        for evlabel in eventlist:
            ev = db.get(evlabel, None)
            
            if ev:
                if ev.last_seen:
                    if now - ev.last_seen >= store.evhand.LAST_SEEN_DELTA:
                        cleanlist.append(evlabel)
                
                else:
                    cleanlist.append(evlabel)
        
        return cleanlist








label call_next_event:


    $ event_label = popEvent()
    if event_label and renpy.has_label(event_label):
        $ allow_dialogue = False
        if not seen_event(event_label):
            $ grant_xp(xp.NEW_EVENT)
        call expression event_label from _call_expression
        $ persistent.current_monikatopic=0


        $ ev = evhand.event_database.get(event_label, None)
        if ev is not None:
            if ev.random and not ev.unlocked:
                python:
                    ev.unlocked=True
                    ev.unlock_date=datetime.datetime.now()


            $ ev.shown_count += 1
            $ ev.last_seen = datetime.datetime.now()

        if _return == 'quit':
            $ persistent.closed_self = True
            jump _quit


        $ allow_dialogue = len(persistent.event_list) == 0
        show monika 1 zorder 2 at t11 with dissolve
    else:
        return False

    return event_label



label unlock_prompt:
    python:
        pool_events = Event.filterEvents(evhand.event_database,unlocked=False,pool=True)
        pool_event_keys = [
            evlabel
            for evlabel in pool_events
            if "no unlock" not in pool_events[evlabel].rules
        ]

        if len(pool_event_keys)>0:
            sel_evlabel = renpy.random.choice(pool_event_keys)
            
            evhand.event_database[sel_evlabel].unlocked = True
            evhand.event_database[sel_evlabel].unlock_date = datetime.datetime.now()

    return





label prompt_menu:
    $ allow_dialogue = False

    python:
        unlocked_events = Event.filterEvents(evhand.event_database,unlocked=True)
        sorted_event_keys = Event.getSortedKeys(unlocked_events,include_none=True)

        unseen_events = []
        for event in sorted_event_keys:
            if not seen_event(event):
                unseen_events.append(event)

        repeatable_events = Event.filterEvents(evhand.event_database,unlocked=True,pool=False)

    show monika at t21

    python:
        talk_menu = []
        if len(unseen_events)>0:
            talk_menu.append(("{b}Неувиденное.{/b}", "unseen"))
        talk_menu.append(("Спросить вопрос.", "prompt"))
        if len(repeatable_events)>0:
            talk_menu.append(("Повторить разговор.", "repeat"))
        talk_menu.append(("Я чувствую себя...", "moods"))
        talk_menu.append(("До свидания.", "goodbye"))
        talk_menu.append(("Забудь.","nevermind"))

        renpy.say(m, "О чем ты хочешь поговорить?", interact=False)
        madechoice = renpy.display_menu(talk_menu, screen="talk_choice")

    if madechoice == "unseen":
        call show_prompt_list (unseen_events) from _call_show_prompt_list

    elif madechoice == "prompt":
        call prompts_categories (True) from _call_prompts_categories

    elif madechoice == "repeat":
        call prompts_categories (False) from _call_prompts_categories_1

    elif madechoice == "moods":
        call mas_mood_start from _call_mas_mood_start
        if not _return:
            jump prompt_menu

    elif madechoice == "goodbye":
        call mas_farewell_start from _call_select_farewell
    else:

        $ _return = None

    show monika at t11
    $ allow_dialogue = True
    jump ch30_loop

label show_prompt_list(sorted_event_keys):
    $ import store.evhand as evhand


    python:
        prompt_menu_items = []
        for event in sorted_event_keys:
            prompt_menu_items.append([unlocked_events[event].prompt,event])

    call screen scrollable_menu(prompt_menu_items, evhand.UNSE_AREA, evhand.UNSE_XALIGN)

    $ pushEvent(_return)

    return

label prompts_categories(pool=True):



    $ cat_lists = list()

    $ current_category = list()
    $ import store.evhand as evhand
    $ picked_event = False
    python:


        unlocked_events = Event.filterEvents(
            evhand.event_database,


            unlocked=True,
            pool=pool
        )


        main_cat_list = list()
        no_cat_list = list() 
        for key in unlocked_events:
            if unlocked_events[key].category:
                evhand.addIfNew(unlocked_events[key].category, main_cat_list)
            else:
                no_cat_list.append(unlocked_events[key])


        main_cat_list.sort()
        no_cat_list.sort(key=Event.getSortPrompt)




        dis_cat_list = [(x.capitalize() + "...",x) for x in main_cat_list]



        no_cat_list = [(x.prompt, x.eventlabel) for x in no_cat_list]


        dis_cat_list.extend(no_cat_list)


        cat_lists.append(evhand._NT_CAT_PANE(dis_cat_list, main_cat_list))

    while not picked_event:
        python:
            prev_items, prev_cats = cat_lists[len(cat_lists)-1]


            if len(current_category) == 0:
                main_items = None

            else:
                
                
                
                
                
                
                unlocked_events = Event.filterEvents(
                    evhand.event_database,

                    category=(False,current_category),
                    unlocked=True,
                    pool=pool
                )
                
                
                
                
                
                
                
                no_cat_list = sorted(
                    unlocked_events.values(),
                    key=Event.getSortPrompt
                )
                
                
                no_cat_list = [(x.prompt, x.eventlabel) for x in no_cat_list]
                
                
                
                
                
                main_cats = []
                
                
                main_items = no_cat_list
                
                """ KEEP this for legacy purposes
#            sorted_event_keys = Event.getSortedKeys(unlocked_events,include_none=True)

            prompt_category_menu = []
            #Make a list of categories

            #Make a list of all categories
            subcategories=set([])
            for event in sorted_event_keys:
                if unlocked_events[event].category is not None:
                    new_categories=set(unlocked_events[event].category).difference(set(current_category))
                    subcategories=subcategories.union(new_categories)

            subcategories = list(subcategories)
            for category in sorted(subcategories, key=lambda s: s.lower()):
                #Don't list additional subcategories if adding them wouldn't change the same you are looking at
                test_unlock = Event.filterEvents(evhand.event_database,full_copy=True,category=[False,current_category+[category]],unlocked=True)

                if len(test_unlock) != len(sorted_event_keys):
                    prompt_category_menu.append([category.capitalize() + "...",category])


            #If we do have a category picked, make a list of the keys
            if sorted_event_keys is not None:
                for event in sorted_event_keys:
                    prompt_category_menu.append([unlocked_events[event].prompt,event])
                """

        call screen twopane_scrollable_menu(prev_items, main_items, evhand.LEFT_AREA, evhand.LEFT_XALIGN, evhand.RIGHT_AREA, evhand.RIGHT_XALIGN, len(current_category)) nopredict



        if _return in prev_cats:

            python:
                if len(current_category) > 0:
                    current_category.pop()
                current_category.append(_return)











        elif _return == -1:
            if len(current_category) > 0:
                $ current_category.pop()
        else:

            $ picked_event = True
            $ pushEvent(_return)

    return