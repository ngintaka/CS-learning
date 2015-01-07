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

story1 = NewsStory('abc','Dog Saves Master','A doggie saved his master', 'A dog jumped into the lake to save his master', 'www.dogstory.com')
story2 = NewsStory('def','Cat Saves Master','A pussy saved his master', 'A cat jumped into the lake to save his master', 'www.catstory.com')
