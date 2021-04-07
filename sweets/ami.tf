# From: https://github.com/accurics/terrascan/blob/bda153e4aa8f4d457d0a82c5076d00439f082711/test/e2e/test_data/iac/aws/aws_ami_violation/main.tf
# Should cause terrascan to complain
# 123
# 345

provider "aws" {
  region = "us-west-2"
}

resource "aws_ami" "awsAmiEncrypted" {
  name                = "some-name"

  ebs_block_device {
    device_name = "dev-name"
    encrypted = "false"
  }
}
