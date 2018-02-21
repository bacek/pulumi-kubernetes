PROJECT_NAME := Kubernetes Package
include build/common.mk

PACK             := kubernetes
PACKDIR          := pack
PROJECT          := github.com/pulumi/pulumi-kubernetes
NODE_MODULE_NAME := @pulumi/kubernetes

TFGEN           := pulumi-tfgen-${PACK}
PROVIDER        := pulumi-provider-${PACK}
VERSION         := $(shell git describe --tags --dirty 2>/dev/null)

GOMETALINTERBIN=gometalinter
GOMETALINTER=${GOMETALINTERBIN} --config=Gometalinter.json

TESTPARALLELISM := 10

build::
	go install -ldflags "-X github.com/pulumi/pulumi-kubernetes/pkg/version.Version=${VERSION}" ${PROJECT}/cmd/${TFGEN}
	go install -ldflags "-X github.com/pulumi/pulumi-kubernetes/pkg/version.Version=${VERSION}" ${PROJECT}/cmd/${PROVIDER}
	$(TFGEN) nodejs --out pack/
	cd ${PACKDIR} && yarn install
	cd ${PACKDIR} && yarn run tsc
	cp README.md LICENSE ${PACKDIR}/package.json ${PACKDIR}/yarn.lock ${PACKDIR}/bin/

lint::
	$(GOMETALINTER) ./cmd/... resources.go | sort ; exit "$${PIPESTATUS[0]}"

install::
	GOBIN=$(PULUMI_BIN) go install -ldflags "-X github.com/pulumi/pulumi-kubernetes/pkg/version.Version=${VERSION}" ${PROJECT}/cmd/${PROVIDER}
	[ ! -e "$(PULUMI_NODE_MODULES)/$(NODE_MODULE_NAME)" ] || rm -rf "$(PULUMI_NODE_MODULES)/$(NODE_MODULE_NAME)"
	mkdir -p "$(PULUMI_NODE_MODULES)/$(NODE_MODULE_NAME)"
	cp -r pack/bin/. "$(PULUMI_NODE_MODULES)/$(NODE_MODULE_NAME)"
	rm -rf "$(PULUMI_NODE_MODULES)/$(NODE_MODULE_NAME)/node_modules"
	cd "$(PULUMI_NODE_MODULES)/$(NODE_MODULE_NAME)" && \
	yarn install --offline --production && \
	(yarn unlink > /dev/null 2>&1 || true) && \
	yarn link

test_all::
	PATH=$(PULUMI_BIN):$(PATH) go test -v -cover -timeout 1h -parallel ${TESTPARALLELISM} ./examples

.PHONY: publish
publish:
	$(call STEP_MESSAGE)
	./scripts/publish.sh

# The travis_* targets are entrypoints for CI.
.PHONY: travis_cron travis_push travis_pull_request travis_api
travis_cron: all
travis_push: only_build publish only_test
travis_pull_request: all
travis_api: all
