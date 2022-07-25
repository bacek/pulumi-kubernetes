// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.kubernetes.authentication.v1beta1;

import com.pulumi.core.Alias;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.kubernetes.Utilities;
import com.pulumi.kubernetes.authentication.v1beta1.TokenReviewArgs;
import com.pulumi.kubernetes.authentication.v1beta1.outputs.TokenReviewSpec;
import com.pulumi.kubernetes.authentication.v1beta1.outputs.TokenReviewStatus;
import com.pulumi.kubernetes.meta.v1.outputs.ObjectMeta;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * TokenReview attempts to authenticate a token to a known user. Note: TokenReview requests may be cached by the webhook token authenticator plugin in the kube-apiserver.
 * 
 */
@ResourceType(type="kubernetes:authentication.k8s.io/v1beta1:TokenReview")
public class TokenReview extends com.pulumi.resources.CustomResource {
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
    @Export(name="metadata", type=ObjectMeta.class, parameters={})
    private Output</* @Nullable */ ObjectMeta> metadata;

    public Output<Optional<ObjectMeta>> metadata() {
        return Codegen.optional(this.metadata);
    }
    /**
     * Spec holds information about the request being evaluated
     * 
     */
    @Export(name="spec", type=TokenReviewSpec.class, parameters={})
    private Output<TokenReviewSpec> spec;

    /**
     * @return Spec holds information about the request being evaluated
     * 
     */
    public Output<TokenReviewSpec> spec() {
        return this.spec;
    }
    /**
     * Status is filled in by the server and indicates whether the request can be authenticated.
     * 
     */
    @Export(name="status", type=TokenReviewStatus.class, parameters={})
    private Output</* @Nullable */ TokenReviewStatus> status;

    /**
     * @return Status is filled in by the server and indicates whether the request can be authenticated.
     * 
     */
    public Output<Optional<TokenReviewStatus>> status() {
        return Codegen.optional(this.status);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public TokenReview(String name) {
        this(name, TokenReviewArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public TokenReview(String name, TokenReviewArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public TokenReview(String name, TokenReviewArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("kubernetes:authentication.k8s.io/v1beta1:TokenReview", name, makeArgs(args), makeResourceOptions(options, Codegen.empty()));
    }

    private TokenReview(String name, Output<String> id, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("kubernetes:authentication.k8s.io/v1beta1:TokenReview", name, null, makeResourceOptions(options, id));
    }

    private static TokenReviewArgs makeArgs(TokenReviewArgs args) {
        var builder = args == null ? TokenReviewArgs.builder() : TokenReviewArgs.builder(args);
        return builder
            .apiVersion("authentication.k8s.io/v1beta1")
            .kind("TokenReview")
            .build();
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .aliases(List.of(
                Output.of(Alias.builder().type("kubernetes:authentication.k8s.io/v1:TokenReview").build())
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
    public static TokenReview get(String name, Output<String> id, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new TokenReview(name, id, options);
    }
}