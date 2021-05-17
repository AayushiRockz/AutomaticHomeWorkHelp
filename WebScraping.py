
#Code is written to open 10 webpages 
# just by entering what you want to
#  search for (from google) and
#  also it helps to open any support needed(from google)


import googlesearch
import webbrowser

def search():
    try:
        from googlesearch import search
    except ImportError: 
        print("No module named 'google' found")
        
        # to search
    query = input("What do you want to search ? :  ")

    for j in search(query, tld="co.in",lang='en', num=1, stop=12, pause=2.0):
        webbrowser.open(j,new=2)
    print("Webpages Opened!")
   


def homeworkHelp():
    consent=input("Do you want to open any google app for your homework/project? (yes/no):  ")
    if(consent=='no'):
        print("OK !")
    else:
        app=input("What do you want to open? Docs/Slides/Sheets/Keep/Jamboard: ")
        if(app=='Docs'):
            webbrowser.open(
                "https://accounts.google.com/ServiceLogin/signinchooser?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fdocument%2F%3Fusp%3Ddocs_alc&followup=https%3A%2F%2Fdocs.google.com%2Fdocument%2F%3Fusp%3Ddocs_alc&ltmpl=docs&flowName=GlifWebSignIn&flowEntry=ServiceLogin",
            new=1)
        elif(app=='Slides'):
            webbrowser.open("https://accounts.google.com/ServiceLogin/signinchooser?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fpresentation%2F%3Fusp%3Dslides_alc&followup=https%3A%2F%2Fdocs.google.com%2Fpresentation%2F%3Fusp%3Dslides_alc&ltmpl=slides&flowName=GlifWebSignIn&flowEntry=ServiceLogin",
            new=1)
        elif(app=='Sheets'):
            webbrowser.open("https://accounts.google.com/ServiceLogin/signinchooser?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2F%3Fusp%3Dsheets_alc&followup=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2F%3Fusp%3Dsheets_alc&ltmpl=sheets&flowName=GlifWebSignIn&flowEntry=ServiceLogin",
            new=1)
        elif(app=='Keep'):
            webbrowser.open("https://accounts.google.com/ServiceLogin/signinchooser?passive=1209600&continue=https%3A%2F%2Fkeep.google.com%2F&followup=https%3A%2F%2Fkeep.google.com%2F&ltmpl=keep&flowName=GlifWebSignIn&flowEntry=ServiceLogin",
            new=1)
        elif(app=='Jamboard'):
            webbrowser.open("https://accounts.google.com/ServiceLogin/signinchooser?service=jamboardcore&passive=1209600&continue=https%3A%2F%2Fjamboard.google.com%2F%3Fusp%3Djam_ald&followup=https%3A%2F%2Fjamboard.google.com%2F%3Fusp%3Djam_ald&flowName=GlifWebSignIn&flowEntry=ServiceLogin",
            new=1)
        print("Your "+app+" has been opened!")
        


def main():
    search();
    homeworkHelp();

main();







        

