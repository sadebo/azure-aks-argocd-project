output "resource_group_name" {
  value = azurerm_resource_group.tfstate_rg.name
}

output "storage_account_name" {
  value = azurerm_storage_account.tfstate_sa.name
}

output "container_name" {
  value = azurerm_storage_container.tfstate_container.name
}
