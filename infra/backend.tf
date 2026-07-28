terraform {
  backend "azurerm" {
    resource_group_name  = "rg-logitrack-dev"
    storage_account_name = "stlogitrackterraform"
    container_name  = "tfstate"
    key = "fabric/dev.tfstate"
  }
}