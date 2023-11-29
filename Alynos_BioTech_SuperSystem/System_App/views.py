from django.shortcuts import render,redirect, get_object_or_404
from .models import Products, ProductDetail, Doctor, DoctorDetails, Department, DepartmentDetails
# Create your views here.
from django.contrib import messages
# from django.http import JsonResponse
from .models import CartItem, CheckoutForm, Appointment, PaymentReport,Blog, BlogDetail, Comment, Purchase, ContactMessage
import locale
import re
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request, "index.html", {'navbar': 'index'})

def about(request):

   doctors = Doctor.objects.all()

   return render(request, "about.html", {'doctors': doctors, 'navbar': 'about'})

def contact(request):
    return render(request, "contact.html", {'navbar': 'contact'})

def submit_message(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            fullname=fullname,
            email=email,
            subject=subject,
            phone=phone,
            message=message
        )

        successive_message = 'Your Message has been sent Successfully!'
        messages.success(request, successive_message)

        return render(request, 'message_confirmation.html', {'success_message': successive_message})

    return redirect('BioTech_App:index')

def message_confirmation(request):

    return render(request, "message_confirmation.html")

def appointment(request):
    return render(request, "appoinment.html", {'navbar': 'contact'})

def department(request):

    departments = Department.objects.all()

    return render(request, "department.html", {'departments': departments, 'navbar': 'department'})

def department_single(request, department_id):

    department = get_object_or_404(Department, pk=department_id)
    details = get_object_or_404(DepartmentDetails, department=department)

    return render(request, "department-single.html", {'department': department, 'details': details, 'navbar': 'department_single'})

def appointment_view(request):
    if request.method == 'POST':
        doctor_name = request.POST.get('doctor')
        department_name = request.POST.get('department')
        date = request.POST.get('date')
        time = request.POST.get('time')
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        # Create Appointment instance without saving to the database
        Appointment.objects.create(
            department_name=department_name,
            doctor_name=doctor_name,
            date=date,
            time=time,
            full_name=full_name,
            phone_number=phone_number,
            message=message
        )

        success_message = 'Appointment booked Successfully.'
        messages.success(request, success_message)

        # Pass the success message to the confirmation page
        return render(request, 'confirmation.html', {'success_message': success_message})

    # Handle cases where the request method is not POST (optional)
    return redirect('BioTech_App:index')

def confirmation(request):
    return render(request, "confirmation.html", {'navbar': 'confirmation'})

def blog_sidebar(request):

    blogs = Blog.objects.all()

    return render(request, "blog-sidebar.html", {'blogs': blogs, 'navbar': 'blog_sidebar'})

def blog_single(request, blog_id):

    blog = get_object_or_404(Blog, id=blog_id)
    blog_detail = get_object_or_404(BlogDetail, blog=blog)

    return render(request, "blog-detail.html", {'blog':blog, 'blog_detail': blog_detail, 'navbar': 'blog_single'})


def comment_section(request, blog_id):

    blog = get_object_or_404(Doctor, id=blog_id)
    comment_detail = get_object_or_404(Comment, blog=blog)

    return render(request, "blog-detail.html", {'blog':blog, 'comment_detail': comment_detail, 'navbar': 'blog_single'})

def checkout(request):
    locale.setlocale(locale.LC_ALL, '')

    cart_summary = request.GET.get('cart_summary', None)
    cart = request.session.get('cart', [])

    # Convert the session cart data to a list of CartItem instances
    cart_items = [
        CartItem(
            product_id=item['product_id'],
            quantity=item['quantity'],
            title=item['title'],
            price=item['price']
        )
        for item in cart
    ]

    # Calculate total_price
    total_price = sum(item.price * item.quantity for item in cart_items)

    formatted_total_price = locale.currency (total_price, grouping=True)

    # Pass the cart_items and cart_summary to the template
    return render(request, 'sales/checkout.html',
                  {'cart_items': cart_items, 'cart_summary': cart_summary, 'total_price': formatted_total_price})

def doctor(request):

    doctors = Doctor.objects.all()

    return render(request, "doctors/doctor.html", {'doctors': doctors, 'navbar': 'doctor'})

def doctor_single(request, doctor_id):

    doctor = get_object_or_404(Doctor, id=doctor_id)
    details = get_object_or_404(DoctorDetails, doctor=doctor)

    return render(request, "doctors/doctor-single.html", {'doctor': doctor, 'details': details, 'navbar': 'doctor_single'})


def product_list(request):

    products = Products.objects.all()

    return render(request, "sales/products.html", {'products': products, 'navbar': products})

def product_detail(request, product_id):

    product = get_object_or_404(Products, id=product_id)
    product_detail = get_object_or_404(ProductDetail, product=product)


    return render(request, 'sales/product_detail.html',{'product': product, 'product_detail': product_detail})

# Pass the cart_items to the template

def add_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    quantity = int(request.POST.get('quantity', 1))  # Ensure quantity is an integer

    # Convert Decimal to float for JSON serialization
    price = float(product.price)

    cart = request.session.get('cart', [])

    # Check if the item is already in the cart
    for item in cart:
        if item['product_id'] == product.id:
            item['quantity'] += quantity
            break
    else:
        # If not, add it to the cart
        cart_item = CartItem(
            product_id=product.id,
            quantity=quantity,
            title=product.title,
            price=price
        )
        cart.append(cart_item.__dict__)

    request.session['cart'] = cart

    messages.success(request, 'Item Added to cart successfully.')


    return redirect('BioTech_App:view_cart')


def view_cart(request):
    # Set the locale to the user's default locale
    locale.setlocale(locale.LC_ALL, '')

    cart = request.session.get('cart', [])

    # Convert product_id to Products object in each cart item
    cart_items = []
    total_price = 0

    for item in cart:
        product_id = item.get('product_id')
        quantity = item.get('quantity', 0)
        title = item.get('title')
        price = item.get('price', 0)

        # Fetch the corresponding Products object
        try:
            product = Products.objects.get(id=product_id)
        except Products.DoesNotExist:
            # Handle the case where the product with the given ID is not found
            product = None

        # Ensure that price and quantity are valid numbers
        try:
            price = float(price)
            quantity = int(quantity)
        except (ValueError, TypeError):
            # Handle the case where price or quantity is not a valid number
            price = 0
            quantity = 0

        # Create the CartItem instance
        cart_item = CartItem(product_id=product_id, quantity=quantity, title=title, price=price)
        cart_items.append(cart_item)

        # Calculate the total price
        total_price += price * quantity

    # Format the total price as currency
    formatted_total_price = locale.currency(total_price, grouping=True)

    context = {
        'navbar':'view_cart',
        'cart': cart_items,
        'total_price': formatted_total_price,
    }

    return render(request, 'sales/view_cart.html', context)


def remove_from_cart(request, item_id):
    cart = request.session.get('cart', [])

    # Find the index of the item with the specified ID
    item_index = next((index for (index, item) in enumerate(cart) if item['product_id'] == item_id), None)

    if item_index is not None:
        # Remove the item from the cart
        del cart[item_index]
        request.session['cart'] = cart

        messages.success(request, 'Selected item has been removed from cart.')

    return redirect('BioTech_App:view_cart')


def payment_page(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        messageinfo = request.POST.get('messageinfo')

        checkout_form = CheckoutForm.objects.create(
            fname=fname,
            lname=lname,
            address=address,
            address2=address2,
            email=email,
            phone=phone,
            messageinfo=messageinfo
        )

        cart = request.session.get('cart', [])

        for item in cart:
            product_id = item['product_id']
            quantity = item['quantity']

            # Retrieve the corresponding Product instance
            product = Products.objects.get(id=product_id)

            # Create a Purchase record
            Purchase.objects.create(
                checkout_form=checkout_form,
                product=product,
                quantity=quantity
            )

        messages.success(request, 'Details Added Successfully!.')

    locale.setlocale(locale.LC_ALL, '')


    cart_summary = request.GET.get('cart_summary', None)
    cart = request.session.get('cart', [])

    # Convert the session cart data to a list of CartItem instances
    cart_items = [
        CartItem(
            product_id=item['product_id'],
            quantity=item['quantity'],
            title=item['title'],
            price=item['price']
        )
        for item in cart
    ]

    # Calculate total_price
    total_price = sum(item.price * item.quantity for item in cart_items)

    formatted_total_price = locale.currency(total_price, grouping=True)


    return render(request, 'sales/payment.html',{'cart_items': cart_items, 'cart_summary': cart_summary, 'total_price': formatted_total_price})

def validate_credit_card(card_number, expiry_date, cvv):
    card_number = ''.join(card_number.split())

    # Basic validation for card number (simple Luhn algorithm check)
    if not re.match(r'^[0-9]{12,19}$', card_number):
        return False, 'Invalid card number'

    # Basic validation for expiry date (MM/YY format)
    if not re.match(r'^(0[1-9]|1[0-2])/[0-9]{2}$', expiry_date):
        return False, 'Invalid expiry date'

    # Basic validation for CVV (3 or 4 digits)
    if not re.match(r'^[0-9]{3,4}$', cvv):
        return False, 'Invalid CVV'

    return True, 'Valid'


def payment_process(request):
    if request.method == 'POST':
        # Retrieve card details from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')



        # Perform basic validation
        is_valid, validation_message = validate_credit_card(card_number, expiry_date, cvv)

        if is_valid:

            PaymentReport.objects.create(
                name=name,
                email=email,
                phone=phone,
                amount=amount
            )

            messages.success(request, 'Payment successful!')

            request.session['cart'] = []

            return redirect('BioTech_App:payment_success')  # Redirect to a success page
        else:
            messages.error(request, f'Payment failed. {validation_message}')
            return render(request, 'sales/payment_failed.html', {'message': validation_message})

    # Handle the case when the form is not submitted via POST
    return render(request, 'sales/payment.html')

def payment_success(request):
    return render(request, "sales/payment_success.html", {'navbar': 'success'})

def payment_failed(request):
    return render(request, "sales/payment_failed.html", {'navbar': 'failed'})