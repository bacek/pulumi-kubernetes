// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.kubernetes.core.v1.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


/**
 * SecretKeySelector selects a key of a Secret.
 * 
 */
public final class SecretKeySelectorArgs extends com.pulumi.resources.ResourceArgs {

    public static final SecretKeySelectorArgs Empty = new SecretKeySelectorArgs();

    /**
     * The key of the secret to select from.  Must be a valid secret key.
     * 
     */
    @Import(name="key", required=true)
    private Output<String> key;

    /**
     * @return The key of the secret to select from.  Must be a valid secret key.
     * 
     */
    public Output<String> key() {
        return this.key;
    }

    /**
     * Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * Specify whether the Secret or its key must be defined
     * 
     */
    @Import(name="optional")
    private @Nullable Output<Boolean> optional;

    /**
     * @return Specify whether the Secret or its key must be defined
     * 
     */
    public Optional<Output<Boolean>> optional() {
        return Optional.ofNullable(this.optional);
    }

    private SecretKeySelectorArgs() {}

    private SecretKeySelectorArgs(SecretKeySelectorArgs $) {
        this.key = $.key;
        this.name = $.name;
        this.optional = $.optional;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(SecretKeySelectorArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private SecretKeySelectorArgs $;

        public Builder() {
            $ = new SecretKeySelectorArgs();
        }

        public Builder(SecretKeySelectorArgs defaults) {
            $ = new SecretKeySelectorArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param key The key of the secret to select from.  Must be a valid secret key.
         * 
         * @return builder
         * 
         */
        public Builder key(Output<String> key) {
            $.key = key;
            return this;
        }

        /**
         * @param key The key of the secret to select from.  Must be a valid secret key.
         * 
         * @return builder
         * 
         */
        public Builder key(String key) {
            return key(Output.of(key));
        }

        /**
         * @param name Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param optional Specify whether the Secret or its key must be defined
         * 
         * @return builder
         * 
         */
        public Builder optional(@Nullable Output<Boolean> optional) {
            $.optional = optional;
            return this;
        }

        /**
         * @param optional Specify whether the Secret or its key must be defined
         * 
         * @return builder
         * 
         */
        public Builder optional(Boolean optional) {
            return optional(Output.of(optional));
        }

        public SecretKeySelectorArgs build() {
            $.key = Objects.requireNonNull($.key, "expected parameter 'key' to be non-null");
            return $;
        }
    }

}