from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl

from scripts.models.base import AccessInterface, Document


class ProviderV1(BaseModel):
    model_config = ConfigDict(extra="forbid")

    #
    # fields for business data collection and maintenance
    #
    schema_version: str = Field(
        default="provider_v1", description="Schema identifier", alias="schema"
    )
    time_created: datetime
    # how to automatically populate service data, if available
    services_populator: dict[str, Any] | None = None
    # parameters for accessing service provider, which typically
    # include "api_endpoint" and "api_key"
    provider_access_info: AccessInterface = Field(
        description="Dictionary of upstream access interface"
    )
    #
    # fields that will be stored in backend database
    #

    # name of the provider should be the same as directory name
    name: str

    # this field is added for convenience. It will be converted to
    # documents during importing.
    logo: str | HttpUrl | None = None

    # this field is added for convenience. It will be converted to
    # documents during importing.
    terms_of_service: None | str | HttpUrl = Field(
        default=None,
        description="Either a path to a .md file or a URL to terms of service",
    )

    documents: list[Document] | None = Field(
        default=None,
        description="List of documents associated with the provider (e.g. logo)",
    )
    #
    # fields for business operation purposes, not stored in backend database
    #

    # internal business data, usually not expose to users, and may not store
    # in database
    description: str | None = None
    homepage: HttpUrl
    contact_email: EmailStr
    secondary_contact_email: EmailStr | None = None
