#!/usr/bin/python3
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'lxlichn@163.com'
password = 'llx14work'
to_addr = ['793567084@qq.com']
smtp_server = 'smtp.163.com'

content = '''
<html>
<body>
<h1>table</h1>
<table>
<tr>
<td>00</td>
<td>01</td>
<td>02</td>
</tr>
<tr>
<td>10</td>
<td>11</td>
<td>12</td>
</tr>
</table>
</body>
</html>
'''

msg = MIMEText(content, 'html', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('qq <%s>' % to_addr[0])
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()



try:
	server = smtplib.SMTP(smtp_server, 25)
	'''server.set_debuglevel(1)'''
	server.login(from_addr, password)
	server.sendmail(from_addr, to_addr, msg.as_string())
	server.quit()
except Exception as e:
	print('failure')
	print(e)
else:
	print('successful')