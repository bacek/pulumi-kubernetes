// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Inputs.Discovery.V1Beta1
{

    /// <summary>
    /// Endpoint represents a single logical "backend" implementing a service.
    /// </summary>
    public class EndpointArgs : Pulumi.ResourceArgs
    {
        [Input("addresses", required: true)]
        private InputList<string>? _addresses;

        /// <summary>
        /// addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100.
        /// </summary>
        public InputList<string> Addresses
        {
            get => _addresses ?? (_addresses = new InputList<string>());
            set => _addresses = value;
        }

        /// <summary>
        /// conditions contains information about the current status of the endpoint.
        /// </summary>
        [Input("conditions")]
        public Input<Pulumi.Kubernetes.Types.Inputs.Discovery.V1Beta1.EndpointConditionsArgs>? Conditions { get; set; }

        /// <summary>
        /// hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must pass DNS Label (RFC 1123) validation.
        /// </summary>
        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        /// <summary>
        /// targetRef is a reference to a Kubernetes object that represents this endpoint.
        /// </summary>
        [Input("targetRef")]
        public Input<Pulumi.Kubernetes.Types.Inputs.Core.V1.ObjectReferenceArgs>? TargetRef { get; set; }

        [Input("topology")]
        private InputMap<string>? _topology;

        /// <summary>
        /// topology contains arbitrary topology information associated with the endpoint. These key/value pairs must conform with the label format. https://kubernetes.io/docs/concepts/overview/working-with-objects/labels Topology may include a maximum of 16 key/value pairs. This includes, but is not limited to the following well known keys: * kubernetes.io/hostname: the value indicates the hostname of the node
        ///   where the endpoint is located. This should match the corresponding
        ///   node label.
        /// * topology.kubernetes.io/zone: the value indicates the zone where the
        ///   endpoint is located. This should match the corresponding node label.
        /// * topology.kubernetes.io/region: the value indicates the region where the
        ///   endpoint is located. This should match the corresponding node label.
        /// </summary>
        public InputMap<string> Topology
        {
            get => _topology ?? (_topology = new InputMap<string>());
            set => _topology = value;
        }

        public EndpointArgs()
        {
        }
    }
}