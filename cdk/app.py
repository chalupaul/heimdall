#!/usr/bin/env python3
import os

import aws_cdk

from cdk.api import Api
from cdk.layers import Layers

from cdk.pipelines import Pipelines


app = aws_cdk.App()
layers = Layers(app, "Heimdall-LambdaLayers")
Api(app, "Heimdall-API", layers=layers.api_layers)

#pipelines = Pipelines(app, "heimdall-pipelines")

app.synth()
