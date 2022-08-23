// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Outputs.Batch.V1
{

    /// <summary>
    /// PodFailurePolicyRule describes how a pod failure is handled when the requirements are met. One of OnExitCodes and onPodConditions, but not both, can be used in each rule.
    /// </summary>
    [OutputType]
    public sealed class PodFailurePolicyRulePatch
    {
        /// <summary>
        /// Specifies the action taken on a pod failure when the requirements are satisfied. Possible values are: - FailJob: indicates that the pod's job is marked as Failed and all
        ///   running pods are terminated.
        /// - Ignore: indicates that the counter towards the .backoffLimit is not
        ///   incremented and a replacement pod is created.
        /// - Count: indicates that the pod is handled in the default way - the
        ///   counter towards the .backoffLimit is incremented.
        /// Additional values are considered to be added in the future. Clients should react to an unknown action by skipping the rule.
        /// </summary>
        public readonly string Action;
        /// <summary>
        /// Represents the requirement on the container exit codes.
        /// </summary>
        public readonly Pulumi.Kubernetes.Types.Outputs.Batch.V1.PodFailurePolicyOnExitCodesRequirementPatch OnExitCodes;
        /// <summary>
        /// Represents the requirement on the pod conditions. The requirement is represented as a list of pod condition patterns. The requirement is satisfied if at least one pattern matches an actual pod condition. At most 20 elements are allowed.
        /// </summary>
        public readonly ImmutableArray<Pulumi.Kubernetes.Types.Outputs.Batch.V1.PodFailurePolicyOnPodConditionsPatternPatch> OnPodConditions;

        [OutputConstructor]
        private PodFailurePolicyRulePatch(
            string action,

            Pulumi.Kubernetes.Types.Outputs.Batch.V1.PodFailurePolicyOnExitCodesRequirementPatch onExitCodes,

            ImmutableArray<Pulumi.Kubernetes.Types.Outputs.Batch.V1.PodFailurePolicyOnPodConditionsPatternPatch> onPodConditions)
        {
            Action = action;
            OnExitCodes = onExitCodes;
            OnPodConditions = onPodConditions;
        }
    }
}
