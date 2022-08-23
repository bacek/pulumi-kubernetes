// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.kubernetes.core.v1.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


/**
 * Describe a container image
 * 
 */
public final class ContainerImageArgs extends com.pulumi.resources.ResourceArgs {

    public static final ContainerImageArgs Empty = new ContainerImageArgs();

    /**
     * Names by which this image is known. e.g. [&#34;kubernetes.example/hyperkube:v1.0.7&#34;, &#34;cloud-vendor.registry.example/cloud-vendor/hyperkube:v1.0.7&#34;]
     * 
     */
    @Import(name="names", required=true)
    private Output<List<String>> names;

    /**
     * @return Names by which this image is known. e.g. [&#34;kubernetes.example/hyperkube:v1.0.7&#34;, &#34;cloud-vendor.registry.example/cloud-vendor/hyperkube:v1.0.7&#34;]
     * 
     */
    public Output<List<String>> names() {
        return this.names;
    }

    /**
     * The size of the image in bytes.
     * 
     */
    @Import(name="sizeBytes")
    private @Nullable Output<Integer> sizeBytes;

    /**
     * @return The size of the image in bytes.
     * 
     */
    public Optional<Output<Integer>> sizeBytes() {
        return Optional.ofNullable(this.sizeBytes);
    }

    private ContainerImageArgs() {}

    private ContainerImageArgs(ContainerImageArgs $) {
        this.names = $.names;
        this.sizeBytes = $.sizeBytes;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ContainerImageArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ContainerImageArgs $;

        public Builder() {
            $ = new ContainerImageArgs();
        }

        public Builder(ContainerImageArgs defaults) {
            $ = new ContainerImageArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param names Names by which this image is known. e.g. [&#34;kubernetes.example/hyperkube:v1.0.7&#34;, &#34;cloud-vendor.registry.example/cloud-vendor/hyperkube:v1.0.7&#34;]
         * 
         * @return builder
         * 
         */
        public Builder names(Output<List<String>> names) {
            $.names = names;
            return this;
        }

        /**
         * @param names Names by which this image is known. e.g. [&#34;kubernetes.example/hyperkube:v1.0.7&#34;, &#34;cloud-vendor.registry.example/cloud-vendor/hyperkube:v1.0.7&#34;]
         * 
         * @return builder
         * 
         */
        public Builder names(List<String> names) {
            return names(Output.of(names));
        }

        /**
         * @param names Names by which this image is known. e.g. [&#34;kubernetes.example/hyperkube:v1.0.7&#34;, &#34;cloud-vendor.registry.example/cloud-vendor/hyperkube:v1.0.7&#34;]
         * 
         * @return builder
         * 
         */
        public Builder names(String... names) {
            return names(List.of(names));
        }

        /**
         * @param sizeBytes The size of the image in bytes.
         * 
         * @return builder
         * 
         */
        public Builder sizeBytes(@Nullable Output<Integer> sizeBytes) {
            $.sizeBytes = sizeBytes;
            return this;
        }

        /**
         * @param sizeBytes The size of the image in bytes.
         * 
         * @return builder
         * 
         */
        public Builder sizeBytes(Integer sizeBytes) {
            return sizeBytes(Output.of(sizeBytes));
        }

        public ContainerImageArgs build() {
            $.names = Objects.requireNonNull($.names, "expected parameter 'names' to be non-null");
            return $;
        }
    }

}
