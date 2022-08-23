// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Outputs.Core.V1
{

    /// <summary>
    /// PodStatus represents information about the status of a pod. Status may trail the actual state of a system, especially if the node that hosts the pod cannot contact the control plane.
    /// </summary>
    [OutputType]
    public sealed class PodStatusPatch
    {
        /// <summary>
        /// Current service state of pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions
        /// </summary>
        public readonly ImmutableArray<Pulumi.Kubernetes.Types.Outputs.Core.V1.PodConditionPatch> Conditions;
        /// <summary>
        /// The list has one entry per container in the manifest. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status
        /// </summary>
        public readonly ImmutableArray<Pulumi.Kubernetes.Types.Outputs.Core.V1.ContainerStatusPatch> ContainerStatuses;
        /// <summary>
        /// Status for any ephemeral containers that have run in this pod.
        /// </summary>
        public readonly ImmutableArray<Pulumi.Kubernetes.Types.Outputs.Core.V1.ContainerStatusPatch> EphemeralContainerStatuses;
        /// <summary>
        /// IP address of the host to which the pod is assigned. Empty if not yet scheduled.
        /// </summary>
        public readonly string HostIP;
        /// <summary>
        /// The list has one entry per init container in the manifest. The most recent successful init container will have ready = true, the most recently started container will have startTime set. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status
        /// </summary>
        public readonly ImmutableArray<Pulumi.Kubernetes.Types.Outputs.Core.V1.ContainerStatusPatch> InitContainerStatuses;
        /// <summary>
        /// A human readable message indicating details about why the pod is in this condition.
        /// </summary>
        public readonly string Message;
        /// <summary>
        /// nominatedNodeName is set only when this pod preempts other pods on the node, but it cannot be scheduled right away as preemption victims receive their graceful termination periods. This field does not guarantee that the pod will be scheduled on this node. Scheduler may decide to place the pod elsewhere if other nodes become available sooner. Scheduler may also decide to give the resources on this node to a higher priority pod that is created after preemption. As a result, this field may be different than PodSpec.nodeName when the pod is scheduled.
        /// </summary>
        public readonly string NominatedNodeName;
        /// <summary>
        /// The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The conditions array, the reason and message fields, and the individual container status arrays contain more detail about the pod's status. There are five possible phase values:
        /// 
        /// Pending: The pod has been accepted by the Kubernetes system, but one or more of the container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while. Running: The pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. Succeeded: All containers in the pod have terminated in success, and will not be restarted. Failed: All containers in the pod have terminated, and at least one container has terminated in failure. The container either exited with non-zero status or was terminated by the system. Unknown: For some reason the state of the pod could not be obtained, typically due to an error in communicating with the host of the pod.
        /// 
        /// More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase
        /// </summary>
        public readonly string Phase;
        /// <summary>
        /// IP address allocated to the pod. Routable at least within the cluster. Empty if not yet allocated.
        /// </summary>
        public readonly string PodIP;
        /// <summary>
        /// podIPs holds the IP addresses allocated to the pod. If this field is specified, the 0th entry must match the podIP field. Pods may be allocated at most 1 value for each of IPv4 and IPv6. This list is empty if no IPs have been allocated yet.
        /// </summary>
        public readonly ImmutableArray<Pulumi.Kubernetes.Types.Outputs.Core.V1.PodIPPatch> PodIPs;
        /// <summary>
        /// The Quality of Service (QOS) classification assigned to the pod based on resource requirements See PodQOSClass type for available QOS classes More info: https://git.k8s.io/community/contributors/design-proposals/node/resource-qos.md
        /// </summary>
        public readonly string QosClass;
        /// <summary>
        /// A brief CamelCase message indicating details about why the pod is in this state. e.g. 'Evicted'
        /// </summary>
        public readonly string Reason;
        /// <summary>
        /// RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before the Kubelet pulled the container image(s) for the pod.
        /// </summary>
        public readonly string StartTime;

        [OutputConstructor]
        private PodStatusPatch(
            ImmutableArray<Pulumi.Kubernetes.Types.Outputs.Core.V1.PodConditionPatch> conditions,

            ImmutableArray<Pulumi.Kubernetes.Types.Outputs.Core.V1.ContainerStatusPatch> containerStatuses,

            ImmutableArray<Pulumi.Kubernetes.Types.Outputs.Core.V1.ContainerStatusPatch> ephemeralContainerStatuses,

            string hostIP,

            ImmutableArray<Pulumi.Kubernetes.Types.Outputs.Core.V1.ContainerStatusPatch> initContainerStatuses,

            string message,

            string nominatedNodeName,

            string phase,

            string podIP,

            ImmutableArray<Pulumi.Kubernetes.Types.Outputs.Core.V1.PodIPPatch> podIPs,

            string qosClass,

            string reason,

            string startTime)
        {
            Conditions = conditions;
            ContainerStatuses = containerStatuses;
            EphemeralContainerStatuses = ephemeralContainerStatuses;
            HostIP = hostIP;
            InitContainerStatuses = initContainerStatuses;
            Message = message;
            NominatedNodeName = nominatedNodeName;
            Phase = phase;
            PodIP = podIP;
            PodIPs = podIPs;
            QosClass = qosClass;
            Reason = reason;
            StartTime = startTime;
        }
    }
}
