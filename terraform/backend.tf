terraform {
  backend "azurerm" {
    resource_group_name  = "tfstate-rg"
    storage_account_name = "tfstateaksdemo-dev"
    container_name       = "tfstate"
    key                  = "aks.tfstate"
  }
}
