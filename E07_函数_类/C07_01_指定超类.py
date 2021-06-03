class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']


s = SPAMFilter()
s.init()
x = s.filter(['SPAM', 'SPAM', 'eggs', 'SPAM', 'SPAM', 'bacon'])
print(x)
