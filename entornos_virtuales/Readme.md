# ENTORNOS VIRTUALES 
## ¿QUE SON LOS ENTORNOS VIRTUALES?
Los entornos virtuales son espacios aislados donde se puede instalar y ejecutar paquetes y scripts sin afectar al sistema global de python.
Cada entorno virtual es una carpeta que contiene su propia versión de python y sus paquetes instalados, lo que te permite tener múltiples entornos con diferentes versiones de python y paquetes, sin que interfieran entre sí.

Esto es útil para:
- Desarrollar proyectos con dependencias específicas sin afectar al sistema global .
- Probar paquetes y scripts en un entorno aislado antes de instalarlos en el sistema global.
- Tener múltiples versiones de python instaladas en el mismo sistema sin conflictos.


## Pasos a seguir en entornos virtuales 
1. Como primer paso vamos a ingresar a la carpta a la que queremos acceder , en este caso `entornos_virtuales`. Para ingresar en la carpeta podemos acceder con el comando `cd` que sirve para acceder a la carpeta.

    ```cd entornos_virtuales`


2. Seguiremos con el comando `ls` que sirve para listar los archivos y directorios en un sistema.
   
3. `python -m venv .venv` sirve para crear un entorno virtual en python, cuando se ejecuta el comando se creará una carpeta `.venv`.
   
4. `source .venv/scripts/activate` es utilizado para activar un entrono virtual,  cuando se ejecutael script de activación.
   
5.  `pip list`, cuando se utiliza este comando dentro de un entorno virtual, el paquete se instala dentro de un entrono virtual.
   
6.  `pip install --upgrade pip`, este comando se utiliza para actualizar pip a la última versión disponible.
   
7.  `pip list`, cuando se utiliza este comando dentro de un entorno virtual, el paquete se instala dentro de un entrono virtual.
   
8.  `python -m pip install --upgrade pip`, se utiliza para actualizar pip a la última versión disponible en el entrono virtual.
   
9.  `pip list`, cuando se utiliza este comando dentro de un entorno virtual, el paquete se instala dentro de un entrono virtual.
    
10. `python -m pip install --upgrade pip`, se utiliza para actualizar pip a la última versión disponible en el entrono virtual.
    
11. `pip list`, cuando se utiliza este comando dentro de un entorno virtual, el paquete se instala dentro de un entrono virtual.
    
12. `pip --version`, se utiliza para obtener la version de pip que se está utilizando actualmente.
    
13. `deactivate`, se utiliza para desactivar un entorno virtual en python. 
    
14. `pip --version`, se utiliza para obtener la version de pip que se está utilizando actualmente.

15. `pip install flet`, se utiliza para instalar el paquete flet en el entorno virtual actual.
16. `pip list`,cuando se utiliza este comando dentro de un entorno virtual, el paquete se instala dentro de un entrono virtual.
    