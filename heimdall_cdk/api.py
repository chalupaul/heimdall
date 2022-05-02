import os
from typing import Sequence
from typing_extensions import runtime
from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as lambda_,
    aws_signer as signer,
    # aws_sqs as sqs,
)
from constructs import Construct

from heimdall_cdk.lib import paths

class Api(Stack):

    def __init__(self, scope: Construct, construct_id: str, layers: Sequence[lambda_.ILayerVersion] = [], **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdktustQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        
        signer_profile = signer.SigningProfile(self, "Signer Profile",
            platform=signer.Platform.AWS_LAMBDA_SHA384_ECDSA
        )

        code_signing_config = lambda_.CodeSigningConfig(self, "Code Signing Config",
            signing_profiles=[signer_profile]
        )

        api_root = lambda_.Function(self, "api root",
            code=lambda_.Code.from_asset(paths.api_root),
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="app.handler",
            layers=layers,
            code_signing_config=code_signing_config
        )
        
