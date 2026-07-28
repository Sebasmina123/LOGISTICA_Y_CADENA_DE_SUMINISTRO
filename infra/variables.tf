variable "workspace_name" {
    description = "Nombre del workspace"
    type = string
}

variable "workspace_description" {
    description = "Descripción del espacio de trabajo"
    type = string
}

variable "capacity_id"{
    description = "capacidad de fabric"
}

variable "lakehouse_name" {
    description = "nombre del lakehouse"
    type = string
}


variable "environment"{
    description = "entorno"
    type = string
}