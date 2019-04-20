import yagmail

def send_mail(to,msg,sub):
	receiver = to
	body = msg
	#filename = "mail.py"
	sender = "vpda.proj@gmail.com"


	yag = yagmail.SMTP(sender)
	yag.send(
	    to=receiver,
	    subject=sub,
	    contents=body,
	    #attachments=filename,     
	)
