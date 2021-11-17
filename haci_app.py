import re

def fn_except_message(fn):
    print('\n'+'Debes escribir solo 1 para "si" y 2 para "no"'+'---fn:'+fn)

def fn_validate_usr(str_usr,int_is_user):
    if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+",str_usr):
        print('\n'+'Debes de escribir una cuenta de correo valida')
        fn_is_user(int_is_usr)
    else:
        return str_usr

def fn_print_header():
    print('\n\n\n'+'Hola estimado usuario, bienvenido a Hagamos Cine: Miles de empleos en todos los departamentos involucrados en la creación y distribución del cine en México y Latino-América.')
    print('\n'+'¿Qué deseas hacer?')
    fn_except_message('fn_print_header')
    str_is_user = input('\n'+'¿Ya tengo cuenta?'+'\n')
    return str_is_user.strip()

def fn_is_user(str_is_user):
    if str_is_user == 1:
        str_usr = input('\n'+'Escribe tu correo'+'\n')
        fn_validate_usr(str_usr,1)
        str_pwd = input('\n'+'Escribe tu contraseña'+'\n')
    elif str_is_user == 2:
        str_new_user = input('\n'+'¿Deseas registrarte?'+'\n')
    else:
        print('leo')
        fn_except_message('fn_is_user')
        #print('\n'+'Debes escribir solo 1 para "si" y 2 para "no"')

if __name__ == '__main__':
    str_is_user = fn_print_header()
    try:
        int_is_user = int(str_is_user)
        fn_is_user(int_is_user)
    except:
        fn_except_message('fn_main')
        #print('\n'+'Debes escribir solo 1 para "si" y 2 para "no"')
        fn_print_header()
