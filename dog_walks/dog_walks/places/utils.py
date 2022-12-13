from django.core.paginator import Paginator


def get_pacinator(request, set, obj_paginate_by, order_by):
    def get_comments_page():
        return request.GET.get('page', 1)

    def get_paginated_comments():
        page = get_comments_page()
        comments = set \
            .order_by(order_by)

        paginator = Paginator(comments, obj_paginate_by)
        return paginator.get_page(page)

    return get_paginated_comments
