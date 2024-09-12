import smtplib as s

sid=s.SMTP("smtp.gmail.com",587)
sid.ehlo()
sid.starttls()
sid.login("skofficial665@gmail.com","jexo obir xhbl kbib")
subject="Test Python"
body="I LOVE PYTHON"
message=(f"subject: {subject}\n\n{body}")
listadd=["sknasiruddin665@gmail.com","facts3989@gmail.com"]
sid.sendmail("skofficial665@gmail.com",listadd,message)
print("Send Mail.........")
sid.quit()
