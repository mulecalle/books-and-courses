import cgi
import html

form = cgi.FieldStorage()
print('Content-type: text/html\n')

print("""
<html>
    <head>
        <meta charset="utf-8"/>
        <title>Pagina de retorno</title>
        <link rel="stylesheet" href="../css/estilos.css" type="text/css" />
    </head>
 
    <body>
        <h1>Hola %s!</h1>
    </body>
    
</html>""" % html.escape(form['nombre'].value))