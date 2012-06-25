#!/usr/bin/python
# -*- coding: utf-8 -*-

#author: sullenlook <sullenlook@sullenlook.eu>
#project: SiriServerCore
#german stein_schere_papier plugin


from plugin import *
import urllib
from BeautifulSoup import BeautifulSoup
from siriObjects.baseObjects import AceObject, ClientBoundCommand
from siriObjects.uiObjects import AddViews, AssistantUtteranceView
from siriObjects.answerObjects import AnswerSnippet, AnswerObject, AnswerObjectLine


class stein_schere_papier(Plugin):

	res = {
		'1': {
			'de-DE': '.*(stein).*',
		},
		'2': {
			'de-DE': '.*(schere).*',
		},
		'3': {
			'de-DE': '.*(papier).*',
		}
	}

	#@register("de-DE", res(.*['1'].*|.*['2'].*|.*['3'].*)['de-DE'])
	@register("de-DE", ".*stein.*|.*schere.*|.*papier.*")
	def stein_schere_papier_get(self, speech, language):
        if language == 'de-DE':
            self.say("Ok {0} lass ins spielen. Du faengst an.".format(self.user_name()))
	    answer = self.ask(u"3, 2, 1, deine Antwort?")
            answer = self.ask(u"\"{0}\" Ok!".format(answer))
            self.say(u"Meine Antwort ist")
	    answer2 = self.say(random.choice(rep))
            self.say(u"\"{0}\" {1} hat gewonnen.").format(answer,answer2))
            self.say(u"Naechste Runde")
	self.complete_request()

#        elif language == 'fr-FR':
#            answer = self.ask(u"Qui est lÃ  ?")
#            answer2 = self.ask(u"{0} qui ?".format(answer))
#            self.say(u"{0} {1} ? Qui est-ce ? Je ne le connais pas.".format(answer,answer2))
#            self.say(u"Je prÃ©fÃ¨re ne pas rÃ©agir Ã  cette blague.")
#		self.complete_request()
#	self.say(random.choice(rep))