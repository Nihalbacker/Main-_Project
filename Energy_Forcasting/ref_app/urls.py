from django.urls import path

from ref_app import views

urlpatterns = [
    path('',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('addsup',views.addsup,name='addsup'),
    path('login_post',views.login_post,name='login_post'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('assignsup',views.assignsup,name='assignsup'),
    path('assignworktosup',views.assignworktosup,name='assignworktosup'),
    path('editassignworkstosup/<int:id>',views.editassignworkstosup,name='editassignworkstosup'),
    path('editassignworkstosuppost',views.editassignworkstosuppost,name='editassignworkstosuppost'),
    path('deleteassignworkstosup/<int:id>',views.deleteassignworkstosup,name='deleteassignworkstosup'),
    path('assigningworktosup',views.assigningworktosup,name='assigningworktosup'),
    path('supviewandassignworksearch',views.supviewandassignworksearch,name='supviewandassignworksearch'),
    path('editsupervsr/<int:id>',views.editsupervsr,name='editsupervsr'),
    path('searchsup',views.searchsup,name='searchsup'),
    path('deletesup/<int:id>',views.deletesup,name='deletesup'),
    path('editsuppost',views.editsuppost,name='editsuppost'),
    path('editworkstosup',views.editworkstosup,name='editworkstosup'),
    path('mngsupervsr',views.mngsupervsr,name='mngsupervsr'),
    path('addsuppost',views.addsuppost,name='addsuppost'),
    path('Verifyworker',views.Verifyworker,name='Verifyworker'),
    path('acceptworker/<int:id>',views.acceptworker,name='acceptworker'),
    path('rejectworker/<int:id>',views.rejectworker,name='rejectworker'),
    path('verifyworkersearch',views.verifyworkersearch,name='verifyworkersearch'),
    path('viewcomplandsendreply',views.viewcomplandsendreply,name='viewcomplandsendreply'),
    path('adminsendreply_post',views.adminsendreply_post,name='adminsendreply_post'),
    path('adminsendreply/<int:id>',views.adminsendreply,name='adminsendreply'),
    path('viewfeedbck',views.viewfeedbck,name='viewfeedbck'),
    path('viewfeedback_search',views.viewfeedback_search,name='viewfeedback_search'),
    path('viewresources',views.viewresources,name='viewresources'),
    path('viewworkstatus',views.viewworkstatus,name='viewworkstatus'),
    path('addresourc',views.addresourc,name='addresourc'),
    path('assignworks',views.assignworks,name='assignworks'),
    path('assignworkstoworker_post',views.assignworkstoworker_post,name='assignworkstoworker_post'),
    path('supviewandassignwork',views.supviewandassignwork,name='supviewandassignwork'),
    path('viewsup_updatestatus/<int:id>',views.viewsup_updatestatus,name='viewsup_updatestatus'),
    # path('updatestatus/<int:id>',views.updatestatus,name='updatestatus'),
    path('updatedstatus',views.updatedstatus,name='updatedstatus'),
    path('editresourc',views.editresourc,name='editresourc'),
    path('mngresources',views.mngresources,name='mngresources'),
    path('sendcomplaint',views.sendcomplaint,name='sendcomplaint'),
    path('sendcoomplaintandviewreply',views.sendcoomplaintandviewreply,name='sendcoomplaintandviewreply'),
    path('sendcomplaint_post',views.sendcomplaint_post,name='sendcomplaint_post'),
    path('sendreply',views.sendreply,name='sendreply'),
    path('sendreplyfordoubt',views.sendreplyfordoubt,name='sendreplyfordoubt'),
    # path('updatestatus',views.updatestatus,name='updatestatus'),
    path('updateworkstatus',views.updateworkstatus,name='updateworkstatus'),
    path('viewcomplaintandsendreply',views.viewcomplaintandsendreply,name='viewcomplaintandsendreply'),
    path('viewcomplandsendreply_search',views.viewcomplandsendreply_search,name='viewcomplandsendreply_search'),
    path('viewdoubtandsendreply',views.viewdoubtandsendreply,name='viewdoubtandsendreply'),
    path('suphome',views.suphome,name='suphome'),
    path('addres',views.addres,name='addres'),
    path('editres/<int:id>',views.editres,name='editres'),
    path('deleteres/<int:id>',views.deleteres,name='deleteres'),
    path('edittaddres',views.edittaddres,name='edittaddres'),
    path('mngresources_search',views.mngresources_search,name='mngresources_search'),
    path('viewresourcessearch',views.viewresourcessearch,name='viewresourcessearch  '),
    path('assignworkstoworker/<assinid>', views.assignworkstoworker, name='assignworkstoworker  '),
    path('viewassignedworkstoworker/<int:id>', views.viewassignedworkstoworker, name='viewassignedworkstoworker'),
    path('viewassignedworkstoworker_search', views.viewassignedworkstoworker_search, name='viewassignedworkstoworker_search'),
    path('forecasting', views.forecasting, name='forecasting'),
    path('forecasting_post', views.forecasting_post, name='forecasting_post'),
    path('viewptr_slr', views.viewptr_slr, name='viewptr_slr'),
    path('viewptr_wnd', views.viewptr_wnd, name='viewptr_wnd'),

    path('chatwithuser', views.chatwithuser, name='chatwithuser'),
    path('chatview', views.chatview, name='chatview'),
    path('coun_msg/<int:id>', views.coun_msg, name='coun_msg'),
    path('coun_insert_chat/<str:msg>/<int:id>', views.coun_insert_chat, name='coun_insert_chat'),

    path('login_code', views.login_code, name='login_code'),
    path('registration', views.registration, name='registration'),
    path('chatwithuser1', views.chatwithuser1, name='chatwithuser1'),
    path('chatview1', views.chatview1, name='chatview1'),
    path('coun_msg1/<int:id>', views.coun_msg1, name='coun_msg1'),
    path('coun_insert_chat1/<str:msg>/<int:id>', views.coun_insert_chat1, name='coun_insert_chat1'),
    path('viewassignedwork_worker', views.viewassignedwork_worker, name='viewassignedwork_worker'),
    path('updatestatusandroid', views.updatestatusandroid, name='updatestatusandroid'),
    path('send_complaints', views.send_complaints, name='send_complaints'),
    path('viewcomplaint', views.viewcomplaint, name='viewcomplaint'),



    path('chatwithworker', views.chatwithworker, name='chatwithworker'),
    path('chatview2', views.chatview2, name='chatview2'),
    path('coun_msg2/<int:id>', views.coun_msg2, name='coun_msg2'),
    path('coun_insert_chat2/<str:msg>/<int:id>', views.coun_insert_chat, name='coun_insert_chat'),

    path('viewworkercomplaintandsendreply', views.viewworkercomplaintandsendreply, name='viewworkercomplaintandsendreply'),
    path('viewworkercomplaintandsendreply_search', views.viewworkercomplaintandsendreply_search, name='viewworkercomplaintandsendreply_search   '),
    path('sendreply/<id>', views.sendreply, name='sendreply'),
    path('sendreply_post', views.sendreply_post, name='sendreply_post'),
    path('resrs', views.resrs, name='resrs'),
    path('send_fbk', views.send_fbk, name='send_fbk'),
    path('send_sup_complaints', views.send_sup_complaints, name='send_sup_complaints'),
    path('view_sup_complaint', views.view_sup_complaint, name='view_sup_complaint'),
    path('viewsupervisor', views.viewsupervisor, name='viewsupervisor'),
    path('viewsupervisorchat', views.viewsupervisorchat, name='viewsupervisorchat'),
    path('view_message2', views.view_message2, name='view_message2'),
    path('in_message2', views.in_message2, name='in_message2'),







        ]