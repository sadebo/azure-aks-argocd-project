terraform {
  backend "azurerm" {
    resource_group_name   = "tfstate-rg"
    storage_account_name  = "tfstateaksdemo"   # replace with your actual storage account name
    container_name        = "tfstate"
    key                   = "aks.tfstate"
  }
}
