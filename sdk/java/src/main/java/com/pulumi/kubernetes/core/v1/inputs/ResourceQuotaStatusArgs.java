// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.kubernetes.core.v1.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


/**
 * ResourceQuotaStatus defines the enforced hard limits and observed use.
 * 
 */
public final class ResourceQuotaStatusArgs extends com.pulumi.resources.ResourceArgs {

    public static final ResourceQuotaStatusArgs Empty = new ResourceQuotaStatusArgs();

    /**
     * Hard is the set of enforced hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/
     * 
     */
    @Import(name="hard")
    private @Nullable Output<Map<String,String>> hard;

    /**
     * @return Hard is the set of enforced hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/
     * 
     */
    public Optional<Output<Map<String,String>>> hard() {
        return Optional.ofNullable(this.hard);
    }

    /**
     * Used is the current observed total usage of the resource in the namespace.
     * 
     */
    @Import(name="used")
    private @Nullable Output<Map<String,String>> used;

    /**
     * @return Used is the current observed total usage of the resource in the namespace.
     * 
     */
    public Optional<Output<Map<String,String>>> used() {
        return Optional.ofNullable(this.used);
    }

    private ResourceQuotaStatusArgs() {}

    private ResourceQuotaStatusArgs(ResourceQuotaStatusArgs $) {
        this.hard = $.hard;
        this.used = $.used;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ResourceQuotaStatusArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ResourceQuotaStatusArgs $;

        public Builder() {
            $ = new ResourceQuotaStatusArgs();
        }

        public Builder(ResourceQuotaStatusArgs defaults) {
            $ = new ResourceQuotaStatusArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param hard Hard is the set of enforced hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/
         * 
         * @return builder
         * 
         */
        public Builder hard(@Nullable Output<Map<String,String>> hard) {
            $.hard = hard;
            return this;
        }

        /**
         * @param hard Hard is the set of enforced hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/
         * 
         * @return builder
         * 
         */
        public Builder hard(Map<String,String> hard) {
            return hard(Output.of(hard));
        }

        /**
         * @param used Used is the current observed total usage of the resource in the namespace.
         * 
         * @return builder
         * 
         */
        public Builder used(@Nullable Output<Map<String,String>> used) {
            $.used = used;
            return this;
        }

        /**
         * @param used Used is the current observed total usage of the resource in the namespace.
         * 
         * @return builder
         * 
         */
        public Builder used(Map<String,String> used) {
            return used(Output.of(used));
        }

        public ResourceQuotaStatusArgs build() {
            return $;
        }
    }

}