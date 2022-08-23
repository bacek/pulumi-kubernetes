// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.kubernetes.apps.v1;

import com.pulumi.core.Alias;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.kubernetes.Utilities;
import com.pulumi.kubernetes.apps.v1.StatefulSetArgs;
import com.pulumi.kubernetes.apps.v1.outputs.StatefulSetSpec;
import com.pulumi.kubernetes.apps.v1.outputs.StatefulSetStatus;
import com.pulumi.kubernetes.meta.v1.outputs.ObjectMeta;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * StatefulSet represents a set of pods with consistent identities. Identities are defined as:
 *   - Network: A single stable DNS and hostname.
 *   - Storage: As many VolumeClaims as requested.
 * 
 * The StatefulSet guarantees that a given network identity will always map to the same storage identity.
 * 
 * This resource waits until its status is ready before registering success
 * for create/update, and populating output properties from the current state of the resource.
 * The following conditions are used to determine whether the resource creation has
 * succeeded or failed:
 * 
 * 1. The value of &#39;spec.replicas&#39; matches &#39;.status.replicas&#39;, &#39;.status.currentReplicas&#39;,
 *    and &#39;.status.readyReplicas&#39;.
 * 2. The value of &#39;.status.updateRevision&#39; matches &#39;.status.currentRevision&#39;.
 * 
 * If the StatefulSet has not reached a Ready state after 10 minutes, it will
 * time out and mark the resource update as Failed. You can override the default timeout value
 * by setting the &#39;customTimeouts&#39; option on the resource.
 * 
 * ## Example Usage
 * 
 */
@ResourceType(type="kubernetes:apps/v1:StatefulSet")
public class StatefulSet extends com.pulumi.resources.CustomResource {
    /**
     * APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
     * 
     */
    @Export(name="apiVersion", type=String.class, parameters={})
    private Output</* @Nullable */ String> apiVersion;

    /**
     * @return APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
     * 
     */
    public Output<Optional<String>> apiVersion() {
        return Codegen.optional(this.apiVersion);
    }
    /**
     * Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
     * 
     */
    @Export(name="kind", type=String.class, parameters={})
    private Output</* @Nullable */ String> kind;

    /**
     * @return Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
     * 
     */
    public Output<Optional<String>> kind() {
        return Codegen.optional(this.kind);
    }
    /**
     * Standard object&#39;s metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
     * 
     */
    @Export(name="metadata", type=ObjectMeta.class, parameters={})
    private Output</* @Nullable */ ObjectMeta> metadata;

    /**
     * @return Standard object&#39;s metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
     * 
     */
    public Output<Optional<ObjectMeta>> metadata() {
        return Codegen.optional(this.metadata);
    }
    /**
     * Spec defines the desired identities of pods in this set.
     * 
     */
    @Export(name="spec", type=StatefulSetSpec.class, parameters={})
    private Output</* @Nullable */ StatefulSetSpec> spec;

    /**
     * @return Spec defines the desired identities of pods in this set.
     * 
     */
    public Output<Optional<StatefulSetSpec>> spec() {
        return Codegen.optional(this.spec);
    }
    /**
     * Status is the current status of Pods in this StatefulSet. This data may be out of date by some window of time.
     * 
     */
    @Export(name="status", type=StatefulSetStatus.class, parameters={})
    private Output</* @Nullable */ StatefulSetStatus> status;

    /**
     * @return Status is the current status of Pods in this StatefulSet. This data may be out of date by some window of time.
     * 
     */
    public Output<Optional<StatefulSetStatus>> status() {
        return Codegen.optional(this.status);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public StatefulSet(String name) {
        this(name, StatefulSetArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public StatefulSet(String name, @Nullable StatefulSetArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public StatefulSet(String name, @Nullable StatefulSetArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("kubernetes:apps/v1:StatefulSet", name, makeArgs(args), makeResourceOptions(options, Codegen.empty()));
    }

    private StatefulSet(String name, Output<String> id, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("kubernetes:apps/v1:StatefulSet", name, null, makeResourceOptions(options, id));
    }

    private static StatefulSetArgs makeArgs(@Nullable StatefulSetArgs args) {
        var builder = args == null ? StatefulSetArgs.builder() : StatefulSetArgs.builder(args);
        return builder
            .apiVersion("apps/v1")
            .kind("StatefulSet")
            .build();
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .aliases(List.of(
                Output.of(Alias.builder().type("kubernetes:apps/v1beta1:StatefulSet").build()),
                Output.of(Alias.builder().type("kubernetes:apps/v1beta2:StatefulSet").build())
            ))
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static StatefulSet get(String name, Output<String> id, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new StatefulSet(name, id, options);
    }
}
