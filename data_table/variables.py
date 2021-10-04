from django.db.models import Max, Min
from .models import ShinyData

filter_option = {str(f.verbose_name): str(f.name) for f in ShinyData._meta.get_fields()[1:]}
FIRST_CHOICES = [i for i in range(-4,5)]
SECOND_CHOICES = [i for i in range(-3,4)]
THIRD_CHOICES = [i for i in range(-1,2)]
GENDER_CHOICES = [i for i in ShinyData.objects.exclude(gender=None).exclude(gender='N/A').values_list('gender', flat=True).distinct()]
AGEGRP_CHOICES = [i for i in ShinyData.objects.exclude(agegrp=None).values_list('agegrp', flat=True).distinct()]
LOCATION_CHOICES = ['---Select---'] + [i for i in ShinyData.objects.values_list('loc', flat=True).distinct()]
CLIMATE_CHOICES = ['---Select---'] + [i for i in ShinyData.objects.values_list('climate', flat=True).distinct()]
TIME_CHOICES = ['---Select---'] + ['6:00 - 8:59', '9:00 - 11:59', '12:00 - 14:59', '15:00 - 17:59']
SEASON_CHOICES = ['---Select---'] + [i for i in ShinyData.objects.values_list('season', flat=True).distinct()]
CITY_CHOICES = ['---Select---'] + [i for i in ShinyData.objects.values_list('city_country', flat=True).distinct()]
SVF_CHOICES = ['---Select---'] + [i for i in ShinyData.objects.exclude(svf=None).values_list('svf', flat=True).distinct()[:5]]
age_min = ShinyData.objects.aggregate(Min('age')).get('age__min')
age_max = ShinyData.objects.aggregate(Max('age')).get('age__max')
height_min = ShinyData.objects.aggregate(Min('height')).get('height__min')
height_max = ShinyData.objects.aggregate(Max('height')).get('height__max')
weight_min = ShinyData.objects.aggregate(Min('weight')).get('weight__min')
weight_max = ShinyData.objects.aggregate(Max('weight')).get('weight__max')

metabolic_rate_min = ShinyData.objects.aggregate(Min('metabolic_rate')).get('metabolic_rate__min')
metabolic_rate_max = ShinyData.objects.aggregate(Max('metabolic_rate')).get('metabolic_rate__max')
clothing_index_min = ShinyData.objects.aggregate(Min('clothing_index')).get('clothing_index__min')
clothing_index_max = ShinyData.objects.aggregate(Max('clothing_index')).get('clothing_index__max')
thermal_history_option = ShinyData.objects.values_list('thermal_history', flat=True).distinct()

thermal_history_list = []

for value in thermal_history_option:
    try:
        thermal_history_list.append(float(value))
    except:
        pass

thermal_history_min = min(thermal_history_list)
thermal_history_max = max(thermal_history_list)

air_temp_min = ShinyData.objects.aggregate(Min('air_temp')).get('air_temp__min')
air_temp_max = ShinyData.objects.aggregate(Max('air_temp')).get('air_temp__max')
relative_humidity_min = ShinyData.objects.aggregate(Min('relative_humidity')).get('relative_humidity__min')
relative_humidity_max = ShinyData.objects.aggregate(Max('relative_humidity')).get('relative_humidity__max')
wind_speed_min = ShinyData.objects.aggregate(Min('wind_speed')).get('wind_speed__min')
wind_speed_max = ShinyData.objects.aggregate(Max('wind_speed')).get('wind_speed__max')
global_temp_min = ShinyData.objects.aggregate(Min('global_temp')).get('global_temp__min')
global_temp_max = ShinyData.objects.aggregate(Max('global_temp')).get('global_temp__max')
mean_radiant_temp_min = ShinyData.objects.aggregate(Min('mean_radiant_temp')).get('mean_radiant_temp__min')
mean_radiant_temp_max = ShinyData.objects.aggregate(Max('mean_radiant_temp')).get('mean_radiant_temp__max')
radiation_min = ShinyData.objects.aggregate(Min('radiation')).get('radiation__min')
radiation_max = ShinyData.objects.aggregate(Max('radiation')).get('radiation__max')
pet_min = ShinyData.objects.aggregate(Min('pet')).get('pet__min')
pet_max = ShinyData.objects.aggregate(Max('pet')).get('pet__max')
utci_min = ShinyData.objects.aggregate(Min('utci')).get('utci__min')
utci_max = ShinyData.objects.aggregate(Max('utci')).get('utci__max')
