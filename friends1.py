import cgi
reshtml='''Content-Type:text/html\n
<HTML><HEAD><TITLE>
CGI
</TITLE></HEAD>
<BODY>Friends list: <I> %s</I>
Your name is: <B>%s</B>friends.
</BODY></HTML>'''
form=cgi.FieldStorage()
who=form['person'].value
howmany=form['person'].value
howmany=form['howmany'].value
print(reshtml %(who,who,howmany))
