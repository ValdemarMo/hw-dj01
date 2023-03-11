from django.urls import path
from calculator.views import dish, home_view
# from calculator.views import hello, sum, pagi

urlpatterns = [
    path('', home_view, name = 'home'),
    path('<name>/', dish),
    # path('admin/', admin.site.urls),
    # path('sum/<int:a>/<int:b>/', sum),
    # path('hello/', hello),
    # path('pagi/', pagi),
    ]