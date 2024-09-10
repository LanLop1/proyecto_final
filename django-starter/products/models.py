from django.db import models
from django.utils import timezone
from stores.models import Store
from a_home.models import Image

class Product(models.Model):
    CATEGORY_CHOICES = [
    ('SIN', 'Sin categoría'),
    ('LIB', 'Libros'),
    ('TEC', 'Tecnología'),
    ('JAR', 'Jardinería'),
    ('ROP', 'Ropa'),
    ('HOG', 'Hogar'),
    ('ELE', 'Electrónicos'),
    ('DEP', 'Deportes'),
    ('JUG', 'Juguetes'),
    ('ORD', 'Ordenadores y Accesorios'),
    ('MOV', 'Móviles y Accesorios'),
    ('COS', 'Cosmética y Belleza'),
    ('SAL', 'Salud y Cuidado Personal'),
    ('ALM', 'Alimentos y Bebidas'),
    ('BEB', 'Bebés y Niños'),
    ('AUT', 'Automóviles y Motocicletas'),
    ('MUS', 'Música e Instrumentos Musicales'),
    ('VID', 'Videojuegos'),
    ('PEL', 'Películas y Series'),
    ('MAS', 'Mascotas y Animales'),
    ('OFI', 'Oficina y Papelería'),
    ('HERR', 'Herramientas y Mejoras del Hogar'),
    ('CAL', 'Calzado'),
    ('REC', 'Recreación al Aire Libre'),
    ('JOY', 'Joyas y Relojes'),
    ('VIA', 'Viajes y Equipaje'),
    ('ART', 'Arte y Manualidades'),
    ('JUE', 'Juegos de Mesa y Puzzles'),
    # Añade más categorías según sea necesario
]

    store = models.ForeignKey(Store, on_delete=models.CASCADE , related_name='store', null=False)
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(max_length=1255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    stockquantity = models.IntegerField(null=False)
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES, default='SIN')
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True, related_name='product_images')
    createdat = models.DateTimeField(default=timezone.now)
    updatedat = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return f"Product name, price, store and stock: {self.name, self.price, self.store, self.stockquantity}"
