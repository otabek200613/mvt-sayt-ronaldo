from django.contrib import admin
from .models import (Home, Home_job, About, Resume_experience, Resume_skill, Resume_skill2,
                     Resume_awards, Resume_education, Service, Project, ProjectsList, Contact_me, Contact, Blog,
                     Comment,Footer)
@admin.register(Home)
class Home_admin(admin.ModelAdmin):
    list_display = ('name','is_active')
    list_filter = ('is_active',)
@admin.register(Resume_education)
class ResumeEducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'university', 'date', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('degree', 'university')
admin.site.register(Home_job)
admin.site.register(About)
admin.site.register(Resume_experience)
admin.site.register(Resume_skill)
admin.site.register(Resume_skill2)
admin.site.register(Resume_awards)
admin.site.register(Service)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['service','title']
admin.site.register(ProjectsList)
admin.site.register(Contact_me)
admin.site.register(Footer)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display =[ 'name',"updated_date",'is_read']
    list_filter = ['is_read','updated_date']
    search_fields = ['name','email']
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','is_active']
    list_editable = ['is_active']
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog','message','created','is_active']
    list_editable = ['is_active']

