from django.db import models
from product.models import Gold

# Create your models here.
class Photo(models.Model):
	main_image=models.ImageField(upload_to="media/earrings")


class earring_code(models.Model):
	jewel_code=models.CharField(max_length=20)
	jewel_name=models.CharField(max_length=40)
	photos=models.ForeignKey(Photo) 
    # def __str__(self):
    # 	return self.jewel_code

class diamond_earring(models.Model):
#------------------------------------------------Not included kt option here.We will put a filter on 18k,14k
	jewel_code=models.ForeignKey(earring_code)
	gold_wt_grams=models.DecimalField(decimal_places=3,max_digits=7)
	gross_wt_gm=models.DecimalField(decimal_places=3,max_digits=7)
	stones_price=models.IntegerField(blank=True)
	stone_string_price=models.IntegerField(blank=True)
	making_price=models.IntegerField()#If 2 digits then percentage else it is the amt in rupees
	diamond_price=models.IntegerField()
	diamond_weight_carats=models.DecimalField(decimal_places=3,max_digits=7)

class gold_and_stone_earring(models.Model):
#--------------------------------------------------Not included kt option here.We will put a filter on 22k,18k,14k
	jewel_code=models.ForeignKey(earring_code)
	gold_wt_grams=models.DecimalField(decimal_places=3,max_digits=7)
	gross_wt_gm=models.DecimalField(decimal_places=3,max_digits=7)
	stones_price=models.IntegerField(blank=True)
	stone_string_price=models.IntegerField(blank=True)
	making_price=models.IntegerField()#If 2 digits then percentage else it is the amt in rupees

class kundan_earring(models.Model):
#-----------------------------------------------------------Not included kt option here.No filter.Only 22k		
    jewel_code=models.ForeignKey(earring_code)
    gold_wt_grams=models.DecimalField(decimal_places=3,max_digits=7)
    gross_wt_gm=models.DecimalField(decimal_places=3,max_digits=7)
    stones_price=models.IntegerField(blank=True)
    stone_string_price=models.IntegerField(blank=True)
    making_price=models.IntegerField()
    #amt in rupees

class polki_earring(models.Model):
#------------------------------------------------------------Not included kt option here.No filter.Only 22k		    
    jewel_code=models.ForeignKey(earring_code)
    gold_wt_grams=models.DecimalField(decimal_places=3,max_digits=7)
    gross_wt_gm=models.DecimalField(decimal_places=3,max_digits=7)
    stones_price=models.IntegerField(blank=True)
    stone_string_price=models.IntegerField(blank=True)
    making_price=models.IntegerField()#amt in rupees	
    uncut_diamond_wt=models.DecimalField(decimal_places=3,max_digits=7)
    uncut_diamond_price=models.IntegerField()


     
		