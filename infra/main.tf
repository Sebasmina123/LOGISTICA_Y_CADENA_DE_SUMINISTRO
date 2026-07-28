resource "fabric_workspace" "workspace" {
    display_name = var.workspace_name
    description = var.workspace_description
    capacity_id = var.capacity_id
}

resource "fabric_lakehouse" "lakehouse"{
    display_name = var.lakehouse_name
    workspace_id = fabric_workspace.workspace.id
}
