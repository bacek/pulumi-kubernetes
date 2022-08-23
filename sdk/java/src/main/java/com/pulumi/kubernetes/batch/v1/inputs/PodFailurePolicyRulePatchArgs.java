// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.kubernetes.batch.v1.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.kubernetes.batch.v1.inputs.PodFailurePolicyOnExitCodesRequirementPatchArgs;
import com.pulumi.kubernetes.batch.v1.inputs.PodFailurePolicyOnPodConditionsPatternPatchArgs;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


/**
 * PodFailurePolicyRule describes how a pod failure is handled when the requirements are met. One of OnExitCodes and onPodConditions, but not both, can be used in each rule.
 * 
 */
public final class PodFailurePolicyRulePatchArgs extends com.pulumi.resources.ResourceArgs {

    public static final PodFailurePolicyRulePatchArgs Empty = new PodFailurePolicyRulePatchArgs();

    /**
     * Specifies the action taken on a pod failure when the requirements are satisfied. Possible values are: - FailJob: indicates that the pod&#39;s job is marked as Failed and all
     *   running pods are terminated.
     * - Ignore: indicates that the counter towards the .backoffLimit is not
     *   incremented and a replacement pod is created.
     * - Count: indicates that the pod is handled in the default way - the
     *   counter towards the .backoffLimit is incremented.
     *   Additional values are considered to be added in the future. Clients should react to an unknown action by skipping the rule.
     * 
     */
    @Import(name="action")
    private @Nullable Output<String> action;

    /**
     * @return Specifies the action taken on a pod failure when the requirements are satisfied. Possible values are: - FailJob: indicates that the pod&#39;s job is marked as Failed and all
     *   running pods are terminated.
     * - Ignore: indicates that the counter towards the .backoffLimit is not
     *   incremented and a replacement pod is created.
     * - Count: indicates that the pod is handled in the default way - the
     *   counter towards the .backoffLimit is incremented.
     *   Additional values are considered to be added in the future. Clients should react to an unknown action by skipping the rule.
     * 
     */
    public Optional<Output<String>> action() {
        return Optional.ofNullable(this.action);
    }

    /**
     * Represents the requirement on the container exit codes.
     * 
     */
    @Import(name="onExitCodes")
    private @Nullable Output<PodFailurePolicyOnExitCodesRequirementPatchArgs> onExitCodes;

    /**
     * @return Represents the requirement on the container exit codes.
     * 
     */
    public Optional<Output<PodFailurePolicyOnExitCodesRequirementPatchArgs>> onExitCodes() {
        return Optional.ofNullable(this.onExitCodes);
    }

    /**
     * Represents the requirement on the pod conditions. The requirement is represented as a list of pod condition patterns. The requirement is satisfied if at least one pattern matches an actual pod condition. At most 20 elements are allowed.
     * 
     */
    @Import(name="onPodConditions")
    private @Nullable Output<List<PodFailurePolicyOnPodConditionsPatternPatchArgs>> onPodConditions;

    /**
     * @return Represents the requirement on the pod conditions. The requirement is represented as a list of pod condition patterns. The requirement is satisfied if at least one pattern matches an actual pod condition. At most 20 elements are allowed.
     * 
     */
    public Optional<Output<List<PodFailurePolicyOnPodConditionsPatternPatchArgs>>> onPodConditions() {
        return Optional.ofNullable(this.onPodConditions);
    }

    private PodFailurePolicyRulePatchArgs() {}

    private PodFailurePolicyRulePatchArgs(PodFailurePolicyRulePatchArgs $) {
        this.action = $.action;
        this.onExitCodes = $.onExitCodes;
        this.onPodConditions = $.onPodConditions;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(PodFailurePolicyRulePatchArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private PodFailurePolicyRulePatchArgs $;

        public Builder() {
            $ = new PodFailurePolicyRulePatchArgs();
        }

        public Builder(PodFailurePolicyRulePatchArgs defaults) {
            $ = new PodFailurePolicyRulePatchArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param action Specifies the action taken on a pod failure when the requirements are satisfied. Possible values are: - FailJob: indicates that the pod&#39;s job is marked as Failed and all
         *   running pods are terminated.
         * - Ignore: indicates that the counter towards the .backoffLimit is not
         *   incremented and a replacement pod is created.
         * - Count: indicates that the pod is handled in the default way - the
         *   counter towards the .backoffLimit is incremented.
         *   Additional values are considered to be added in the future. Clients should react to an unknown action by skipping the rule.
         * 
         * @return builder
         * 
         */
        public Builder action(@Nullable Output<String> action) {
            $.action = action;
            return this;
        }

        /**
         * @param action Specifies the action taken on a pod failure when the requirements are satisfied. Possible values are: - FailJob: indicates that the pod&#39;s job is marked as Failed and all
         *   running pods are terminated.
         * - Ignore: indicates that the counter towards the .backoffLimit is not
         *   incremented and a replacement pod is created.
         * - Count: indicates that the pod is handled in the default way - the
         *   counter towards the .backoffLimit is incremented.
         *   Additional values are considered to be added in the future. Clients should react to an unknown action by skipping the rule.
         * 
         * @return builder
         * 
         */
        public Builder action(String action) {
            return action(Output.of(action));
        }

        /**
         * @param onExitCodes Represents the requirement on the container exit codes.
         * 
         * @return builder
         * 
         */
        public Builder onExitCodes(@Nullable Output<PodFailurePolicyOnExitCodesRequirementPatchArgs> onExitCodes) {
            $.onExitCodes = onExitCodes;
            return this;
        }

        /**
         * @param onExitCodes Represents the requirement on the container exit codes.
         * 
         * @return builder
         * 
         */
        public Builder onExitCodes(PodFailurePolicyOnExitCodesRequirementPatchArgs onExitCodes) {
            return onExitCodes(Output.of(onExitCodes));
        }

        /**
         * @param onPodConditions Represents the requirement on the pod conditions. The requirement is represented as a list of pod condition patterns. The requirement is satisfied if at least one pattern matches an actual pod condition. At most 20 elements are allowed.
         * 
         * @return builder
         * 
         */
        public Builder onPodConditions(@Nullable Output<List<PodFailurePolicyOnPodConditionsPatternPatchArgs>> onPodConditions) {
            $.onPodConditions = onPodConditions;
            return this;
        }

        /**
         * @param onPodConditions Represents the requirement on the pod conditions. The requirement is represented as a list of pod condition patterns. The requirement is satisfied if at least one pattern matches an actual pod condition. At most 20 elements are allowed.
         * 
         * @return builder
         * 
         */
        public Builder onPodConditions(List<PodFailurePolicyOnPodConditionsPatternPatchArgs> onPodConditions) {
            return onPodConditions(Output.of(onPodConditions));
        }

        /**
         * @param onPodConditions Represents the requirement on the pod conditions. The requirement is represented as a list of pod condition patterns. The requirement is satisfied if at least one pattern matches an actual pod condition. At most 20 elements are allowed.
         * 
         * @return builder
         * 
         */
        public Builder onPodConditions(PodFailurePolicyOnPodConditionsPatternPatchArgs... onPodConditions) {
            return onPodConditions(List.of(onPodConditions));
        }

        public PodFailurePolicyRulePatchArgs build() {
            return $;
        }
    }

}
