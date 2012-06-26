#!/usr/bin/python
# -*- coding: utf-8 -*-

#author: sullenlook <sullenlook@sullenlook.eu>
#project: SiriServerCore
#german stein_schere_papier plugin


from plugin import *

class steinscherepapier(Plugin):

    @register("de-DE", ".*stein .*schere .*papier.*")
    def st_knock(self, speech, language):
        if language == 'de-DE':
            rep = ["Stein","Schere","Papier"]
            rep2 = ["Du hast Gewonnen!","Ich hab Gewonnen!","Unendschieden wir muessen wiederholen!"]
            answer = self.ask(u"Ok lass uns Spielen! Du faengst an")
            answer = self.ask(random.choice(rep))
            answer = self.ask(random.choice(rep))
            self.say(random.choice(rep))
            self.say(random.choice(rep2))
        self.complete_request()