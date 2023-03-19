#este codigo solicita una contrasena y que esta sea una buena segura
import re
passw = 'R@uL$@nx3z'
ojo = 0
while True:
    if (len(passw)<=8):
        ojo = -1
        break
    elif not re.search("[a-z]", passw):
        ojo = -1
        break
    elif not re.search("[A-Z]", passw):
        ojo = -1
        break
    elif not re.search("[0-9]", passw):
        ojo = -1
        break
    elif not re.search("[_@$]", passw):
        ojo = -1
        break
    else:
        ojo = 0
        print('password segura')
        break
if ojo == -1:
    print('password no segura')