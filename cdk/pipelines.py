from constructs import Construct
from aws_cdk import (
    Stack,
    aws_codecommit as codecommit,
    pipelines
)

class Pipelines(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope,id,**kwargs)

        connection_arn = ("arn:aws:codestar-connections:"
            "us-west-2:"
            "905590892698:"
            "connection/ae670e38-6cab-4613-8444-0a860aa06dcb"
        )

        repo = pipelines.CodePipelineSource.connection("chalupaul/heimdall", 
            "main",
            connection_arn=connection_arn
        )

        synth_step = pipelines.ShellStep(
            "Synth",
            input=repo,
            commands = [
                "pip install -r cdk/requirements.txt",
                "npm install -g aws-cdk",
                "cdk synth"
                #"ls -la",
                #"pip install poetry",
                #"poetry install",
                #"npm install -g aws-cdk",
                #"pwd",
                #"ls",
                #"poetry env list --full-path",
                #"poetry run task cdksynth"
            ]
        )

        self.pipeline = pipelines.CodePipeline(
            self,
            "Deploy Main",
            self_mutation=True,
            synth=synth_step
        )