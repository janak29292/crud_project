from django.urls import path
from .views import SchoolCreateAPIView, SchoolRetrieveAPIView, SchoolUpdateAPIView, SchoolDestroyAPIView, SchoolAutoComplete

app_name = 'crud'

urlpatterns = [
	path('new', SchoolCreateAPIView.as_view()),
	path('<int:pk>', SchoolRetrieveAPIView.as_view()),
	path('<int:pk>/update', SchoolUpdateAPIView.as_view()),
	path('<int:pk>/destroy', SchoolDestroyAPIView.as_view()),
	path('auto', SchoolAutoComplete.as_view()),
]
