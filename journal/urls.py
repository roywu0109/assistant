from django.urls import path
from .views import JournalList, JournalCreate, JournalUpdate, JournalDelete

urlpatterns = [
    path('', JournalList.as_view()), 
    path('create/', JournalCreate.as_view(),name="journal_list"),
    path('<int:pk>/update/', JournalUpdate.as_view(),name="journal_create"), 
    path('<int:pk>/delete/', JournalDelete.as_view()),
]