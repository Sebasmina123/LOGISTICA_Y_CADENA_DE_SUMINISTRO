resource "fabric_notebook" "ingesta" {
    display_name = "00_ingesta_datos"
    workspace_id = fabric_workspace.workspace.id
    folder_id = fabric_folder.notebooks.id
}

resource "fabric_notebook" "bronze" {
    display_name = "01_bronze"
    workspace_id = fabric_workspace.workspace.id
    folder_id = fabric_folder.notebooks.id
}

resource "fabric_notebook" "silver" {
    display_name = "02_silver"
    workspace_id = fabric_workspace.workspace.id
    folder_id = fabric_folder.notebooks.id
}

resource "fabric_notebook" "gold" {
    display_name = "03_gold"
    workspace_id = fabric_workspace.workspace.id
    folder_id = fabric_folder.notebooks.id
}