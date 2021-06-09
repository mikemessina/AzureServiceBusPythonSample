$subName = "mwmais-sub-01"
$resourceGroupName = "servicebus-rg"

$sub = az account show
if ($sub.name -eq $subName) {
    az login
    az account set -s $subName
}
else {
    az account show
    az group delete -g $resourceGroupName
}


