from django.urls import resolve, Resolver404, URLResolver
from django.urls.resolvers import URLPattern
from django.utils.deprecation import MiddlewareMixin


class URLMiddleware(MiddlewareMixin):
    def get_matched_middleware(self, path, middleware_method):
        try:
            resolver_match = resolve(path)
        except Resolver404:
            return []

        matched_middleware = []
        for match in resolver_match.tried[-1]:
            middleware_class = None
            if isinstance(match, URLPattern):
                middleware_class = match.default_args.get('middleware')
            elif isinstance(match, URLResolver):
                middleware_class = match.default_kwargs.get('middleware')

            if not middleware_class:
                continue

            middleware_instance = middleware_class()
            if hasattr(middleware_instance, middleware_method):
                matched_middleware.append(middleware_instance)

        return matched_middleware

    def process_view(self, request, view_func, view_args, view_kwargs):
        matched_middleware = self.get_matched_middleware(request.path, 'process_view')
        for middleware in matched_middleware:
            response = middleware.process_view(request, view_func, view_args, view_kwargs)
            if response:
                return response
