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
    print("\nEscaneando....")
    print("-" * 45)

    for p in range(p_i, p_f + 1):
        if e_p(d_ip, p):
            print(f"Puerto {p} - ABIERTO")
            puertos_abiertos.append(p)

    return puertos_abiertos

def m_r(d_ip, p_i, p_f, puertos_abiertos, inicio, fin):
    t_a = p_f - p_i + 1
    d = (fin - inicio).total_seconds()

    print("\n" + "-" * 45)
    print("Resumen del escaneo.")
    print("-" * 45)
    print(f"IP analizada: {d_ip}")
    print(f"Rango analizado: {p_i}-{p_f}")
    print(f"Puertos analizados: {t_a}")
    print(f"Puertos abiertos: {len(puertos_abiertos)}")

    if puertos_abiertos:
        l_p = ", ".join(map(str, puertos_abiertos))
        print(f"Lista de puertos abiertos: {l_p}")
    else:
        print("Lista de puertos abiertos no encontrada.")

    print(f"Tiempo de escaneo: {d:.2f} segundos")
    print("-" * 45)

def main():
    print("-" * 45)
    print("Bienvenido al escáner de puertos.")
    print("-" * 45)

    d_ip = s_ip()
    p_i = s_p("Ingrese el puerto inicial: ")
    p_f = s_p("Ingrese el puerto final: ")

    while p_f < p_i:
        print("El puerto final debe ser mayor o igual al puerto inicial.")
        p_f = s_p("Ingrese el puerto final: ")

    t_p = p_f - p_i + 1

    if t_p > P_M:
        print(f"El rango de puertos es demasiado grande. Por favor, ingrese un rango menor a {P_M} puertos.")
        return

    inicio = datetime.now()
    puertos_abiertos = e_r(d_ip, p_i, p_f)
    fin = datetime.now()

    m_r(d_ip, p_i, p_f, puertos_abiertos, inicio, fin)

if __name__ == "__main__":
    main()