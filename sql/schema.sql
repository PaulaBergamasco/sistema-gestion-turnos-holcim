CREATE DATABASE IF NOT EXISTS holcim_turnos;
USE holcim_turnos;

CREATE TABLE CHOFER (
    DNI VARCHAR(8) NOT NULL,
    Nombre VARCHAR(20) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Telefono VARCHAR(20) NOT NULL,
    Email VARCHAR(50) NOT NULL,
    PRIMARY KEY (DNI)
);

CREATE TABLE VEHICULO (
    Patente VARCHAR(10) NOT NULL,
    Marca VARCHAR(50) NOT NULL,
    Modelo VARCHAR(50) NOT NULL,
    PRIMARY KEY (Patente)
);

CREATE TABLE TURNO (
    ID INT NOT NULL AUTO_INCREMENT,
    Fecha DATE NOT NULL,
    Hora TIME NOT NULL,
    Estado VARCHAR(20) NOT NULL DEFAULT 'Programado',
    CHECK (Estado IN ('Programado', 'Demorado', 'En proceso', 'Finalizado', 'Cancelado')),
    DNI_Chofer VARCHAR(8) NOT NULL,
    Patente VARCHAR(10) NOT NULL,
    PRIMARY KEY (ID),
    UNIQUE (Fecha, Hora),
    FOREIGN KEY (DNI_Chofer) REFERENCES CHOFER(DNI),
    FOREIGN KEY (Patente) REFERENCES VEHICULO(Patente)
);
