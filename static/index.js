function form_handler(event) {
    alert(event)
    event.preventDefault();
}

function send_data(){
    document.querySelector('form').addEventListener("submit", form_handler);
    // alert("go");
    var text = document.getElementById("text").value;
//    console.log(text)
//    document.getElementById("prediction").innerText = "summary";
var transcript = text;
   var meetId = "xxx-Xxxx-xxx"; 
   var email_id="djadhav20comp@student.mes.ac.in";
   const now = new Date();
   const h = now.getHours();
   const m = now.getMinutes();
   const St_time = `${h}:${m}`
   var names=[];
   
//    alert(transcript);

   fetch('http://127.0.0.1:8000/predict',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body: JSON.stringify({
            Transcript: transcript,
            MeetId: meetId,
            Email_id: email_id,
            names:names,
            attendess:names.length,
            st_time:St_time,
            pltfName:"-"

            
        })
    })
    .then(response => response.json())
    .then(data => {
        if(data["status"] == "send")
        {
            alert("Email send successfully, Please also check spam!");
        }
        else{
            alert("Error");
        }
    })
    .catch(error => {
        console.error(error);
    });
   alert("Email send succcessfully")
}