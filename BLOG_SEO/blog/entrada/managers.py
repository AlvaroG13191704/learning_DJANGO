from django.db import models

class EntryManager(models.Manager):
    #Entry procediments
    def entrada_en_portada(self):
        return self.filter(
            public = True,
            portada = True,
        ).order_by('-created').first()

    #return the last 4 entries
    def entradas_en_homes(self):
        return self.filter(
            public = True,
            in_home = True
        ).order_by('-created')[:4]
    
    #return the last 6 entries recently
    def entradas_recientes(self):
        return self.filter(
            public = True,
            in_home = True
        ).order_by('-created')[:6]

    def buscar_entrada(self,kword,categoria):
        if len(categoria):
            return self.filter(
                category__short_name=categoria,
                title__icontains=kword,
                public = True
            ).order_by('-created')
        else:
            return self.filter(
                title__icontains=kword,
                public=True
            ).order_by('-created')