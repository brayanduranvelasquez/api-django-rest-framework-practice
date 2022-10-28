from rest_framework.viewsets import ModelViewSet
from .models import PersonModel
from .serializers import PersonSerializer

class PersonApiViewSet(ModelViewSet):
    serializer_class= PersonSerializer
    queryset= PersonModel.objects.all()
