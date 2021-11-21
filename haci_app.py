import re, json, hashlib, getpass, base64, mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="usr_haci",
  password="$]tw}pUKa_B>&[k#ajNV8Q9d]hWW&%g?",
  database="db_haci"
)

def fn_except_message(fn):
    print('\n'+'ATENCIÓN: Debes escribir solo 1 para "si" y 2 para "no"'+'---origen:'+fn)

def fn_validate_email(str_email):
    if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+",str_email):
        return False
    else:
        if len(str_email) > 0 and len(str_email) <= 40:
            return True
        else:
            return False

def fn_validate_pwd(str_pwd):
    if len(str_pwd) >= 8 and len(str_pwd) <= 24:
        return True
    else:
        return False

def fn_validate_name(str_name):
    if len(str_name) > 0 and len(str_name) <= 50:
        return True
    else:
        return False

def fn_print_header():
    print('\n\n\n'+'INICIA PROGRAMA')
    print('\n\n\n'+'Hola estimado usuario, bienvenido a Hagamos Cine: Miles de empleos en todos los departamentos involucrados en la creación y distribución del cine en México y Latino-América.')
    print('\n'+'¿Qué deseas hacer?')
    fn_except_message('fn_print_header')
    str_is_user = input('\n'+'¿Ya tengo cuenta?'+'\n')
    return str_is_user.strip()

def fn_is_user(int_is_user):
    if int_is_user == 1:
        print('\n\n\n'+'BIENVENIDO A HAGAMOS CINE - ACCEDER A LA PLATAFORMA')
        str_email = input('\n'+'Escribe tu correo'+'\n')
        if fn_validate_email(str_email):
            #str_pwd = input('\n'+'Escribe tu contraseña'+'\n')
            str_pwd = getpass.getpass()
            if fn_validate_pwd(str_pwd):
                obj_json = {'email':str_email,'pwd':hashlib.md5(str_pwd.encode()).hexdigest()}

                #DE USO EXCLUSIVO PARA LENGUAJES DE EJECUCIÓN EN EL CLIENTE
                #str_json = json.dumps(obj_json)
                #str_base64 = base64.b64encode(str_json.encode('ascii'))

                mycursor = mydb.cursor()
                sql = 'SELECT COUNT(email) AS L1 FROM schUsuarios WHERE estatus = 1 AND email = %s AND contrasena = %s;'
                adr = (obj_json['email'],obj_json['pwd'],)
                mycursor.execute(sql, adr)
                myresult = mycursor.fetchall()
                for x in myresult:
                    if x[0]==1:
                        print('\n'+'Acceso concedido - BIENVENIDO A HOME')
                    else:
                        print('\n'+'ERROR: Verifica tus credenciales')
            else:
                print('\n'+'ERROR: Tu contraseña debe de tener más de 8 letras y/o simbolos y menos de 24 letrasy/o simbolos')
                fn_is_user(int(fn_print_header()))
        else:
            print('\n'+'ERROR: Tu correo debe de tener menos de 40 letras y/o simbolos')
            fn_is_user(int(fn_print_header()))
    elif int_is_user == 2:
        print('\n\n\n'+'BIENVENIDO A HAGAMOS CINE - CREAR CUENTA')
        str_nam = input('\n'+'Escribe tu nombre'+'\n')
        if fn_validate_name(str_nam):
            str_email = input('\n'+'Escribe tu correo'+'\n')
            if fn_validate_email(str_email):
                #str_pwd = input('\n'+'Escribe tu contraseña'+'\n')
                str_pwd = getpass.getpass()
                if fn_validate_pwd(str_pwd):
                    obj_json = {'name':str_nam,'email':str_email,'pwd':hashlib.md5(str_pwd.encode()).hexdigest()}

                    #DE USO EXCLUSIVO PARA LENGUAJES DE EJECUCIÓN EN EL CLIENTE
                    #str_json = json.dumps(obj_json)
                    #str_base64 = base64.b64encode(str_json.encode('ascii'))

                    mycursor = mydb.cursor()
                    sql = 'SELECT COUNT(email) AS L1 FROM schUsuarios WHERE estatus = 1 AND email = %s;'
                    adr = (obj_json['email'],)
                    mycursor.execute(sql, adr)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        if x[0]==1:
                            print('\n'+'ERROR: El usuario ya existe')
                        else:
                            mycursor = mydb.cursor()
                            sql = 'INSERT INTO schUsuarios (name, email, contrasena) VALUES (%s, %s, %s);'
                            val = (obj_json['name'],obj_json['email'],obj_json['pwd'],)
                            mycursor.execute(sql, val)
                            mydb.commit()
                            print(mycursor.rowcount, '\n'+'Nuevo usuario - BIENVENIDO A HOME')
                else:
                    print('\n'+'ERROR: Tu contraseña debe de tener más de 8 letras y/o simbolos y menos de 24 letrasy/o simbolos')
                    fn_is_user(int(fn_print_header()))
            else:
                print('\n'+'ERROR: Tu correo debe de tener menos de 40 letras y/o simbolos')
                fn_is_user(int(fn_print_header()))
        else:
            print('\n'+'ERROR: Tu nombre debe de tener menos de 50 letras y/o simbolos')
            fn_is_user(int(fn_print_header()))

    else:
        fn_except_message('fn_is_user')

if __name__ == '__main__':
    try:
        fn_is_user(int(fn_print_header()))
        print('\n\n\n'+'TERMINA PROGRAMA')
    except:
        fn_except_message('fn_main')
