// Copyright 2016-2022, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi"
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * CustomResourcePatch represents an instance of a CustomResourceDefinition (CRD). For example, the
 * CoreOS Prometheus operator exposes a CRD `monitoring.coreos.com/ServiceMonitor`; to
 * instantiate this as a Pulumi resource, one could call `new CustomResourcePatch`, passing the
 * `ServiceMonitor` resource definition as an argument.
 */
export class CustomResourcePatch extends pulumi.CustomResource {
    /**
     * APIVersion defines the versioned schema of this representation of an object. Servers should
     * convert recognized schemas to the latest internal value, and may reject unrecognized
     * values. More info:
     * https://git.k8s.io/community/contributors/devel/api-conventions.md#resources
     */
    public readonly apiVersion!: pulumi.Output<string>;

    /**
     * Kind is a string value representing the REST resource this object represents. Servers may
     * infer this from the endpoint the client submits requests to. Cannot be updated. In
     * CamelCase. More info:
     * https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds
     */
    public readonly kind!: pulumi.Output<string>;

    /**
     * Standard object metadata; More info:
     * https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata.
     */
    public readonly metadata!: pulumi.Output<outputs.meta.v1.ObjectMeta>;

    public getInputs(): CustomResourcePatchArgs { return this.__inputs; }
    private readonly __inputs: CustomResourcePatchArgs;

    /**
     * Create a CustomResourcePatch resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CustomResourcePatchArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            for (const key of Object.keys(args)) {
                inputs[key] = (args as any)[key];
            }
        } else {
            for (const key of Object.keys(args)) {
                inputs[key] = undefined;
            }
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(`kubernetes:${args.apiVersion}:${args.kind}Patch`, name, inputs, opts);
        this.__inputs = args;
    }
}

/**
 * The set of arguments for constructing a CustomResourcePatch resource.
 *
 * NOTE: This type is fairly loose, since other than `apiVersion` and `kind`, there are no
 * fields required across all CRDs.
 */
export interface CustomResourcePatchArgs {
    /**
     * APIVersion defines the versioned schema of this representation of an object. Servers should
     * convert recognized schemas to the latest internal value, and may reject unrecognized
     * values. More info:
     * https://git.k8s.io/community/contributors/devel/api-conventions.md#resources
     */
    apiVersion: pulumi.Input<string>;

    /**
     * Kind is a string value representing the REST resource this object represents. Servers may
     * infer this from the endpoint the client submits requests to. Cannot be updated. In
     * CamelCase. More info:
     * https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds
     */
    kind: pulumi.Input<string>;

    /**
     * Standard object metadata; More info:
     * https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata.
     */
    metadata?: pulumi.Input<inputs.meta.v1.ObjectMeta>;
    [othersFields: string]: pulumi.Input<any>;
}