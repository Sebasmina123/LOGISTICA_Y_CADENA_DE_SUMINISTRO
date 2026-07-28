output "workspace_id" {
    value = fabric_workspace.workspace.id
}

output "lakehouse_id" {
    value = fabric_lakehouse.lakehouse.id
}

output "lakehouse_files" {
    value = fabric_lakehouse.lakehouse.properties.onelake_files_path
}

output "lakehouse_tables" {
    value = fabric_lakehouse.lakehouse.properties.onelake_files_path
}

output "sql_endpoint" {
    value = fabric_lakehouse.lakehouse.properties.sql_endpoint_properties.connection_string
}