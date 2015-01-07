
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



def makeTrigger(triggerMap, triggerType, params, name):

    
    if triggerType == "SUBJECT":
        trig = SubjectTrigger(params)
    elif triggerType == "TITLE":
        trig = TitleTrigger(params)
    elif triggerType == "SUMMARY":
        trig = SummaryTrigger(params)
    elif triggerType == "PHRASE":
        trig = PhraseTrigger(params)
    elif triggerType == "NOT":
        trig = NotTrigger(params)
    elif triggerType == "AND":
        trig = AndTrigger(params)
    elif triggerType == "OR":
        trig = OrTrigger(params)
        
    triggerMap[name] = trig
    print triggerMap


makeTrigger({}, "PHRASE", "Qantas is stupid", "t4")
