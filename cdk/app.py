#!/usr/bin/env python3
import os

from aws_cdk import (
    Stack,
    App,
)

from cdk.api import Api
from cdk.layers import Layers


app = App()


class MainStack(Stack):
    def __init__(self, scope):
        super().__init__(scope, "Heimdall")

        layers = Layers(self, "Heimdall-LambdaLayers")
        api = Api(self, "Heimdall-API", layers=layers.layers)


# pipelines = Pipelines(app, "heimdall-pipelines")

MainStack(app)

app.synth()
