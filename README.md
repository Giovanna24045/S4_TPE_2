# Escáner de Puertos TCP en Python

## Descripción

Este proyecto consiste en el desarrollo de una aplicación básica en Python que permite realizar un escaneo de puertos TCP sobre un equipo autorizado.

La aplicación solicita al usuario una dirección IP, un puerto inicial y un puerto final. Posteriormente, comprueba cada puerto del rango seleccionado mediante conexiones TCP e identifica aquellos que se encuentran abiertos.

Cuando es posible, el programa también muestra el servicio asociado al puerto encontrado. Al finalizar el proceso, presenta un resumen con la información obtenida durante el escaneo.

> **Importante:** El programa debe utilizarse únicamente sobre equipos propios, máquinas virtuales o entornos de laboratorio autorizados.

## Objetivo

Desarrollar una aplicación básica en Python capaz de realizar un escaneo de puertos TCP sobre un equipo autorizado, identificar los puertos abiertos dentro de un rango determinado y presentar un resumen de los resultados obtenidos.

## Características

* Validación de direcciones IP.
* Validación de números de puerto.
* Selección de puerto inicial y puerto final.
* Escaneo de puertos mediante conexiones TCP.
* Identificación de puertos abiertos.
* Identificación del servicio asociado cuando está disponible.
* Barra de progreso durante el escaneo.
* Cálculo del tiempo empleado.
* Resumen de los resultados obtenidos.
* Control del rango máximo de puertos a analizar.

## Tecnologías utilizadas

* Python
* Biblioteca `socket`
* Biblioteca `ipaddress`
* Biblioteca `datetime`
* Visual Studio Code
* GitHub

## Estructura del proyecto

```text
scanner-puertos-python/
│
├── scanner_puertos.py
├── README.md
└── MANUAL_USO.md
```

## Requisitos

Para ejecutar el programa se necesita:

* Python 3 instalado.
* Visual Studio Code u otro editor de código.
* Acceso a una terminal.
* Un equipo propio, máquina virtual o laboratorio autorizado para realizar las pruebas.

## Ejecución

Desde la terminal, ubicarse en la carpeta del proyecto y ejecutar:

```bash
python scanner_puertos.py
```

En algunos sistemas puede ser necesario utilizar:

```bash
python3 scanner_puertos.py
```

## Funcionamiento

Al iniciar la aplicación, el programa solicita:

1. Dirección IP.
2. Puerto inicial.
3. Puerto final.

Después de validar los datos ingresados, comienza el escaneo del rango seleccionado.

Durante el proceso se muestra el avance del escaneo y los puertos que sean identificados como abiertos.

Al finalizar, se presenta un resumen que contiene:

* IP analizada.
* Rango de puertos.
* Cantidad de puertos analizados.
* Cantidad de puertos abiertos.
* Servicios identificados.
* Tiempo utilizado en el escaneo.

## Funciones principales

El programa se encuentra dividido en diferentes funciones para organizar el proceso:

* `v_ip()` — valida la dirección IP.
* `s_p()` — solicita y valida un número de puerto.
* `s_ip()` — solicita y valida la dirección IP.
* `o_s()` — intenta obtener el servicio asociado a un puerto TCP.
* `e_p()` — comprueba si un puerto acepta una conexión TCP.
* `e_r()` — realiza el escaneo del rango de puertos.
* `m_r()` — muestra el resumen de los resultados.
* `main()` — coordina la ejecución principal del programa.

## Uso responsable

El escaneo de puertos es una técnica utilizada en seguridad informática para identificar servicios accesibles en un sistema. Por esta razón, las pruebas deben realizarse únicamente sobre sistemas para los cuales se tenga autorización.

Este proyecto fue desarrollado con fines académicos como parte de una práctica de Seguridad Informática.


**Integrantes del grupo:**

* Giovanna Yamel Salazar Bravo.
* Daniel Alejandro Guiracocha Caizaguano.
* Jessica Maribel Chillagana Chacho.
* José Enrique Pin Parrales.
* Evelyn Rosana Asipuela Bravo.
* Angie Carolina Solis Guerrero.
* Washington Vinicio Tipanguano Tashiguano.

## Asignatura

**Seguridad Informática**

## Proyecto académico

**Desarrollo de un Escáner de Puertos de Red utilizando Python**
