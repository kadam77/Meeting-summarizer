#tejas Model
from flask import Flask, render_template, request,jsonify,flash,request,session,redirect, url_for
import threading
import os,smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication #to create different type of payload
#####################################################################################
#jayesh formated text
from datetime import date
import gridfs
import pymongo 



# Import date class from datetime module
from datetime import date,datetime

#databse connections in app1
import tokenSum,email1,word_list
##################################################################################

from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.secret_key = "ser"

# pipe = pickle.load(open("samsum_summarry_model.pk", 'rb'))
#All variables
text=""
meet_id=""
receiver_email =""
summary1=""
img_buffer = None
cur_datetime = ""
pdfname = ""
attendees=4
names=['dhananjay','jayesh','tk','aw']
cur_date=None
duration=""
title="Summary"
pltfName="Google Meet-d"
st_time=""
cur_time=""

@app.route('/')
def index():
    # return render_template('index.html')

    return render_template("index.html")
    


@app.route('/predict', methods = ['POST','GET'])
def predict():
    print("Processing...")
    global text,meet_id,img_buffer,cur_datetime,cur_date,names,attendees,cur_time,duration,pltfName,st_time
    cur_datetime = datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    cur_date = date.today()
    cur_time = datetime.now().strftime('%H:%M')
    
    # duration = Duration(st_time,cur_time)
    text = request.get_json().get('Transcript')
    meet_id = request.get_json().get('MeetId')
    receiver_email = request.get_json().get('Email_id')
    names = request.get_json().get('names')#array of names of attendees
    # attendees = request.get_json().get('attendess')#count of attendees
    attendees = len(names)
    st_time = request.get_json().get('st_time')
    pltfName= request.get_json().get('pltfName')

    duration = calTime(st_time,cur_time)
#checking every variable:
    print(meet_id)
    print(receiver_email)
    print(names)
    print(attendees)
    print(st_time)
    print(pltfName)
    print(duration)
    print(cur_time,cur_date,cur_datetime)
######################################

    global summary1

    prediction = tokenSum.summary(text)
    print("summary:")
    # print(prediction[0]["summary_text"]) #change due to chunking
    print(prediction)
    summary1 = prediction
    # print(type(summary1))
    # res = str(prediction[0]["summary_text"])#change due to chunking
    res  = prediction
    # result = {'summary':res}
    resp = {'status':'send'} # we can also use try and catch block to check email send sucessfully or not
    # print(res)
    m=word_list.action(text)
    print(m)
    thread = threading.Thread(target=email1.Send_Mail, args=(summary1,meet_id,cur_date,attendees,names,text,title,cur_time,duration,m,receiver_email)) # send mail function is called from separate thread to stop refreshing the page when email send in one http cycle
    thread.start()
    # Send_Mail(res)
    # Send_Mail(res,meet_id,receiver_email)
    
    print("***end***")
    return jsonify(resp)


def calTime(st_time,end_time):
    start_hour, start_minute = map(int, st_time.split(':'))
    end_hour, end_minute = map(int, end_time.split(':'))
    
    # calculate duration in minutes
    total_minutes = (end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)
    
    # return duration in minutes
    return str(total_minutes)


#HTML endpoint
@app.route('/sidebar',methods =["GET", "POST"])
def page2():
    session['my_data'] = "djadhav20comp@student.mes.ac.in"# give email here
    return render_template('sidebar.html',usdata=row.find())
#------------------------Download_function-----------------------------------------------------
@app.route('/download',methods=["GET","POST"])
def page3():
  filename=""
  if request.method == "POST":
       print("here")
       filename= request.form.get('fn')
  print(type(filename))
  print(filename)
  data=db.fs.files.find_one({'filename':filename})
  my_id=data['_id']
  outputdata=fs.get(my_id).read()
  download_location=f"static/downloaded_pdf/{filename}.pdf"
  output=open(download_location,'wb')
  output.write(outputdata)
  output.close()
  print("download complete")
  return render_template('sidebar.html',usdata=row.find(),down="Download Successsfully")
#--------------------------------------------------------------------------------------------

@app.route('/view',methods=["GET","POST"])
def page4():
  filename=""
  if request.method == "POST":
       print("here")
       filename= request.form.get('fn1')
  print(type(filename))
  print(filename)
  filename1=filename
  usdata=row.find_one({'filename':filename1})
  data=db.fs.files.find_one({'filename':filename})
  my_id=data['_id']
  outputdata=fs.get(my_id).read()
  download_location=f"static/downloaded_pdf/{filename}.pdf"
  output=open(download_location,'wb')
  output.write(outputdata)
  output.close()
  name1=usdata['name']
  for x in name1:
     print(x)
  print("download complete")
  return render_template('tdata.html',name=filename,note=usdata['Note'],date=usdata['Date'],title=usdata['Title'],names=usdata['name'],duration=usdata['duration'],trans=usdata['transcript'])
#############################
#login
@app.route('/login',methods=["GET","POST"])
def page6():
  logindata=[]
  if request.method == "POST":
       print("here")
  
       email= request.form.get('email')
       psw = request.form.get('psw')
       logindata.insert(0,email)
       logindata.insert(1,psw)
       print(email)
       print(psw)
       findresult=ls.count_documents({ 'Email':email,'Password':psw}, limit = 1)
       print(findresult)
       if findresult==1:
          print("already exist")
          return render_template('sidebar.html',usdata=row.find({'Email':email}))
          # return redirect(url_for("/sidebar.html"))
       else: 
          return render_template('login.html',mssg="Account Does not exits,Please Signup")
  #ndata=ls.find({"Name":name});
  #print(ndata)
  return render_template('login.html')

#############################
#signUp
@app.route('/signup',methods=["GET","POST"])
def page5():
  logindata=[]
  if request.method == "POST":
       print("here")
       name = request.form.get('name')
       email= request.form.get('email')
       psw = request.form.get('psw')
       logindata.insert(0,name)
       logindata.insert(1,email)
       logindata.insert(2,psw)
       print(name)
       print(email)
       print(psw)
       findresult=ls.count_documents({ 'Email':email,'Password':psw}, limit = 1)
       print(findresult)
       
       if findresult==1:
          print("already exist")
          return render_template('signup.html',mssg="Account Already exists,Please login")
       else: 
         print("---------------inserting data-------------") 
         udata={'Name':name, 'Email':email,'Password':psw}
         ls.insert_one(udata)
         return render_template('login.html')
  #ndata=ls.find({"Name":name});
  #print(ndata)
  return render_template('signup.html')
#############################

#############################

if __name__ == "__main__":
    client= pymongo.MongoClient("mongodb+srv://kevinrotern:jayesh@cluster0.h7nnxmo.mongodb.net/test")
    db= client['deepblue']
    row=db['pastmeeting'] 
    ls=db['loginsignin'] 
    fs=gridfs.GridFS(db)
    app.run(debug=True, port=8000)
