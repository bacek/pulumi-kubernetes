// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Outputs.Discovery.V1
{

    /// <summary>
    /// Endpoint represents a single logical "backend" implementing a service.
    /// </summary>
    [OutputType]
    public sealed class EndpointPatch
    {
        /// <summary>
        /// addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267
        /// </summary>
        public readonly ImmutableArray<string> Addresses;
        /// <summary>
        /// conditions contains information about the current status of the endpoint.
        /// </summary>
        public readonly Pulumi.Kubernetes.Types.Outputs.Discovery.V1.EndpointConditionsPatch Conditions;
        /// <summary>
        /// deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead.
        /// </summary>
        public readonly ImmutableDictionary<string, string> DeprecatedTopology;
        /// <summary>
        /// hints contains information associated with how an endpoint should be consumed.
        /// </summary>
        public readonly Pulumi.Kubernetes.Types.Outputs.Discovery.V1.EndpointHintsPatch Hints;
        /// <summary>
        /// hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation.
        /// </summary>
        public readonly string Hostname;
        /// <summary>
        /// nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node.
        /// </summary>
        public readonly string NodeName;
        /// <summary>
        /// targetRef is a reference to a Kubernetes object that represents this endpoint.
        /// </summary>
        public readonly Pulumi.Kubernetes.Types.Outputs.Core.V1.ObjectReferencePatch TargetRef;
        /// <summary>
        /// zone is the name of the Zone this endpoint exists in.
        /// </summary>
        public readonly string Zone;

        [OutputConstructor]
        private EndpointPatch(
            ImmutableArray<string> addresses,

            Pulumi.Kubernetes.Types.Outputs.Discovery.V1.EndpointConditionsPatch conditions,

            ImmutableDictionary<string, string> deprecatedTopology,

            Pulumi.Kubernetes.Types.Outputs.Discovery.V1.EndpointHintsPatch hints,

            string hostname,

            string nodeName,

            Pulumi.Kubernetes.Types.Outputs.Core.V1.ObjectReferencePatch targetRef,

            string zone)
        {
            Addresses = addresses;
            Conditions = conditions;
            DeprecatedTopology = deprecatedTopology;
            Hints = hints;
            Hostname = hostname;
            NodeName = nodeName;
            TargetRef = targetRef;
            Zone = zone;
        }
    }
}
