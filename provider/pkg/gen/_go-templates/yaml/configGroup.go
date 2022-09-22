// Copyright 2016-2021, Pulumi Corporation.
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

package yaml

import (
	"fmt"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ConfigGroup creates a set of Kubernetes resources from Kubernetes YAML. The YAML text may be supplied using
// any of the following formats:
//
// 1. Using a filename or a list of filenames:
// 2. Using a file pattern or a list of file patterns:
// 3. Using a literal string containing YAML, or a list of such strings:
// 4. Any combination of files, patterns, or YAML strings:
//
// ## Example Usage
// ### Local File
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/yaml"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//	    pulumi.Run(func(ctx *pulumi.Context) error {
//	        _, err := yaml.NewConfigGroup(ctx, "example",
//	            &yaml.ConfigGroupArgs{
//	                Files: []string{"foo.yaml"},
//	            },
//	        )
//	        if err != nil {
//	            return err
//	        }
//
//	        return nil
//	    })
//	}
//
// ```
// ### Multiple Local Files
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/yaml"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//	    pulumi.Run(func(ctx *pulumi.Context) error {
//	        _, err := yaml.NewConfigGroup(ctx, "example",
//	            &yaml.ConfigGroupArgs{
//	                Files: []string{"foo.yaml", "bar.yaml"},
//	            },
//	        )
//	        if err != nil {
//	            return err
//	        }
//
//	        return nil
//	    })
//	}
//
// ```
// ### Local File Pattern
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/yaml"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//	    pulumi.Run(func(ctx *pulumi.Context) error {
//	        _, err := yaml.NewConfigGroup(ctx, "example",
//	            &yaml.ConfigGroupArgs{
//	                Files: []string{"yaml/*.yaml"},
//	            },
//	        )
//	        if err != nil {
//	            return err
//	        }
//
//	        return nil
//	    })
//	}
//
// ```
// ### Multiple Local File Patterns
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/yaml"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//	    pulumi.Run(func(ctx *pulumi.Context) error {
//	        _, err := yaml.NewConfigGroup(ctx, "example",
//	            &yaml.ConfigGroupArgs{
//	                Files: []string{"yaml/*.yaml", "bar/*.yaml"},
//	            },
//	        )
//	        if err != nil {
//	            return err
//	        }
//
//	        return nil
//	    })
//	}
//
// ```
// ### Literal YAML String
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/yaml"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//	    pulumi.Run(func(ctx *pulumi.Context) error {
//	        _, err := yaml.NewConfigGroup(ctx, "example",
//	            &yaml.ConfigGroupArgs{
//	                YAML: []string{
//	                    `
//
// apiVersion: v1
// kind: Namespace
// metadata:
//
//	name: foo
//
// `,
//
//	                },
//	            })
//	        if err != nil {
//	            return err
//	        }
//
//	        return nil
//	    })
//	}
//
// ```
// ### YAML with Transformations
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/yaml"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//	    pulumi.Run(func(ctx *pulumi.Context) error {
//	        _, err := yaml.NewConfigGroup(ctx, "example",
//	            &yaml.ConfigGroupArgs{
//	                Files: []string{"foo.yaml"},
//	                Transformations: []yaml.Transformation{
//	                    // Make every service private to the cluster, i.e., turn all services into ClusterIP
//	                    // instead of LoadBalancer.
//	                    func(state map[string]interface{}, opts ...pulumi.ResourceOption) {
//	                        if state["kind"] == "Service" {
//	                            spec := state["spec"].(map[string]interface{})
//	                            spec["type"] = "ClusterIP"
//	                        }
//	                    },
//
//	                    // Set a resource alias for a previous name.
//	                    func(state map[string]interface{}, opts ...pulumi.ResourceOption) {
//	                        if state["kind"] == "Deployment" {
//	                            aliases := pulumi.Aliases([]pulumi.Alias{
//	                                {
//	                                    Name: pulumi.String("oldName"),
//	                                },
//	                            })
//	                            opts = append(opts, aliases)
//	                        }
//	                    },
//
//	                    // Omit a resource from the Chart by transforming the specified resource definition
//	                    // to an empty List.
//	                    func(state map[string]interface{}, opts ...pulumi.ResourceOption) {
//	                        name := state["metadata"].(map[string]interface{})["name"]
//	                        if state["kind"] == "Pod" && name == "test" {
//	                            state["apiVersion"] = "core/v1"
//	                            state["kind"] = "List"
//	                        }
//	                    },
//	                },
//	            },
//	        )
//	        if err != nil {
//	            return err
//	        }
//
//	        return nil
//	    })
//	}
//
// ```
type ConfigGroup struct {
	pulumi.ResourceState

	Resources map[string]pulumi.Resource
}

// The set of arguments for constructing a ConfigGroup resource.
type ConfigGroupArgs struct {
	// Files is a set of paths, globs, or URLs that uniquely identify files.
	Files []string
	// YAML is list of strings containing Kubernetes resource definitions in YAML.
	YAML []string
	// Objs is a collection of object maps representing Kubernetes resources.
	Objs []map[string]interface{}
	// Transformations is an optional list of transformations to apply to Kubernetes resource definitions
	// before registering with the engine.
	Transformations []Transformation
	// ResourcePrefix is an optional prefix for the auto-generated resource names. For example, a resource named `bar`
	// created with resource prefix of `"foo"` would produce a resource named `"foo-bar"`.
	ResourcePrefix string
	// Skip await logic for all resources in this YAML. Resources will be marked ready as soon as they are created.
	// Warning: This option should not be used if you have resources depending on Outputs from the YAML.
	SkipAwait bool
}

// NewConfigGroup registers a new resource with the given unique name, arguments, and options.
func NewConfigGroup(ctx *pulumi.Context,
	name string, args *ConfigGroupArgs, opts ...pulumi.ResourceOption) (*ConfigGroup, error) {

	// Register the resulting resource state.
	configGroup := &ConfigGroup{
		Resources: map[string]pulumi.Resource{},
	}
	err := ctx.RegisterComponentResource("kubernetes:yaml:ConfigGroup", name, configGroup, opts...)
	if err != nil {
		return nil, err
	}

	// Now provision all child resources by parsing the YAML files.
	if args != nil {
		// Honor the resource name prefix if specified.
		if args.ResourcePrefix != "" {
			name = args.ResourcePrefix + "-" + name
		}

		// Parse and decode the YAML files.
		parseOpts := append(opts, pulumi.Parent(configGroup))
		rs, err := parseDecodeYamlFiles(ctx, args, true, parseOpts...)
		if err != nil {
			return nil, err
		}
		configGroup.Resources = rs
	}

	// Finally, register all of the resources found.
	err = ctx.RegisterResourceOutputs(configGroup, pulumi.Map{})
	if err != nil {
		return nil, errors.Wrapf(err, "registering child resources")
	}

	return configGroup, nil
}

// GetResource returns a resource defined by a built-in Kubernetes group/version/kind, name and namespace.
// For example, GetResource("v1/Pod", "foo", "") would return a Pod called "foo" from the "default" namespace.
func (cf *ConfigGroup) GetResource(gvk, name, namespace string) pulumi.Resource {
	id := name
	if len(namespace) > 0 && namespace != "default" {
		id = fmt.Sprintf("%s/%s", namespace, name)
	}
	key := fmt.Sprintf("%s::%s", gvk, id)
	return cf.Resources[key]
}
