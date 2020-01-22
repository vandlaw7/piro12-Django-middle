from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', lambda req: redirect('blog:post_list'), name='root'),  # URL Reverse
    path('accounts/', include('accounts.urls'))

]
