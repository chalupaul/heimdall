from constructs import Construct
from aws_cdk import (
    Stack,
    aws_kms,
    aws_s3,
    pipelines,
    RemovalPolicy,
    Duration,
    aws_codebuild
)

class Pipelines(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope,id,**kwargs)
        key_arn = ("arn:aws:kms:"
            "us-west-2:905590892698:key/"
            "53db5ecd-5b1f-4b44-ad6e-b6016288f699")
        s3_key = aws_kms.Key.from_key_arn(self, 'S3Key', key_arn)

        lifecycle_rule = aws_s3.LifecycleRule(
            abort_incomplete_multipart_upload_after=Duration.days(1),
            expiration=Duration.days(30)
        )
        cache_bucket = aws_s3.Bucket(self, "buildcache",
            auto_delete_objects=True,
            removal_policy=RemovalPolicy.DESTROY,
            bucket_key_enabled=True,
            encryption_key=s3_key,
            enforce_ssl=True,
            lifecycle_rules=[lifecycle_rule]
            )

        connection_arn = ("arn:aws:codestar-connections:"
            "us-west-2:"
            "905590892698:"
            "connection/ae670e38-6cab-4613-8444-0a860aa06dcb"
        )

        repo = pipelines.CodePipelineSource.connection("chalupaul/heimdall", 
            "main",
            connection_arn=connection_arn
        )

        codebuild_defaults = pipelines.CodeBuildOptions(
            partial_build_spec=aws_codebuild.BuildSpec.from_object({
                "version": "0.2",
                "cache": {
                    "paths": [
                        ".venv",
                        "/root/.pyenv",
                        "/root/.cache"
                    ]
                }
            })
        )
        synth_step = pipelines.ShellStep(
            "Synth",
            input=repo,
            commands = [
                "ls -la",
                "ls -la $HOME",
                "pip install poetry",
                "poetry install",
                "npm install -g aws-cdk",
                "pwd",
                "ls -la",
                "poetry env list --full-path",
                "poetry run task cdksynth",
                "echo MY HOME IS $HOME",
                "ls -la $HOME"
            ]
        )

        self.pipeline = pipelines.CodePipeline(
            self,
            "Deploy Main",
            self_mutation=True,
            synth=synth_step,
            code_build_defaults=codebuild_defaults
        )