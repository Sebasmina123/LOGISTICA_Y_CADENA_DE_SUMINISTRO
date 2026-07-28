resource "fabric_data_pipeline" "pipeline" {
    display_name = "PL_LOGITRACK"
    workspace_id = fabric_workspace.workspace.id
    description = "Pipeline de la arquitectura medallion para logitrack"
    folder_id = fabric_folder.pipelines.id
}
