import os
from typing import Sequence
from typing_extensions import runtime
from aws_cdk import (
    # Duration,
    NestedStack,
    aws_lambda,
    aws_signer,
    aws_logs,
    aws_kms
    # aws_sqs as sqs,
)
from constructs import Construct

from cdk.common import paths


class Api(NestedStack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        layers: Sequence[aws_lambda.ILayerVersion] = [],
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        signer_profile = aws_signer.SigningProfile(
            self, "HeimdallSP", platform=aws_signer.Platform.AWS_LAMBDA_SHA384_ECDSA
        )

        code_signing_config = aws_lambda.CodeSigningConfig(
            self, "HeimdallCSC", signing_profiles=[signer_profile]
        )

        #encryption_config = aws_lambda.e
        env_vars = {
           "LOG_LEVEL": "INFO",
           "POWERTOOLS_SERVICE_NAME": "heimdall-api",
           "POWERTOOLS_LOGGER_SAMPLE_RATE": 0.1,
           "POWERTOOLS_LOGGER_LOG_EVENT": True,
           "POWERTOOLS_METRICS_NAMESPACE": "heimdall-api",
        }

        api_root = aws_lambda.Function(
            self,
            "api root",
            code=aws_lambda.Code.from_asset(paths.api_root),
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            handler="app.handler",
            layers=layers,
            code_signing_config=code_signing_config,
            log_retention=aws_logs.RetentionDays.ONE_MONTH,
            tracing=aws_lambda.Tracing.ACTIVE,
            environment=env_vars
        )
