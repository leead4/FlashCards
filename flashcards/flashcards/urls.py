from django.conf.urls import url, include
from rest_framework import routers
from cardsAPI import views
from cardsAPI.views import FileUploadView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'documents', views.DocumentViewSet)
router.register(r'decks', views.DeckViewSet)
router.register(r'cards', views.CardViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^upload/', FileUploadView.as_view())
    

]

