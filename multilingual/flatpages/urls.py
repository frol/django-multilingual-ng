try:
    from django.conf.urls import patterns
except ImportError:
    from django.conf.urls.defaults import patterns # Django < 1.4

urlpatterns = patterns('multilingual.flatpages.views',
    (r'^(?P<url>.*)$', 'multilingual_flatpage'),
)
