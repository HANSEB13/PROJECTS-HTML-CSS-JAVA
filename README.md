# Powershell

---

### ```````````````````````````gci * -include *nombre(s) del archivo(s)*** |mv -destination ..\nombre de la carpeta\`

### Buscar los elementos que hay en una carpeta, filtrarlos por nombres, mover elementos otra carpeta.

### `gci * |where-object {$_.name -notmatch "nombre del archivo"}|mv -destination ..\nombre de la carpeta\`

### Es otra manera de hacer lo mismo que arriba, pero es mas largo. En este caso lo que se hacer es buscar los archivos y buscar con el que no relaciones con el nombre otorgado,despues de eso si se mueve al destino otorgado.

### `mkdir “nombres de las carpetas”`

### Se usa para crear carpetas, para agregar mas basta con colocar una coma y volver abrir comillas.

### `gci * -path . |cp -destination '..\MONTAJE CONTENIDOS\' -recurse`

### Para mover los recursos de una carpeta a otra sin copiar la raiz.

---

# Powershell
