// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.kubernetes.autoscaling.v2beta1.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.kubernetes.autoscaling.v2beta1.outputs.ContainerResourceMetricSource;
import com.pulumi.kubernetes.autoscaling.v2beta1.outputs.ExternalMetricSource;
import com.pulumi.kubernetes.autoscaling.v2beta1.outputs.ObjectMetricSource;
import com.pulumi.kubernetes.autoscaling.v2beta1.outputs.PodsMetricSource;
import com.pulumi.kubernetes.autoscaling.v2beta1.outputs.ResourceMetricSource;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class MetricSpec {
    /**
     * @return container resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod of the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the &#34;pods&#34; source. This is an alpha feature and can be enabled by the HPAContainerMetrics feature flag.
     * 
     */
    private @Nullable ContainerResourceMetricSource containerResource;
    /**
     * @return external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).
     * 
     */
    private @Nullable ExternalMetricSource external;
    /**
     * @return object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).
     * 
     */
    private @Nullable ObjectMetricSource object;
    /**
     * @return pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.
     * 
     */
    private @Nullable PodsMetricSource pods;
    /**
     * @return resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the &#34;pods&#34; source.
     * 
     */
    private @Nullable ResourceMetricSource resource;
    /**
     * @return type is the type of metric source.  It should be one of &#34;Object&#34;, &#34;Pods&#34; or &#34;Resource&#34;, each mapping to a matching field in the object.
     * 
     */
    private String type;

    private MetricSpec() {}
    /**
     * @return container resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod of the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the &#34;pods&#34; source. This is an alpha feature and can be enabled by the HPAContainerMetrics feature flag.
     * 
     */
    public Optional<ContainerResourceMetricSource> containerResource() {
        return Optional.ofNullable(this.containerResource);
    }
    /**
     * @return external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).
     * 
     */
    public Optional<ExternalMetricSource> external() {
        return Optional.ofNullable(this.external);
    }
    /**
     * @return object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).
     * 
     */
    public Optional<ObjectMetricSource> object() {
        return Optional.ofNullable(this.object);
    }
    /**
     * @return pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.
     * 
     */
    public Optional<PodsMetricSource> pods() {
        return Optional.ofNullable(this.pods);
    }
    /**
     * @return resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the &#34;pods&#34; source.
     * 
     */
    public Optional<ResourceMetricSource> resource() {
        return Optional.ofNullable(this.resource);
    }
    /**
     * @return type is the type of metric source.  It should be one of &#34;Object&#34;, &#34;Pods&#34; or &#34;Resource&#34;, each mapping to a matching field in the object.
     * 
     */
    public String type() {
        return this.type;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(MetricSpec defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable ContainerResourceMetricSource containerResource;
        private @Nullable ExternalMetricSource external;
        private @Nullable ObjectMetricSource object;
        private @Nullable PodsMetricSource pods;
        private @Nullable ResourceMetricSource resource;
        private String type;
        public Builder() {}
        public Builder(MetricSpec defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.containerResource = defaults.containerResource;
    	      this.external = defaults.external;
    	      this.object = defaults.object;
    	      this.pods = defaults.pods;
    	      this.resource = defaults.resource;
    	      this.type = defaults.type;
        }

        @CustomType.Setter
        public Builder containerResource(@Nullable ContainerResourceMetricSource containerResource) {
            this.containerResource = containerResource;
            return this;
        }
        @CustomType.Setter
        public Builder external(@Nullable ExternalMetricSource external) {
            this.external = external;
            return this;
        }
        @CustomType.Setter
        public Builder object(@Nullable ObjectMetricSource object) {
            this.object = object;
            return this;
        }
        @CustomType.Setter
        public Builder pods(@Nullable PodsMetricSource pods) {
            this.pods = pods;
            return this;
        }
        @CustomType.Setter
        public Builder resource(@Nullable ResourceMetricSource resource) {
            this.resource = resource;
            return this;
        }
        @CustomType.Setter
        public Builder type(String type) {
            this.type = Objects.requireNonNull(type);
            return this;
        }
        public MetricSpec build() {
            final var o = new MetricSpec();
            o.containerResource = containerResource;
            o.external = external;
            o.object = object;
            o.pods = pods;
            o.resource = resource;
            o.type = type;
            return o;
        }
    }
}
