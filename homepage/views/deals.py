from django.conf import settings
from django_mako_plus import view_function, jscontext
from bs4 import BeautifulSoup
import requests
import html5lib
from homepage import models as hmod
import re
from datetime import datetime, timedelta  
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
import time
import smtplib
from decimal import Decimal


@view_function
def process_request(request):
       
    hmod.RecentAds.objects.all().delete()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }

    with requests.Session() as s:
        r = s.get('https://classifieds.ksl.com/s/Recreational+Vehicles/Motorcycles,+Dirt+Bikes+Used', headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        start = str(soup).find('listings:')
        sub1 = str(soup)[start + 11:]

        end = str(sub1).find('}]')
        sub2 = str(sub1)[:end]

        itemList = sub2.split('}')  #this is a list of all the items!
        
        for item in itemList:

            start1 = str(item).find('{"id":')
            s = str(item)[start1:]
            end1 = str(item).find('memberId":')
            ksl_id = str(item)[start1 + 6 : end1 - 2]
            
            start1 = str(item).find('displayTime":')
            s = str(item)[start1:]
            end1 = str(item).find('modifyTime":')
            displayTime = str(item)[start1 + 14 : end1 - 4]

            start1 = str(item).find('category":')
            s = str(item)[start1:]
            end1 = str(item).find('subCategory":')
            category = str(item)[start1 + 11 : end1 - 3]

            start1 = str(item).find('subCategory":')
            s = str(item)[start1:]
            end1 = str(item).find('price":')
            subCategory = str(item)[start1 + 14 : end1 - 3]

            start1 = str(item).find('price":')
            s = str(item)[start1:]
            end1 = str(item).find('title":')
            price = str(item)[start1 + 7 : end1 - 2]

            start1 = str(item).find('title":')
            s = str(item)[start1:]
            end1 = str(item).find('description":')
            title = str(item)[start1 + 8 : end1 - 3]    

            start1 = str(item).find('city":')
            s = str(item)[start1:]
            end1 = str(item).find('state":')
            city = str(item)[start1 + 7 : end1 - 3]

            start1 = str(item).find('state":')
            s = str(item)[start1:]
            end1 = str(item).find('zip":')
            state = str(item)[start1 + 8 : end1 - 3]

            start1 = str(item).find('name":')
            s = str(item)[start1:]
            end1 = str(item).find('homePhone":')
            name = str(item)[start1 + 7 : end1 - 3]

            start1 = str(item).find('favorited":')
            s = str(item)[start1:]
            end1 = str(item).find('listingType":')
            favorited = str(item)[start1 + 11 : end1 - 2]

            start1 = str(item).find('description":')
            s = str(item)[start1:]
            end1 = str(item).find('marketType":')
            description = str(item)[start1 + 14 : end1 - 3]
            
            if str(item).find('cellPhone":'):
                start1 = str(item).find('cellPhone":')
                s = str(item)[start1:]
                end1 = str(item).find('email":')
                cellPhone = str(item)[start1 + 12 : end1 - 3]
            else:
                cellPhone = None
            # if len(cellPhone) > 14:
            #     cellPhone = None

            start1 = str(item).find('description":')
            s = str(item)[start1:]
            end1 = str(item).find('marketType":')
            description = str(item)[start1 + 14 : end1 - 3]
            
            item = hmod.Ad()
            item.ksl_id = ksl_id
            item.displayTime = displayTime
            item.category = category
            item.subCategory = subCategory
            item.price = price
            item.title = title
            item.city = city
            item.state = state
            item.name = name
            item.cellPhone = cellPhone
            item.favorited = favorited
            item.description = description

            recent_item = hmod.RecentAds()
            recent_item.ksl_id = ksl_id
            recent_item.displayTime = displayTime
            recent_item.category = category
            recent_item.subCategory = subCategory
            recent_item.price = price
            recent_item.title = title
            recent_item.city = city
            recent_item.state = state
            recent_item.name = name
            recent_item.cellPhone = cellPhone
            recent_item.favorited = favorited
            recent_item.description = description

            #convert title to lowercase before checking!! duh dude                    
            if 'CRF' in title or 'crf' in title or 'Crf' in title:
                item.brand = "CRF"
                recent_item.brand = "CRF"
                make = "honda"
            elif 'CR' in title or 'Cr' in title or 'cr' in title: #this is case sensitive...
                item.brand = "CR"
                recent_item.brand = "CR"
                make = "honda"
            elif 'XR' in title or 'xr' in title or 'Xr' in title:
                item.brand = "XR"
                recent_item.brand = "XR"
                make = "honda"
            elif 'Honda' in title or 'honda' in title:   
                item.brand = 'honda'
                recent_item.brand = 'honda' 
                make = "honda"
                      
            elif 'YZ' in title or 'Yz' in title or 'yz' in title:
                item.brand = "YZ"
                recent_item.brand = "YZ"
                make = "yamaha"
            elif 'TTR' in title or 'TT-R' in title or 'ttr' in title or 'Ttr' in title  or 'TT R' in title  or 'tt r' in title:
                item.brand = "TTR"
                recent_item.brand = "TTR"
                make = "yamaha"
            elif 'WR' in title or 'Wr' in title or 'wr' in title:
                item.brand = "WR"
                recent_item.brand = "WR"
                make = "yamaha"
            elif 'PW' in title or 'pw' in title or 'Pw' in title:
                item.brand = "PW"
                recent_item.brand = "PW"
                make = "yamaha"
            elif 'TW' in title or 'tw' in title or 'Tw' in title:
                item.brand = "TW"
                recent_item.brand = "TW"
                make = "yamaha"
            elif 'Yamaha' in title or 'yamaha' in title:
                item.brand = "yamaha"
                recent_item.brand = "yamaha"
                make = "yamaha"

            elif 'KTM' in title or 'Ktm' in title or 'ktm' in title:
                item.brand = "ktm"
                recent_item.brand = "ktm"
                make = "ktm"
                 
            elif 'DR-Z' in title or 'DRZ' in title or 'dr-z' in title or 'drz' in title or 'Drz' in title:
                item.brand = "DR-Z"
                recent_item.brand = "DR-Z"
                make = "suzuki"
            elif 'RMZ' in title or 'Rmz' in title or 'rmz' in title:
                item.brand = "RM-Z"
                recent_item.brand = "RM-Z"
                make = "suzuki"
            elif 'RM' in title or 'Rm' in title or 'rm' in title:
                item.brand = "RM"
                recent_item.brand = "RM"
                make = "suzuki"
            elif 'Suzuki' in title or 'suzuki' in title:
                item.brand = "suzuki"
                recent_item.brand = "suzuki"
                make = "suzuki"
           
            elif 'KLX' in title or 'Klx' in title or 'klx' in title:
                item.brand = "KLX"
                recent_item.brand = "KLX"
                make = "kawasaki"
            elif 'KX' in title or 'kx' in title or 'Kx' in title:
                item.brand = "KX"
                recent_item.brand = "KX"
                make = "kawasaki"
            elif 'Kawasaki' in title or 'kawasaki' in title:
                item.brand = "kawasaki"
                recent_item.brand = "kawasaki"
                make = "kawasaki"

            elif 'Husqvarna' in title or 'husqvarna' in title: 
                item.brand = "husqvarna"
                recent_item.brand = "husqvarna"
                make = None
            
            else:
                item.brand = "other"
                recent_item.brand = "other"
                make = None

            if re.match(r'\b(19|20)\d{2}\b', title):
                year = re.match(r'\b(19|20)\d{2}\b', title)
            
                item.year = str(year)[38:42]
                recent_item.year = str(year)[38:42]              

                i = str(title).find(str(item.year))
                sub = str(title)[i + 4:]
                
            else:
                if re.match(r'\b(19|20)\d{2}\b', description):
                    year = re.match(r'\b(19|20)\d{2}\b', description)                    
                    item.year = str(year)[38:42]
                    recent_item.year = str(year)[38:42] 

                    i = str(title).find(str(item.year))
                    sub = str(title)[i + 4:]
                else:
                    sub = str(title)
                    item.year = None 
                    recent_item.year = None     


            size = find_size(sub)
            item.size = size
            recent_item.size = size

            item.make = make
            recent_item.make = make

            model = None

            if make != None and (item.brand != None and item.brand != 'honda' and item.brand != 'kawasaki' and item.brand != 'suzuki' and item.brand != 'yamaha' and item.brand != 'husqvarna' and item.brand != 'other'): #is not None?
                
                model = find_model(make, title, item.brand)
                
                if size > 0:
                    if model != None:
                        # if make == "honda":
                        #     model = str(item.size) + 'f' #item.size can't be 0
                        # #elif model == "yamaha":
                        if (make != "ktm"):
                            model = item.brand + model
                        item.model = model
                        recent_item.model = model
                    
            if make != None and model != None and item.year != None:
                # url = 'https://www.kbb.com/motorcycles/' + make + '/' + model + '/' + item.year + '/?pricetype=trade-in'
                # print(url)
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
                }

                with requests.Session() as sesh:     
                    r = sesh.get('https://www.kbb.com/motorcycles/' + make + '/' + model + '/' + item.year + '/?pricetype=trade-in', headers=headers) #make/model/year
                    soup = BeautifulSoup(r.content, 'html.parser')

                start = str(soup).find('msrp')
                sub3 = str(soup)[start:]
                
                end = str(sub3).find('options')
                sub4 = str(sub3)[:end]

                start = str(sub4).find('tradeIn')
                sub5 = str(sub4)[start:]
                
                kbb_value = str(sub5)[9 : -2]           

                if kbb_value != None and kbb_value != "":

                    item.kbb_value = kbb_value
                    recent_item.kbb_value = kbb_value

                    item.difference = Decimal(price) - Decimal(kbb_value)
                    recent_item.difference = Decimal(price) - Decimal(kbb_value)


            if item.year != None and item.brand != "other": 
                if not hmod.Ad.objects.filter(price = Decimal(item.price), city = item.city, state = item.state, year = item.year, brand = item.brand, size = item.size):
                    item.save()   
            if recent_item.year != None and recent_item.brand != "other": 
                recent_item.save()


    year_param1 = None
    price_param1 = None
    size_param1 = None

    if request.method == 'POST':  
        form = SearchForm(request.POST)
        if form.is_valid():
            year_param1 = form.cleaned_data.get('year')
            price_param1 = form.cleaned_data.get('price')
            size_param1 = form.cleaned_data.get('size')           
    else:
        form = SearchForm()

    if year_param1 is None:
        year_param = 2001
    else:
        year_param = year_param1

    if price_param1 is None:
        price_param = 1200
    else:
        price_param = price_param1

    if size_param1 is None:
        size_param = 50
    else:
        size_param = size_param1

    
    # my_items = hmod.RecentAds.objects.filter(year__gte = year_param, price__lte = price_param, size__gte = size_param)

    # old_items = hmod.Ad.objects.filter(year__gte = year_param, price__lte = price_param, size__gte = size_param)

    deals = hmod.RecentAds.objects.all().exclude(kbb_value = None).order_by('difference')


    # my_titles = []
    # my_prices = []
    # my_years = []
    # my_cities = []
    # my_sizes = []

    # for x in my_items:
    #     my_titles.append(x.title)
    #     my_prices.append(x.price)
    #     my_years.append(x.year)
    #     my_cities.append(x.city)
    #     my_sizes.append(x.size)

    # old_titles = []
    # old_prices = []
    # old_years = []
    # old_cities = []
    # old_sizes = []

    # for x in old_items:
    #     old_titles.append(x.title)
    #     old_prices.append(x.price)
    #     old_years.append(x.year)
    #     old_cities.append(x.city)
    #     old_sizes.append(x.size)

    # some_text = 'Test'

    # send(some_text)

    context = {
        #'my_items' : my_items,
        'form': form,
        'deals': deals,
        # jscontext('my_titles'): my_titles,
        # jscontext('my_prices'): my_prices,
        # jscontext('my_years'): my_years,
        # jscontext('my_cities'): my_cities,
        # jscontext('my_sizes'): my_sizes,

        # jscontext('old_titles'): old_titles,
        # jscontext('old_prices'): old_prices,
        # jscontext('old_years'): old_years,
        # jscontext('old_cities'): old_cities,
        # jscontext('old_sizes'): old_sizes,
    }
    return request.dmp.render('deals.html', context)


class SearchForm(forms.Form):
    year = forms.IntegerField(label='Minimum Year')
    #brand = forms.CharField(label='Brand')
    price = forms.DecimalField(label='Maximum Price')
    size = forms.IntegerField(label='Minimum Size')

    def clean(self):
        if int(self.cleaned_data.get('year')) < 1920 or int(self.cleaned_data.get('year')) > 2020:
            raise forms.ValidationError("Select an appropriate year")
        if int(self.cleaned_data.get('size')) < 50 or int(self.cleaned_data.get('size')) > 650:
            raise forms.ValidationError("Select an appropriate size")
        if int(self.cleaned_data.get('price')) is None:
            raise forms.ValidationError("Please enter a price")

        return self.cleaned_data


def find_model(make, my_title, my_brand): #description

    title = my_title.lower()
    brand = my_brand.lower()
    #if make == "honda": # does this need to be brand specific? 
    
    #450 SE for yahamas 2012 or 13?
    if '450x' in title or '450 x' in title:
        return '450x'
    elif '450fx' in title or '450 fx' in title:
        return '450fx'
    elif '450f' in title or '450 f' in title:
        if(make == 'kawasaki'):           
                return '450e-kx450f'
        else:
            return '450f'
    elif '450r' in title or '450 r' in title:
        return '450r'
    elif '450sxf' in title or '450 sxf' in title or '450 sx-f' in title:
        return '450-sx-f'
    elif '450sx' in title or '450 sx' in title:
        return '450-sx'
    elif '450xc' in title or '450 xc' in title:
        return '450-xc'
    elif '450exc' in title or '450 exc' in title:
        return '450-exc'
    elif '450' in title:
        if(make == 'honda'):
            # if(brand == 'xr' or brand == 'cr'):
            return '450r'
        elif(make == 'yamaha'):
            return '450f'
        else:
            return '450'
    elif '426f' in title or '426 f' in title:
        return '426f'
    elif '426' in title:
        return '426f'
    elif '400xcw' in title or '400 xcw' in title or '400 xc-w' in title:
        return '400-xc-w'
    elif '400r' in title or '400 r' in title:
        return '400r' 
    elif '400e' in title or '400 e' in title:
        return '400e' 
    elif '400sm' in title or '400 sm' in title:
        return '400sm' 
    elif '400s' in title or '400 s' in title:
        return '400s' 
    elif '400' in title:
        if(make == 'honda'):
            if(brand == 'xr' or brand == 'cr'):
                return '400r'
            else:
                return '400f'
        else:
            return '400'  
    elif '350sxf' in title or '300 sxf' in title or '300 sx-f' in title: 
        return '350-sx-f'
    elif '300xc' in title or '300 xc' in title: 
        return '300-xc'
    elif '250xcf' in title or '250 xcf' in title or '250 xc-f' in title:
        return '250-xc-f'
    elif '250xc' in title or '250 xc' in title:
        return '250-xc'
    elif '250x' in title or '250 x' in title: #or in description....
        return '250x'
    elif '250r' in title or '250 r' in title: 
        return '250r'
    elif '250l' in title or '250 l' in title:
        return '250l'
    elif '250fx' in title or '250 fx' in title:
        return '250fx'
    elif '250f' in title or '250 f' in title:
        if(make == 'kawasaki'):
            return '250w-kx250f'
        return '250f'
    elif '250sxf' in title or '250 sxf' in title or '250 sx-f' in title:
        return '250-sx-f'
    elif '250sx' in title or '250 sx' in title:
        return '250-sx'
    elif '250' in title:
        if(make == 'honda'):
            # if(brand == 'xr' or brand == 'cr'):
            return '250r'
            # else:
            #     return '250f'
        else:
            return '250'
    elif '230f' in title or '230 f' in title:
        return '230f'
    elif '230' in title:
        if(make == 'honda'):
            if(brand == 'xr' or brand == 'cr'):
                return '230r'
            else:
                return '230f'
        else:
            return '230'
    elif '230l' in title or '230 l' in title:
        return '230l'
    elif '225' in title:
        return '225'
    elif '200se' in title or '200 se' in title:
        return '200se'
    elif '200r' in title or '200 r' in title:
        return '200r'
    elif '200xc' in title or '200 xc' in title:
        return '200-xc'
    # elif '200' in title:  #this will break with years.... 2001 2002
    #     if(make = 'honda'):
    #         model = '200f'
    #     else:
    #         model = '200'
    elif '150r' in title or '150 r' in title:
        return '150r'
    elif '150f' in title or '150 f' in title:
        return '150f'
    elif '150sx' in title or '150 sx' in title:
        return '150-sx'
    elif '150' in title:
        if(make == 'honda'):
            if(brand == 'xr' or brand == 'cr'):
                return '150r'
            else:
                return '150f'
        else:
            return '125'
    elif '125r' in title or '125 r' in title:
        return '125r'
    elif '125f' in title or '125 f' in title:
        return '125f'
    elif '125le' in title or '125 le' in title:
        return '125le'
    elif '125l' in title or '125 l' in title:
        return '125l'
    elif '125e' in title or '125 e' in title:
        return '125e'
    elif '125sx' in title or '125 sx' in title:
        return '125-sx'
    elif '125' in title:
        if(make == 'honda'):
            if(brand == 'xr' or brand == 'cr'):
                return '125r'
            else:
                return '125f'
        else:
            return '125'
    elif '110f' in title or '110 f' in title:
        return '110f'
    elif '110e' in title or '110 e' in title:
        return '110e'
    elif '110' in title: #these work for yamaha but might mess up honda..?
        if(make == 'honda'):
            if(brand == 'xr'):
                return '110r'
            else:
                return '110f'
        else:
            return '110'
    elif '105sx' in title or '105 sx' in title:
        return '105-sx'
    elif '105xc' in title or '105 xc' in title:
        return '105-xc'
    elif '100f' in title or '100 f' in title:
        return '100f'
    elif '100r' in title or '100 r' in title: 
        return '100r'
    elif '100' in title:
        if(make == 'honda'):
            if(brand == 'xr' or brand == 'cr'):
                return '100r'
            else:
                return '100f'
        else:
            return '100'
    elif '90e' in title or '90 e' in title: 
        return '90e'
    elif '90' in title:
        if(make == 'yamaha'):
            return '90e'
        return '90'
    elif '85xc' in title or '85 xc' in title:
        return '85-xc'
    elif '85r' in title or '85 r' in title:
        return '85r'
    elif '85l' in title or '85 l' in title:
        return '85l'
    elif '85sx' in title or '85 sx' in title:
        return '85-sx'
    elif '85' in title:
        if(make == 'honda'):
            if(brand == 'xr' or brand == 'cr'):
                return '85r'
            else:
                return '85f'
        elif(make == 'kawasaki'):           
                return '85a'
        else:
            return '85'
    elif '80f' in title or '80 f' in title:
        return '80f'
    elif '80r' in title or '80 r' in title:
        return '80r'
    elif '80' in title:
        if(make == 'honda'):
            if(brand == 'xr' or brand == 'cr'):
                return '80r'
            else:
                return '80f'
        else:
            return '80'
    elif '70f' in title or '70 f' in title:
        return '70f'
    elif '70r' in title or '70 r' in title:
        return '70r'
    elif '70' in title:
        if(make == 'honda'):
            if(brand == 'xr' or brand == 'cr'):
                return '70r'
            else:
                return '70f'
        else:
            return '70' 
    elif '65xc' in title or '65 xc' in title:
        return '65-xc'
    elif '65sx' in title or '65 sx' in title:
        return '65-sx'
    elif '65' in title:
        if(make == 'kawasaki'):           
            return '65a'
        else:
            return '65'
    elif '60' in title:
        if(make == 'honda'):
            if(brand == 'xr' or brand == 'cr'):
                return '60r'
            else:
                return '60f'
        else:
            return '60'
    elif '50f' in title or '50 f' in title:
        return '50f'
    elif '50r' in title or '50 r' in title:
        return '50r'
    elif '50e' in title or '50 e' in title:
        return '50e'
    elif '50sx' in title or '50 sx' in title:
        if 'junior' in title or 'jr' in title:
            return '50-sx-junior'
        elif 'mini' in title:
            return '50-sx-mini'
        return '50-sx'
    elif '50' in title:  #this will sometimes pull in 500 sized bikes..
        if 'junior' in title or 'jr' in title:
            return '50-sx-junior'
        elif 'mini' in title:
            return '50-sx-mini'
        if(make == 'honda'):
            if(brand == 'xr' or brand == 'cr'):
                return '50r'
            else:
                return '50f'
        elif(make == 'ktm'):
            return '50-sx'
        return '50'
    else:
        return None        

    # else:
    #     model = None

    #return model


def find_size(sub):
    if '650' in sub: 
        return 650
    elif '600' in sub:
        return 600
    elif '550' in sub:
        return 550
    elif '500' in sub:
        return 500
    elif '465' in sub:
        return 465
    elif '450' in sub:
        return 450
    elif '400' in sub:
        return 400
    elif '360' in sub:
        return 360
    elif '350' in sub:
        return 350
    elif '300' in sub:
        return 300
    elif '250' in sub:
        return 250
    elif '230' in sub:
        return 230
    elif '200' in sub:
        return 200
    elif '150' in sub:
        return 150
    elif '125' in sub:
        return 125
    elif '110' in sub:
        return 110
    elif '100' in sub:
        return 100
    elif '90' in sub:
        return 90
    elif '85' in sub:
        return 85
    elif '80' in sub:
        return 80
    elif '75' in sub:
        return 75
    elif '70' in sub:
        return 70
    elif '65' in sub:
        return 65
    elif '60' in sub:
        return 60
    elif '50' in sub:
        return 50
    else:
        return 0      




# <!-- 
#         <form method="POST">
#             <table >
#                 ${ form }                    
#             </table>   
#             <input type="submit" value="Search"> 
#         </form>

#         <br>
#         <br>

#         <table>
#             <tr>
#                 <th>Title</th>               
#                 <th>Price</th>
#             </tr>
#             %for i in range (len(my_items)):            
#                 <tr>
#                     <td>${ my_items[i].title }</td>               
#                     <td>${ my_items[i].price }</td>
#                 </tr>          
#             %endfor
#         </table>

#         <br/>
#         <br /> -->

