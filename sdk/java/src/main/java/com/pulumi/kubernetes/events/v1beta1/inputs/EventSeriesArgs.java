// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.kubernetes.events.v1beta1.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


/**
 * EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time.
 * 
 */
public final class EventSeriesArgs extends com.pulumi.resources.ResourceArgs {

    public static final EventSeriesArgs Empty = new EventSeriesArgs();

    /**
     * count is the number of occurrences in this series up to the last heartbeat time.
     * 
     */
    @Import(name="count", required=true)
    private Output<Integer> count;

    /**
     * @return count is the number of occurrences in this series up to the last heartbeat time.
     * 
     */
    public Output<Integer> count() {
        return this.count;
    }

    /**
     * lastObservedTime is the time when last Event from the series was seen before last heartbeat.
     * 
     */
    @Import(name="lastObservedTime", required=true)
    private Output<String> lastObservedTime;

    /**
     * @return lastObservedTime is the time when last Event from the series was seen before last heartbeat.
     * 
     */
    public Output<String> lastObservedTime() {
        return this.lastObservedTime;
    }

    /**
     * Information whether this series is ongoing or finished. Deprecated. Planned removal for 1.18
     * 
     */
    @Import(name="state")
    private @Nullable Output<String> state;

    /**
     * @return Information whether this series is ongoing or finished. Deprecated. Planned removal for 1.18
     * 
     */
    public Optional<Output<String>> state() {
        return Optional.ofNullable(this.state);
    }

    private EventSeriesArgs() {}

    private EventSeriesArgs(EventSeriesArgs $) {
        this.count = $.count;
        this.lastObservedTime = $.lastObservedTime;
        this.state = $.state;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(EventSeriesArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private EventSeriesArgs $;

        public Builder() {
            $ = new EventSeriesArgs();
        }

        public Builder(EventSeriesArgs defaults) {
            $ = new EventSeriesArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param count count is the number of occurrences in this series up to the last heartbeat time.
         * 
         * @return builder
         * 
         */
        public Builder count(Output<Integer> count) {
            $.count = count;
            return this;
        }

        /**
         * @param count count is the number of occurrences in this series up to the last heartbeat time.
         * 
         * @return builder
         * 
         */
        public Builder count(Integer count) {
            return count(Output.of(count));
        }

        /**
         * @param lastObservedTime lastObservedTime is the time when last Event from the series was seen before last heartbeat.
         * 
         * @return builder
         * 
         */
        public Builder lastObservedTime(Output<String> lastObservedTime) {
            $.lastObservedTime = lastObservedTime;
            return this;
        }

        /**
         * @param lastObservedTime lastObservedTime is the time when last Event from the series was seen before last heartbeat.
         * 
         * @return builder
         * 
         */
        public Builder lastObservedTime(String lastObservedTime) {
            return lastObservedTime(Output.of(lastObservedTime));
        }

        /**
         * @param state Information whether this series is ongoing or finished. Deprecated. Planned removal for 1.18
         * 
         * @return builder
         * 
         */
        public Builder state(@Nullable Output<String> state) {
            $.state = state;
            return this;
        }

        /**
         * @param state Information whether this series is ongoing or finished. Deprecated. Planned removal for 1.18
         * 
         * @return builder
         * 
         */
        public Builder state(String state) {
            return state(Output.of(state));
        }

        public EventSeriesArgs build() {
            $.count = Objects.requireNonNull($.count, "expected parameter 'count' to be non-null");
            $.lastObservedTime = Objects.requireNonNull($.lastObservedTime, "expected parameter 'lastObservedTime' to be non-null");
            return $;
        }
    }

}