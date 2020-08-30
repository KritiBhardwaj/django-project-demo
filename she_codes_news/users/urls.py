from django.urls import path
from .views import CreateAccountView
from .views import ChangeAccountView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),name='createAccount'),
    # path('change-account/', ChangeAccountView.as_view(),name='changeAccount')
    path('<int:pk>/',ChangeAccountView.as_view(),name='changeAccount')
]