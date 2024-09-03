from django.urls import path

from myapp import admin, views

urlpatterns = [
    path('admin_log/',views.admin_log),
    path('company/',views.company),
    path('view_company/',views.view_company),
    path('services/',views.services),
    path('admin_home/',views.admin_home),
    path('view_service/',views.view_service),
    path('edit_service/<id>',views.edit_service),
    path('view_edview/',views.view_edview),
    path('delete/<id>',views.delete),
    path('manage_gallery/',views.manage_gallery),
    path('view_gallery/',views.view_gallery),
    path('edit_gallery/<id>',views.edit_gallery),
    path('view_galEdit/',views.view_galEdit),
    path('gal_delete/<id>',views.gal_delete),
    path('register/',views.Register1),
    path('user_home/',views.user_home),
    path('view_prof/',views.view_prof),
    path('edit_prf/<id>',views.edit_prf),
    path('vw_prf_ed/',views.vw_prf_ed),
    path('admn_vw_usr/',views.admn_vw_usr),
    path('explore_ser/',views.explore_ser),
    path('request/<id>',views.request),
    path('approve/<id>',views.approve),
    path('Reject/<id>',views.Reject),
    path('admn_vw_request/',views.admn_vw_request),
    path('ad_viw_apprvd_reqst/',views.ad_viw_apprvd_reqst),
    path('usr_vw_aprv_sts/',views.usr_vw_aprv_sts),
    path('usr_vw_rjct_sts/',views.usr_vw_rjct_sts),
    path('comp/',views.comp),
    path('compost/',views.compost),
    path('vw_comp/',views.vw_comp),
    path('sendReply/<id>',views.sendReply),
    path('sndReplypost/',views.sndReplypost),
    path('reply/',views.reply),
    path('chng_pass/',views.chng_pass),
    path('chngepass/',views.chngepass),
    path('usr_pass/',views.usr_pass),
    path('us_chngepass/',views.us_chngepass),
    path('payment/<id>',views.payment1),
    path('admn_vw_pymnt/',views.admn_vw_pymnt),
    path('land/',views.land),
    path('emilchnge/',views.emilchnge),
    path('phnchnge/',views.phnchnge),
    path('logout/',views.logout),




]
