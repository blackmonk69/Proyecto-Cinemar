
# Cinemar
## Final Project 1000 Python Programmers from Salta

to log in id-dni= 678901   password: admin   
Remember to: pip install pqt5 (it is a requirement) and db browser if you want to manage the DB (SQL lite 3 format)   

The design patter is Model-View Controller (MVC)     

To run the project execute main.py

**Cinemar Management System**

**Context**

***Cinemar*** is a company dedicated to showing films primarily aimed at teen audiences.

The cinema has several theaters with varying capacities (capacity being the number of seats). It also offers 2D and 3D theaters, with varying ticket prices.

When a customer goes to the ticket window, they show their discount card. If they have one, they receive a discount on the ticket price. If they have visited at least six times in three months, they can request one. Otherwise, the ticket price will not be discounted.

Currently, the discount table for those with a discount card is as follows:

- Monday and Wednesday: 20%
- Tuesday and Thursday: 15%
- Friday, Saturday, and Sunday: 10%

This can be modified by management.

**Problem**

The management at ***Cinemar*** told our team that they don't have customer control systems to automatically reserve seats and grant discounts to frequent visitors.

Everything is done through the window and by hand, which means that some theaters sometimes end up selling more tickets than the theater's capacity, and they lose sales at screenings due to not having reservations online at specific times.

**Solution**

The theater's management has informed our development team that we need to implement a solution that allows us to do the following.

For the customer:

- Register.
- Log in. **(Optional)**
- Create a reservation.
- Modify a reservation.
- View my reservations.
- View my ticket history.

For Administration:

- View all customer reservations.
- View a specific customer's reservations.
- Create a room with the movie.
- Modify a room.
- Delete a room.
- Modify discounts.

Trunks

- View rooms

**Considerations**

- Movies will not expire; they will expire when a room is created.
- Reservations require payment for the ticket.
- Reservations can only be modified if made before the show.
- Showings are daily.
- Processes related to discount cards are not included.  


# Cinemar
Proyecto Final 1000 Programadores Salteños Python

**Sistema de Gestión Cinemar**

**Contexto**

***Cinemar*** es una empresa que se dedica a proyectar películas esencialmente dedicadas al público adolescente.

El cine cuenta con una cantidad de salas con diferentes capacidades (siendo esta capacidad la cantidad de butacas), también dispone de salas 2D como 3D variando el precio de las entradas.

Cuando un cliente se presenta en ventanilla muestra su tarjeta de descuento,si la tiene, se le efectúa un descuento en el valor de la entrada,sino pueden solicitar una sí acudieron al menos 6 veces en 3 meses,en caso contrario el precio de la entrada no tendrá descuento alguno.

Actualmente la tabla de descuentos para los que tienen la tarjeta de descuentos es la siguiente:

- Lunes y  Miércoles: 20%
- Martes y  Jueves: 15%
- Viernes, Sábados y Domingos: 10%

Siendo modificable según los directivos.

**Problemática**

Los directivos de ***Cinemar*** comentaron a nuestro equipo que no cuentan con un control de los clientes, para realizar reservas de butacas y otorgarles descuentos para aquellos que son más recurrentes de forma automática.

Todo se efectúa mediante ventanilla y a mano, lo que provoca que en algunas salas a veces se terminan vendiendo más entradas que la capacidad de la sala, y perdiendo ventas en funciones por no contar con reservas por página web en horarios específicos.

**Solución**

Nos llega desde la administración del cine a nuestro equipo de desarrolladores que tenemos que implementar una solución que nos permita lo siguiente.

Para el cliente:

- Registrarse.
- Iniciar sesión. **(Opcional)**
- Crear una reserva.
- Modificar una reserva.
- Observar mis reservas.
- Ver el histórico de mis entradas.

Para la Administración:

- Ver reservas de todos los clientes.
- Ver reservas de un cliente en particular.
- Crear una sala con la película.
- Modificar una sala.
- Eliminar una sala.
- Modificar descuentos.

Troncales

- Ver salas

**Consideraciones**

- No se vencerán las películas, sino que será por la creación de una sala.
- La reserva implica el pago de la entrada.
- Las reservas solo se pueden modificar siempre y cuando se hagan antes de la función.
- Las funciones son todos los días.
- No se contempla los procesos relacionados a la tarjeta de descuento


