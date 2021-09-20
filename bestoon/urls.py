from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('expense/', views.ExpenseList.as_view()),
    path('income/', views.IncomeList.as_view()),
]