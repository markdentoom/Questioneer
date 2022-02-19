from collections import OrderedDict
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PageNumberPaginationNoCount(PageNumberPagination):
    """Just get PageNumberPagination, but remove count from get_paginated_response"""

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("results", data),
                ]
            )
        )
