def Send_Email(DIV,CITY,CRYPT):
        import smtplib
        from email.MIMEMultipart import MIMEMultipart
        from email.MIMEText import MIMEText
        from email.MIMEBase import MIMEBase
        from email import encoders

        fromaddr = "netcommtsd@dayzim.com"
        toaddr = "david.henderson@dayzim.com"
        subject = "test Email " + CITY
        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subject

        body = "This is a test email\n next line\n next line"

        msg.attach(MIMEText(body, 'plain'))

        filename = "output.txt"
        attachment = open("/output.txt", "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        server = smtplib.SMTP('172.25.0.181', 25)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
