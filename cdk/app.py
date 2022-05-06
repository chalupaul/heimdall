#!/usr/bin/env python3
import os

from aws_cdk import (
    Stack,
    App,
)

from cdk.api import Api
from cdk.layers import Layers




class MainStack(Stack):
    def __init__(self, scope):
        super().__init__(scope, "Heimdall")

        layers = Layers(scope, "Heimdall-LambdaLayers")
        api = Api(scope, "Heimdall-API", layers=layers.layers)

#pipelines = Pipelines(app, "heimdall-pipelines")

app = MainStack(App())
app.synth()
