from django.forms import Form
from .models import Post, Autor

class Post_Create(Form):
    class Meta:
        model = Post
        fiels = ('__all__')