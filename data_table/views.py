from django.shortcuts import render
from django_tables2 import RequestConfig
from django_tables2.export import TableExport
from .models import ShinyData
import django_tables2 as tables
from .variables import filter_option, GENDER_CHOICES, AGEGRP_CHOICES, LOCATION_CHOICES, CLIMATE_CHOICES, TIME_CHOICES, \
    SEASON_CHOICES, CITY_CHOICES, SVF_CHOICES, age_min, age_max, height_min, height_max, weight_max, weight_min, \
    metabolic_rate_min, metabolic_rate_max, clothing_index_min, clothing_index_max, thermal_history_min, \
    thermal_history_max, air_temp_min, air_temp_max, relative_humidity_min, relative_humidity_max, wind_speed_min, \
    wind_speed_max, global_temp_min, global_temp_max, mean_radiant_temp_min, mean_radiant_temp_max, radiation_min, \
    radiation_max, pet_min, pet_max, utci_min, utci_max

previous_setting = []

def isValid(x):
    return x != '' and x is not None


def DataFilter(t, request):

    isSelected = False

    tsv7_query = request.GET.getlist('thermal_sensation_vote_7')  # subjective assessment
    tsv9_query = request.GET.getlist('thermal_sensation_vote_9')
    tcv_query = request.GET.getlist('thermal_comfort_vote')
    tpv7_query = request.GET.getlist('thermal_preference_vote_7')
    tp_query = request.GET.getlist('thermal_preference')
    ta_query = request.GET.getlist('thermal_acceptance')
    wsv_query = request.GET.getlist('wind_sensation_vote')
    ssv_query = request.GET.getlist('solar_sensation_vote')
    hsv_query = request.GET.getlist('humidity_sensation_vote')

    if tsv7_query:
        isSelected = True
        t = t.filter(thermal_sensation_vote_7__in=tsv7_query)
        print(t)
    if tsv9_query:
        isSelected = True
        t = t.filter(thermal_sensation_vote_9__in=tsv9_query)
        print(t)
    if tcv_query:
        isSelected = True
        t = t.filter(thermal_comfort_vote__in=tcv_query)
    if tpv7_query:
        isSelected = True
        t = t.filter(thermal_preference_vote_7__in=tpv7_query)
    if tp_query:
        isSelected = True
        t = t.filter(thermal_preference__in=tp_query)
    if ta_query:
        isSelected = True
        t = t.filter(thermal_acceptance__in=ta_query)
    if wsv_query:
        isSelected = True
        t = t.filter(wind_sensation_vote__in=wsv_query)
    if ssv_query:
        isSelected = True
        t = t.filter(solar_sensation_vote__in=ssv_query)
    if hsv_query:
        isSelected = True
        t = t.filter(humidity_sensation_vote__in=hsv_query)

    gender_query = request.GET.get('gender_query')  # demography
    age_query = request.GET.get('age')
    agegrp_query = request.GET.getlist('age_grp')
    height_query = request.GET.get('height')
    weight_query = request.GET.get('weight')

    if isValid(gender_query):
        isSelected = True
        t = t.filter(gender=str(gender_query))

    if isValid(age_query) and age_query.split(',') != [f'{age_min:g}',f'{age_max:g}']:
        print('age')
        isSelected = True
        t = t.filter(age__range=age_query.split(','))

    if agegrp_query:
        print('agegrp')
        isSelected = True
        t = t.filter(agegrp__in=agegrp_query)

    if isValid(height_query) and height_query.split(',') != [f'{height_min:g}',f'{height_max:g}']:
        print('height')
        isSelected = True
        t = t.filter(height__range=height_query.split(','))

    if isValid(weight_query) and weight_query.split(',') != [f'{weight_min:g}',f'{weight_max:g}']:
        print('weight')
        t = t.filter(weight__range=weight_query.split(','))

    metabolic_rate_query = request.GET.get('metabolic_rate')  # individual activity background
    clothing_index_query = request.GET.get('clothing_index')
    thermal_history_query = request.GET.get('thermal_history')

    if isValid(metabolic_rate_query) and metabolic_rate_query.split(',') != [f'{metabolic_rate_min:g}',f'{metabolic_rate_max:g}']:
        print('metabolic rate')
        isSelected = True
        t = t.filter(metabolic_rate__range=metabolic_rate_query.split(','))
    if isValid(clothing_index_query) and clothing_index_query.split(',') != [f'{clothing_index_min:g}',f'{clothing_index_max:g}']:
        print('clothing index')
        isSelected = True
        t = t.filter(clothing_index__range=clothing_index_query.split(','))
    if isValid(thermal_history_query) and thermal_history_query.split(',') != [f'{thermal_history_min:g}',f'{thermal_history_max:g}']:
        print('thermal history')
        isSelected = True
        t = t.filter(thermal_history__range=thermal_history_query.split(','))

    air_temp_query = request.GET.get('air_temp')  # individual activity background
    relative_humidity_query = request.GET.get('relative_humidity')
    wind_speed_query = request.GET.get('wind_speed')
    global_temp_query = request.GET.get('global_temp')
    mean_radiant_temp_query = request.GET.get('mean_radiant_temp')
    radiation_query = request.GET.get('radiation')
    pet_query = request.GET.get('pet')
    utci_query = request.GET.get('utci')

    if isValid(air_temp_query) and air_temp_query.split(',') != [f'{air_temp_min:g}',f'{air_temp_max:g}']:
        print('air temperature')
        isSelected = True
        t = t.filter(air_temp__range=air_temp_query.split(','))
    if isValid(relative_humidity_query) and relative_humidity_query.split(',') != [f'{relative_humidity_min:g}',f'{relative_humidity_max:g}']:
        print('relative humidity')
        isSelected = True
        t = t.filter(relative_humidity__range=relative_humidity_query.split(','))
    if isValid(wind_speed_query) and wind_speed_query.split(',') != [f'{wind_speed_min:g}',f'{wind_speed_max:g}']:
        print('wind speed')
        isSelected = True
        t = t.filter(wind_speed__range=wind_speed_query.split(','))
    if isValid(global_temp_query) and global_temp_query.split(',') != [f'{global_temp_min:g}',f'{global_temp_max:g}']:
        print('global temp')
        isSelected = True
        t = t.filter(global_temp__range=global_temp_query.split(','))
    if isValid(mean_radiant_temp_query) and mean_radiant_temp_query.split(',') != [f'{mean_radiant_temp_min:g}',f'{mean_radiant_temp_max:g}']:
        print('mean radiant temp')
        isSelected = True
        t = t.filter(mean_radiant_temp__range=mean_radiant_temp_query.split(','))
    if isValid(radiation_query) and radiation_query.split(',') != [f'{radiation_min:g}',f'{radiation_max:g}']:
        print('radiation')
        isSelected = True
        t = t.filter(radiation__range=radiation_query.split(','))
    if isValid(pet_query) and pet_query.split(',') != [f'{pet_min:g}',f'{pet_max:g}']:
        print('pet')
        isSelected = True
        t = t.filter(pet__range=pet_query.split(','))
    if isValid(utci_query) and utci_query.split(',') != [f'{utci_min:g}',f'{utci_max:g}']:
        print('utci')
        isSelected = True
        t = t.filter(utci__range=utci_query.split(','))

    loc_query = request.GET.get('location')  # survey background
    climate_query = request.GET.get('climate')
    time_query = request.GET.get('time')
    season_query = request.GET.get('season')
    city_query = request.GET.get('city')
    svf_query = request.GET.get('svf')

    if loc_query != '---Select---':
        print('location')
        isSelected = True
        t = t.filter(loc=loc_query)
    if climate_query != '---Select---':
        print('climate')
        isSelected = True
        t = t.filter(climate=climate_query)
    if time_query != '---Select---':
        print('time')
        isSelected = True
        t = t.filter(time__range=time_query.split(' - '))
    if season_query != '---Select---':
        print('season')
        isSelected = True
        t = t.filter(season=season_query)
    if city_query != '---Select---':
        print('city')
        isSelected = True
        t = t.filter(city_country=city_query)
    if svf_query != '---Select---':
        print('svf')
        isSelected = True
        t = t.filter(svf=svf_query)

    if not isSelected:
        t = ShinyData.objects.all()
        print('no change')

    return t


def SelectColumnFilter(request):

    isChosen = False

    global previous_setting

    filter_choice = []

    if not previous_setting:
        if 'select' in request.POST:
            isChosen = True
            filter_choice = request.POST.getlist('column_choices')
            previous_setting = filter_choice

    else:
        isChosen = True
        if 'select' in request.POST:
            filter_choice = request.POST.getlist('column_choices')
            previous_setting = filter_choice
        else:
            if request.GET:
                filter_choice = previous_setting
            else:
                previous_setting = []

    return isChosen, filter_choice


def ShowData(request):

    isChosen, filter_choice = SelectColumnFilter(request)


    class ShinyDataTable(tables.Table):
        class Meta:
            model = ShinyData
            if isChosen:
                exclude = ["no"] + filter_choice
            else:
                exclude = ["no"]
            attrs = {'class': 'paleblue'}

    t = ShinyData.objects.all()

    if 'search' in request.GET:
        print('data filter')
        t = DataFilter(t, request)
    elif 'reset' in request.GET:
        t = ShinyData.objects.all()

    table = ShinyDataTable(t)
    RequestConfig(request).configure(table)

    export_format = request.GET.get('_export', None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response('Outdoor_Thermal_Comfort_Data.{}'.format(export_format))

    context = {
        'table': table,
        'filter_option': filter_option,
        'GENDER_CHOICES': GENDER_CHOICES,
        'AGEGRP_CHOICES': AGEGRP_CHOICES,
        'LOCATION_CHOICES': LOCATION_CHOICES,
        'CLIMATE_CHOICES': CLIMATE_CHOICES,
        'TIME_CHOICES': TIME_CHOICES,
        'SEASON_CHOICES': SEASON_CHOICES,
        'CITY_CHOICES': CITY_CHOICES,
        'SVF_CHOICES': SVF_CHOICES,
        'age_min': age_min,
        'age_max': age_max,
        'height_min': height_min,
        'height_max': height_max,
        'weight_min': weight_min,
        'weight_max': weight_max,
        'metabolic_rate_min': metabolic_rate_min,
        'metabolic_rate_max': metabolic_rate_max,
        'clothing_index_min': clothing_index_min,
        'clothing_index_max': clothing_index_max,
        'thermal_history_min': thermal_history_min,
        'thermal_history_max': thermal_history_max,
        'air_temp_min': air_temp_min,
        'air_temp_max': air_temp_max,
        'relative_humidity_min': relative_humidity_min,
        'relative_humidity_max': relative_humidity_max,
        'wind_speed_min': wind_speed_min,
        'wind_speed_max': wind_speed_max,
        'global_temp_min': global_temp_min,
        'global_temp_max': global_temp_max,
        'mean_radiant_temp_min': mean_radiant_temp_min,
        'mean_radiant_temp_max': mean_radiant_temp_max,
        'radiation_min': radiation_min,
        'radiation_max': radiation_max,
        'pet_min': pet_min,
        'pet_max': pet_max,
        'utci_min': utci_min,
        'utci_max': utci_max,
    }

    return render(request, 'data_table/index.html', context)
