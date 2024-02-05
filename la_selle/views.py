from django.shortcuts import render


def custom_404(request, exception):
    """
    returns custom 404 page
    """
    return render(request, '404.html', status=404)
