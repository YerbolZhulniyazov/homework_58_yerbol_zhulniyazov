from django.urls import path
from webapp.views.base import IndexView
from webapp.views.issues import (
    AddView, DetailView, UpdateView,
    DeleteView, ConfirmDelete,
)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/<int:pk>/', DetailView.as_view(), name='detail_view'),
    path('issues/add', AddView.as_view(), name='add_view'),
    path('issue/<int:pk>/update/', UpdateView.as_view(), name='issue_update'),
    path('issue/<int:pk>/delete/', DeleteView.as_view(), name='issue_delete'),
    path('issue/<int:pk>/confirm_delete/', ConfirmDelete.as_view(), name='confirm_delete')
]
