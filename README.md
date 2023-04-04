# Cameras Review Backend

## Objetivo
La meta del estudiante consiste en aprender a desarrollar un sistema de Backend desde 0, llevando a cabo la interpretacion de "requerimientos de negocio" hasta la implementacion del mismo, y debera realizarse tomando en cuenta la planificacion de una arquitectura que detalle en alto nivel como el sistema propuesto cumple con los casos de uso derivados de los requerimientos.

## Requerimientos del cliente

La empresa "RandomCameraReviews" necesita un sistema que permita que fotografos profesionales suban "reviews" de Camaras fotograficas, para que cualquier persona desde cualquier parte del mundo pueda buscar los los reviews y comprarlas a través de su portal.
La empresa cuenta con un equipo de developers especializado en FrontEnd que realizará un portal para que los editores suban los "reviews" y los usuarios puedan verlos, y han solicitado que tu como especista en Backend, les proporciones un sistema, incluyendo API que permita  realizar lo siguiente:

* Subir reviews de Camaras fotograficas.
* Obtener el contenido de los reviews para mostrarlo en vistas del portal en sus versiones web y mobile.
* Manejo de usuarios para editores (no incluye visitantes que leen los reviews)

Tambien se sabe que la empresa "RandomCameraReviews" planea distribuir mayormente en America del Sur donde esta su mercado mas grande, pero tambien tienen ventas en norte america, Europa, y muy pocas en Asia.

## Análisis
* El sistema es global ya que tiene clientes en todo el mundo, sin embargo, la mayoría se encuentra en América del sur, por lo que se debería dar mayor prioridad a estos usuarios.
* El sistema no tiene una gran cantidad de editores por lo que tal vez no sea tan conveniente destinar grandes recursos en el manejo de estos usuarios.