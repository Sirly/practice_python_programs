# File: wordChart.py
# Kevin Nakashima
#   Takes a text file
#       Program will count the number of times each word occurs in file
#       Program will print out a histogram of words and frequencies
#==============================================================================
# RESOURCES
#   http://programminghistorian.org/lessons/counting-frequencies
#   http://moderndata.plot.ly/generate-html-reports-with-python-pandas-and-plotly/
#   https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
#   https://www.tutorialspoint.com/python/python_dictionary.htm
#   http://help.plot.ly/embed-graphs-in-websites/
# IMPORTS


# CLASS DECLARATIONS
class report():
    __slots__ = ['word','wordlist','fName','shortest','longtest','most','least']
    def __init__(self, fName):
        self.word = ""
        self.wordlist = {}
        self.fName = fName
        self.shortest = ""
        self.longest = ""
        self.most = ""
        self.least = ""
        
    def addWord(self):
        self.word = self.word.lower()
        if len(self.word) == 1:
            self.shortest = self.word
        if len(self.word) > len(self.longest):
            self.longest = self.word
        if self.word in self.wordlist:
            #if dictionary has word, increment frequency
            self.wordlist[self.word] = self.wordlist[self.word] + 1
        else:#if not in dictionary, create
            self.wordlist[self.word] = 1
            #reset word
        self.word = ""

    def mostLeast(self):
        self.most = max(self.wordlist, key=self.wordlist.get)
        self.least = min(self.wordlist, key=self.wordlist.get)

    
    def writeReport(self, f):
        self.mostLeast()
        outFile = open(f + ".html", 'w')
        outFile.write('''<!doctype html>\n
              <html>\n
              <head>\n
              <title>\n''')
        outFile.write(self.fName + "Analysis")
        outFile.write('''</title>\n
              <meta name="description" content="Our first page">\n
              <meta name="keywords" content="html tutorial template">\n
              </head>\n
              <body>\n''')
        outFile.write("<p>Longest Word:  {}</p>".format(self.longest))
        outFile.write("<p>Shortest Word:  {}</p>".format(self.shortest))
        outFile.write("<p>Word used most:  {}</p>".format(self.most))
        outFile.write("<p>Word used least:  {}</p>".format(self.least))
        for keys, values in self.wordlist.items():
            line = "<p>{} : {} </p>".format(keys, values)
            outFile.write(line)
        outFile.write("</body>\n\
              </html>")
        #close output File
        outFile.close()

def main():
    #variable declarations
    r = report(input("Enter the file name: "))
    #open file to read
    with open(r.fName) as f:
        while True:
            #read one character at a time
            c = f.read(1)            
            #if not alphanumeric, ignore
            if c.isalpha():
                r.word += c
            elif c == ' ' or c == '\n':
                r.addWord()
            elif not c:
                r.addWord()
                break

    f = r.fName.split('.')
    r.writeReport(f[0])
    
main()
