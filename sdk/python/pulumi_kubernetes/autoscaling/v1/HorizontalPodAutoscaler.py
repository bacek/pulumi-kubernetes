# *** WARNING: this file was generated by the Pulumi Kubernetes codegen tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
from typing import Optional

import pulumi
import pulumi.runtime
from pulumi import Input, ResourceOptions

from ... import tables, version


class HorizontalPodAutoscaler(pulumi.CustomResource):
    """
    configuration of a horizontal pod autoscaler.
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

    metadata: pulumi.Output[dict]
    """
    Standard object metadata. More info:
    https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata
    """

    spec: pulumi.Output[dict]
    """
    behaviour of autoscaler. More info:
    https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status.
    """

    status: pulumi.Output[dict]
    """
    current information about the autoscaler.
    """

    def __init__(self, resource_name, opts=None, metadata=None, spec=None, __name__=None, __opts__=None):
        """
        Create a HorizontalPodAutoscaler resource with the given unique name, arguments, and options.

        :param str resource_name: The _unique_ name of the resource.
        :param pulumi.ResourceOptions opts: A bag of options that control this resource's behavior.
        :param pulumi.Input[dict] metadata: Standard object metadata. More info:
               https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata
        :param pulumi.Input[dict] spec: behaviour of autoscaler. More info:
               https://git.k8s.io/community/contributors/devel/api-conventions.md#spec-and-status.
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

        __props__['apiVersion'] = 'autoscaling/v1'
        __props__['kind'] = 'HorizontalPodAutoscaler'
        __props__['metadata'] = metadata
        __props__['spec'] = spec

        __props__['status'] = None

        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(version=version.get_version()))

        super(HorizontalPodAutoscaler, self).__init__(
            "kubernetes:autoscaling/v1:HorizontalPodAutoscaler",
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None):
        """
        Get the state of an existing `HorizontalPodAutoscaler` resource, as identified by `id`.
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
        return HorizontalPodAutoscaler(resource_name, opts)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
