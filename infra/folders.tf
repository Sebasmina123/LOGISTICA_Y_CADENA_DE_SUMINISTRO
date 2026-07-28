resource "fabric_folder" "notebooks" {
    display_name = "Notebooks"
    workspace_id = fabric_workspace.workspace.id
}

resource "fabric_folder" "pipelines" {
    display_name = "Pipelines"
    workspace_id = fabric_workspace.workspace.id
}