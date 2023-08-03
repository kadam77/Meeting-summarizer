import os,smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication #to create different type of payload
import createPdf,app1
from datetime import datetime



def Send_Mail(summary,meet_id,cur_date,attendees,names,text,title,time,duration,m,to_email_id="djadhav20comp@student.mes.ac.in"):

    ######################### Creating Img and pdf #######################################

    # summmaryImg = createImg(summary)
    pdf = createPdf.createPDF(title,meet_id,attendees,time,duration,to_email_id,summary)
    cur_date = cur_date.strftime('%d-%m-%Y')
    curdate = datetime.now().strftime('%Y-%m-%d_%H_%M')
    pdfname = meet_id
    pdfname = "{}_{}.pdf".format(pdfname,curdate)
    ############################################################################
    
    # file_name = meet_id+"_summary.txt"
    # with open(file_name,"w") as file:
    #     file.write("Meeting ID: "+meet_id+"\n\n")
    #     file.write("Summary"+"\n")
    #     file.write(summary)

    #create a multipart message object
    msg = MIMEMultipart()

    msg.attach(MIMEText("Summary of meet is attached to this mail!"))

    #attaching a .txt file
    # with open(file_name,"rb") as file:
    #     attachment = MIMEApplication(file.read(),_subtype="txt")
    #     attachment.add_header("Content-Disposition","attachment",filename=file_name) # it indicates email to handle it as separate attachment not in mail body 
    #     msg.attach(attachment)
    
    #attaching image
    # with open(summmaryImg, 'rb') as f:
    #     img_data = f.read()
    #     image = MIMEImage(img_data, name='image.jpg')
    #     msg.attach(image)
    # img_attachment = MIMEImage(img_buffer.getvalue(), 'png')
    # msg.attach(img_attachment)

    # Read the PDF file and attach it to the message object
    
    with open(pdf, 'rb') as f:
        attachment = MIMEApplication(f.read(), _subtype='pdf')
        attachment.add_header('Content-Disposition', 'attachment', filename=pdfname)
        msg.attach(attachment)
    
    #set the email sender and receiver
    from_addr = "deepbluestm19@gmail.com"
    # to_addr = "djadhav20comp@student.mes.ac.in"
    to_addr = to_email_id
    Cc = ['tkadam20comp@student.mes.ac.in','djadhav20comp@student.mes.ac.in','jrajbhar20ce@student.mes.ac.in']
    subject = "Summary of today's meet, meeting id: "+meet_id

    msg["from"] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = subject
    # msg["Cc"] = ','.join(Cc)

    #send email using smtp
    with smtplib.SMTP("smtp.gmail.com",587) as smtp:
        smtp.starttls()
        smtp.login(from_addr,"xxx-xxx-xxx-xxxxxx")
        # smtp.sendmail(from_addr,[to_addr]+ Cc ,msg.as_string())
        smtp.sendmail(from_addr,[to_addr],msg.as_string())
    #add code to put data in database
    
    

    app1.addEntry(pdf,cur_date,attendees,names,text,duration,pdfname,to_email_id,m,"Summary")
    print("email send successfully")
    
#########################################################################################
