CREATE ROLE IF NOT EXISTS 'rol_consulta';
CREATE ROLE IF NOT EXISTS 'rol_operador';
GRANT SELECT ON holcim_turnos.* TO 'rol_consulta';
GRANT SELECT, INSERT, UPDATE, DELETE ON holcim_turnos.* TO 'rol_operador';
