#use less secure apps  and turn it on
#turn off 2 factor authentication
from email.message import EmailMessage
import smtplib
def credentials():
    id = "iser_ email id"
    pwd = "user email password"

    return (id, pwd)

try:
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587) #set up a connection on smtp server
    smtpObj.ehlo() #checks whaether connection is ok, will give error if connecton is not ok
    smtpObj.starttls() #TLS- TRansport layer security to ensure our messgage go securly
    
    id = credentials()[0] 
    pwd = credentials()[1]

    smtpObj.login(id,pwd)  # login in to my id

    with open('all_email.csv', 'r')as email_file:
        csv_reader = csv.DictReader(email_file) # allowing to converteach row into a file
       


        for row in csv_reader:
            msg= EmailMessage()
            msg["To"] = row["To"]
            msg["From"] =row["From"]
    
            msg["Subject"] =row["Subject"]
            msg.set_content(row["Content"])

            smtpObj.send_message(msg)

    # msg = EmailMessage() #create email message object

    # msg["From"] ="alex"
    # msg["To"]= "cewe88@ypo.com"
    # msg["Subject"] = "testing"
    # msg.set_content("Hi how are you?") #particular message

    # smtpObj.send_message(msg) # it will send an email using the given email object

    smtpObj.quit() # it will quit the curreent smtp connction

except Exception as err:
    print(err)

