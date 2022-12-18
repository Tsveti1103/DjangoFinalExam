from django.urls import path, include
from dog_walks.common.views import index, map_page, like_night, CreteNightCommentView, like_eat, \
    CreteEatCommentView, like_walk, CreteWalkCommentView, want_to_visit_night, want_to_visit_eat, \
    want_to_visit_walk, CreateNightReportView, SearchResultsView, CreateEatReportView, CreateWalkReportView, AboutUs, \
    ContactUsView, TermsAndConditions, share

urlpatterns = (
    path('', index, name='index'),
    path('about_us/', AboutUs.as_view(), name='about us'),
    path('contact_us/', ContactUsView.as_view(), name='contact us'),
    path('terms-and-conditions/', TermsAndConditions.as_view(), name='terms and conditions'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path('map/', map_page, name='map'),
    path('share/', share, name='share'),
    path('night/<int:pk>/', include([
        path('like/', like_night, name='like night'),
        path('want_to_visit/', want_to_visit_night, name='want to visit night'),
        path('comment/', CreteNightCommentView.as_view(), name='comment night'),
        path('report/', CreateNightReportView.as_view(), name='report night'),
    ])),
    path('eat/<int:pk>/', include([
        path('like/', like_eat, name='like eat'),
        path('want_to_visit/', want_to_visit_eat, name='want to visit eat'),
        path('comment/', CreteEatCommentView.as_view(), name='comment eat'),
        path('report/', CreateEatReportView.as_view(), name='report eat'),

    ])),
    path('walk/<int:pk>/', include([
        path('like/', like_walk, name='like walk'),
        path('want_to_visit/', want_to_visit_walk, name='want to visit walk'),
        path('comment/', CreteWalkCommentView.as_view(), name='comment walk'),
        path('report/', CreateWalkReportView.as_view(), name='report walk'),

    ])),
)
