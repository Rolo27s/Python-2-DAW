"""
7. Manejo de Archivos de Texto: Escribe un programa en Python que lea el contenido de un archivo de texto llamado entrada.txt y copie su contenido a otro archivo llamado salida.txt. Asegúrate de manejar posibles errores, como la falta del archivo de entrada, y proporciona mensajes informativos en caso de éxito o fallo.
"""
try:
    archivoEntrada = open('entrada.txt', 'r')
    archivoSalida = open('salida.txt', 'w')
    
    try:
        # Copio el archivo de Entrada en el archivo de Salida
        archivoSalida.write(archivoEntrada.read())
        print("Archivo de salida generado con éxito")
    except:
        print ("Ocurrió un problema en la copia del archivo")
    
except:
    print ("Ocurrió un problema con la apertura de los archivos de texto")

