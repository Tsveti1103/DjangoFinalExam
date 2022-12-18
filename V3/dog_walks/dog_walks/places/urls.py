from django.urls import path, include

from dog_walks.places.views import CretePlaceToEatView, CretePlaceToSleepView, CretePlaceToWalkView, \
    SleepPlacesListView, EatPlacesListView, WalkPlacesListView, NightEditView, NightDetailsView, EatDetailsView, \
    EatEditView, WalkDetailsView, WalkEditView

urlpatterns = (
    path('create_place_to_eat/', CretePlaceToEatView.as_view(), name='create place to eat'),
    path('create_place_to_sleep/', CretePlaceToSleepView.as_view(), name='create place to sleep'),
    path('create_place_to_walk/', CretePlaceToWalkView.as_view(), name='create place to walk'),
    path('places_to_sleep/', SleepPlacesListView.as_view(), name='all places to sleep'),
    path('places_to_eat/', EatPlacesListView.as_view(), name='all places to eat'),
    path('places_to_walk/', WalkPlacesListView.as_view(), name='all places to walk'),
    path('night/<int:pk>/', include([
        path('edit/', NightEditView.as_view(), name='edit night'),
        path('details/', NightDetailsView.as_view(), name='details night'),

    ])),
    path('eat/<int:pk>/', include([
        path('edit/', EatEditView.as_view(), name='edit eat'),
        path('details/', EatDetailsView.as_view(), name='details eat'),

    ])),
    path('walk/<int:pk>/', include([
        path('edit/', WalkEditView.as_view(), name='edit walk'),
        path('details/', WalkDetailsView.as_view(), name='details walk'),
    ])),

)
