import os
from aws_cdk import (
    aws_lambda as lambda_,
    RemovalPolicy,
    Stack
)
from typing import Sequence

from constructs import Construct

from cdk.common import paths

class Layers(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        site_dir = os.path.join(paths.venv_root, "Lib", "site-packages")
        api_layer = lambda_.LayerVersion(self, "Heimdall-API-Layer",
            removal_policy=RemovalPolicy.DESTROY,
            code=lambda_.Code.from_asset(site_dir),
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_9],
        )
        self.api_layers: Sequence[lambda_.ILayerVersion] = [api_layer]