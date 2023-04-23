from django.urls import path
from django.contrib import admin
from blog.views import Generic_Post_List, Generic_Update_Post_List, Create_List_Retrieve_View_Set, Comment_List_Create_View

urlpatterns = [
   path("generic_API",Generic_Post_List.as_view()),
   path("update_posts/<int:pk>",Generic_Update_Post_List.as_view(), {'http_method': 'PUT'}),
   path('delete_posts/<int:pk>/delete/', Generic_Update_Post_List.as_view(), {'http_method': 'DELETE'}),
   path('test/',Create_List_RetrievE_View_Set.as_view({'get':"list",'post':'create'})),
   path('comments_On_post',Comment_List_Create_View.as_view()),
]
