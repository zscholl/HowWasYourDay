#########################################################################
#   This is the main class for How Was Your Day, a journaling and goal  #
# tracking application.                                                 #
#                                                                       #
#  Author: Zak Scholl                                                   #
#  Email:                                                               #
#  Last Update: 7/3/2015                                                #
#                                                                       #
#  Known Bugs:                                                          #
#                                                                       # 
#########################################################################

import xml.etree.cElementTree as ElementTree
from Tkinter import *

class HowWasYourDay:

    def __init__(self):
        """
        Initializes an instance of the application, loads in all goal data
        and sets up a new xml formatted document to write the new journal
        entry in
        """
        #Set up new XML document to store new information
        journal = ElementTree.Element("Journal")
        journalEntry = ElementTree.SubElement(journal, "JournalEntry")
        tomorrow = ElementTree.SubElement(journal, "Tomorrow")
        tomorrowRating = ElementTree.SubElement(journal, "TomorrowRating")


    def mainMenu(self):
        """
        Manages all menu options and input/output
        """
        #Use tinkter to write a GUI interface
        
    
    def writeNewJournalEntry(self, fd, inputDictionary): 
        """
        Writes a new journal entry into the current journal or creates
        a new journal folder if none exists. Takes in a file descriptor
        of the journal entry
        """
   
    def displayJournalEntries(self):
        """
        Displays all the journal entries and allows the user to select
        data to see in detail
        """
    def writeSubjectNotes(self):
        """
        Writes a new subject with notes
        """

    def writeNewGoal(self):
        """
        Creates and writes a new goal in the goals folder. 
        """

    def displayCurrentGoals(self):
        """
        Displays current active goals
        """

    def updateGoal(self, goal, updateField, updateValue):
       """
       Updates an existing goal
       """
        
    def removeGoal(self, goal):
        """
        Removes an existing goal
        """

class Window(Frame):
    """
    Tkinter class to manage the GUI window
    """
    mainBackground = "#011f4b"
    grayBorder = "#939393"
    textColor = "#b3cde0"
    inputBackground = "#03396c" 
   
    def __init__(self, parent):
        """
        initializes a window class
        """ 
        Frame.__init__(self, parent, bg="#011f4b")

        #help(Frame)
        
        self.parent = parent                                     
        
        self.initMain()

    
    def initMain(self):
        """
        Initializes the main instance of the GUI
        Gray border: #939393
        Blue bckgrnd: #011f4b
        Blue text: #b3cde0
        """

        self.parent.title("How Was Your Day, A Journaling and Goal Tracking Application")
        
        self.centerWindow()

        self.pack(fill=BOTH, expand=1) 
        
        welcomeMessage = Label(self, text="How Was Your Day?", bg=self.mainBackground, fg=self.textColor)
        #help(welcomeMessage)
        welcomeMessage.pack(side=TOP, padx=5, pady=5)
         
        TextBlock = Text(self, height=15, width=50, insertbackground=self.textColor, highlightbackground=self.grayBorder, highlightthickness=1, bg=self.inputBackground, fg=self.textColor)
        TextBlock.pack(side=TOP, padx=5, pady=5)
        #help(TextBlock)

        buttonPanel = Frame(self, bg=self.mainBackground)
        buttonPanel.pack(fill=BOTH, expand=1)
        #help(buttonPanel)

        nextButton = Button(self, text="Next", highlightbackground=self.mainBackground)
        #help(nextButton)
        nextButton.pack(side=RIGHT, padx=5, pady=5)
        
        nextButton.bind("<Button-1>", submitJournalText)

    def centerWindow(self):
        """
        Centers the window in the middle of the user's screen
        """
        w = 500
        h = 350

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
       
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

def submitJournalText(event):
    """
    Takes the text data out of the text object on the first window page, then unpacks
    the frame to reset the display and go to the next "page"
    """
    #help(event.widget.master)
    slaves = event.widget.master.slaves()
    
    textArea = slaves[1] #hardcoded for now, find a more general method of grabbing the text area from a list
    
    journalEntry = textArea.get("0.0", "end")
    
    for index in range (0, len(slaves)):
        slaves[index].pack_forget()
    
    print journalEntry

def main():
    
    root = Tk()
    
    window = Window(root)

    root.mainloop()

    appInstance = HowWasYourDay()
    appInstance.mainMenu()

if __name__ == '__main__':
    main()
