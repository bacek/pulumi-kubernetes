// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Outputs.Autoscaling.V2Beta1
{

    /// <summary>
    /// MetricStatus describes the last-read state of a single metric.
    /// </summary>
    [OutputType]
    public sealed class MetricStatusPatch
    {
        /// <summary>
        /// container resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.
        /// </summary>
        public readonly Pulumi.Kubernetes.Types.Outputs.Autoscaling.V2Beta1.ContainerResourceMetricStatusPatch ContainerResource;
        /// <summary>
        /// external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).
        /// </summary>
        public readonly Pulumi.Kubernetes.Types.Outputs.Autoscaling.V2Beta1.ExternalMetricStatusPatch External;
        /// <summary>
        /// object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).
        /// </summary>
        public readonly Pulumi.Kubernetes.Types.Outputs.Autoscaling.V2Beta1.ObjectMetricStatusPatch Object;
        /// <summary>
        /// pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.
        /// </summary>
        public readonly Pulumi.Kubernetes.Types.Outputs.Autoscaling.V2Beta1.PodsMetricStatusPatch Pods;
        /// <summary>
        /// resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.
        /// </summary>
        public readonly Pulumi.Kubernetes.Types.Outputs.Autoscaling.V2Beta1.ResourceMetricStatusPatch Resource;
        /// <summary>
        /// type is the type of metric source.  It will be one of "Object", "Pods" or "Resource", each corresponds to a matching field in the object.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private MetricStatusPatch(
            Pulumi.Kubernetes.Types.Outputs.Autoscaling.V2Beta1.ContainerResourceMetricStatusPatch containerResource,

            Pulumi.Kubernetes.Types.Outputs.Autoscaling.V2Beta1.ExternalMetricStatusPatch external,

            Pulumi.Kubernetes.Types.Outputs.Autoscaling.V2Beta1.ObjectMetricStatusPatch @object,

            Pulumi.Kubernetes.Types.Outputs.Autoscaling.V2Beta1.PodsMetricStatusPatch pods,

            Pulumi.Kubernetes.Types.Outputs.Autoscaling.V2Beta1.ResourceMetricStatusPatch resource,

            string type)
        {
            ContainerResource = containerResource;
            External = external;
            Object = @object;
            Pods = pods;
            Resource = resource;
            Type = type;
        }
    }
}
