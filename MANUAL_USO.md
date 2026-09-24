# Manual de Uso

## Escáner de Puertos TCP en Python

## 1. Introducción

Este manual explica los requisitos y pasos necesarios para instalar, ejecutar y utilizar la aplicación de escaneo de puertos TCP desarrollada en Python por el grupo 14.

La aplicación permite ingresar una dirección IP y un rango de puertos para comprobar cuáles aceptan conexiones TCP. Los resultados se muestran directamente en la consola despues de escanear todos los puertos.

El programa debe utilizarse exclusivamente sobre equipos propios, máquinas virtuales o entornos de laboratorio autorizados.

---

## 2. Requisitos

Para utilizar la aplicación se requiere:

* Computadora.
* Python 3 instalado.
* Visual Studio Code.
* Acceso a una terminal.
* Nuestro programa`scanner_puertos.py`.

No es necesario instalar bibliotecas externas para ejecutar el programa, debido a que utiliza bibliotecas incluidas en Python tales como:

* `ipaddress`
* `socket`
* `datetime`

---

## 3. Instalación de Python

Antes de ejecutar el programa se debe comprobar que Python se encuentre instalado.

En Visual Studio Code se puede abrir una terminal y ejecutar:

```bash
python --version
```

Si el sistema utiliza el comando `python3`, se puede ejecutar:

```bash
python3 --version
```

La terminal deberá mostrar la versión instalada de Python.

---

## 4. Abrir el proyecto en Visual Studio Code

1. Abrir Visual Studio Code.
2. Seleccionar la opción para abrir una carpeta.
3. Seleccionar la carpeta del proyecto:

```
scanner-puertos-python
```

4. Verificar que dentro de la carpeta se encuentren los siguientes archivos:

```
scanner_puertos.py
README.md
MANUAL_USO.md
```

---

## 5. Ejecutar la aplicación

Abrir la terminal integrada de Visual Studio Code con ctrl + ñ
Ejecutar:

```bash
python scanner_puertos.py
```

En caso de que el sistema utilice `python3`, ejecutar:

```bash
python3 scanner_puertos.py
```

Al ejecutarse correctamente aparecerá el encabezado de la aplicación:

```text
============================================================
              ESCÁNER DE PUERTOS TCP
============================================================
Herramienta desarrollada en Python
Uso exclusivo en equipos autorizados.
============================================================
```

---

## 6. Ingresar la dirección IP

El programa solicitará:

```text
Ingrese la dirección IP:
```

Se debe ingresar la dirección IP del equipo autorizado que será analizado.

Por ejemplo:

```text
127.0.0.1
```

La aplicación verifica que la dirección IP tenga un formato válido.

Si se introduce una dirección incorrecta, el programa mostrará un mensaje solicitando nuevamente la información.

---

## 7. Ingresar el puerto inicial

Después de introducir la dirección IP, el programa solicitará:

```text
Ingrese el puerto inicial:
```

Se debe ingresar un número de puerto entre:

```text
1 y 65535
```

Por ejemplo:

```text
1
```

---

## 8. Ingresar el puerto final

A continuación, el programa solicitará:

```text
Ingrese el puerto final:
```

Por ejemplo:

```text
100
```

En este caso, el programa analizará los puertos comprendidos entre el puerto 1 y el puerto 100.

El puerto final debe ser mayor o igual al puerto inicial.

---

## 9. Límite del escaneo

La aplicación establece un límite máximo de 1024 puertos por ejecución.

Si el rango seleccionado supera este límite, el programa mostrará un mensaje indicando que el rango es demasiado grande y finalizará el proceso.

Por ejemplo, si se selecciona:

```text
Puerto inicial: 1
Puerto final: 2000
```

el programa no realizará el escaneo debido a que el rango supera el máximo establecido.

---

## 10. Ejecución del escaneo

Después de introducir correctamente los datos, el programa inicia el escaneo.

Durante el proceso se muestra información sobre el rango seleccionado y el avance del escaneo.

Cuando se encuentra un puerto abierto, se muestra información similar a:

```text
[ABIERTO] Puerto 22    Servicio: ssh
```

El nombre del servicio depende de la información disponible en el sistema.

---

## 11. Interpretación de los resultados

Un puerto mostrado como:

```text
[ABIERTO]
```

indica que el programa pudo establecer correctamente una conexión TCP con ese puerto durante la prueba.

La información del servicio permite identificar, cuando es posible, el servicio normalmente asociado con ese número de puerto.

Por ejemplo:

```text
Puerto       Servicio            Estado
------------------------------------------------------------
22           ssh                 ABIERTO
80           http                ABIERTO
443          https               ABIERTO
```

Si el programa no puede identificar el servicio asociado, mostrará:

```text
desconocido
```

Esto no significa que el puerto esté cerrado. Significa que no se encontró un nombre de servicio asociado mediante la consulta realizada por Python.

---

## 12. Resumen del escaneo

Al finalizar el proceso, la aplicación presenta un resumen similar a:

```text
============================================================
                    RESUMEN DEL ESCANEO
============================================================
IP analizada:        127.0.0.1
Rango analizado:     1-100
Puertos analizados:  100
Puertos abiertos:    3
Tiempo de escaneo:   2.84 segundos
```

También se muestra la lista de puertos abiertos y los servicios identificados.

---

## 13. Funciones utilizadas

El programa se encuentra dividido en funciones para facilitar su organización.

### `v_ip()`

Valida la dirección IP ingresada por el usuario.

### `s_ip()`

Solicita la dirección IP y utiliza `v_ip()` para comprobar que sea válida.

### `s_p()`

Solicita un número de puerto y verifica que se encuentre entre 1 y 65535.

### `o_s()`

Intenta identificar el servicio TCP asociado a un puerto.

### `e_p()`

Comprueba individualmente si un puerto acepta una conexión TCP.

### `e_r()`

Recorre el rango de puertos seleccionado y realiza las comprobaciones.

### `m_r()`

Muestra el resumen final del escaneo y los servicios encontrados.

### `main()`

Coordina todas las funciones y controla el flujo principal de la aplicación.

---

## 14. Ejemplo de uso

Un ejemplo de ejecución puede ser:

```text
============================================================
              ESCÁNER DE PUERTOS TCP
============================================================
Herramienta desarrollada en Python
Uso exclusivo en equipos autorizados.
============================================================

Ingrese la dirección IP: 127.0.0.1

Ingrese el puerto inicial: 1
Ingrese el puerto final: 100
```

Después de ingresar los datos, comenzará el proceso de escaneo.

El resultado dependerá de los servicios que se encuentren activos en el equipo analizado.

---

## 15. Recomendaciones

* Verificar que la dirección IP sea correcta.
* Utilizar rangos de puertos adecuados para la práctica.
* No realizar escaneos sobre equipos sin autorización.
* Guardar capturas de pantalla de las pruebas realizadas.
* Verificar que el código utilizado en las pruebas corresponda con la versión almacenada en GitHub.

---

## 16. Uso autorizado

El programa fue desarrollado con fines académicos para la práctica de Seguridad Informática.

Las pruebas deben realizarse únicamente sobre:

* Equipo propio.
* Máquina virtual propia.
* Laboratorio autorizado.

No se debe utilizar la aplicación para analizar sistemas, redes o dispositivos sobre los cuales no se tenga autorización.

---

## 17. Información del proyecto

**Proyecto:** Desarrollo de un Escáner de Puertos de Red utilizando Python

**Asignatura:** Seguridad Informática

**Lenguaje:** Python

**Archivo principal:** `scanner_puertos.py`

**Repositorio:** Se incorporará el enlace al repositorio de GitHub una vez creado.
