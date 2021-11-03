from django.urls import URLResolver
from django.urls.resolvers import URLPattern
from django.utils.deprecation import MiddlewareMixin

from test_app.constants import MIDDLEWARE_KEY


class RoutingMiddleware(MiddlewareMixin):
    def get_matched_middleware(self, request):
        try:
            resolver_match = request.resolver_match
        except AttributeError:
            return []

        matched_middleware = []
        for match in resolver_match.tried[-1]:
            middleware = None
            if isinstance(match, URLPattern):
                middleware = match.default_args.get(MIDDLEWARE_KEY)
            elif isinstance(match, URLResolver):
                middleware = match.default_kwargs.get(MIDDLEWARE_KEY)

            if not middleware:
                continue

            matched_middleware.append(middleware)

        return matched_middleware

    def process_view(self, request, view_func, view_args, view_kwargs):
        view_kwargs.pop(MIDDLEWARE_KEY, None)
        matched_middleware = self.get_matched_middleware(request)
        for middleware in matched_middleware:
            response = middleware(request, view_func, view_args, view_kwargs)
            if response:
                return response
