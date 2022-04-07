from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'login.html')

def user_id(request, user_id):
    context = {
        "one_user": User.objects.get(id=user_id)
    }
    return render( request, "login.html", context)

def create_user(request):
    if request.method == "POST":
        errors = User.objects.create_validator(request.POST, request.FILES)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], profile_pic=request.FILES['profile_pic'], city=request.POST['city'], state=request.POST['states'], email=request.POST['email'], password=pw_hash)
            request.session['user_id'] = user.id
            return redirect('/user/success')
    return redirect('/')

def dashboard(request):
    if "user_id" not in request.session:
        return redirect('/')
    context = {
        "user_image":User.objects.all(),
        "current_user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, "dashboard.html", context)

def login(request):
    if request.method == "POST":
        user_with_email = User.objects.filter(email=request.POST['email'])
        if user_with_email:
            user = user_with_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/user/success')
        messages.error(request,"Email or Password is incorrect")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def account(request, user_id):
    if "user_id" not in request.session:
        return redirect('/')
    context = {
        "user_id": User.objects.get(id=request.session['user_id']),
        "portfolio_objects": Portfolio.objects.all(),
        "account_user": User.objects.get(id=user_id)
    }
    return render(request, "account.html", context)

def profile_pic_update(request):
    # this function is specifically for updating photos
    if "user_id" not in request.session:
        return redirect('/')
    if len(request.FILES) == 1:
        profile_pic_update = User.objects.get(id=request.session['user_id'])
        profile_pic_update.profile_pic = request.FILES['profile_pic']
        profile_pic_update.save()
        print("hello!")
    return redirect(f'/user/account/{profile_pic_update.id}')

def personal_info(request, user_id):
    #this function updates the personal info
    if "user_id" in request.session:
        if request.method == "POST":
            if 'first_name' in request.POST:
                errors = User.objects.create_validator_update(request.POST, request.FILES)
            if 'bio' in request.POST:
                errors = User.objects.create_validator_update_two(request.POST, request.FILES)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect(f'/user/account/{user_id}')
            personal_info = User.objects.get(id=user_id)
            if 'first_name' in request.POST:
                print("Hello!")
                password = request.POST['password']
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                personal_info.first_name = request.POST['first_name']
                personal_info.last_name = request.POST['last_name']
                personal_info.city = request.POST['city']
                personal_info.state = request.POST['states']
                personal_info.email = request.POST['email']
                personal_info.password = pw_hash
            if 'bio' in request.POST:
                personal_info.bio = request.POST['bio']
            if 'website' in request.POST:
                personal_info.website = request.POST['website']
            personal_info.save()
    return redirect('/user/success')

def create_portfolio(request):
    current_user = User.objects.get(id=request.session['user_id'])
    portfolio = Portfolio.objects.create(title=request.POST['title'], price=request.POST['price'], portfolio_image=request.FILES['portfolio_image'], content_creator = current_user)
    return redirect('/user/success')

def content_creator(request, user_id):
    if "user_id" not in request.session:
        return redirect('/')
    context = {
        "content_creator":User.objects.get(id=user_id),
        "user_portfolio":User.objects.get(id=user_id).user_portfolio.all(),
        "user_id": User.objects.get(id=request.session['user_id']),
        "user_media": User.objects.get(id=user_id).user_social_media
    }
    return render(request, "creator.html", context)

def add_to_cart(request, user_id):
    if "user_id" not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    if 'cart' not in request.session:
        line_items = []
        total_price = 0.00
        cart = Cart.objects.create(total_price=0.00, user_id=user.id)
        request.session['cart'] = cart.id
    else:
        print('cart')
        # line_items = request.session['line_items']
        print('cart2')
        total_price = request.session['total_price']
        cart = Cart.objects.get(id=request.session['cart'])
    # item_list makes a list of all the items on the view cart page
    if request.method == 'POST':
        item = Portfolio.objects.get(id=request.POST['item'])
        qty = int(request.POST['quantity_ordered'])
        if request.POST['item'] == item.id:
            qty = int(request.POST['quantity_ordered']) + 1 
        # the append is adding items to the empty item list above when you click add to cart
        total_price += float(item.price)* qty
        cart = Cart.objects.get(id=request.session['cart'])
        cart.total_price = total_price
        request.session['cart'] = cart.id
        line_items = []
        cart.save()
        line_item = CartItem.objects.create(cart = cart, item = item, quantity = request.POST['quantity_ordered'])
        line_items.append(line_item.id)
        request.session['total_price'] = total_price
    # request.session['line_items'] = line_items
    # print(line_items)
    # this is so we can create a session for the cart the user creates
    return redirect(f'/user/contentcreator/{user_id}')

def remove_from_cart(request, line_id):
    item = CartItem.objects.get(id=line_id)
    # we are grabbing item id and the cart id that's in session
    portfolio = Portfolio.objects.get(id=item.item_id)
    # first item on ;ine 155 is from the variable on line 154 and the second item is from the relationship between portfolio and cart item
    request.session['total_price'] = float(request.session['total_price']) - float(portfolio.price)*item.quantity
    item.delete()
    # we reduce the total price of the cart by the item and price and the quantity

    return redirect('/user/viewcart')



def view_cart(request):
    # if 'cart' not in request.session:
    #     cart = {}
    #     line_items = {}
    # else:
    print("Working")
    user = User.objects.get(id=request.session['user_id'])
    print("Working1")
    cart = Cart.objects.filter(user_id=user.id).last()
    print("Working2")
    line_items = CartItem.objects.filter(cart = cart.id)
    print("Working3")
    # request.session['line_items'] = line_items
    request.session['cart'] = cart.id
    request.session['total_price'] = float(cart.total_price)
    print("Working2.5")
    context = {
        "cart": cart,
        "line_items": line_items,
        "current_user": User.objects.get(id=request.session['user_id'])
    }
    print("Working4")
    return render(request, "view_cart.html", context)

def checkout(request):
    cart = Cart.objects.get(id=request.session['cart'])
    line_items = CartItem.objects.filter(cart = cart.id)
    context = {
        "order_total": cart,
        "line_items": line_items
    }
    return render(request, "checkout.html", context)

def media(request, user_id):
    if request.method == POST:
        current_user = User.objects.get(id=request.session['user_id'])
        media = Media.objects.create(facebook=request.POST['facebook'], linkedin=request.POST['linkedin'], instagram=request.POST['instagram'], twitter=request.POST['twitter'], user_media=current_user)
        return redirect(f'/user/account/{user_id}')