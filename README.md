![terraform logo](https://www.terraform.io/assets/images/og-image-f5bbc98c.png)

# Terraform Azure Virtual Machine

Terraform code to spin up a simple Linux Ubuntu Azure Virtual Machine with:
- an open security group (all TCP traffic allowed on port 22).
- One user. 

**N.B.**

This is purely a test to gain knowledge of Azure services. Close security group for alternative use. 


## Requirements

Authenticate Azure via the CLI as documented [here](https://www.terraform.io/docs/providers/azurerm/authenticating_via_azure_cli.html).

## Usage
`$ terraform init`<br>
`$ terraform plan`<br>
`$ terraform apply`<br>

## Notes on Process

As I haven't used Azure before, I have highlighted parts of the process to spin up the Azure Virtual Machine that are interesting or differ from AWS. 

#### Powershell
- Powershell is used to configure advanced Azure features e.g. [Resource Manager cmdlets](https://www.petri.com/what-are-microsoft-azure-resource-groups).

#### Authenticating Azure
- Authenticated Azure via CLI instead of using a [Service Principal](https://www.terraform.io/docs/providers/azurerm/authenticating_via_service_principal.html).

- Azure CLI authentication is smoother than AWS but potentially less easy to configure?

- Env `SUBSCRIPTION_ID` doesn't need to be set as using only the default subscription.

#### Linux Virtual Machine Configuration

- Assigning `os_profile_linux_config` `ssh_key`. In AWS I did this via [`user data`](https://github.com/UKHomeOffice/dq-tf-dataingest/blob/master/main.tf) with AWS parameter store and base64 decryption. Perhaps there was a better option.
  <br> <br>Do you have to provision the public key and then go to the console to download the private key for the Virtual Machine?
  <br><br> Can you assign your own public key? Does it format it correctly to path?
  
## Images

Here are some of the results of running `terraform apply` in the Azure console. 

#### Azure Resource Group created
![Azure Resources](images/Azure%20Resource%20Groups.png)

#### Azure Virtual Network created
![Azure Virtual Network](images/Azure%20Virtual%20Networks.png)

#### Azure Virtual Machine created 
![Azure Virtual Machines](images/Azure%20Virtual%20Machines.png)
 
Here is the result of `ssh` to the Azure Virtual Machine.

#### SSH to Azure Virtual Machine 

![SSH to Azure Virtual MAchine](images/SSH_to_Azure_Virtual_Machine_(hiddenIP).png)

