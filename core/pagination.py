from rest_framework.pagination import PageNumberPagination


class SmallPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'
    max_page_size = 50


class StandardPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    max_page_size = 50


class LargePageNumberPagination(PageNumberPagination):
    page_size = 15
    page_query_param = 'page'
    max_page_size = 50
