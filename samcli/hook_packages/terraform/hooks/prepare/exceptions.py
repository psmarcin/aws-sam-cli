"""
Module containing prepare hook-related exceptions
"""
import os

from samcli.commands.exceptions import UserException

ONE_LAMBDA_LAYER_LINKING_ISSUE_LINK = "https://github.com/aws/aws-sam-cli/issues/4395"
LOCAL_VARIABLES_SUPPORT_ISSUE_LINK = "https://github.com/aws/aws-sam-cli/issues/4396"


class InvalidResourceLinkingException(UserException):
    fmt = "An error occurred when attempting to link two resources: {message}"

    def __init__(self, message):
        msg = self.fmt.format(message=message)
        UserException.__init__(self, msg)


class OneResourceLinkingLimitationException(UserException):
    fmt = (
        "AWS SAM CLI could not process a Terraform project that contains a source resource that is linked to more "
        "than one destination resource. Destination resource(s) defined by {dest_resource_list} could not be linked to "
        "source resource {source_resource_id}.{line_sep}Related issue: {issue_link}."
    )

    def __init__(self, dest_resource_list, source_resource_id):
        msg = self.fmt.format(
            dest_resource_list=dest_resource_list,
            source_resource_id=source_resource_id,
            issue_link=ONE_LAMBDA_LAYER_LINKING_ISSUE_LINK,
            line_sep=os.linesep,
        )
        UserException.__init__(self, msg)


class OneLambdaLayerLinkingLimitationException(OneResourceLinkingLimitationException):
    """
    Exception specific for Lambda function linking to more than one layer
    """


class LocalVariablesLinkingLimitationException(UserException):
    fmt = (
        "AWS SAM CLI could not process a Terraform project that uses local variables to define linked resources. "
        "Destination resource(s) defined by {local_variable_reference} could not be linked to destination "
        "resource {dest_resource_list}.{line_sep}Related issue: {issue_link}."
    )

    def __init__(self, local_variable_reference, dest_resource_list):
        msg = self.fmt.format(
            local_variable_reference=local_variable_reference,
            dest_resource_list=dest_resource_list,
            issue_link=LOCAL_VARIABLES_SUPPORT_ISSUE_LINK,
            line_sep=os.linesep,
        )
        UserException.__init__(self, msg)


class FunctionLayerLocalVariablesLinkingLimitationException(LocalVariablesLinkingLimitationException):
    """
    Exception specific for Lambda function linking to a layer defined as a local
    """


class InvalidSamMetadataPropertiesException(UserException):
    pass


class OpenAPIBodyNotSupportedException(UserException):
    fmt = (
        "AWS SAM CLI is unable to process a Terraform project that uses an OpenAPI specification to "
        "define the API Gateway resource. AWS SAM CLI does not currently support this "
        "functionality. Affected resource: {api_id}."
    )

    def __init__(self, api_id):
        msg = self.fmt.format(
            api_id=api_id,
        )
        UserException.__init__(self, msg)
