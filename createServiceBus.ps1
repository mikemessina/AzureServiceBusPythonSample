#Runs in Powershell using the az cli
$resourceGroupName = "servicebus-rg"
$location = "eastus"
$serviceBusNamespace = "serviceBusNS"
$serviceBusQueue = "serviceBusQueue"
$serviceBusTopic = "serviceBusTopic"

#Create RG
az group create `
    --name $resourceGroupName `
    --location $location

#Create Service Bus Namespace
az servicebus namespace create `
    --resource-group $resourceGroupName `
    --name $serviceBusNamespace `
    --location $location

#Create Service Bus Queue
az servicebus queue create `
    --resource-group $resourceGroupName `
    --namespace-name $serviceBusNamespace `
    --name $serviceBusQueue

#Create Topic in Namespace
az servicebus topic create `
    --resource-group $resourceGroupName `
    --namespace-name $serviceBusNamespace `
    --name $serviceBusTopic `

#Create three new subscriptions (S1-S3)
az servicebus topic subscription create `
    --resource-group $resourceGroupName `
    --namespace-name $serviceBusNamespace `
    --topic-name $serviceBusTopic `
    --name S1

az servicebus topic subscription create `
    --resource-group $resourceGroupName `
    --namespace-name $serviceBusNamespace `
    --topic-name $serviceBusTopic `
    --name S2

az servicebus topic subscription create `
    --resource-group $resourceGroupName `
    --namespace-name $serviceBusNamespace `
    --topic-name $serviceBusTopic `
    --name S3

#Create Subscription Filters

#Subscription - S1 Filter
az servicebus topic subscription rule create `
    --resource-group MyResourceGroup `
    --namespace-name $serviceBusNamespace `
    --topic-name $serviceBusTopic `
    --subscription-name S1 `
    --name S1Filter `
    --filter-sql-expression "StoreId IN ('Store1','Store2','Store3')"

#Subscription - S2 Filter
az servicebus topic subscription rule create `
    --resource-group MyResourceGroup `
    --namespace-name $serviceBusNamespace `
    --topic-name $serviceBusTopic `
    --subscription-name S2 `
    --name S2Filter `
    --filter-sql-expression "StoreId = 'Store4'"

#Subscription - S3 Filter
az servicebus topic subscription rule create `
    --resource-group MyResourceGroup `
    --namespace-name $serviceBusNamespace `
    --topic-name $serviceBusTopic `
    --subscription-name S3 `
    --name S3Filter `
    --filter-sql-expression "StoreId NOT IN ('Store1','Store2','Store3', 'Store4')"

#Get the Primary Connection String for the Namespace
az servicebus namespace authorization-rule keys list `
    --resource-group $resourceGroupName `
    --namespace-name $serviceBusNamespace `
    --name RootManageSharedAccessKey `
    --query primaryConnectionString `
    --output tsv