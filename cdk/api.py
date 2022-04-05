import os
from typing_extensions import runtime
from aws_cdk import (
    # Duration,
    RemovalPolicy,
    Stack,
    aws_lambda as lambda_,
    aws_signer as signer,
    aws_s3 as s3,
    # aws_sqs as sqs,
)
from constructs import Construct

from pathlib import Path

class HeimdallApi(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdktustQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        base_root = Path(__file__).parent.resolve()
        venv_root = os.path.join(base_root, '.venv')
        api_root = os.path.join(base_root, "heimdall", "api")
        
        signer_profile = signer.SigningProfile(self, "Signer Profile",
            platform=signer.Platform.AWS_LAMBDA_SHA384_ECDSA
        )

        code_signing_config = lambda_.CodeSigningConfig(self, "Code Signing Config",
            signing_profiles=[signer_profile]
)
        api_layer = lambda_.LayerVersion(self, "API Layer",
            removal_policy=RemovalPolicy.DESTROY,
            code=lambda_.Code.from_asset(venv_root),
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_9],
        )
        api_root = lambda_.Function(self, "api root",
            code=lambda_.Code.from_asset(api_root),
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="app.handler",
            layers=[api_layer],
            code_signing_config=code_signing_config
        )
        
