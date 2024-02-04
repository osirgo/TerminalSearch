'''
Busqueda de archivos y carpetas (directorios) por la terminal.

Argumento:
Se ingresa un string como patrón de búsqueda.

Retorna:
Despliega en pantalla la ruta (path) para acceder al archivo 
o directorio buscado.
'''

from os import system

def validar_patron(patron, tipoP = 'n'):
	''' 
	Toma una cadena (string) como patrón y verifica que no 
	contenga caracteres invalidos y su concordancia para nombres.

	Argumento:
	patron. La cadena a validar.
	tipoP. Para indicar si el string es un:
			nombre (valor n) o
			path-ruta (valor p)

	Retorna:
	True si el patrón en valido, False en caso contrario.
	'''

	if patron[0] == ' ' or patron[-1] == ' ':
		return False
	elif '/' in patron and tipoP == 'n':
		return False
	elif '/' in patron and tipoP == 'p':
		return True
	else:
		return True

def crear_cadena_busqueda(cadena_original):
    '''
    Toma una cadena (string) que es el elemento a búscar y lo 
    transforma en una expresión regular adecuada para que 
    considere todos los casos posibles.

    Argumento:
    Cadena_original. Es el elemento a búscar.

    Retorna:
    Expresión regular.
    '''

    cadena_final = ''
    for caracter in cadena_original:
        if caracter.isalpha():
			# Añade por cada caracter la expresión [minúsculaMayúscula]
            cadena_final += str([caracter.lower() + caracter.upper()])
        else:
			# Si no es un caracter alfabetico no lo modifica
            cadena_final += caracter
	# Elimina el caracter ' y retorna el string resultante como expresión regular
    return cadena_final.replace("'", "")

def fallo(mensaje = '', logic = True):
	# Finaliza la ejecución del script
	if logic == False:
		print('Patrón inválido')
	else:
		print(mensaje)
	exit()

def lugar_de_busqueda():
	print('Ingrese ruta de búsqueda(path)...\n\
	   presione [ENTER] para búsqueda global por defecto\n\
	   Ingrese [.] para una búsqueda local' )
	path = input('Ruta (path): ')

	if path == '':
		path = '/'
	
	if validar_patron(path, 'p'):
		return path
	else:
		fallo('Ruta (path) inválida')

# Main
patron = input('Ingrese patrón de búsqueda: ')  # String original a validar
patronBusqueda = crear_cadena_busqueda(patron)  # String procesado para usar como patron de búsqueda

# Selecciona que se va a buscar
opcionB_archivo_carpeta = input('Ingrese objeto a buscar: 1-Archivo, 2-Directorio: ')
path = lugar_de_busqueda()

if opcionB_archivo_carpeta == '1' and validar_patron(patron) == True:
    # Selecciona el tipo de búsqueda a realizar
	opcionBusqueda = input('Tipo de busqueda: 1-Simplificada 2-Extendida: ')

	if opcionB_archivo_carpeta == '1' and opcionBusqueda == '1':  # Buscar archivos
		system(f"find {path} -type f -name '{patronBusqueda}' 2>&1 | grep -v 'Permission denied'")
	elif opcionB_archivo_carpeta == '1' and opcionBusqueda == '2':
		system(f"find {path} -type f -name '{patronBusqueda}'")
	else:
		fallo('Opción de búsqueda inválida', validar_patron(patron))
elif opcionB_archivo_carpeta == '2' and validar_patron(patron) == True:
    # Selecciona el tipo de búsqueda a realizar
	opcionBusqueda = input('Tipo de busqueda: 1-Simplificada 2-Extendida: ')

	if opcionB_archivo_carpeta == '2' and opcionBusqueda == '1':  # Buscar directorios
		system(f"find {path} -type d -name '{patronBusqueda}' 2>&1 | grep -v 'Permission denied'")
	elif opcionB_archivo_carpeta == '2' and opcionBusqueda == '2':
		system(f"find {path} -type d -name '{patronBusqueda}'")
	else:
		fallo('Opción de búsqueda inválida', validar_patron(patron))
else:
	fallo('Selección de objeto inválido', validar_patron(patron))

print('Fin de la búsqueda...')
