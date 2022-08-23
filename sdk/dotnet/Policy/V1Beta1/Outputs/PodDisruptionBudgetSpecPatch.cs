// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Outputs.Policy.V1Beta1
{

    /// <summary>
    /// PodDisruptionBudgetSpec is a description of a PodDisruptionBudget.
    /// </summary>
    [OutputType]
    public sealed class PodDisruptionBudgetSpecPatch
    {
        /// <summary>
        /// An eviction is allowed if at most "maxUnavailable" pods selected by "selector" are unavailable after the eviction, i.e. even in absence of the evicted pod. For example, one can prevent all voluntary evictions by specifying 0. This is a mutually exclusive setting with "minAvailable".
        /// </summary>
        public readonly Union<int, string> MaxUnavailable;
        /// <summary>
        /// An eviction is allowed if at least "minAvailable" pods selected by "selector" will still be available after the eviction, i.e. even in the absence of the evicted pod.  So for example you can prevent all voluntary evictions by specifying "100%".
        /// </summary>
        public readonly Union<int, string> MinAvailable;
        /// <summary>
        /// Label query over pods whose evictions are managed by the disruption budget.
        /// </summary>
        public readonly Pulumi.Kubernetes.Types.Outputs.Meta.V1.LabelSelectorPatch Selector;

        [OutputConstructor]
        private PodDisruptionBudgetSpecPatch(
            Union<int, string> maxUnavailable,

            Union<int, string> minAvailable,

            Pulumi.Kubernetes.Types.Outputs.Meta.V1.LabelSelectorPatch selector)
        {
            MaxUnavailable = maxUnavailable;
            MinAvailable = minAvailable;
            Selector = selector;
        }
    }
}
