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
            

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

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

class TitleTrigger(WordTrigger):

    def __init__(self,word):
        self.word = str.lower(word)

    def evaluate(self,story):
        self.Title = story.getTitle()
        return self.isWordIn(self.Title)
        

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
