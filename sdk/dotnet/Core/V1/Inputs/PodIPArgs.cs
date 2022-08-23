// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Inputs.Core.V1
{

    /// <summary>
    /// IP address information for entries in the (plural) PodIPs field. Each entry includes:
    /// 
    /// 	IP: An IP address allocated to the pod. Routable at least within the cluster.
    /// </summary>
    public class PodIPArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// ip is an IP address (IPv4 or IPv6) assigned to the pod
        /// </summary>
        [Input("ip")]
        public Input<string>? Ip { get; set; }

        public PodIPArgs()
        {
        }
        public static new PodIPArgs Empty => new PodIPArgs();
    }
}
