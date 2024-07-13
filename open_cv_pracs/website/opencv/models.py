from django.db import models

class UploadingImg(models.Model):
    Plastic_types = (
        ('1', 'PE-C2'),
        ('2', 'PE-HD'),
        ('3', 'PE-LD'),
        ('4', 'PE-LLD'),
        ('5', 'PE-MD'),
        ('6', 'PE-UHMW'),
        ('7', 'PE-VLD'),
        ('8', 'PET'),
        ('9', 'PP'),
        ('10', 'PVC-C'),
        ('11', 'PVC-U'),
    )
    Visibility = (
        ('1', 'прозрачный'),
        ('2', 'полупрозрачный'),
        ('3', 'непрозрачный'),
    )
    Color_plastic = (
        ('1', 'синий'),
        ('2', 'зеленый'),
        ('3', 'коричневый'),
    )
    id_img = models.AutoField(primary_key=True)
    title_text_img = models.CharField(max_length=15, verbose_name='full name')
    img_file = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now=True)
    plastic_type = models.CharField(max_length=10, choices=Plastic_types, default=Plastic_types[7][0])
    visible = models.CharField(max_length=14, choices=Visibility, default=Visibility[1][0])
    color = models.CharField(max_length=10, choices=Color_plastic, null=True, default=Color_plastic[0][0])

    def __str__(self):
        return self.title_text_img
