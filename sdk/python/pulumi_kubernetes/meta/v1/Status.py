# *** WARNING: this file was generated by the Pulumi Kubernetes codegen tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
from typing import Optional

import pulumi
import pulumi.runtime
from pulumi import Input, ResourceOptions

from ... import tables, version


class Status(pulumi.CustomResource):
    """
    Status is a return value for calls that don't return other objects.
    """

    apiVersion: pulumi.Output[str]
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should
    convert recognized schemas to the latest internal value, and may reject unrecognized values.
    More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources
    """

    kind: pulumi.Output[str]
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer
    this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More
    info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds
    """

    code: pulumi.Output[int]
    """
    Suggested HTTP return code for this status, 0 if not set.
    """

    details: pulumi.Output[dict]
    """
    Extended data associated with the reason.  Each reason may define its own extended details. This
    field is optional and the data returned is not guaranteed to conform to any schema except that
    defined by the reason type.
    """

    message: pulumi.Output[str]
    """
    A human-readable description of the status of this operation.
    """

    metadata: pulumi.Output[dict]
    """
    Standard list metadata. More info:
    https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds
    """

    reason: pulumi.Output[str]
    """
    A machine-readable description of why this operation is in the "Failure" status. If this value
    is empty there is no information available. A Reason clarifies an HTTP status code but does not
    override it.
    """

    status: pulumi.Output[str]
    """
    Status of the operation. One of: "Success" or "Failure". More info:
    https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status
    """

    def __init__(self, resource_name, opts=None, code=None, details=None, message=None, metadata=None, reason=None, __name__=None, __opts__=None):
        """
        Create a Status resource with the given unique name, arguments, and options.

        :param str resource_name: The _unique_ name of the resource.
        :param pulumi.ResourceOptions opts: A bag of options that control this resource's behavior.
        :param pulumi.Input[int] code: Suggested HTTP return code for this status, 0 if not set.
        :param pulumi.Input[dict] details: Extended data associated with the reason.  Each reason may define its own extended
               details. This field is optional and the data returned is not guaranteed to conform to
               any schema except that defined by the reason type.
        :param pulumi.Input[str] message: A human-readable description of the status of this operation.
        :param pulumi.Input[dict] metadata: Standard list metadata. More info:
               https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds
        :param pulumi.Input[str] reason: A machine-readable description of why this operation is in the "Failure" status. If
               this value is empty there is no information available. A Reason clarifies an HTTP
               status code but does not override it.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'v1'
        __props__['kind'] = 'Status'
        __props__['code'] = code
        __props__['details'] = details
        __props__['message'] = message
        __props__['metadata'] = metadata
        __props__['reason'] = reason

        __props__['status'] = None

        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(version=version.get_version()))

        super(Status, self).__init__(
            "kubernetes:core/v1:Status",
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None):
        """
        Get the state of an existing `Status` resource, as identified by `id`.
        Typically this ID  is of the form [namespace]/[name]; if [namespace] is omitted,
        then (per Kubernetes convention) the ID becomes default/[name].

        Pulumi will keep track of this resource using `resource_name` as the Pulumi ID.

        :param str resource_name: _Unique_ name used to register this resource with Pulumi.
        :param pulumi.Input[str] id: An ID for the Kubernetes resource to retrieve.
               Takes the form [namespace]/[name] or [name].
        :param Optional[pulumi.ResourceOptions] opts: A bag of options that control this
               resource's behavior.
        """
        opts = ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))
        return Status(resource_name, opts)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
