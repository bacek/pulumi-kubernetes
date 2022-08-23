# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ... import core as _core
from ... import meta as _meta

__all__ = [
    'Endpoint',
    'EndpointConditions',
    'EndpointConditionsPatch',
    'EndpointHints',
    'EndpointHintsPatch',
    'EndpointPatch',
    'EndpointPort',
    'EndpointPortPatch',
    'EndpointSlice',
    'ForZone',
    'ForZonePatch',
]

@pulumi.output_type
class Endpoint(dict):
    """
    Endpoint represents a single logical "backend" implementing a service.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "deprecatedTopology":
            suggest = "deprecated_topology"
        elif key == "nodeName":
            suggest = "node_name"
        elif key == "targetRef":
            suggest = "target_ref"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in Endpoint. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        Endpoint.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        Endpoint.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 addresses: Sequence[str],
                 conditions: Optional['outputs.EndpointConditions'] = None,
                 deprecated_topology: Optional[Mapping[str, str]] = None,
                 hints: Optional['outputs.EndpointHints'] = None,
                 hostname: Optional[str] = None,
                 node_name: Optional[str] = None,
                 target_ref: Optional['_core.v1.outputs.ObjectReference'] = None,
                 zone: Optional[str] = None):
        """
        Endpoint represents a single logical "backend" implementing a service.
        :param Sequence[str] addresses: addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267
        :param 'EndpointConditionsArgs' conditions: conditions contains information about the current status of the endpoint.
        :param Mapping[str, str] deprecated_topology: deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead.
        :param 'EndpointHintsArgs' hints: hints contains information associated with how an endpoint should be consumed.
        :param str hostname: hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation.
        :param str node_name: nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node.
        :param '_core.v1.ObjectReferenceArgs' target_ref: targetRef is a reference to a Kubernetes object that represents this endpoint.
        :param str zone: zone is the name of the Zone this endpoint exists in.
        """
        pulumi.set(__self__, "addresses", addresses)
        if conditions is not None:
            pulumi.set(__self__, "conditions", conditions)
        if deprecated_topology is not None:
            pulumi.set(__self__, "deprecated_topology", deprecated_topology)
        if hints is not None:
            pulumi.set(__self__, "hints", hints)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if node_name is not None:
            pulumi.set(__self__, "node_name", node_name)
        if target_ref is not None:
            pulumi.set(__self__, "target_ref", target_ref)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def addresses(self) -> Sequence[str]:
        """
        addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267
        """
        return pulumi.get(self, "addresses")

    @property
    @pulumi.getter
    def conditions(self) -> Optional['outputs.EndpointConditions']:
        """
        conditions contains information about the current status of the endpoint.
        """
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter(name="deprecatedTopology")
    def deprecated_topology(self) -> Optional[Mapping[str, str]]:
        """
        deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead.
        """
        return pulumi.get(self, "deprecated_topology")

    @property
    @pulumi.getter
    def hints(self) -> Optional['outputs.EndpointHints']:
        """
        hints contains information associated with how an endpoint should be consumed.
        """
        return pulumi.get(self, "hints")

    @property
    @pulumi.getter
    def hostname(self) -> Optional[str]:
        """
        hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> Optional[str]:
        """
        nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node.
        """
        return pulumi.get(self, "node_name")

    @property
    @pulumi.getter(name="targetRef")
    def target_ref(self) -> Optional['_core.v1.outputs.ObjectReference']:
        """
        targetRef is a reference to a Kubernetes object that represents this endpoint.
        """
        return pulumi.get(self, "target_ref")

    @property
    @pulumi.getter
    def zone(self) -> Optional[str]:
        """
        zone is the name of the Zone this endpoint exists in.
        """
        return pulumi.get(self, "zone")


@pulumi.output_type
class EndpointConditions(dict):
    """
    EndpointConditions represents the current condition of an endpoint.
    """
    def __init__(__self__, *,
                 ready: Optional[bool] = None,
                 serving: Optional[bool] = None,
                 terminating: Optional[bool] = None):
        """
        EndpointConditions represents the current condition of an endpoint.
        :param bool ready: ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be "true" for terminating endpoints.
        :param bool serving: serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition. This field can be enabled with the EndpointSliceTerminatingCondition feature gate.
        :param bool terminating: terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating. This field can be enabled with the EndpointSliceTerminatingCondition feature gate.
        """
        if ready is not None:
            pulumi.set(__self__, "ready", ready)
        if serving is not None:
            pulumi.set(__self__, "serving", serving)
        if terminating is not None:
            pulumi.set(__self__, "terminating", terminating)

    @property
    @pulumi.getter
    def ready(self) -> Optional[bool]:
        """
        ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be "true" for terminating endpoints.
        """
        return pulumi.get(self, "ready")

    @property
    @pulumi.getter
    def serving(self) -> Optional[bool]:
        """
        serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition. This field can be enabled with the EndpointSliceTerminatingCondition feature gate.
        """
        return pulumi.get(self, "serving")

    @property
    @pulumi.getter
    def terminating(self) -> Optional[bool]:
        """
        terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating. This field can be enabled with the EndpointSliceTerminatingCondition feature gate.
        """
        return pulumi.get(self, "terminating")


@pulumi.output_type
class EndpointConditionsPatch(dict):
    """
    EndpointConditions represents the current condition of an endpoint.
    """
    def __init__(__self__, *,
                 ready: Optional[bool] = None,
                 serving: Optional[bool] = None,
                 terminating: Optional[bool] = None):
        """
        EndpointConditions represents the current condition of an endpoint.
        :param bool ready: ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be "true" for terminating endpoints.
        :param bool serving: serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition. This field can be enabled with the EndpointSliceTerminatingCondition feature gate.
        :param bool terminating: terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating. This field can be enabled with the EndpointSliceTerminatingCondition feature gate.
        """
        if ready is not None:
            pulumi.set(__self__, "ready", ready)
        if serving is not None:
            pulumi.set(__self__, "serving", serving)
        if terminating is not None:
            pulumi.set(__self__, "terminating", terminating)

    @property
    @pulumi.getter
    def ready(self) -> Optional[bool]:
        """
        ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be "true" for terminating endpoints.
        """
        return pulumi.get(self, "ready")

    @property
    @pulumi.getter
    def serving(self) -> Optional[bool]:
        """
        serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition. This field can be enabled with the EndpointSliceTerminatingCondition feature gate.
        """
        return pulumi.get(self, "serving")

    @property
    @pulumi.getter
    def terminating(self) -> Optional[bool]:
        """
        terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating. This field can be enabled with the EndpointSliceTerminatingCondition feature gate.
        """
        return pulumi.get(self, "terminating")


@pulumi.output_type
class EndpointHints(dict):
    """
    EndpointHints provides hints describing how an endpoint should be consumed.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "forZones":
            suggest = "for_zones"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EndpointHints. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EndpointHints.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EndpointHints.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 for_zones: Optional[Sequence['outputs.ForZone']] = None):
        """
        EndpointHints provides hints describing how an endpoint should be consumed.
        :param Sequence['ForZoneArgs'] for_zones: forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing.
        """
        if for_zones is not None:
            pulumi.set(__self__, "for_zones", for_zones)

    @property
    @pulumi.getter(name="forZones")
    def for_zones(self) -> Optional[Sequence['outputs.ForZone']]:
        """
        forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing.
        """
        return pulumi.get(self, "for_zones")


@pulumi.output_type
class EndpointHintsPatch(dict):
    """
    EndpointHints provides hints describing how an endpoint should be consumed.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "forZones":
            suggest = "for_zones"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EndpointHintsPatch. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EndpointHintsPatch.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EndpointHintsPatch.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 for_zones: Optional[Sequence['outputs.ForZonePatch']] = None):
        """
        EndpointHints provides hints describing how an endpoint should be consumed.
        :param Sequence['ForZonePatchArgs'] for_zones: forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing.
        """
        if for_zones is not None:
            pulumi.set(__self__, "for_zones", for_zones)

    @property
    @pulumi.getter(name="forZones")
    def for_zones(self) -> Optional[Sequence['outputs.ForZonePatch']]:
        """
        forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing.
        """
        return pulumi.get(self, "for_zones")


@pulumi.output_type
class EndpointPatch(dict):
    """
    Endpoint represents a single logical "backend" implementing a service.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "deprecatedTopology":
            suggest = "deprecated_topology"
        elif key == "nodeName":
            suggest = "node_name"
        elif key == "targetRef":
            suggest = "target_ref"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EndpointPatch. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EndpointPatch.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EndpointPatch.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 addresses: Optional[Sequence[str]] = None,
                 conditions: Optional['outputs.EndpointConditionsPatch'] = None,
                 deprecated_topology: Optional[Mapping[str, str]] = None,
                 hints: Optional['outputs.EndpointHintsPatch'] = None,
                 hostname: Optional[str] = None,
                 node_name: Optional[str] = None,
                 target_ref: Optional['_core.v1.outputs.ObjectReferencePatch'] = None,
                 zone: Optional[str] = None):
        """
        Endpoint represents a single logical "backend" implementing a service.
        :param Sequence[str] addresses: addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267
        :param 'EndpointConditionsPatchArgs' conditions: conditions contains information about the current status of the endpoint.
        :param Mapping[str, str] deprecated_topology: deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead.
        :param 'EndpointHintsPatchArgs' hints: hints contains information associated with how an endpoint should be consumed.
        :param str hostname: hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation.
        :param str node_name: nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node.
        :param '_core.v1.ObjectReferencePatchArgs' target_ref: targetRef is a reference to a Kubernetes object that represents this endpoint.
        :param str zone: zone is the name of the Zone this endpoint exists in.
        """
        if addresses is not None:
            pulumi.set(__self__, "addresses", addresses)
        if conditions is not None:
            pulumi.set(__self__, "conditions", conditions)
        if deprecated_topology is not None:
            pulumi.set(__self__, "deprecated_topology", deprecated_topology)
        if hints is not None:
            pulumi.set(__self__, "hints", hints)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if node_name is not None:
            pulumi.set(__self__, "node_name", node_name)
        if target_ref is not None:
            pulumi.set(__self__, "target_ref", target_ref)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def addresses(self) -> Optional[Sequence[str]]:
        """
        addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267
        """
        return pulumi.get(self, "addresses")

    @property
    @pulumi.getter
    def conditions(self) -> Optional['outputs.EndpointConditionsPatch']:
        """
        conditions contains information about the current status of the endpoint.
        """
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter(name="deprecatedTopology")
    def deprecated_topology(self) -> Optional[Mapping[str, str]]:
        """
        deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead.
        """
        return pulumi.get(self, "deprecated_topology")

    @property
    @pulumi.getter
    def hints(self) -> Optional['outputs.EndpointHintsPatch']:
        """
        hints contains information associated with how an endpoint should be consumed.
        """
        return pulumi.get(self, "hints")

    @property
    @pulumi.getter
    def hostname(self) -> Optional[str]:
        """
        hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> Optional[str]:
        """
        nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node.
        """
        return pulumi.get(self, "node_name")

    @property
    @pulumi.getter(name="targetRef")
    def target_ref(self) -> Optional['_core.v1.outputs.ObjectReferencePatch']:
        """
        targetRef is a reference to a Kubernetes object that represents this endpoint.
        """
        return pulumi.get(self, "target_ref")

    @property
    @pulumi.getter
    def zone(self) -> Optional[str]:
        """
        zone is the name of the Zone this endpoint exists in.
        """
        return pulumi.get(self, "zone")


@pulumi.output_type
class EndpointPort(dict):
    """
    EndpointPort represents a Port used by an EndpointSlice
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "appProtocol":
            suggest = "app_protocol"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EndpointPort. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EndpointPort.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EndpointPort.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 app_protocol: Optional[str] = None,
                 name: Optional[str] = None,
                 port: Optional[int] = None,
                 protocol: Optional[str] = None):
        """
        EndpointPort represents a Port used by an EndpointSlice
        :param str app_protocol: The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol.
        :param str name: The name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is dervied from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or '-'. * must start and end with an alphanumeric character. Default is empty string.
        :param int port: The port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer.
        :param str protocol: The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.
        """
        if app_protocol is not None:
            pulumi.set(__self__, "app_protocol", app_protocol)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter(name="appProtocol")
    def app_protocol(self) -> Optional[str]:
        """
        The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol.
        """
        return pulumi.get(self, "app_protocol")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is dervied from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or '-'. * must start and end with an alphanumeric character. Default is empty string.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        The port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def protocol(self) -> Optional[str]:
        """
        The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.
        """
        return pulumi.get(self, "protocol")


@pulumi.output_type
class EndpointPortPatch(dict):
    """
    EndpointPort represents a Port used by an EndpointSlice
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "appProtocol":
            suggest = "app_protocol"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EndpointPortPatch. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EndpointPortPatch.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EndpointPortPatch.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 app_protocol: Optional[str] = None,
                 name: Optional[str] = None,
                 port: Optional[int] = None,
                 protocol: Optional[str] = None):
        """
        EndpointPort represents a Port used by an EndpointSlice
        :param str app_protocol: The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol.
        :param str name: The name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is dervied from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or '-'. * must start and end with an alphanumeric character. Default is empty string.
        :param int port: The port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer.
        :param str protocol: The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.
        """
        if app_protocol is not None:
            pulumi.set(__self__, "app_protocol", app_protocol)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter(name="appProtocol")
    def app_protocol(self) -> Optional[str]:
        """
        The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol.
        """
        return pulumi.get(self, "app_protocol")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is dervied from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or '-'. * must start and end with an alphanumeric character. Default is empty string.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        The port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def protocol(self) -> Optional[str]:
        """
        The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.
        """
        return pulumi.get(self, "protocol")


@pulumi.output_type
class EndpointSlice(dict):
    """
    EndpointSlice represents a subset of the endpoints that implement a service. For a given service there may be multiple EndpointSlice objects, selected by labels, which must be joined to produce the full set of endpoints.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "addressType":
            suggest = "address_type"
        elif key == "apiVersion":
            suggest = "api_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EndpointSlice. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EndpointSlice.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EndpointSlice.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 address_type: str,
                 endpoints: Sequence['outputs.Endpoint'],
                 api_version: Optional[str] = None,
                 kind: Optional[str] = None,
                 metadata: Optional['_meta.v1.outputs.ObjectMeta'] = None,
                 ports: Optional[Sequence['outputs.EndpointPort']] = None):
        """
        EndpointSlice represents a subset of the endpoints that implement a service. For a given service there may be multiple EndpointSlice objects, selected by labels, which must be joined to produce the full set of endpoints.
        :param str address_type: addressType specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. This field is immutable after creation. The following address types are currently supported: * IPv4: Represents an IPv4 Address. * IPv6: Represents an IPv6 Address. * FQDN: Represents a Fully Qualified Domain Name.
        :param Sequence['EndpointArgs'] endpoints: endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000 endpoints.
        :param str api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param str kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param '_meta.v1.ObjectMetaArgs' metadata: Standard object's metadata.
        :param Sequence['EndpointPortArgs'] ports: ports specifies the list of network ports exposed by each endpoint in this slice. Each port must have a unique name. When ports is empty, it indicates that there are no defined ports. When a port is defined with a nil port value, it indicates "all ports". Each slice may include a maximum of 100 ports.
        """
        pulumi.set(__self__, "address_type", address_type)
        pulumi.set(__self__, "endpoints", endpoints)
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'discovery.k8s.io/v1')
        if kind is not None:
            pulumi.set(__self__, "kind", 'EndpointSlice')
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if ports is not None:
            pulumi.set(__self__, "ports", ports)

    @property
    @pulumi.getter(name="addressType")
    def address_type(self) -> str:
        """
        addressType specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. This field is immutable after creation. The following address types are currently supported: * IPv4: Represents an IPv4 Address. * IPv6: Represents an IPv6 Address. * FQDN: Represents a Fully Qualified Domain Name.
        """
        return pulumi.get(self, "address_type")

    @property
    @pulumi.getter
    def endpoints(self) -> Sequence['outputs.Endpoint']:
        """
        endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000 endpoints.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[str]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def metadata(self) -> Optional['_meta.v1.outputs.ObjectMeta']:
        """
        Standard object's metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def ports(self) -> Optional[Sequence['outputs.EndpointPort']]:
        """
        ports specifies the list of network ports exposed by each endpoint in this slice. Each port must have a unique name. When ports is empty, it indicates that there are no defined ports. When a port is defined with a nil port value, it indicates "all ports". Each slice may include a maximum of 100 ports.
        """
        return pulumi.get(self, "ports")


@pulumi.output_type
class ForZone(dict):
    """
    ForZone provides information about which zones should consume this endpoint.
    """
    def __init__(__self__, *,
                 name: str):
        """
        ForZone provides information about which zones should consume this endpoint.
        :param str name: name represents the name of the zone.
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        name represents the name of the zone.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class ForZonePatch(dict):
    """
    ForZone provides information about which zones should consume this endpoint.
    """
    def __init__(__self__, *,
                 name: Optional[str] = None):
        """
        ForZone provides information about which zones should consume this endpoint.
        :param str name: name represents the name of the zone.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        name represents the name of the zone.
        """
        return pulumi.get(self, "name")


