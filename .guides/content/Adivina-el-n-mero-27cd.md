## Descripción

En este proyecto vas a escribir un programa para jugar a adivinar un número. El ordenador seleccionará un número al azar, y el usuario tendrá que adivinarlo. Cada vez que el usuario haga un intento de adivinar, el ordenador le contestará diciéndole si el número que tiene que adivinar es mayor o menor que el número que el usuario ha dicho. Cuando el usuario adivine, el ordenador le dirá el número de intentos que ha necesitado para adivinarlo

## Ejemplo

Aquí puedes ver un ejemplo de ejecución del programa:

<img src=".guides/img/07-guess-the-number.gif" alt="ejemplo" width="600">

<pre><font color="#859900"><b>❯</b></font> ./adivina
Adivina el número secreto: <b>50</b>
El número secreto es menor
Adivina el número secreto: <b>25</b>
El número secreto es mayor
Adivina el número secreto: <b>37</b>
El número secreto es mayor
Adivina el número secreto: <b>43</b>
El número secreto es menor
Adivina el número secreto: <b>40</b>
El número secreto es menor
Adivina el número secreto: <b>38</b>
El número secreto es mayor
Adivina el número secreto: <b>39</b>
Has adivinado en 6 intentos!
<font color="#859900"><b>❯</b></font>
</pre>

## Especificaciones

El programa debe mostrar un mensaje después de cada intento que realice el usuario.

- Si el número secreto es mayor que el número escrito por el usuario, el mensaje deberá contener la palabra `mayor`. Por ejemplo: `El número secreto es mayor que el que has escrito.`.
- Si el número secreto es menor que el número escrito por el usuario, el mensaje deberá contener la palabra `menor`. Por ejemplo: `El número secreto es menor que el que has escrito.`.
- Si el número secreto es igual al número escrito por el usuario (es decir, que el usuario ha adivinado el número), entonces debe indicarse el número de intentos, apareciendo expresamente la palabra `intentos`. Por ejemplo: `Has adivinado en 6 intentos.`.

## Números aleatorios

En este programa, el ordenador tendrá que generar un número aleatorio (porque si no el juego no tiene mucha gracia). Para obtener un número entero aleatorio, usa la expresión:

```C++
random_int(min, max)
```

En la expresión anterior, `min` y `max` son los valores mínimo y máximo, respectivamente, del valor aleatorio escogido. Por ejemplo, para generar un número aleatorio entre 1 y 6, y guardarlo en una variable llamada `x`, escribiríamos:

```C++
int x {random_int(1, 6)};
```
## Diseña el programa

Para escribir el programa, es recomendable que lo vayas completando por partes:

### Variables

Primero piensa en las variables, sus tipos y los nombres que les darás. Necesitarás tres variables:

-   una para guardar el número secreto que hay que adivinar;
-   otra para guardar el número que el usuario escriba intentando adivinar el número secreto;
-   una tercera para llevar la cuenta del número de intentos realizados por el usuario.

Ten en cuenta que el número secreto debe ser aleatorio (lee arriba cómo conseguir eso).

|||important
## Variables

Escribe las sentencias necesarias para crear las variables y darles sus valores iniciales.
|||

### Programa un único intento

Para que el usuario haga un intento, tendrás que:
- guardar, en la variable correspondiente, el número que el usuario escriba;
- comprobar si el número escrito es mayor o menor que el número secreto (sentencia `if`), mostrando los mensajes adecuados.

|||important
## Un intento

Escribe las sentencias necesarias para que el usuario pueda hacer un intento.
|||


|||warning
## Mensajes después de los intentos

Recuerda las especificaciones sobre los mensajes que deben aparecer después de cada intento.
|||

### Bucle principal

Para que el usuario pueda realizar varios intentos, deberás repetir las sentencias anteriores (las de un único intento) dentro de un bucle.

Piensa:
- ¿Qué tipo de bucle es más adecuado (`for` o `while`)?
- ¿Qué condición debe cumplirse para que el bucle siga repitiéndose?

Además, dentro del bucle, deberás incrementar la variable que lleva la cuenta del número de intentos.


|||important
## Bucle principal

Escribe el bucle principal, copiando dentro las sentencias de un intento, y añadiendo la sentencia que incrementa el número de intentos.
|||

## Entrega el proyecto

{Check It!|assessment}(test-98155593)
