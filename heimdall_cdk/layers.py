from aws_cdk import (
    aws_lambda as lambda_,
    RemovalPolicy,
    Stack
)
from typing import Sequence

from constructs import Construct

from heimdall_cdk.lib import paths

class Layers(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        api_layer = lambda_.LayerVersion(self, "API Layer",
            removal_policy=RemovalPolicy.DESTROY,
            code=lambda_.Code.from_asset(paths.venv_root),
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_9],
        )
        self.api_layers: Sequence[lambda_.ILayerVersion] = [api_layer]