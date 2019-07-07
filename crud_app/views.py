from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from dal import autocomplete
from .models import School
from .serializers import SchoolSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class SchoolCreateAPIView(CreateAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer


class SchoolRetrieveAPIView(RetrieveAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer

class SchoolUpdateAPIView(UpdateAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer

class SchoolDestroyAPIView(DestroyAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer

class SchoolAutoComplete(autocomplete.Select2QuerySetView, APIView):

	def get_queryset(self):

		qs=School.objects.all()
		if self.q:
			qs = qs.filter(name__istartswith=self.q)

		return qs

	def render_to_response(self, context):
		"""Return a JSON response in Select2 format."""
		q = self.request.GET.get('q', None)

		create_option = self.get_create_option(context, q)

		return Response(
			{
				'results': self.get_results(context) + create_option,
				'pagination': {
					'more': self.has_more(context)
				}
			})

class HelloView(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		content = {'message': 'Hello, World!'}
		return Response(content)
