
# Meeting Summarizer

STM_19 Summarizer is a Chrome extension that generates meeting transcripts and summaries. It works seamlessly on both Google Meet and Microsoft Teams. Additionally, it offers a web interface where users can access and download summaries of past meetings.

## How to run

### How to add pickle file (ML model)
- As pickle file is above 1.3 gb it cannot be uploaded here, follow the  below steps to get pickle file
- got to [drive_link](https://drive.google.com/file/d/1RO6grOqxrBPxxGWhv842ajJlOAnmIJs-/view?usp=share_link) and download zip file
- unzip it and cut and paste it in the folder where all files are present or in folder where repo is cloned.

### How to run extension
- download zip file and unzip extensions
- on chrome go to extension/ manage extension, switch on developer mode and click load unpacked
- upload the extension folder here, eg:  GoogleMeetTranscript
- once it is done begin with the meeting as usual and click start button(will be added by extension).

### Create virtual environment
- virtualenv env
#### code for activate it
- .\env\Scripts\activate.ps1

### install requirements
- pip install -r requirements.txt

#### run
- py app.py

## Important Note
- This include a module email1.py, in this at line 70 replace xxx-xxx-xxx-xxxxxx with your password.
- xxx-xxx-xxx-xxxxxx is the gmail authentication password use to send summary automatically on mail
- to generate this key refer following video:
- [Link](https://youtu.be/g_j6ILT-X0k)

- Also change the default receiver email_id at line 11.

## Authors

- [@Tejas Kadam](https://github.com/kadam77)
- [@Dhananjay Jadhav](https://github.com/dkjadhav-28)
- [@Abhishek Wafare](https://github.com/AbhishekWafare)
- [@Jayesh Rajbhar](https://github.com/kevinrotern)

