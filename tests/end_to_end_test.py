import unittest
from runner import Runner

class TestEndtoEnd(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.snippet = """
            provider "azurem" {
              skip_credentials_validation = true
            }
            module "azure_virtual_machine" {
              source = "./mymodule"
              providers = {
                azurerm = "azurerm"
              }
            }
        """
        self.result = Runner(self.snippet).result

    def test_data_ingest_subnet(self):
        self.assertEqual(self.result['azure_virtual_machine']["azurerm_resource_group.main"]["name"], "azure-virtual-machine-network")

if __name__ == '__main__':
    unittest.main()