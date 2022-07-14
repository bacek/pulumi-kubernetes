// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Outputs.FlowControl.V1Alpha1
{

    /// <summary>
    /// LimitResponse defines how to handle requests that can not be executed right now.
    /// </summary>
    [OutputType]
    public sealed class LimitResponsePatch
    {
        /// <summary>
        /// `queuing` holds the configuration parameters for queuing. This field may be non-empty only if `type` is `"Queue"`.
        /// </summary>
        public readonly Pulumi.Kubernetes.Types.Outputs.FlowControl.V1Alpha1.QueuingConfigurationPatch Queuing;
        /// <summary>
        /// `type` is "Queue" or "Reject". "Queue" means that requests that can not be executed upon arrival are held in a queue until they can be executed or a queuing limit is reached. "Reject" means that requests that can not be executed upon arrival are rejected. Required.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private LimitResponsePatch(
            Pulumi.Kubernetes.Types.Outputs.FlowControl.V1Alpha1.QueuingConfigurationPatch queuing,

            string type)
        {
            Queuing = queuing;
            Type = type;
        }
    }
}