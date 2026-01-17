from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Count, Q


from .forms import ContactForm,CommentForm
from .models import (Home, Home_job, About,Resume_experience,Resume_skill,
                     Resume_skill2,Resume_awards,Resume_education,
                     Service,Project,ProjectsList,Contact_me,Blog)


def home(request):

    home=Home.objects.filter(is_active=True)
    home_job=Home_job.objects.all()
    about=About.objects.filter(is_active=True)
    experience=Resume_experience.objects.filter(is_active=True)
    skill=Resume_skill.objects.filter(is_active=True)
    skill2=Resume_skill2.objects.filter(is_active=True)
    awards=Resume_awards.objects.filter(is_active=True)
    education=Resume_education.objects.filter(is_active=True)
    service=Service.objects.filter(is_active=True)
    project=Project.objects.all()
    projectslist=ProjectsList.objects.filter(is_active=True)
    contact_me=Contact_me.objects.filter(is_active=True)
    blogs=Blog.objects.filter(is_active=True).annotate(
        approved_comments_count=Count(
            'comments',
            filter=Q(comments__is_active=True)
        )
    )[::-1]
    page_title = home.first().page_title if home.exists() else "My Portfolio"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/#contact-section')
    context = {
        'home':home,
        'home_job':home_job,
        'about':about,
        'experience':experience,
        'skill':skill,
        'skill2':skill2,
        'awards':awards,
        'education':education,
        'service':service,
        'project':project,
        'projectslist':projectslist,
        'contact_me':contact_me,
        'form':form,
        'blogs':blogs,
        'page_title': page_title



    }

    return render(request,'index.html',context)






def BlogDetails(request, pk):
    home = Home.objects.filter(is_active=True)

    blog = get_object_or_404(Blog, pk=pk, is_active=True)

    comments = blog.comments.filter(is_active=True)
    page_title = home.first().page_title if home.exists() else "My Portfolio"
    form = CommentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.blog = blog
        new_comment.save()
        return redirect('blog detail', pk=blog.pk)

    ctx = {
        'home': home,
        'comments': comments,
        'form': form,
        'blog': blog,
        'page_title': page_title# bitta blog
    }
    return render(request, 'single.html', ctx)
