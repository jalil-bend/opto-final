from django.urls import path
from . import views
from records import views as records_views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('print-credentials/', views.print_credentials, name='print_credentials'),
    path('researcher/register/', views.researcher_register, name='researcher_register'),
    path('professional/dashboard/', views.professional_dashboard, name='professional_dashboard'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('researcher/dashboard/', views.researcher_dashboard, name='researcher_dashboard'),
    path('discussions/', views.discussions_list, name='discussions_list'),
    path('discussions/<int:discussion_id>/', views.chat_view, name='chat_view'),
    path('discussions/create/<int:user_id>/', views.create_discussion, name='create_discussion'),
    path('generate-access-code/', views.generate_access_code, name='generate_access_code'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('patient/<int:patient_id>/', views.patient_profile, name='patient_profile'),
    path('patient/<int:patient_id>/records/', views.view_patient_records, name='view_records'),
    path('patient/<int:patient_id>/upload-record/', records_views.upload_record, name='upload_record_for_patient'),
    path('profile/', views.profile, name='profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('view-patient-records/', views.view_patient_records, name='view_patient_records'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/add-user/', views.add_user, name='add_user'),
    path('admin/manage-users/', views.manage_users, name='manage_users'),
    path('admin/user/<int:user_id>/', views.view_user, name='view_user'),
    path('admin/user/<int:user_id>/edit/', views.edit_user, name='edit_user'),
    path('admin/user/<int:user_id>/delete/', views.delete_user, name='delete_user'),
]