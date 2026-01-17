from .models import Footer,About

def global_footer(request):
    return {
        'footer_items': Footer.objects.filter(is_active=True),
        'about': About.objects.filter(is_active=True),
    }
