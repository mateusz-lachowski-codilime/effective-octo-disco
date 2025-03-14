"""
URL configuration for test_graphene project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
import strawberry
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from graphene_django.views import GraphQLView
from strawberry.django.views import GraphQLView as StrawberryGraphQLView

from testapp.schema import schema
from testapp.strawberry_schema import strawberry_schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
    path("graphql2/", StrawberryGraphQLView.as_view(schema=strawberry_schema)),
    path('__debug__/', include(debug_toolbar.urls)),
    path('api/', include('testapp.urls')),
]
