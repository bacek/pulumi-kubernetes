# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'BoundObjectReferencePatchArgs',
    'BoundObjectReferenceArgs',
    'TokenRequestSpecPatchArgs',
    'TokenRequestSpecArgs',
    'TokenReviewSpecPatchArgs',
    'TokenReviewSpecArgs',
]

@pulumi.input_type
class BoundObjectReferencePatchArgs:
    def __init__(__self__, *,
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 uid: Optional[pulumi.Input[str]] = None):
        """
        BoundObjectReference is a reference to an object that a token is bound to.
        :param pulumi.Input[str] api_version: API version of the referent.
        :param pulumi.Input[str] kind: Kind of the referent. Valid kinds are 'Pod' and 'Secret'.
        :param pulumi.Input[str] name: Name of the referent.
        :param pulumi.Input[str] uid: UID of the referent.
        """
        if api_version is not None:
            pulumi.set(__self__, "api_version", api_version)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if uid is not None:
            pulumi.set(__self__, "uid", uid)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[str]]:
        """
        API version of the referent.
        """
        return pulumi.get(self, "api_version")

    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_version", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of the referent. Valid kinds are 'Pod' and 'Secret'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the referent.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[str]]:
        """
        UID of the referent.
        """
        return pulumi.get(self, "uid")

    @uid.setter
    def uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uid", value)


@pulumi.input_type
class BoundObjectReferenceArgs:
    def __init__(__self__, *,
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 uid: Optional[pulumi.Input[str]] = None):
        """
        BoundObjectReference is a reference to an object that a token is bound to.
        :param pulumi.Input[str] api_version: API version of the referent.
        :param pulumi.Input[str] kind: Kind of the referent. Valid kinds are 'Pod' and 'Secret'.
        :param pulumi.Input[str] name: Name of the referent.
        :param pulumi.Input[str] uid: UID of the referent.
        """
        if api_version is not None:
            pulumi.set(__self__, "api_version", api_version)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if uid is not None:
            pulumi.set(__self__, "uid", uid)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[str]]:
        """
        API version of the referent.
        """
        return pulumi.get(self, "api_version")

    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_version", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of the referent. Valid kinds are 'Pod' and 'Secret'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the referent.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[str]]:
        """
        UID of the referent.
        """
        return pulumi.get(self, "uid")

    @uid.setter
    def uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uid", value)


@pulumi.input_type
class TokenRequestSpecPatchArgs:
    def __init__(__self__, *,
                 audiences: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 bound_object_ref: Optional[pulumi.Input['BoundObjectReferencePatchArgs']] = None,
                 expiration_seconds: Optional[pulumi.Input[int]] = None):
        """
        TokenRequestSpec contains client provided parameters of a token request.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] audiences: Audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences.
        :param pulumi.Input['BoundObjectReferencePatchArgs'] bound_object_ref: BoundObjectRef is a reference to an object that the token will be bound to. The token will only be valid for as long as the bound object exists. NOTE: The API server's TokenReview endpoint will validate the BoundObjectRef, but other audiences may not. Keep ExpirationSeconds small if you want prompt revocation.
        :param pulumi.Input[int] expiration_seconds: ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response.
        """
        if audiences is not None:
            pulumi.set(__self__, "audiences", audiences)
        if bound_object_ref is not None:
            pulumi.set(__self__, "bound_object_ref", bound_object_ref)
        if expiration_seconds is not None:
            pulumi.set(__self__, "expiration_seconds", expiration_seconds)

    @property
    @pulumi.getter
    def audiences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences.
        """
        return pulumi.get(self, "audiences")

    @audiences.setter
    def audiences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "audiences", value)

    @property
    @pulumi.getter(name="boundObjectRef")
    def bound_object_ref(self) -> Optional[pulumi.Input['BoundObjectReferencePatchArgs']]:
        """
        BoundObjectRef is a reference to an object that the token will be bound to. The token will only be valid for as long as the bound object exists. NOTE: The API server's TokenReview endpoint will validate the BoundObjectRef, but other audiences may not. Keep ExpirationSeconds small if you want prompt revocation.
        """
        return pulumi.get(self, "bound_object_ref")

    @bound_object_ref.setter
    def bound_object_ref(self, value: Optional[pulumi.Input['BoundObjectReferencePatchArgs']]):
        pulumi.set(self, "bound_object_ref", value)

    @property
    @pulumi.getter(name="expirationSeconds")
    def expiration_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response.
        """
        return pulumi.get(self, "expiration_seconds")

    @expiration_seconds.setter
    def expiration_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "expiration_seconds", value)


@pulumi.input_type
class TokenRequestSpecArgs:
    def __init__(__self__, *,
                 audiences: pulumi.Input[Sequence[pulumi.Input[str]]],
                 bound_object_ref: Optional[pulumi.Input['BoundObjectReferenceArgs']] = None,
                 expiration_seconds: Optional[pulumi.Input[int]] = None):
        """
        TokenRequestSpec contains client provided parameters of a token request.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] audiences: Audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences.
        :param pulumi.Input['BoundObjectReferenceArgs'] bound_object_ref: BoundObjectRef is a reference to an object that the token will be bound to. The token will only be valid for as long as the bound object exists. NOTE: The API server's TokenReview endpoint will validate the BoundObjectRef, but other audiences may not. Keep ExpirationSeconds small if you want prompt revocation.
        :param pulumi.Input[int] expiration_seconds: ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response.
        """
        pulumi.set(__self__, "audiences", audiences)
        if bound_object_ref is not None:
            pulumi.set(__self__, "bound_object_ref", bound_object_ref)
        if expiration_seconds is not None:
            pulumi.set(__self__, "expiration_seconds", expiration_seconds)

    @property
    @pulumi.getter
    def audiences(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences.
        """
        return pulumi.get(self, "audiences")

    @audiences.setter
    def audiences(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "audiences", value)

    @property
    @pulumi.getter(name="boundObjectRef")
    def bound_object_ref(self) -> Optional[pulumi.Input['BoundObjectReferenceArgs']]:
        """
        BoundObjectRef is a reference to an object that the token will be bound to. The token will only be valid for as long as the bound object exists. NOTE: The API server's TokenReview endpoint will validate the BoundObjectRef, but other audiences may not. Keep ExpirationSeconds small if you want prompt revocation.
        """
        return pulumi.get(self, "bound_object_ref")

    @bound_object_ref.setter
    def bound_object_ref(self, value: Optional[pulumi.Input['BoundObjectReferenceArgs']]):
        pulumi.set(self, "bound_object_ref", value)

    @property
    @pulumi.getter(name="expirationSeconds")
    def expiration_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response.
        """
        return pulumi.get(self, "expiration_seconds")

    @expiration_seconds.setter
    def expiration_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "expiration_seconds", value)


@pulumi.input_type
class TokenReviewSpecPatchArgs:
    def __init__(__self__, *,
                 audiences: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 token: Optional[pulumi.Input[str]] = None):
        """
        TokenReviewSpec is a description of the token authentication request.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] audiences: Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver.
        :param pulumi.Input[str] token: Token is the opaque bearer token.
        """
        if audiences is not None:
            pulumi.set(__self__, "audiences", audiences)
        if token is not None:
            pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter
    def audiences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver.
        """
        return pulumi.get(self, "audiences")

    @audiences.setter
    def audiences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "audiences", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        Token is the opaque bearer token.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)


@pulumi.input_type
class TokenReviewSpecArgs:
    def __init__(__self__, *,
                 audiences: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 token: Optional[pulumi.Input[str]] = None):
        """
        TokenReviewSpec is a description of the token authentication request.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] audiences: Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver.
        :param pulumi.Input[str] token: Token is the opaque bearer token.
        """
        if audiences is not None:
            pulumi.set(__self__, "audiences", audiences)
        if token is not None:
            pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter
    def audiences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver.
        """
        return pulumi.get(self, "audiences")

    @audiences.setter
    def audiences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "audiences", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        Token is the opaque bearer token.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)


