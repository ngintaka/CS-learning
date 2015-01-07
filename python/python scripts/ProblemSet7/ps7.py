# 6.00.1x Problem Set 7
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *


#-----------------------------------------------------------------------
#
# Problem Set 7

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def getGuid(self):
        return self.guid

    def getTitle(self):
        return self.title

    def getSubject(self):
        return self.subject


    def getSummary(self):
        return self.summary

    def getLink(self):
        return self.link
            

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

class WordTrigger(Trigger):
    def __init__(self,word):
        self.word = str.lower(word)


    def isWordIn(self,text):
        import string
        self.text = string.lower(text)
        for i in string.punctuation:
            self.text = self.text.replace(i,' ')
        self.text = self.text.split(' ')
        count = 0
        for n in self.text:
            if self.word == n:
                count += 1
        if count > 0:
            return True
        else:
            return False

    
        
# TODO: TitleTrigger
class TitleTrigger(WordTrigger):

    def evaluate(self,story):
        self.Tit = story.getTitle()
        return self.isWordIn(self.Tit)
        
# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):

    def evaluate(self,story):
        self.Sub = story.getSubject()
        return self.isWordIn(self.Sub)


# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):

    def evaluate(self,story):
        self.Sum = story.getSummary()
        return self.isWordIn(self.Sum)

# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
class NotTrigger(Trigger):

    def __init__(self,trigger):
        self.trig = trigger

    def evaluate(self,story):
        self.story = story
        return not self.trig.evaluate(story)

# TODO: AndTrigger
class AndTrigger(Trigger):


    def __init__(self,trigger1,trigger2):
        self.trig1 = trigger1
        self.trig2 = trigger2

    def evaluate(self,story):
        self.story = story
        if self.trig1.evaluate(story) + self.trig2.evaluate(story) >1:
            return True
        else:
            return False


# TODO: OrTrigger
class OrTrigger(Trigger):


    def __init__(self,trigger1,trigger2):
        self.trig1 = trigger1
        self.trig2 = trigger2

    def evaluate(self,story):
        self.story = story
        if self.trig1.evaluate(story) + self.trig2.evaluate(story) >0:
            return True
        else:
            return False


# Phrase Trigger
class PhraseTrigger(Trigger):

    def __init__(self,pt):
        self.pt = pt
        
    def evaluate(self,story):
        self.story = story
        s = story.getTitle() + story.getSubject() + story.getSummary()
        if self.pt in s:
            return True
        else:
            return False


# Question 9

# TODO: PhraseTrigger

#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    final = []
    #print 'TRIGGGERLIST',triggerlist
    for s in stories:
        for t in triggerlist:
            if t.evaluate(s):
                final.append(s)
                break
         
     
    return final

#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(triggerMap, triggerType, params, name):

    if triggerType == "SUBJECT":
        params = " ".join(params)
        trig = SubjectTrigger(params)
    elif triggerType == "TITLE":
        params = " ".join(params)
        trig = TitleTrigger(params)
    elif triggerType == "SUMMARY":
        params = " ".join(params)
        trig = SummaryTrigger(params)
    elif triggerType == "PHRASE":
        params = " ".join(params)
        trig = PhraseTrigger(params)
    elif triggerType == "NOT":
        trig = NotTrigger(triggerMap[params[0]])
    elif triggerType == "AND":
        trig = AndTrigger(triggerMap[params[0]], triggerMap[params[1]])

    elif triggerType == "OR":
        trig = OrTrigger(triggerMap[params[0]], triggerMap[params[1]])
        
    triggerMap[name] = trig
    return trig


def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    #print "TRIGGERMAP",triggerMap
    #print "TRIGGERS",triggers
    return triggers
    
import thread

SLEEPTIME = 10 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        #t1 = TitleTrigger("surfer")
       # t2 = SubjectTrigger("Google")
       # t3 = PhraseTrigger("France")
       # t4 = OrTrigger(t2, t3)
       # triggerlist = [t1, t4]
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        triggerlist = readTriggerConfig("triggers.txt")
        #print 'TRIGGERLIST',triggerlist

        # **** from here down is about drawing ****
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
        
        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)

        # Gather stories
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            # Process the stories
            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception, e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Flynn News Service")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()

