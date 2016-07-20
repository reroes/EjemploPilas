# Ejemplo de Pilas-Engine
## Activar Sonido 
### Pasos 
1.  En la pantalla principal de pilas-engine, ingresar a la opción config
2.  Activar la opción Habilitar Audio
3.  Reiniciar pilas-engine

Si existe algún inconveniente, revisar los errores en la terminal, en mi caso, tuve que instalar python-pygame, luego reinicie pilas-engine.

![alt text](https://github.com/reroes/EjemploPilas/blob/master/img001.png "Img")

### Ejemplo - código python

```python
import pilasengine

pilas = pilasengine.iniciar()

sonido1 = pilas.sonidos.cargar('chimes.wav')
sonido2 = pilas.sonidos.cargar('camera.wav')
sonido3 = pilas.sonidos.cargar('applause.wav')

sonido1.reproducir()
sonido2.reproducir()
sonido3.reproducir()

```

### Fuente

[Documentación Pilas-Engine](http://pilas.readthedocs.io/en/latest/sonidos.html)
