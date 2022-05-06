import os
from aws_cdk import (
    NestedStack,
    aws_lambda,
    RemovalPolicy
)
from typing import Sequence

from constructs import Construct

from cdk.common import paths

class Layers(NestedStack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        api_layer = aws_lambda.LayerVersion(self, "Heimdall-API-Layer",
            removal_policy=RemovalPolicy.RETAIN,
            code=aws_lambda.Code.from_asset(paths.layer_dir),
            compatible_runtimes=[aws_lambda.Runtime.PYTHON_3_9],
        )

        self.layers: Sequence[aws_lambda.ILayerVersion] = [api_layer]