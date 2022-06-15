from django.contrib.sitemaps import Sitemap
#The sitemap is the structure of a webpage
#
from entrada.models import Entry

class EntrySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Entry.objects.filter(public=True)
    
    def lastmod(self,obj):
        return obj.created

class Sitemap(Sitemap):
    protocol = 'https'

    def __init__(self,names):
        self.names= names

    def items(self):
        return self.names
    
    def changefreq(self,obj):
        return 'weekly'