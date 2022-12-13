from django.shortcuts import render

# TODO logging
def page_not_found_handler(request, exception=None):
    # logging.error("Wrong URL requested")
    return render(request, '../templates/errors/404.html', )


def custom_handler500(request):
    return render(request, '../templates/errors/500.html', )


def permission_denied_handler(request, exception=None):
    # logging.error("Wrong URL requested")
    return render(request, '../templates/errors/403.html', )


def csrf_failure(request, reason=""):
    # logging.error("Wrong URL requested")
    return render(request, '../templates/errors/403.html', )
