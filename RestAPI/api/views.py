from .models import Artcile
from .serializers import ArticleSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
# Create your views here.

def home(request):
    art = Artcile.objects.get(id=1)
    print("******1",art,"********")
    serializer = ArticleSerializer(art)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = "application/json")



