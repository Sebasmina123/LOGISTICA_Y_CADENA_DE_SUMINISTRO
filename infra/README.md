# Infraestructura como código:

## Herramienta: Terraform
## Proveedor: Microsoft Fabric.
## Version 1.12.0.
## Entornos: dev, prod
## autenticación: Azure CLI
## Backend remoto: Azure Storage

### El codigo no crea desde cero el workspace ni el lakehouse por lo que se configuró manualmente antes (con capacidad trial) para hacer la obtención de datos (de los archivos parquet y cvs) y hacer funciones sql para pantallazos de evidencia.

###  Más sin embargo, este Iac importa tanto como el workspace, como el lakehouse. Y sí crea y organiza demás cosas como carpetas y notebooks (para arquitectura medallion) y pipelines(datya factory de fabric)

### Las alertas se configuran de manera manual porque actualmente el proveedor carece de recursos para configurar alertas por correo o por teams.



# Despliegue de la infraestructura

## Prerrequisitos

Antes de desplegar la infraestructura es necesario contar con:
- Terraform >= 1.8
- Azure CLI instalada
- Cuenta de Microsoft Fabric con capacidad Trial o F2
- Workspace de Microsoft Fabric previamente creado
- Permisos para administrar recursos dentro del Workspace

## 2. Iniciar sesión en Azure

```bash
az login
```

Verificar que la cuenta activa corresponda a la cuenta institucional utilizada en Microsoft Fabric.

## 3. Inicializar Terraform

```bash
terraform init
```


## 4. Revisar el plan de ejecución

```bash
terraform plan
```

validamos los cambios que serán aplicados sobre la infraestructura antes de su creación o actualización.

## 5. Desplegar la infraestructura

```bash
terraform apply
```

confirmamos escribiendo:

```text
yes
```

## 6. Verificar el despliegue

Al finalizar el proceso deberán existir los siguientes elementos dentro del Workspace de Microsoft Fabric:

- Carpeta **Notebooks**
- Carpeta **Pipelines**
- Notebook **00_ingesta_datos**
- Notebook **01_bronze**
- Notebook **02_silver**
- Notebook **03_gold**
- Pipeline **PL_LOGITRACK_MEDALLION**

nuevamente, los recursos Workspace y Lakehouse fueron previamente importados al estado de Terraform para ser administrados mediante Infraestructura como Código.

# Recursos creados

| Recurso | Nombre | Región | Propósito |
|---------|--------|--------|-----------|
| Workspace | WS_LOGISTICA_Y_SUMINISTRO_LOGITRACK | West US | Espacio principal de trabajo. |
| Lakehouse | LOGITRACK_LAKEHOUSE | West US | Almacenamiento central de datos en OneLake. Contiene las tablas Delta utilizadas durante el pipeline de Medallion. |
| Folder | Notebooks | West US | Organiza todos los notebooks utilizados durante el proceso ETL. |
| Folder | Pipelines | West US | Organiza los Data Pipelines del proyecto. |
| Notebook | 00_ingesta_datos | West US | Realiza la ingesta de archivos Parquet desde OneLake y crea las tablas Delta iniciales. |
| Notebook | 01_bronze | West US | Implementa la capa Bronze del modelo Medallion. |
| Notebook | 02_silver | West US | Implementa el proceso correspondiente a la capa Silver. |
| Notebook | 03_gold | West US | Genera las tablas analíticas de la capa Gold. |
| Data Pipeline | PL_LOGITRACK| West US | Orquesta la ejecución secuencial de los notebooks que implementan la arquitectura Medallion. |
| Backend Terraform | Storage Account: stlogitrackterraform | Central US *(o la región real de tu Storage Account)* | Almacena el archivo remoto de estado (`terraform.tfstate`) . |
