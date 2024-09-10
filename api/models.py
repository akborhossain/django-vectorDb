from django.db import models

# Create your models here.
from pgvector.django import VectorField
from pgvector.django import HnswIndex, IvfflatIndex


class ProductVector(models.Model):
    productId=models.CharField(max_length=30, primary_key=True)
    productEmbeding = VectorField(dimensions=1536)
    productRelatedText=models.TextField(blank=True, null=True)
    class Meta:
        indexes = [
            HnswIndex(
                name='my_index',
                fields=['embedding'],
                m=32,
                ef_construction=128,
                opclasses=['vector_l2_ops']
            )
        ]
        
