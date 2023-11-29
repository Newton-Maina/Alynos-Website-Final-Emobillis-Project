from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='doctor_images/',null=True, blank=True)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DoctorDetails(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctor_images/', null=True, blank=True)
    intro1 = models.TextField()
    intro2 = models.TextField()
    educational_year1 = models.CharField(max_length=15)
    school_year1 = models.CharField(max_length=255)
    description_year1 = models.TextField()
    educational_year2 = models.CharField(max_length=15, blank=True, null=True)
    school_year2 = models.CharField(max_length=255, blank=True, null=True)
    description_year2 = models.TextField(blank=True, null=True)
    educational_year3 = models.CharField(max_length=15, blank=True, null=True)
    school_year3 = models.CharField(max_length=255, blank=True, null=True)
    description_year3 = models.TextField(blank=True, null=True)
    educational_year4 = models.CharField(max_length=15, blank=True, null=True)
    school_year4 = models.CharField(max_length=255, blank=True, null=True)
    description_year4 = models.TextField(blank=True, null=True)
    skills = models.TextField()
    expertise_area1 = models.CharField(max_length=255)
    expertise_area2 = models.CharField(max_length=255, blank=True, null=True)
    expertise_area3 = models.CharField(max_length=255, blank=True, null=True)
    expertise_area4 = models.CharField(max_length=255, blank=True, null=True)
    expertise_area5 = models.CharField(max_length=255, blank=True, null=True)
    expertise_area6 = models.CharField(max_length=255, blank=True, null=True)


class Department(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='department_images/',null=True, blank=True)
    description =models.TextField()

    def __str__(self):
        return self.name

class DepartmentDetails(models.Model):
    department = models.OneToOneField(Department, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='department_images/', null=True, blank=True)
    description1 = models.TextField()
    description2 = models.TextField()
    service_feature1 = models.CharField(max_length=255)
    service_feature2 = models.CharField(max_length=255, blank=True, null=True)
    service_feature3 = models.CharField(max_length=255, blank=True, null=True)
    service_feature4 = models.CharField(max_length=255, blank=True, null=True)
    service_feature5 = models.CharField(max_length=255, blank=True, null=True)
    service_feature6 = models.CharField(max_length=255, blank=True, null=True)


class Products(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    image = models.ImageField(upload_to='product_images/',null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class ProductDetail(models.Model):
    product = models.OneToOneField(Products, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', default=0.0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    additional_info = models.TextField()
    specifications1 = models.CharField(max_length=300, blank=True, null=True)
    specifications2 = models.CharField(max_length=300, blank=True, null=True)
    specifications3 = models.CharField(max_length=300, blank=True, null=True)
    specifications4 = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.product.title

class ProductReview(models.Model):
    review = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    rating = models.PositiveIntegerField()
    review_text = models.TextField()

    def __str__(self):
        return f"{self.username} - {self.review.product.title} Review"

class CartItem:
    def __init__(self, product_id, quantity, title, price):
        self.product_id = product_id
        self.quantity = quantity
        self.title = title
        try:
            self.price = float(price)
        except ValueError:
            self.price = 0.0

    def remove_from_cart(self, cart):
        """
        Remove the current item from the cart.

        Args:
            cart (list): The list representing the cart.
        """
        cart.remove(self)

class CheckoutForm(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    messageinfo = models.TextField(blank=True, null=True)
    products = models.ManyToManyField(Products, through='Purchase')

class Purchase(models.Model):
    checkout_form = models.ForeignKey(CheckoutForm, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} {self.product.title}(s) for {self.checkout_form.fname} {self.checkout_form.lname}"



class Appointment(models.Model):
    doctor_name = models.CharField(max_length=255)
    department_name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"{self.full_name}'s Appointment"

class PaymentReport(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount} - {self.timestamp}"

    class Meta:
        verbose_name_plural = "Payment Reports"

class PurchasedProduct(models.Model):
    product = models.ForeignKey(ProductDetail, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)

class Blog(models.Model):
    name = models.CharField(max_length=255)
    definition = models.CharField(max_length=500)
    image = models.ImageField(upload_to='blog_images/', default=0.0)
    description=models.TextField()


class BlogDetail(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
    intro =models.TextField()
    intro_detail = models.TextField()
    quote = models.CharField(max_length=500, blank=False, null=False)
    quote_expl = models.TextField()
    more_cont = models.TextField(blank=True)

class Comment(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='comment_images/', default=0.0)
    country = models.CharField(max_length=100)
    date_posted = models.CharField(max_length=255)
    message = models.TextField()

class ContactMessage(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.fullname} - {self.email}"



