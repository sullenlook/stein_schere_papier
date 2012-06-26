#!/usr/bin/python
# -*- coding: utf-8 -*-

#author: sullenlook <sullenlook@sullenlook.eu>
#project: SiriServerCore
#german stein_schere_papier plugin


from plugin import *
from BeautifulSoup import BeautifulSoup
import feedparser
import random
import re
import urllib2, urllib, uuid
import json
from xml.dom import minidom

class steinscherepapier(Plugin):

    @register("de-DE", ".*stein .*schere .*papier.*")
    def st_stein(self, speech, language):
        if language == 'de-DE':
            rep = ["Stein","Schere","Papier"]
            rep2 = ["Du hast Gewonnen!","Ich hab Gewonnen!","Unendschieden wir muessen wiederholen!"]
            answer = self.ask(u"Ok lass uns Spielen! Du faengst an")
            answer = self.ask(random.choice(rep))
            answer = self.ask(random.choice(rep))
            self.say(random.choice(rep))
            self.say(random.choice(rep2))
        self.complete_request()