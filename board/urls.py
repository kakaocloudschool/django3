from django.contrib import admin
from django.urls import path, include
import board.views
import user.views

from django.contrib.auth import views as auth_views