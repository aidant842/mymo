from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils import timezone
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import AgentFilter, ContactForm
from listings.models import SaleListing, RentListing, SaleListingImage, RentListingImage
from profiles.models import UserProfile
from listings.forms import FilterForm
from products.models import Product

from operator import attrgetter
from itertools import chain


def estate_agents(request):
    agents = UserProfile.objects.filter(is_agent=True).exclude(id=1)
    agent_filter = AgentFilter()
    query_dictionary = {}
    county_query = request.GET.get('county')
    name_query = request.GET.get('name')
    contact_form = ContactForm(initial={'email': request.user.userprofile.email,
                                        'phone_number': request.user.userprofile.phone_number,
                                        'full_name': request.user.userprofile.full_name,})

    if name_query != '' and name_query is not None:
        query_dictionary['name_query'] = name_query

        agents = agents.filter(Q(company_name__icontains=name_query))

    if county_query != '' and county_query is not None:
        query_dictionary['county_query'] = county_query
        agents = agents.filter(Q(address__icontains=county_query))

    """ setup paginator """

    paginator = Paginator(agents, 20)
    page = request.GET.get('page')

    try:
        agents = paginator.page(page)
    except PageNotAnInteger:
        agents = paginator.page(1)

    except EmptyPage:
        agents = paginator.page(paginator.num_pages)

    template = 'estate_agents/estate_agents.html'
    context = {
        'agent_filter': agent_filter,
        'agents': agents,
        'contact_form': contact_form,
    }
    return render(request, template, context)


def estate_agents_profile(request, name, profile_id):
    profile = get_object_or_404(UserProfile, pk=profile_id)
    contact_form = ContactForm(initial={'email': request.user.userprofile.email,
                                        'phone_number': request.user.userprofile.phone_number,
                                        'full_name': request.user.userprofile.full_name,})
    if not name == profile.company_name_to_url():
        raise Http404
    if not profile.is_agent:
        messages.error(request, 'This user is not an agent.')
        return redirect('home')
    sale_listings = SaleListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(), user_profile=profile)
    rent_listings = RentListing.objects.filter(is_listed=True, expiration_date__gt=timezone.now(), user_profile=profile)

    result_list = list(chain(sale_listings, rent_listings))

    result_list.sort(key=attrgetter('date_created'), reverse=True)
    result_list.sort(key=attrgetter('is_spotlight'), reverse=True)
    total_listings = len(result_list)

    """ setup paginator """

    paginator = Paginator(result_list, 20)
    page = request.GET.get('page')

    try:
        result_list = paginator.page(page)
    except PageNotAnInteger:
        result_list = paginator.page(1)

    except EmptyPage:
        result_list = paginator.page(paginator.num_pages)

    template = 'estate_agents/estate_agents_profile.html'

    context = {
        'profile': profile,
        'result_list': result_list,
        'total_listings': total_listings,
        'contact_form': contact_form,
    }

    return render(request, template, context)


@login_required
@require_POST
def contact_agent(request):
    profile = get_object_or_404(UserProfile, pk=request.POST.get('profile_id'))
    listing = ''
    if request.POST.get('product_id'):
        product = Product.objects.get(id=request.POST.get('product_id'))
        if product.category.name == 'sale':
            listing = SaleListing.objects.get(id=request.POST.get('listing_id'))
        else:
            listing = RentListing.objects.get(id=request.POST.get('listing_id'))

    cust_name = request.POST.get('full_name')
    cust_email = request.POST.get('email')
    cust_phone = request.POST.get('phone_number')
    message = request.POST.get('message')
    agents_email = profile.email
    subject = render_to_string(
            'estate_agents/contact_emails/contact_email_subject.txt',
            {'listing': listing, 'cust_name': cust_name}
        )

    body = render_to_string(
        'estate_agents/contact_emails/contact_email_body.txt',
        {'listing': listing, 'cust_email': cust_email,
         'cust_name': cust_name, 'cust_phone': cust_phone,
         'message': message}
    )

    send_mail(
                subject,
                body,
                cust_email,
                [agents_email],
            )
    messages.success(request, 'E-mail sent to Agent.')
    return redirect(request.META.get('HTTP_REFERER'))
