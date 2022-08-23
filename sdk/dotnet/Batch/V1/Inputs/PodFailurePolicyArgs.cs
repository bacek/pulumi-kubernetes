// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Inputs.Batch.V1
{

    /// <summary>
    /// PodFailurePolicy describes how failed pods influence the backoffLimit.
    /// </summary>
    public class PodFailurePolicyArgs : global::Pulumi.ResourceArgs
    {
        [Input("rules", required: true)]
        private InputList<Pulumi.Kubernetes.Types.Inputs.Batch.V1.PodFailurePolicyRuleArgs>? _rules;

        /// <summary>
        /// A list of pod failure policy rules. The rules are evaluated in order. Once a rule matches a Pod failure, the remaining of the rules are ignored. When no rule matches the Pod failure, the default handling applies - the counter of pod failures is incremented and it is checked against the backoffLimit. At most 20 elements are allowed.
        /// </summary>
        public InputList<Pulumi.Kubernetes.Types.Inputs.Batch.V1.PodFailurePolicyRuleArgs> Rules
        {
            get => _rules ?? (_rules = new InputList<Pulumi.Kubernetes.Types.Inputs.Batch.V1.PodFailurePolicyRuleArgs>());
            set => _rules = value;
        }

        public PodFailurePolicyArgs()
        {
        }
        public static new PodFailurePolicyArgs Empty => new PodFailurePolicyArgs();
    }
}
