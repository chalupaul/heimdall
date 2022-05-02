#!/usr/bin/env python3
import os

import aws_cdk

from heimdall_cdk.api import Api
from heimdall_cdk.layers import Layers

from heimdall_cdk.pipelines import Pipelines


app = aws_cdk.App()
#layers = Layers(app, "LambdaLayers")
#Api(app, "API", layers=layers.api_layers)

pipelines = Pipelines(app, "heimdall-pipelines")

app.synth()
