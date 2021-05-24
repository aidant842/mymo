from django.shortcuts import render

def property_register(request):
    filter_form = FilterForm()

    listings = SoldListing.objects.all()

    query_dictionary = {}
    price_query = request.GET.get('price')
    county_query = request.GET.get('county')
    property_type_query = request.GET.get('property_type')
    no_of_bedrooms_query = request.GET.get('bedrooms')
    no_of_bathrooms_query = request.GET.get('bathrooms')
    ber_rating_query = request.GET.get('ber_rating')
    area_query = request.GET.get('area')
    keyword_query = request.GET.get('keyword')
    sort = request.GET.get('sort', None)

    if price_query != '' and price_query is not None:
        query_dictionary['price_query'] = price_query
        price_query = int(price_query)
        listings = listings.filter(price__lte=price_query,)
    if county_query != '' and county_query is not None:
        query_dictionary['county_query'] = county_query
        listings = listings.filter(county__icontains=county_query,)
    if property_type_query != '' and property_type_query is not None:
        query_dictionary['property_type_query'] = property_type_query
        listings = listings.filter(property_type__icontains=property_type_query,)
    if no_of_bedrooms_query != '' and no_of_bathrooms_query is not None:
        query_dictionary['no_of_bedrooms_query'] = no_of_bedrooms_query
        listings = listings.filter(no_of_bedrooms__gte=no_of_bedrooms_query,)
    if no_of_bathrooms_query != '' and no_of_bathrooms_query is not None:
        query_dictionary['no_of_bathrooms_query'] = no_of_bathrooms_query
        listings = listings.filter(no_of_bathrooms__gte=no_of_bathrooms_query,)
    if ber_rating_query != '' and ber_rating_query is not None:
        query_dictionary['ber_rating_query'] = ber_rating_query
        listings = listings.filter(ber_rating__icontains=ber_rating_query,)
    if area_query != '' and area_query is not None:
        query_dictionary['area_query'] = area_query
        area_queries = Q(area__icontains=area_query) | Q(county__icontains=area_query)
        listings = listings.filter(area_queries)
    if keyword_query != '' and keyword_query is not None:
        query_dictionary['keyword_query'] = keyword_query
        keyword_queries = Q(area__icontains=keyword_query) | Q(description__icontains=keyword_query) | Q(county__icontains=keyword_query) | Q(company_name__icontains=keyword_query)
        listings = listings.filter(keyword_queries)
    if sort != '' and sort is not None:
        query_dictionary['sort'] = sort
        sortkey = sort.split('-')[0]
        direction = sort.split('-')[1]
        if direction == 'desc' or sortkey == 'date_created':
            sortkey = f'-{sortkey}'
        listings = listings.order_by(sortkey)
    else:
        listings = listings.order_by('-is_spotlight', '-date_created')

    total_listings = listings.count()

    """ setup paginator """

    paginator = Paginator(listings, 20)
    page = request.GET.get('page')

    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        listings = paginator.page(1)

    except EmptyPage:
        listings = paginator.page(paginator.num_pages)

    template = 'listings/property_register.html'
    context = {
        'filter_form': filter_form,
        'listings': listings,
        'query_dictionary': query_dictionary,
        'total_listings': total_listings,
        'page': page,
    }

    return render(request, template, context)
