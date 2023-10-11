from abc import ABC, abstractmethod

from adrf.views import APIView
from rest_framework.generics import (
    RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
)


class BaseView(APIView, ABC):
    """Abstract base class for all API views."""


class BaseReadView(BaseView, RetrieveAPIView):
    """Abstract base class for all read API views."""

    @abstractmethod
    async def get(self, request, *args, **kwargs):
        """Abstract method for all read API views."""


class BaseCreateView(BaseView, CreateAPIView):
    """Abstract base class for all create API views."""

    @abstractmethod
    async def post(self, request, *args, **kwargs):
        """Abstract method for all create API views."""


class BaseDeleteView(BaseView, DestroyAPIView):
    """Abstract base class for all delete API views."""

    @abstractmethod
    async def delete(self, request, *args, **kwargs):
        """Abstract method for all delete API views."""


class BaseUpdateView(BaseView, UpdateAPIView):
    """Abstract base class for all update API views."""

    @abstractmethod
    async def put(self, request, *args, **kwargs):
        """Abstract method for all update API views."""
