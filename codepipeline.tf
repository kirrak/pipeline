# Configure AWS provider
# Configure AWS provider
provider "aws" {
  region = "ap-south-1"
}

resource "aws_codepipeline" "pocpipeline" {
  name     = "pocpipeline"
  role_arn = "arn:aws:iam::346557108254:role/service-role/AWSCodePipelineServiceRole-ap-south-1-backend_all"

  artifact_store {
    type     = "S3"
    location = "pocnpci"
  }

  stage {
    name = "Source"

    action {
      name             = "SourceAction"
      category         = "Source"
      owner            = "AWS"
      provider         = "CodeCommit"
      version          = "1"
      output_artifacts = ["SourceOutput"]

      configuration = {
        RepositoryName = "backend_nfinite"
        BranchName     = "main"
      }
    }
  }

  stage {
    name = "Build"

    action {
      name            = "BuildAction"
      category        = "Build"
      owner           = "AWS"
      provider        = "CodeBuild"
      version         = "1"
      input_artifacts = ["SourceOutput"]

      configuration = {
        ProjectName = "initiate"
      }
    }
  }
}

data "aws_codecommit_repository" "backend_nfinite" {
  repository_name = "backend_nfinite"
}

output "pipeline_arn" {
  value = "arn:aws:iam::346557108254:role/service-role/AWSCodePipelineServiceRole-ap-south-1-backend_all"
}
