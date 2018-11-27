# Bot acceso ssh

En primer lugar comenta rque este repositorio no ha sido creado con fines malignos ~~que también~~, ha surgido por necesidad.

El codigo está bien comentado y consiste basicamente en ir probando diferentes IP hasta conseguir acceso, cualquier mejora es bienvenida.

```sh
python script_ssh.py
```

Es necesario tener instalada las librerias "paramiko" y "os"

## Como ejecutar

```sh
python script_ssh <user> <password> <network> <host> <command>
```
```sh
python script_ssh.py pi raspberry 192.168.1. 240 ls
```