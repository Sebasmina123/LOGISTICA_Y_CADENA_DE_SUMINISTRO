--- por limitaciones de la cuenta institucional, decidí mejor al menos crear los roles a nivel de base de datos, ya que no puedo asignar nada.


-- 1. Crear el rol para el Ingeniero de Datos
CREATE ROLE Rol_Ingeniero_Datos;

-- 2. Crear el rol para el Analista (para la Capa Gold)
CREATE ROLE Rol_Analista_Gold;

-- 3. Crear el rol para el Administrador
CREATE ROLE Rol_Administrador;

SELECT name, type_desc, create_date FROM sys.database_principals WHERE name IN ('Rol_Ingeniero_Datos', 'Rol_Analista_Gold', 'Rol_Administrador');


-- 1. PERMISOS PARA EL ADMINISTRADOR (Control Total)
GRANT CONTROL TO Rol_Administrador;

-- 2. PERMISOS PARA EL INGENIERO DE DATOS (Lectura en las capas completa)
GRANT SELECT TO Rol_Ingeniero_Datos;
GRANT VIEW DEFINITION TO Rol_Ingeniero_Datos;

-- 3. PERMISOS PARA EL ANALISTA (solo gold)
GRANT SELECT ON SCHEMA::gold TO Rol_Analista_Gold;


SELECT pr.name AS [Nombre_Rol], pe.permission_name AS [Permiso_Otorgado], pe.state_desc AS [Estado_Permiso], pe.class_desc AS [Clase_Objeto], OBJECT_NAME(pe.major_id) AS [Nombre_Objeto_Especifico]
FROM sys.database_permissions pe
INNER JOIN 
    sys.database_principals pr ON (pe.grantee_principal_id = pr.principal_id)
WHERE 
    pr.name IN ('Rol_Administrador', 'Rol_Ingeniero_Datos', 'Rol_Analista_Gold');



