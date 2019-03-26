
**Core Packages**
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly


**URL Tips**
snippets/
snippets<drf_format_suffix:format>
snippets/<int:pk>/
snippets/<int:pk><drf_format_suffix:format>
users/
users<drf_format_suffix:format>
users/<int:pk>/
users/<int:pk><drf_format_suffix:format>
api-auth/

**Learning Points**
Goal to learn: create permission for who can edit or read only. 
