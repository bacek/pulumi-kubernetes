// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.kubernetes.discovery.v1beta1.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.kubernetes.core.v1.inputs.ObjectReferencePatchArgs;
import com.pulumi.kubernetes.discovery.v1beta1.inputs.EndpointConditionsPatchArgs;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


/**
 * Endpoint represents a single logical &#34;backend&#34; implementing a service.
 * 
 */
public final class EndpointPatchArgs extends com.pulumi.resources.ResourceArgs {

    public static final EndpointPatchArgs Empty = new EndpointPatchArgs();

    /**
     * addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100.
     * 
     */
    @Import(name="addresses")
    private @Nullable Output<List<String>> addresses;

    /**
     * @return addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100.
     * 
     */
    public Optional<Output<List<String>>> addresses() {
        return Optional.ofNullable(this.addresses);
    }

    /**
     * conditions contains information about the current status of the endpoint.
     * 
     */
    @Import(name="conditions")
    private @Nullable Output<EndpointConditionsPatchArgs> conditions;

    /**
     * @return conditions contains information about the current status of the endpoint.
     * 
     */
    public Optional<Output<EndpointConditionsPatchArgs>> conditions() {
        return Optional.ofNullable(this.conditions);
    }

    /**
     * hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must pass DNS Label (RFC 1123) validation.
     * 
     */
    @Import(name="hostname")
    private @Nullable Output<String> hostname;

    /**
     * @return hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must pass DNS Label (RFC 1123) validation.
     * 
     */
    public Optional<Output<String>> hostname() {
        return Optional.ofNullable(this.hostname);
    }

    /**
     * nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node. This field can be enabled with the EndpointSliceNodeName feature gate.
     * 
     */
    @Import(name="nodeName")
    private @Nullable Output<String> nodeName;

    /**
     * @return nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node. This field can be enabled with the EndpointSliceNodeName feature gate.
     * 
     */
    public Optional<Output<String>> nodeName() {
        return Optional.ofNullable(this.nodeName);
    }

    /**
     * targetRef is a reference to a Kubernetes object that represents this endpoint.
     * 
     */
    @Import(name="targetRef")
    private @Nullable Output<ObjectReferencePatchArgs> targetRef;

    /**
     * @return targetRef is a reference to a Kubernetes object that represents this endpoint.
     * 
     */
    public Optional<Output<ObjectReferencePatchArgs>> targetRef() {
        return Optional.ofNullable(this.targetRef);
    }

    /**
     * topology contains arbitrary topology information associated with the endpoint. These key/value pairs must conform with the label format. https://kubernetes.io/docs/concepts/overview/working-with-objects/labels Topology may include a maximum of 16 key/value pairs. This includes, but is not limited to the following well known keys: * kubernetes.io/hostname: the value indicates the hostname of the node
     *   where the endpoint is located. This should match the corresponding
     *   node label.
     * * topology.kubernetes.io/zone: the value indicates the zone where the
     *   endpoint is located. This should match the corresponding node label.
     * * topology.kubernetes.io/region: the value indicates the region where the
     *   endpoint is located. This should match the corresponding node label.
     * 
     */
    @Import(name="topology")
    private @Nullable Output<Map<String,String>> topology;

    /**
     * @return topology contains arbitrary topology information associated with the endpoint. These key/value pairs must conform with the label format. https://kubernetes.io/docs/concepts/overview/working-with-objects/labels Topology may include a maximum of 16 key/value pairs. This includes, but is not limited to the following well known keys: * kubernetes.io/hostname: the value indicates the hostname of the node
     *   where the endpoint is located. This should match the corresponding
     *   node label.
     * * topology.kubernetes.io/zone: the value indicates the zone where the
     *   endpoint is located. This should match the corresponding node label.
     * * topology.kubernetes.io/region: the value indicates the region where the
     *   endpoint is located. This should match the corresponding node label.
     * 
     */
    public Optional<Output<Map<String,String>>> topology() {
        return Optional.ofNullable(this.topology);
    }

    private EndpointPatchArgs() {}

    private EndpointPatchArgs(EndpointPatchArgs $) {
        this.addresses = $.addresses;
        this.conditions = $.conditions;
        this.hostname = $.hostname;
        this.nodeName = $.nodeName;
        this.targetRef = $.targetRef;
        this.topology = $.topology;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(EndpointPatchArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private EndpointPatchArgs $;

        public Builder() {
            $ = new EndpointPatchArgs();
        }

        public Builder(EndpointPatchArgs defaults) {
            $ = new EndpointPatchArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param addresses addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100.
         * 
         * @return builder
         * 
         */
        public Builder addresses(@Nullable Output<List<String>> addresses) {
            $.addresses = addresses;
            return this;
        }

        /**
         * @param addresses addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100.
         * 
         * @return builder
         * 
         */
        public Builder addresses(List<String> addresses) {
            return addresses(Output.of(addresses));
        }

        /**
         * @param addresses addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100.
         * 
         * @return builder
         * 
         */
        public Builder addresses(String... addresses) {
            return addresses(List.of(addresses));
        }

        /**
         * @param conditions conditions contains information about the current status of the endpoint.
         * 
         * @return builder
         * 
         */
        public Builder conditions(@Nullable Output<EndpointConditionsPatchArgs> conditions) {
            $.conditions = conditions;
            return this;
        }

        /**
         * @param conditions conditions contains information about the current status of the endpoint.
         * 
         * @return builder
         * 
         */
        public Builder conditions(EndpointConditionsPatchArgs conditions) {
            return conditions(Output.of(conditions));
        }

        /**
         * @param hostname hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must pass DNS Label (RFC 1123) validation.
         * 
         * @return builder
         * 
         */
        public Builder hostname(@Nullable Output<String> hostname) {
            $.hostname = hostname;
            return this;
        }

        /**
         * @param hostname hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must pass DNS Label (RFC 1123) validation.
         * 
         * @return builder
         * 
         */
        public Builder hostname(String hostname) {
            return hostname(Output.of(hostname));
        }

        /**
         * @param nodeName nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node. This field can be enabled with the EndpointSliceNodeName feature gate.
         * 
         * @return builder
         * 
         */
        public Builder nodeName(@Nullable Output<String> nodeName) {
            $.nodeName = nodeName;
            return this;
        }

        /**
         * @param nodeName nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node. This field can be enabled with the EndpointSliceNodeName feature gate.
         * 
         * @return builder
         * 
         */
        public Builder nodeName(String nodeName) {
            return nodeName(Output.of(nodeName));
        }

        /**
         * @param targetRef targetRef is a reference to a Kubernetes object that represents this endpoint.
         * 
         * @return builder
         * 
         */
        public Builder targetRef(@Nullable Output<ObjectReferencePatchArgs> targetRef) {
            $.targetRef = targetRef;
            return this;
        }

        /**
         * @param targetRef targetRef is a reference to a Kubernetes object that represents this endpoint.
         * 
         * @return builder
         * 
         */
        public Builder targetRef(ObjectReferencePatchArgs targetRef) {
            return targetRef(Output.of(targetRef));
        }

        /**
         * @param topology topology contains arbitrary topology information associated with the endpoint. These key/value pairs must conform with the label format. https://kubernetes.io/docs/concepts/overview/working-with-objects/labels Topology may include a maximum of 16 key/value pairs. This includes, but is not limited to the following well known keys: * kubernetes.io/hostname: the value indicates the hostname of the node
         *   where the endpoint is located. This should match the corresponding
         *   node label.
         * * topology.kubernetes.io/zone: the value indicates the zone where the
         *   endpoint is located. This should match the corresponding node label.
         * * topology.kubernetes.io/region: the value indicates the region where the
         *   endpoint is located. This should match the corresponding node label.
         * 
         * @return builder
         * 
         */
        public Builder topology(@Nullable Output<Map<String,String>> topology) {
            $.topology = topology;
            return this;
        }

        /**
         * @param topology topology contains arbitrary topology information associated with the endpoint. These key/value pairs must conform with the label format. https://kubernetes.io/docs/concepts/overview/working-with-objects/labels Topology may include a maximum of 16 key/value pairs. This includes, but is not limited to the following well known keys: * kubernetes.io/hostname: the value indicates the hostname of the node
         *   where the endpoint is located. This should match the corresponding
         *   node label.
         * * topology.kubernetes.io/zone: the value indicates the zone where the
         *   endpoint is located. This should match the corresponding node label.
         * * topology.kubernetes.io/region: the value indicates the region where the
         *   endpoint is located. This should match the corresponding node label.
         * 
         * @return builder
         * 
         */
        public Builder topology(Map<String,String> topology) {
            return topology(Output.of(topology));
        }

        public EndpointPatchArgs build() {
            return $;
        }
    }

}
