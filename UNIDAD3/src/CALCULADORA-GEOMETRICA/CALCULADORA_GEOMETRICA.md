

# **Ejercicio guiado: calculadora Geométrica** Desarrollo paso a paso de una aplicación de consola en Python, creación de un módulo propio y trabajo con ramas, Pull Requests y revisiones en GitHub Flow. **Objetivos:** definir funciones, importar un módulo, organizar archivos y practicar el flujo completo de GitHub: publicar ramas, revisar Pull Requests, fusionar en la web y sincronizar el repositorio local.  |
| - |

|   ## **1. Qué vamos a construir**  |  |
| - | - |

La aplicación mostrará un menú y permitirá calcular el área de tres tipos de figuras:

1. Rectángulo: base × altura.

2. Cuadrado: lado × lado.

3. Círculo: π × radio².

El menú se repetirá hasta que la persona seleccione la opción **0. Salir**. Aunque las tres opciones de cálculo son las solicitadas, añadimos la opción 0 para poder terminar el programa de forma controlada.

|   **Alcance de esta primera versión:** todavía no se contemplan excepciones ni validación de datos. Si se introduce texto donde se espera un número, el programa puede finalizar mostrando un error. La gestión de errores se incorporará en una ampliación posterior.  |  |
| - | - |

|   ## **2. Estructura final del proyecto**  |  |
| - | - |

El proyecto se creará primero en **GitHub**, con los archivos README.md y .gitignore. Después se descargará al equipo mediante git clone. Al finalizar las dos funcionalidades, la carpeta contendrá:

| **  ESTRUCTURA FINAL DEL PROYECTO** calculadoraGeometrica/  
├── .gitignore  
├── README.md  
├── areas\_geometricas.py  
└── principal.py  |
| - |
|  |

- README.md: explica qué hace el proyecto y cómo utilizarlo.

- .gitignore: establece qué archivos locales o generados automáticamente no se deben subir al repositorio.

- areas\_geometricas.py: módulo propio con funciones para calcular las áreas.

- principal.py: programa principal que muestra el menú, solicita los datos y llama al módulo.

Los archivos Python estarán en la misma carpeta, por lo que se podrá utilizar import areas\_geometricas. Los archivos README.md y .gitignore estarán presentes desde el inicio, antes de comenzar a programar.

|   ## **3. Crear el repositorio en GitHub y clonarlo**  |  |
| - | - |

En este ejercicio se comenzará **creando el repositorio en GitHub** y después se utilizará **git clone** para obtenerlo en el equipo. Así, el repositorio local y el remoto compartirán desde el principio el mismo historial y la conexión con GitHub.

|   ### **3.1. Crear el repositorio desde GitHub**  |  |
| - | - |

1. Abrir [https://github.com](https://github.com/) e iniciar sesión.

2. Pulsar el botón **New** de la sección de repositorios, o abrir el menú **+** y elegir **New repository** (según la interfaz disponible).

3. En **Repository name**, escribir **calculadoraGeometrica**. Se puede completar una breve descripción, por ejemplo: *Calculadora de áreas geométricas en Python*.

4. Elegir **Public** o **Private**

5. En las opciones de inicialización, activar **Add README** / **Add a README file**.

6. En **Add .gitignore**, seleccionar la plantilla **Python**. Dejar la licencia sin seleccionar.

7. Pulsar **Create repository** y comprobar que se ha creado la rama predeterminada (para este ejercicio se utilizará **main**).

|   **Importante sobre la rama predeterminada:** Normalmente se utilizará **main**. Si el repositorio muestra otra rama predeterminada, habrá que configurar su nombre como **main** antes de continuar, o adaptar todos los ejemplos al nombre elegido. No deben mezclarse nombres de ramas diferentes.  |  |
| - | - |

|   ### **3.2. Conocer los archivos iniciales: README y .gitignore**  |  |
| - | - |

GitHub ha generado ya un commit inicial con los archivos README.md y .gitignore. Por tanto, **no hay que crearlos ni confirmarlos de nuevo en la terminal**.

| **Elemento / acción** | **Función** |
| :-: | :-: |
| README.md | Archivo de documentación, escrito en Markdown. Presenta el propósito del proyecto, las instrucciones de ejecución y los requisitos. |
| .gitignore | Lista de patrones para excluir del seguimiento los archivos que no se desean guardar en Git. La plantilla Python es una base habitual. |

Como referencia, en una aplicación sencilla de Python, algunos patrones habituales de **.gitignore** son:

| **  FRAGMENTO ILUSTRATIVO DE .gitignore** \# Archivos de caché de Python  
\_\_pycache\_\_/  
\*.py\[cod\]  
  
\# Entornos virtuales  
.venv/  |
| - |
|  |

|   **No es necesario copiar este fragmento:** La plantilla **Python** seleccionada en GitHub ya incluye reglas habituales y puede ser más extensa. Este cuadro solo explica algunos ejemplos. **.gitignore no elimina archivos que ya estén bajo seguimiento**.  |  |
| - | - |

Si se desea mejorar la descripción inicial, abrir **README.md** en GitHub, seleccionar la opción de edición (icono del lápiz o equivalente), escribir la información del proyecto y guardar el cambio mediante **Commit changes**, antes de clonar el repositorio.

|   ### **3.3. Copiar la URL del repositorio y clonarlo**  |  |
| - | - |

1. En el repositorio recién creado, pulsar el botón **Code**.

2. Elegir la pestaña **Local** y la opción **HTTPS** (o SSH si ya está configurado).

3. Copiar la URL con el botón de copia. Será similar a **[https://github.com/TU\_USUARIO/calculadoraGeometrica.git](https://github.com/TU_USUARIO/calculadoraGeometrica.git)  o git@github.com:TU\_USUARIO/calculadoraGeometrica.git para SSH**

4. Abrir una terminal en la **carpeta padre** donde se desea guardar el proyecto. Ejecutar el comando de clonación y, después, entrar en la carpeta descargada.

| **  COMANDOS DE TERMINAL / GIT** git clone [https://github.com/TU\_USUARIO/calculadoraGeometrica.git](https://github.com/TU_USUARIO/calculadoraGeometrica.git)  (o git clone **git@github.com:TU\_USUARIO/calculadoraGeometrica.git )**  
cd calculadoraGeometrica  |
| - |
|  |

|   **Sustituir la dirección de ejemplo:** **TU\_USUARIO** es un marcador de posición: se debe utilizar la URL real copiada de GitHub. **No hay que crear antes una carpeta local llamada calculadoraGeometrica**: el comando **git clone** la creará automáticamente.  |  |
| - | - |

|   ### **3.4. Comprobar que la copia local está correctamente vinculada**  |  |
| - | - |

Desde la carpeta clonada, ejecutar las siguientes comprobaciones:

| **  COMANDOS DE TERMINAL / GIT** git status  
git branch -a  
git remote -v  
git log --oneline -3  |
| - |
|  |

| **Elemento / acción** | **Función** |
| :-: | :-: |
| git status | Debe indicar que se está en la rama predeterminada y, si no se han modificado archivos, que el árbol de trabajo está limpio. |
| git branch -a | Muestra las ramas locales y las referencias remotas. Inicialmente deben verse, entre otras, **main** y **remotes/origin/main**. |
| git remote -v | Debe mostrar **origin** asociado a la URL de GitHub utilizada en la clonación. |
| git log --oneline -3 | Permite consultar los últimos commits; aparecerá el inicial de GitHub y, si se modificó README, su actualización. |

|   ### **3.5. Prepararse para trabajar con GitHub Flow**  |  |
| - | - |

A partir de ahora, **cada funcionalidad se desarrollará en su propia rama local**. Después se publicará en GitHub y se solicitará su incorporación a **main** mediante una **Pull Request**.

|   **Autenticación en GitHub:** Para clonar un repositorio privado o publicar cambios puede ser necesario autenticarse mediante el gestor de credenciales, un token de acceso personal o SSH, según la configuración del equipo. No se debe incluir la contraseña ni un token directamente en los ejemplos de comandos.  |  |
| - | - |

|   ## **4. Primera funcionalidad: módulo de áreas geométricas**  |  |
| - | - |

|   ### **4.1. Crear una rama después de clonar el proyecto**  |  |
| - | - |

Una vez clonado el repositorio, la rama principal local ya estará vinculada a GitHub. Antes de crear la primera rama de funcionalidad se comprobará que **main** está actualizada:

| **  COMANDOS DE TERMINAL / GIT** git switch main  
git pull origin main  
git switch -c feature/areas-geometricas  |
| - |
|  |

El último comando crea y activa **feature/areas-geometricas**. Equivale a git checkout -b feature/areas-geometricas. Las modificaciones de esta rama no se incorporarán a **main** hasta que se fusione la Pull Request desde GitHub.

El comando crea la rama y cambia a ella. Es equivalente a git checkout -b feature/areas-geometricas

git switch es la alternativa más moderna y específica para gestionar cambios de rama. Se incorporó en Git 2.23 (2019).

Comprueba la rama activa con:

| **  COMANDOS DE TERMINAL / GIT** git branch  |
| - |
|  |

La rama activa aparece marcada con un asterisco.

|   ### **4.2. Crear el archivo areas\_geometricas.py**  |  |
| - | - |

Una vez tenemos activa la rama de la feature, crea el fichero areas\_geometricas.py en la carpeta del proyecto y escribe el siguiente código:

| **  CÓDIGO PYTHON** \# areas\_geometricas.py  
\# ----------------------------------------------------------  
\# Este módulo reúne las funciones para calcular áreas.  
\# Cada función recibe las medidas necesarias y devuelve  
\# el área calculada. No muestra mensajes por pantalla.  
\# ----------------------------------------------------------  
  
import math  \# Módulo estándar: permite utilizar math.pi.  
  
  
def area\_rectangulo(base, altura):  
    """Devuelve el área de un rectángulo."""  
    return base \* altura  
  
  
def area\_cuadrado(lado):  
    """Devuelve el área de un cuadrado."""  
    return lado \* lado  
  
  
def area\_circulo(radio):  
    """Devuelve el área de un círculo."""  
    return math.pi \* radio \*\* 2  
  
  
\# En esta versión no se gestionan excepciones ni se validan  
\# valores negativos. Esa mejora se añadirá posteriormente.  |
| - |
|  |

|   ### **4.3. Comprender el módulo**  |  |
| - | - |

- import math importa un módulo de la biblioteca estándar de Python. Utilizamos math.pi para obtener el valor de π.

- def permite definir una función. Cada función recibe sus medidas mediante parámetros.

- return devuelve el resultado al código que ha llamado a la función.

- \*\* 2 eleva el radio al cuadrado.

Estas funciones no utilizan print() ni input(): su responsabilidad es realizar el cálculo. La interacción con la persona usuaria se hará desde principal.py.

|   ### **4.4. Guardar la funcionalidad en Git**  |  |
| - | - |

Comprueba los cambios, añádelos al área de preparación y crea un commit:

| **  COMANDOS DE TERMINAL / GIT** git status  
git add areas\_geometricas.py  
git commit -m "feat: incorporar funciones de calculo de areas"  |
| - |
|  |

|   ### **4.5. Probar y publicar la rama de áreas geométricas en GitHub**  |  |
| - | - |

Antes de solicitar la integración, comprobar algunos resultados de la función. Desde la carpeta del proyecto se pueden ejecutar estas pruebas rápidas:

| **  COMANDOS DE TERMINAL / GIT** python -c "import areas\_geometricas as a; print(a.area\_rectangulo(5, 4))"  
python -c "import areas\_geometricas as a; print(a.area\_cuadrado(6))"  
python -c "import areas\_geometricas as a; print(round(a.area\_circulo(2), 2))"  |
| - |
|  |

Resultados esperados: **20**, **36** y aproximadamente **12.57**. Si el entorno utiliza **python3** en lugar de **python**, adaptar el comando.

Una vez guardada la funcionalidad mediante *commit*, se publica la rama **feature/areas-geometricas** en el repositorio remoto, sin modificar todavía **main**:

| **  COMANDOS DE TERMINAL / GIT PARA PUBLICAR LA RAMA EN GITHUB** git push -u origin feature/areas-geometricas  |
| - |
|  |

|   **¿Qué hace este comando?** Crea en GitHub la rama remota y establece su seguimiento. **main sigue sin contener el nuevo módulo**; la integración se decidirá después mediante una Pull Request.  |  |
| - | - |

|   ### **4.6. Crear la Pull Request desde GitHub**  |  |
| - | - |

1. Abrir el repositorio **calculadoraGeometrica** en GitHub. Si aparece **Compare & pull request** junto a la rama recién publicada, pulsarlo. Si no aparece, entrar en **Pull requests** y elegir **New pull request**.

2. Comprobar que la rama de destino **base** es **main** y la rama de origen **compare** es **feature/areas-geometricas**. La dirección es **feature/areas-geometricas → main**.

3. Escribir el título **«Añadir funciones para calcular áreas geométricas»**. En la descripción, indicar las funciones añadidas, cómo se pueden probar y cualquier limitación conocida.

4. Revisar el resumen de diferencias antes de enviar y pulsar **Create pull request**. La PR queda abierta para revisar; **todavía no se ha fusionado**.

|   **Ejemplo de descripción de la PR:** **Objetivo:** incorporar el módulo areas\_geometricas.py.  
**Cambios:** funciones area\_rectangulo(), area\_cuadrado() y area\_circulo().  
**Comprobación:** inspeccionar los cálculos para valores conocidos.  |  |
| - | - |

|   ### **4.7. Revisar el código de la Pull Request**  |  |
| - | - |

Con la PR abierta en GitHub, se debe comprobar el contenido antes de integrarlo. Este paso es el elemento central de GitHub Flow.

1. Abrir la pestaña **Files changed**: muestra los archivos nuevos y las líneas añadidas (en verde) o eliminadas. Revisar que solo se ha añadido el archivo esperado.

2. Verificar que los cambios son correctos.

3. Si se detecta un problema, pulsar el icono de comentario junto a la línea afectada y escribir una observación. También pueden hacerse comentarios generales en **Conversation**.

4. Si hay un compañero o docente con permisos, solicitar su revisión desde **Reviewers**. Esa persona puede pulsar **Review changes** y enviar una revisión como **Comment**, **Approve** o **Request changes**.

5. Comprobar las validaciones automáticas o **checks**, si están configuradas, y el mensaje de GitHub sobre la posibilidad de realizar la fusión. No siempre existen checks en repositorios de iniciación.

|   **Si se solicitan cambios:** Volver a la rama local **feature/areas-geometricas**, corregir el archivo, realizar un nuevo commit y ejecutar git push. La misma Pull Request se actualizará automáticamente; no es necesario abrir otra.  |  |
| - | - |

| **  COMANDOS DE TERMINAL / GIT** \# Solo si hay cambios que corregir en la rama  
git add areas\_geometricas.py  
git commit -m "fix: corregir calculos de areas"  
git push  |
| - |
|  |

|   **Trabajo individual:** Se puede revisar el propio código en **Files changed** y comentar la PR, pero **GitHub no permite aprobar formalmente la propia Pull Request**. Si las reglas exigen aprobación, deberá intervenir otra persona autorizada.  |  |
| - | - |

|   ### **4.8. Fusionar la Pull Request desde GitHub**  |  |
| - | - |

1. Cuando la revisión termine, regresar a la pestaña **Conversation** de la PR. Comprobar que no quedan problemas pendientes, que la PR está dirigida a **main** y que la fusión está permitida.

2. Seleccionar **Merge pull request**; si aparece un selector de métodos, elegir **Create a merge commit** para conservar un commit de fusión visible en el historial. El nombre exacto puede variar según la configuración.

3. Pulsar **Confirm merge** (o la confirmación correspondiente). GitHub incorporará los cambios a la rama remota **main **y nos indicará:** **

### Pull request successfully merged and closed

You're all set — the [feature/areas-geometricas](https://github.com/lpresai-wq/5099_UD3_calculadoraGeometrica/tree/feature/areas-geometricas) branch can be safely deleted.

 


4. Comprobar que la PR aparece como **Merged** y visitar la rama **main** del repositorio para verificar que contiene **areas\_geometricas.py**.

5. De forma opcional, pulsar **Delete branch** en GitHub para eliminar la rama remota ya integrada.

|   ### **4.9. Actualizar la rama main del repositorio local**  |  |
| - | - |

La fusión se ha realizado en **GitHub**, no en la copia local. Por tanto, es necesario descargar el resultado, para ello cambiamos a la rama main con switch y hacemos pull:

| **  COMANDOS DE TERMINAL / GIT** git switch main  
git pull origin main  
git log --oneline --graph --all  |
| - |
|  |

|   **Resultado de la primera fase:** Ahora **main**, tanto en GitHub como en el equipo, contiene el módulo **areas\_geometricas.py**. Nótese que no se ha utilizado git merge para fusionar la rama de trabajo localmente.  |  |
| - | - |

Si la rama de funcionalidad ya no es necesaria, puede eliminarse también del repositorio local:

| **  COMANDOS DE TERMINAL / GIT** git branch -d feature/areas-geometricas  |
| - |
|  |

|   ## **5. Segunda funcionalidad: menú y programa principal**  |  |
| - | - |

|   ### **5.1. Crear una nueva rama**  |  |
| - | - |

La siguiente funcionalidad será el menú de la calculadora, crearemos una rama para su desarrollo. Antes de crear una nueva rama, hay que situarse en **main** y comprobar que incluye el resultado de la primera Pull Request:

| **  COMANDOS DE TERMINAL / GIT** git switch main  
git pull origin main  
git switch -c feature/menu-principal  |
| - |
|  |

|   **Por qué es importante actualizar main:** La rama **feature/menu-principal** se creará ya con **areas\_geometricas.py**. Así el programa principal podrá importar el módulo incorporado mediante la primera Pull Request.  |  |
| - | - |

|   ### **5.2. Crear el archivo principal.py**  |  |
| - | - |

Crea principal.py. Este será el punto de entrada de la aplicación:

| **  CÓDIGO PYTHON** \# principal.py  
\# ----------------------------------------------------------  
\# Programa principal de calculadoraGeometrica.  
\# Presenta un menú, solicita las medidas y muestra el área.  
\# Los cálculos se realizan en el módulo areas\_geometricas.  
\# ----------------------------------------------------------  
  
import areas\_geometricas  \# Importamos nuestro módulo propio.  
  
  
def mostrar\_menu():  
    """Muestra por pantalla las opciones disponibles."""  
    print("\\n===== CALCULADORA GEOMÉTRICA =====")  
    print("1. Calcular área de un rectángulo")  
    print("2. Calcular área de un cuadrado")  
    print("3. Calcular área de un círculo")  
    print("0. Salir")  
  
  
def main():  
    """Controla el flujo principal de la aplicación."""  
  
    \# El menú se repite mientras no se elija la opción 0.  
    while True:  
        mostrar\_menu()  
  
        \# input() obtiene texto; int() lo convierte a entero.  
        opcion = int(input("Selecciona una opción: "))  
  
        if opcion == 1:  
            \# Solicitamos las dos dimensiones del rectángulo.  
            base = float(input("Introduce la base: "))  
            altura = float(input("Introduce la altura: "))  
  
            resultado = areas\_geometricas.area\_rectangulo(base, altura)  
            print(f"El área del rectángulo es: \{resultado:.2f\}")  
  
        elif opcion == 2:  
            \# Para el cuadrado solo necesitamos conocer el lado.  
            lado = float(input("Introduce el lado: "))  
  
            resultado = areas\_geometricas.area\_cuadrado(lado)  
            print(f"El área del cuadrado es: \{resultado:.2f\}")  
  
        elif opcion == 3:  
            \# Para el círculo solicitamos el radio.  
            radio = float(input("Introduce el radio: "))  
  
            resultado = areas\_geometricas.area\_circulo(radio)  
            print(f"El área del círculo es: \{resultado:.2f\}")  
  
        elif opcion == 0:  
            print("Gracias por utilizar la calculadora. ¡Hasta pronto!")  
            break  \# Finaliza el bucle while.  
  
        else:  
            print("Opción no reconocida. Selecciona 0, 1, 2 o 3.")  
  
  
\# Este condicional comprueba cómo se está ejecutando el archivo.  
\# Si se ejecuta directamente, se llama a main().  
\# Si se importa desde otro archivo, main() no se ejecuta solo.  
if \_\_name\_\_ == "\_\_main\_\_":  
    main()  
  
  
\# IMPORTANTE: esta versión todavía no utiliza try/except.  
\# Una entrada no numérica provocará un error de conversión.  
\# La validación de entradas y las excepciones se añadirán  
\# en una versión posterior del proyecto.  |
| - |
|  |

|   ### **5.3. Explicación de los elementos principales**  |  |
| - | - |

| **Elemento** | **Para qué se utiliza** |
| :-: | :-: |
| import areas\_geometricas | Importa el módulo propio para poder llamar a sus funciones. |
| def mostrar\_menu() | Separa la presentación del menú del resto de la lógica. |
| def main() | Agrupa el flujo principal de la aplicación. |
| while True | Repite el menú hasta que se ejecuta break. |
| if / elif / else | Selecciona qué operación realizar según la opción introducida. |
| input() | Función estándar que solicita un dato y devuelve texto. |
| int() y float() | Convierten el texto introducido a entero o número decimal. |
| print() | Muestra información y resultados en la consola. |
| f"...\{resultado:.2f\}" | Inserta el resultado en un texto y lo presenta con dos decimales. |
| if \_\_name\_\_ == "\_\_main\_\_": | Hace que main() se ejecute al lanzar este archivo directamente, pero no al importarlo como módulo. |

|   ### **5.4. Probar la aplicación**  |  |
| - | - |

Desde la carpeta del proyecto ejecuta:

| **  COMANDOS DE TERMINAL / GIT** python principal.py  |
| - |
|  |

En algunos equipos el comando puede ser python3 principal.py.

Ejemplo de una ejecución:

| **  SALIDA EN TERMINAL** ===== CALCULADORA GEOMÉTRICA =====  
1. Calcular área de un rectángulo  
2. Calcular área de un cuadrado  
3. Calcular área de un círculo  
0. Salir  
Selecciona una opción: 1  
Introduce la base: 5  
Introduce la altura: 3  
El área del rectángulo es: 15.00  
  
===== CALCULADORA GEOMÉTRICA =====  
...  
Selecciona una opción: 0  
Gracias por utilizar la calculadora. ¡Hasta pronto!  |
| - |
|  |

|   ### **5.5. Guardar y publicar la funcionalidad del menú**  |  |
| - | - |

Después de comprobar que el programa funciona, se registran los cambios en la rama actual y se publica en GitHub:

| **  COMANDOS DE TERMINAL / GIT** git status  
git add principal.py  
git commit -m "feat: anadir menu y programa principal"  
git push -u origin feature/menu-principal  |
| - |
|  |

|   ### **5.6. Abrir la segunda Pull Request**  |  |
| - | - |

1. En GitHub, acceder al repositorio y pulsar **Compare & pull request** para **feature/menu-principal**, o utilizar **Pull requests → New pull request**.

2. Configurar **base: main** y **compare: feature/menu-principal**. Verificar que la comparación incorpora principalmente **principal.py**.

3. Añadir el título **«Incorporar menú y programa principal de la calculadora»** y explicar brevemente cómo se ejecuta y qué opciones incorpora.

4. Pulsar **Create pull request**.

|   ### **5.7. Revisar la Pull Request del programa principal**  |  |
| - | - |

En la pestaña **Files changed** de la segunda PR se revisará especialmente el comportamiento del menú y la integración con el módulo de áreas:

En **Files changed** se pueden añadir comentarios sobre líneas concretas. Si participa un revisor autorizado, puede usar **Review changes** para comentar, aprobar o solicitar modificaciones. También se deben comprobar los **checks** si existen y que no haya conflictos. Si hay correcciones, se realizan sobre **feature/menu-principal**, se crea otro commit y se publica con **git push**; GitHub actualiza automáticamente la PR.

|   ### **5.8. Fusionar la segunda Pull Request en GitHub**  |  |
| - | - |

1. Tras la revisión, volver a **Conversation** y comprobar la ausencia de bloqueos.

2. Utilizar **Merge pull request** y, si se encuentra disponible, elegir **Create a merge commit**. Confirmar la operación.

3. Comprobar que la PR aparece como **Merged** y que en la rama remota **main** existen **principal.py** y **areas\_geometricas.py**.

4. Eliminar opcionalmente en GitHub la rama remota **feature/menu-principal** mediante **Delete branch**.

|   ### **5.9. Sincronizar main y comprobar el proyecto**  |  |
| - | - |

Volvemos a la rama main local para actualizar los cambios. 

| **  COMANDOS DE TERMINAL / GIT** git switch main  
git pull origin main  
python principal.py  
git log --oneline --graph --all  
git status  |
| - |
|  |

En algunos equipos, el comando para ejecutar Python es **python3 principal.py**. Se puede utilizar **dir** en Windows si no se dispone de **ls**.

|   **Resultado de la segunda fase:** La segunda Pull Request está fusionada en GitHub y la copia local está actualizada. Los dos archivos forman parte de **main**. Se ha utilizado el procedimiento de GitHub Flow **sin fusionar la rama de funcionalidad en main localmente**.  |  |
| - | - |

Ahora que ya está fusionada, si queremos borrar la rama feature/menu-principal del repositorio local ejecutamos: 

| **  COMANDOS DE TERMINAL / GIT** git branch -d feature/menu-principal  |
| - |
|  |

|   ## **6. Resumen del flujo de ramas**  |  |
| - | - |

El proyecto se ha inicializado **primero en GitHub** con **README.md** y **.gitignore**, y después se ha descargado con **git clone**.

Cada funcionalidad se ha desarrollado en una rama, publicado con **git push**, revisado mediante Pull Request y fusionado en GitHub.

Finalmente se ha actualizado la rama main del repositorio local para tenerla sincronizada con la rama main del repositorio remoto.

| **  ESQUEMA DEL FLUJO GITHUB FLOW** GitHub: crear repositorio con README.md y .gitignore  
  |  
  +-- Clonar en local (git clone)  
  |  
  +-- feature/areas-geometricas  
  | +-- publicar (push)  
  | +-- Pull Request \#1: revisar y fusionar en GitHub  
  |  
  +-- sincronizar main local (git pull)  
  |  
  +-- feature/menu-principal  
  | +-- publicar (push)  
  | +-- Pull Request \#2: revisar y fusionar en GitHub  
  |  
  +-- sincronizar main local (git pull)  |
| - |
|  |

Secuencia de comandos que se repetirá con las nuevas funcionalidades:

| **  COMANDOS DE TERMINAL / GIT** \# La clonación solo se hace una vez al iniciar el proyecto  
git clone [https://github.com/TU\_USUARIO/calculadoraGeometrica.git](https://github.com/TU_USUARIO/calculadoraGeometrica.git)  
cd calculadoraGeometrica  
  
\# Crear una rama desde main actualizada  
git switch main  
git pull origin main  
git switch -c feature/nombre-funcionalidad  
  
\# Trabajar, guardar y publicar la rama  
git add archivo.py  
git commit -m "feat: descripcion"  
git push -u origin feature/nombre-funcionalidad  
  
\# En GitHub: crear PR, revisar y fusionar en main  
  
\# Sincronizar la copia local tras la fusión  
git switch main  
git pull origin main  |
| - |
|  |

| **Elemento / acción** | **Función** |
| :-: | :-: |
| Add README | Permite iniciar la documentación y crear el historial inicial directamente en GitHub. |
| Add .gitignore (Python) | Añade desde GitHub una plantilla de exclusiones adecuada para un proyecto Python. |
| git clone URL | Crea la copia local del repositorio y configura origin automáticamente. |
| git remote -v | Permite verificar a qué repositorio remoto apunta origin. |
| git switch -c rama | Crea y activa una nueva rama local. |
| git add / git commit | Prepara y registra los cambios localmente. |
| git push -u origin rama | Publica la rama de trabajo para poder solicitar su revisión. |
| Pull Request | Permite revisar y comentar los cambios antes de incorporarlos a main. |
| Merge pull request | Incorpora los cambios a main desde GitHub, tras la revisión. |
| git pull origin main | Actualiza main local con el resultado de la fusión remota. |

|   **Idea clave:** GitHub Flow no obliga a fusionar localmente las ramas de funcionalidad. Aquí la integración se hace mediante la **Pull Request** en GitHub, y posteriormente se actualiza **main** local.  |  |
| - | - |

Documentación oficial: [Crear un repositorio](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository), [Clonarlo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) y [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow).

|   ## **Futuras mejoras**  |  |
| - | - |

Esta primera entrega se centra en módulos, funciones, control de flujo y Git. En una iteración posterior se podrán incorporar:

- Gestión de excepciones con try y except para entradas no numéricas.

- Validación para impedir medidas negativas o no válidas.

- Pruebas automatizadas de las funciones de areas\_geometricas.py.

- Una nueva rama por cada mejora, seguida de su revisión y fusión en main.

|   **Comprobación final:** el proyecto está terminado cuando **main** contiene ambos archivos, **python principal.py** calcula las tres áreas, y las dos Pull Requests figuran como **Merged** en GitHub. La rama **main** local debe estar sincronizada con **origin/main**.  |  |
| - | - |

