import json


class Job:
    def __init__(self, title, company, start, end=None):
        self.title = title
        self.company = company
        self.start = start.strftime("%b %Y")
        if end:
            self.end = end.strftime("%b %Y")
        else:
            self.end = "present"
        self.duties = []
    
    def sortDuties(self):
        self.duties = sorted(self.duties, key=lambda _duty: _duty[1], reverse = True)
        
    def addDuty(self, duty, priority=1):
        self.duties.append((duty, priority))
        self.sortDuties()
    
    def __str__(self):
        self.sortDuties()
        print("%s - %s" %(self.company, self.title))
        print("%s - %s" %(self.start, self.end))
        for duty, priority in self.duties:
            print("%s" %(duty))
        print("\n")
    
    def output(self):
        filename = ("%s %s" %(self.company, self.title)).replace(" ", "-").lower()
        with open("%s.json" %(filename), 'w') as outfile:
            json.dump(self.__dict__, outfile, ensure_ascii=False, indent=4)