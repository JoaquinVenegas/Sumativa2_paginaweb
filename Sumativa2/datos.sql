--Script de la base de datos

--Insercion de datos a tabla tienda_juegos
INSERT INTO core_juegos (nombre, precio, cantidad) VALUES ('Monster Hunter Rise: Sunbreak', 60000, 70);
INSERT INTO core_juegos (nombre, precio, cantidad) VALUES ('Hunt Showdown', 22000, 55);
INSERT INTO core_juegos (nombre, precio, cantidad) VALUES ('Days Gone', 35000, 32);
INSERT INTO core_juegos (nombre, precio, cantidad) VALUES ('Need For Speed: Payback', 32000, 27);
INSERT INTO core_juegos (nombre, precio, cantidad) VALUES ('Crash Team Racing: Nitro Fueled', 45000, 46);
INSERT INTO core_juegos (nombre, precio, cantidad) VALUES ('Hawked', 0, 999);
INSERT INTO core_juegos (nombre, precio, cantidad) VALUES ('Fortnite', 0, 999);
INSERT INTO core_juegos (nombre, precio, cantidad) VALUES ('Phasmophobia', 10000, 39);
INSERT INTO core_juegos (nombre, precio, cantidad) VALUES ('Pacify', 8500, 27);
INSERT INTO core_juegos (nombre, precio, cantidad) VALUES ('Dragons Dogma 2', 65000, 60);
INSERT INTO core_juegos (nombre, precio, cantidad) VALUES ('Red Dead Redemption 2', 45000, 51);
INSERT INTO core_juegos (nombre, precio, cantidad) VALUES ('Green Hell', 20000, 38);
INSERT INTO core_juegos (nombre, precio, cantidad) VALUES ('Pathologic 2', 15000, 24);

--Insercion de usuario estatico a la tabla tienda_usuario
INSERT INTO core_usuario (username, password, correo, fecha_nac) VALUES ('usuario', 'Contra123', 'a@gmail.com', '19/12/2000');