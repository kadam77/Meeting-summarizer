from datetime import date
from fpdf import FPDF
from datetime import datetime
import os

#All variables
# title=app.title
# meeting_id=app.meet_id
# meetname=app.pltfName
# attendee_no=str(app.attendees)

# time=app.cur_time
# duration=app.duration
# # name="jaey"
# heid="Host Mail-Id: "+app.receiver_email
#     # transcript="A game is a structured form of play, usually undertaken for entertainment or fun, and sometimes used as an educational tool.[1] Many games are also considered to be work (such as professional players of spectator sports or games) or art (such as jigsaw puzzles or games involving an artistic layout such as Mahjong, solitaire, or some video games).Games are sometimes played purely for enjoyment, sometimes for achievement or reward as well. They can be played alone, in teams, or online; by amateurs or by professionals. The players may have an audience of non-players, such as when people are entertained by watching a chess championship. On the other hand, players in a game may constitute their own audience as they take their turn to play. Often, part of the entertainment for children playing a game is deciding who is part of their audience and who is a player. A toy and a game are not the same. Toys generally allow for unrestricted play whereas games present rules for the player to follow.Key components of games are goals, rules, challenge, and interaction. Games generally involve mental or physical stimulation, and often both. Many games help develop practical skills, serve as a form of exercise, or otherwise perform an educational, simulational, or psychological role. Attested as early as 2600 BC,[2][3] games are a universal part of human experience and present in all cultures. The Royal Game of Ur, Senet, and Mancala are some of the oldest known games.[4] "
# transcript = app.summary1

def createPDF(title,meeting_id,attendee_no,time,duration,heid,transcript):
    today = date.today()
    Date=today.strftime("%B %d, %Y")
    def prxt(lines0):
        for line in lines0:
            f.write(line)
        f.write('\n\n')
    def titlefont():
        pdf.set_font("Times", size=20)
        pdf.cell(0, 55, txt=title, ln=1, align="C")


    bs="\033[1m"
    be="\033[0m"
    mid1=bs+'Meeting ID: '
    
    mid=["Meeting Id: "+meeting_id]
    dt=['Date & Time: '+Date+' '+time]
    dur=['Duration: '+duration]
    sray=['Summary: \n'+transcript]
    atno=["Attendee No :"+str(attendee_no)]
    
    with open('downloads/file2.txt', 'w') as f:
        prxt(dt)
        prxt(mid)
        f.write(heid)
        f.write('\n\n')
        prxt(atno)
        prxt(dur)
        f.close()
    with open('downloads\dummy.txt', 'w') as f:
        prxt(sray)
        f.close()

    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Times", size=13)
    # open the text file in read mode
    f = open("downloads/file2.txt", "r")
    f1 = open("downloads\dummy.txt", "r")
    titlefont()
    pdf.set_font("Times", size=13)
    #pdf.cell(0,55,txt=title,ln=1,align="C")
    # insert the texts in pdf
    i=0
    for x in f:
        i = i + 1
        if i<10:
            pdf.cell(0,6, txt=x,ln=1)
        else:
            pdf.l_margin = 25
            pdf.t_margin = 25
            pdf.cell(0, 24, txt=x, ln=1)
            print(i)
    pdf.set_left_margin(25)
    pdf.set_right_margin(25)
    for x1 in f1:
        pdf.image("bag1_2.png", x=0, y=0, w=pdf.w, h=pdf.h)
        pdf.multi_cell(0,6, txt=x1,)

    # save the pdf with name .pdf
    curdate = datetime.now().strftime('%Y-%m-%d_%H_%M')
    pdfname = "a_"
    pdfname = "{}_{}.pdf".format(pdfname,curdate)
    pdf.output(f"downloads\{pdfname}")
    print("end")
    f.close()
    f1.close()
    os.remove("downloads/file2.txt")
    os.remove("downloads\dummy.txt")
    return f"downloads\{pdfname}"
#-----------------------------------------
#code written for removing page from plain pdf , adding bg to all and then again add to pdf...(above is optimized code)