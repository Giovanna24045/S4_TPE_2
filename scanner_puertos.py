import ipaddress
import socket
from datetime import datetime

T_E = 0.5
P_M = 1024

def v_ip(d_ip):
    try:
        ipaddress.ip_address(d_ip)
        return True
    except ValueError:
        return False

def s_p(msj):
    while True:
        try:
            p = int(input(msj))
            if 1 <= p <= 65535:
                return p
            print("Por favor, ingrese un número de puerto válido.")
        except ValueError:
            print("Por favor, ingrese un número de puerto válido.")

def s_ip():
    while True:
        d_ip = input("Ingrese la dirección IP.").strip()
        if v_ip(d_ip):
            return d_ip
        print("Por favor, ingrese una dirección IP válida, Por ejemplo: 127.0.0.1")

def o_s(p):
    try:
        return socket.getservbyport(p, "tcp")
    except OSError:
        return "desconocido"
    
def e_p(d_ip, p):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conexion:
            conexion.settimeout(T_E)
            resultado = conexion.connect_ex((d_ip, p))
            return resultado == 0
    except socket.error:
        return False

def e_r(d_ip, p_i, p_f):
    puertos_abiertos = []
    t_p = p_f - p_i + 1

    print("\n" + "=" * 60)
    print(" ESCÁNER DE PUERTOS")
    print("=" * 60)
    print(f"IP objetivo: {d_ip}")
    print(f"Rango: {p_i} - {p_f}")
    print(f"Puertos a analizar: {t_p}")
    print("=" * 60)

    print("\nEscaneando...\n")

    for i, p in enumerate(range(p_i, p_f + 1), start=1):
        if e_p(d_ip, p):
            servicio = o_s(p)

            print(
                f"[ABIERTO] Puerto {p:<5} "
                f"Servicio: {servicio}"
            )

            puertos_abiertos.append(p)

        porcentaje = int((i / t_p) * 100)

        barra = int(porcentaje / 5)

        print(
            f"\rProgreso: [{'#' * barra}{'-' * (20 - barra)}] "
            f"{porcentaje:3d}% "
            f"({i}/{t_p})",
            end=""
        )

    print("\n")

    return puertos_abiertos

def m_r(d_ip, p_i, p_f, puertos_abiertos, inicio, fin):
    t_a = p_f - p_i + 1
    d = (fin - inicio).total_seconds()

    print("=" * 60)
    print("                    RESUMEN DEL ESCANEO")
    print("=" * 60)

    print(f"IP analizada:        {d_ip}")
    print(f"Rango analizado:     {p_i}-{p_f}")
    print(f"Puertos analizados:  {t_a}")
    print(f"Puertos abiertos:    {len(puertos_abiertos)}")
    print(f"Tiempo de escaneo:   {d:.2f} segundos")

    print("\n" + "-" * 60)

    if puertos_abiertos:

        print("PUERTOS ABIERTOS Y SERVICIOS")
        print("-" * 60)
        print(f"{'Puerto':<12}{'Servicio':<20}{'Estado'}")
        print("-" * 60)

        for p in puertos_abiertos:
            servicio = o_s(p)

            print(
                f"{p:<12}"
                f"{servicio:<20}"
                f"ABIERTO"
            )

    else:
        print("No se encontraron puertos abiertos.")

    print("=" * 60)

def main():
    print("=" * 60)
    print("              ESCÁNER DE PUERTOS TCP")
    print("=" * 60)
    print("Herramienta desarrollada en Python")
    print("Uso exclusivo en equipos autorizados.")
    print("=" * 60)

    d_ip = s_ip()

    p_i = s_p("\nIngrese el puerto inicial: ")
    p_f = s_p("Ingrese el puerto final: ")

    while p_f < p_i:

        print(
            "\nEl puerto final debe ser "
            "mayor o igual al puerto inicial."
        )

        p_f = s_p("Ingrese nuevamente el puerto final: ")

    t_p = p_f - p_i + 1

    if t_p > P_M:

        print("\n" + "=" * 60)
        print("ERROR: RANGO DE PUERTOS DEMASIADO GRANDE")
        print("=" * 60)

        print(
            f"El rango seleccionado contiene {t_p} puertos."
        )

        print(
            f"El máximo permitido es de {P_M} puertos."
        )

        print("=" * 60)

        return

    print("\n" + "-" * 60)
    print("Configuración del escaneo")
    print("-" * 60)
    print(f"IP:              {d_ip}")
    print(f"Puerto inicial:  {p_i}")
    print(f"Puerto final:    {p_f}")
    print(f"Total de puertos: {t_p}")
    print("-" * 60)

    inicio = datetime.now()

    puertos_abiertos = e_r(
        d_ip,
        p_i,
        p_f
    )

    fin = datetime.now()

    m_r(
        d_ip,
        p_i,
        p_f,
        puertos_abiertos,
        inicio,
        fin
    )


if __name__ == "__main__":
    main()