from flask import Flask 
import pymongo 
from flask import Flask,render_template,request,flash
import gridfs  
  
app = Flask(__name__) #creating the Flask class object   
app.secret_key = "ser"
client= pymongo.MongoClient("mongodb+srv://kevinrotern:jayesh@cluster0.h7nnxmo.mongodb.net/test")
db= client['deepblue']
row=db['pastmeeting'] 
fs=gridfs.GridFS(db)
#gloabal variables required


  
def addEntry(pdf,date,attendees,names,transcript,duration,pdfname,email_id,m,title="Summary"):

 #--------------------------UPLOAD------------------------------------- 
#  pdf1="static/files/dwdm_exp10_og.pdf"
  pdf1 = pdf
  pdf_data=open(pdf1,"rb")
  data=pdf_data.read()
  fs=gridfs.GridFS(db)
  pdfname = pdfname.replace(".pdf","")
  print(pdfname," ",duration)
  fs.put(data,filename=pdfname)
 #-------------------------DOWNLOAD--------------------------------
 #data=db.fs.files.find_one({'filename':"jayesh"})
 #my_id=data['_id']
 #outputdata=fs.get(my_id).read()
 #download_location="C:/Users/Jayesh/OneDrive/Desktop/deepblue/website_database/static/downloaded_pdf/"+"sucess.pdf"
 #output=open(download_location,'wb')
 #output.write(outputdata)
 #output.close()
# print("download complete")
#---------------------------END-------------------------------------------
  uval={'Date': date, 'Title':title,'Note':attendees,'filename':pdfname,'name':names,"transcript":transcript,"duration":duration,"Email":email_id,"actions":m}
  row.insert_one(uval)
#  x=row.find({'filename':"jayesh"})
#  for i in x:
   
#   print(i['Title'])
#  return render_template("index.html")
 #x = row.find({"_id" : {"$oid": "6429e37dddb48aa860b94e30"}},{'_id': 0, 'Date': 0,
   #              'Title': 1, 'Note': 0,'pdfdata':1})

