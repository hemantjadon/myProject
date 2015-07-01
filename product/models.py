from django.db import models

# Create your models here.
class Gold(models.Model):
	karat=models.IntegerField(unique=True)
	price_per_gram=models.IntegerField()
	def __str__(self):
		return self.name
	class Meta:
		db_table='gold'

class Photos(models.Model):
	main_image=models.ImageField(upload_to="/uploads")
	first_image=models.ImageField(upload_to="/uploads")
	second_image=models.ImageField(upload_to="/uploads")
	third_image=models.ImageField(upload_to="/uploads")
	fourth_image=models.ImageField(upload_to="/uploads")

class ProductCode(models.Model):
    jewel_code=models.CharField(max_length=15)
    jewel_name=models.CharField(max_length=50)
    photos=models.ForeignKey(Photos)
    #A Product can have a multiple variety of diamonds.Diamond class will do the work 
    def __str__(self):
    	return self.name

# class ProductDimensions(models.Model):
# 	sub_product_code=models.ForeignKey(subProduct)
# 	height_mm=models.IntegerField()
# 	width_mm=models.IntegerField()    


class subProduct(models.Model):
	jewel_code=models.ForeignKey(ProductCode) #A Product eg A ring can have varied sizes thus diff details.Hence subProduct
	type_of_jewel=models.CharField(max_length=30)
	karat=models.ForeignKey(Gold)
	weight_grams=models.IntegerField()
	height_mm=models.IntegerField()
	width_mm=models.IntegerField() 
	stones_or_pearls_price=models.IntegerField()
	stones_string_price=models.IntegerField()
	uncut_diamond_weight=models.IntegerField()
	uncut_diamond_price=models.IntegerField()
	making_price=models.IntegerField()
	stock_quantity=models.IntegerField(default=0)
	size=models.IntegerField()


class Diamond(models.Model):
	product_code=models.ForeignKey(ProductCode)
	diamond_color=models.CharField(max_length=2)
	diamond_clarity=models.CharField(max_length=2)
	diamond_weight_carats=models.IntegerField()
	#number_of_diamonds=models.IntegerField()
	shape=models.CharField(max_length=20)
	setting_type=models.CharField(max_length=20)


		