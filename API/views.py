from django.shortcuts import render
from classes.models import Classroom
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)

from .serializers import (
	CreateSerializer,
	ClassroomListSerializer,
	ClassroomDetailSerializer,
	ClassroomCreateUpdateSerializer,

	)

class ClassroomListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer



class ClassroomDetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'



class ClassroomCreateView(CreateAPIView):
     serializer_class = CreateSerializer
     def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class ClassroomUpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


class ClassroomDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'




