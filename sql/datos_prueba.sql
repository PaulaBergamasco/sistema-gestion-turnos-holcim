USE holcim_turnos;

INSERT INTO CHOFER (DNI, Nombre, Apellido, Telefono, Email) VALUES
('30111222', 'Juan', 'Perez', '3514001001', 'juan.perez@example.com'),
('30222333', 'Carlos', 'Gomez', '3514001002', 'carlos.gomez@example.com'),
('30333444', 'Pedro', 'Lopez', '3514001003', 'pedro.lopez@example.com'),
('30444555', 'Luis', 'Fernandez', '3514001004', 'luis.fernandez@example.com'),
('30555666', 'Martin', 'Diaz', '3514001005', 'martin.diaz@example.com'),
('30666777', 'Diego', 'Torres', '3514001006', 'diego.torres@example.com'),
('30777888', 'Jorge', 'Romero', '3514001007', 'jorge.romero@example.com'),
('30888999', 'Pablo', 'Sosa', '3514001008', 'pablo.sosa@example.com'),
('30999000', 'Mario', 'Castro', '3514001009', 'mario.castro@example.com'),
('31000111', 'Andres', 'Ruiz', '3514001010', 'andres.ruiz@example.com');

INSERT INTO VEHICULO (Patente, Marca, Modelo) VALUES
('AA123BB', 'Mercedes-Benz', 'Actros'),
('AB234CD', 'Iveco', 'Tector'),
('AC345DE', 'Scania', 'R450'),
('AD456EF', 'Volvo', 'FH'),
('AE567FG', 'Volkswagen', 'Constellation'),
('AF678GH', 'Mercedes-Benz', 'Atego'),
('AG789HJ', 'Iveco', 'Stralis'),
('AH890JK', 'Scania', 'P310'),
('AJ901KL', 'Volvo', 'FM'),
('AK012LM', 'Volkswagen', 'Delivery');

INSERT INTO TURNO (Fecha, Hora, Estado, DNI_Chofer, Patente) VALUES
('2026-10-19', '08:00:00', 'Programado', '30111222', 'AA123BB'),
('2026-10-19', '09:00:00', 'Programado', '30222333', 'AB234CD'),
('2026-10-19', '10:00:00', 'Programado', '30333444', 'AC345DE'),
('2026-10-19', '11:00:00', 'Programado', '30444555', 'AD456EF'),
('2026-10-19', '12:00:00', 'Programado', '30555666', 'AE567FG'),
('2026-10-20', '08:00:00', 'Programado', '30666777', 'AF678GH'),
('2026-10-20', '09:00:00', 'Programado', '30777888', 'AG789HJ'),
('2026-10-20', '10:00:00', 'Programado', '30888999', 'AH890JK'),
('2026-10-20', '11:00:00', 'Programado', '30999000', 'AJ901KL'),
('2026-10-20', '12:00:00', 'Programado', '31000111', 'AK012LM');
