# Generated by Django 3.2.17 on 2023-03-21 08:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CensusTable',
            fields=[
                ('sstart', models.DateTimeField(blank=True, null=True)),
                ('eend', models.DateTimeField(blank=True, null=True)),
                ('name_of_the_ulb', models.CharField(blank=True, max_length=50, null=True)),
                ('cencus_code', models.IntegerField(blank=True, null=True)),
                ('tree_common_name', models.CharField(blank=True, max_length=50, null=True)),
                ('scientific_name', models.CharField(blank=True, max_length=50, null=True)),
                ('tree_type', models.CharField(blank=True, max_length=50, null=True)),
                ('tree_gps_location', models.CharField(blank=True, max_length=220, null=True)),
                ('tree_gps_location_latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('tree_gps_location_longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('tree_gps_location_altitude', models.CharField(blank=True, max_length=50, null=True)),
                ('tree_gps_location_precision', models.CharField(blank=True, max_length=50, null=True)),
                ('photo', models.CharField(blank=True, max_length=70, null=True)),
                ('photo_url', models.BinaryField(blank=True, null=True)),
                ('tree_girth_in_inches', models.IntegerField(blank=True, null=True)),
                ('tree_height_in_cm', models.IntegerField(blank=True, null=True)),
                ('tree_canopy', models.CharField(blank=True, max_length=250, null=True)),
                ('total_area_in_sq_kms_under_all_trees', models.IntegerField(blank=True, null=True)),
                ('total_area_in_sq_kms_under_native_indegeniuos_trees', models.IntegerField(blank=True, null=True)),
                ('current_tree_age', models.IntegerField(blank=True, null=True)),
                ('age_of_tree_when_planted', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_plantation', models.DateField(blank=True, null=True)),
                ('present_status_of_tree', models.CharField(blank=True, max_length=50, null=True)),
                ('tree_ownership_plantation_initiated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('please_specify_tree_ownership', models.CharField(blank=True, max_length=50, null=True)),
                ('name_of_the_owner', models.CharField(blank=True, max_length=50, null=True)),
                ('field_version_field', models.CharField(blank=True, db_column='__version__', max_length=50, null=True)),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('field_uuid', models.CharField(blank=True, db_column='_uuid', max_length=50, null=True)),
                ('field_submission_time', models.DateField(blank=True, db_column='_submission_time', null=True)),
                ('field_validation_status', models.CharField(blank=True, db_column='_validation_status', max_length=50, null=True)),
                ('field_notes', models.CharField(blank=True, db_column='_notes', max_length=50, null=True)),
                ('field_status', models.CharField(blank=True, db_column='_status', max_length=50, null=True)),
                ('field_submitted_by', models.CharField(blank=True, db_column='_submitted_by', max_length=50, null=True)),
                ('field_tags', models.CharField(blank=True, db_column='_tags', max_length=50, null=True)),
                ('field_index', models.IntegerField(blank=True, db_column='_index', null=True)),
                ('tree_gps_location_geom', models.TextField(blank=True, null=True)),
                ('name_of_the_user', models.CharField(blank=True, max_length=250, null=True)),
                ('please_specify_common_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'census_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AhmedSchoolForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('lat', models.CharField(blank=True, max_length=255, null=True)),
                ('lng', models.CharField(blank=True, max_length=255, null=True)),
                ('altitude', models.CharField(blank=True, max_length=255, null=True)),
                ('gram_panchayat_name', models.CharField(blank=True, max_length=255, null=True)),
                ('principal_name', models.CharField(blank=True, max_length=255, null=True)),
                ('data_entry_date', models.DateField(blank=True, null=True)),
                ('officer_designation', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_no', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('school_level', models.CharField(blank=True, max_length=255, null=True)),
                ('school_type', models.CharField(blank=True, max_length=255, null=True)),
                ('sch_building_type', models.CharField(blank=True, max_length=255, null=True)),
                ('sch_building_use', models.CharField(blank=True, max_length=255, null=True)),
                ('sch_location', models.CharField(blank=True, max_length=255, null=True)),
                ('tot_boys_students', models.IntegerField(blank=True, null=True)),
                ('tot_girls_students', models.IntegerField(blank=True, null=True)),
                ('tot_diff_abled_students', models.IntegerField(blank=True, null=True)),
                ('drinking_water_availability_per_day', models.CharField(blank=True, max_length=255, null=True)),
                ('water_storage_in_school', models.CharField(blank=True, max_length=255, null=True)),
                ('is_water_quality_check_done', models.CharField(blank=True, max_length=255, null=True)),
                ('is_sanitization_done_timely', models.CharField(blank=True, max_length=255, null=True)),
                ('solid_waste_management', models.CharField(blank=True, max_length=255, null=True)),
                ('sewage_water_management', models.CharField(blank=True, max_length=255, null=True)),
                ('is_toilet_facility_available', models.CharField(blank=True, max_length=255, null=True)),
                ('tot_boys_toilets', models.IntegerField(blank=True, null=True)),
                ('tot_girls_toilets', models.IntegerField(blank=True, null=True)),
                ('tot_diff_abled_toilets', models.IntegerField(blank=True, null=True)),
                ('kitchen_hygiene', models.CharField(blank=True, max_length=255, null=True)),
                ('hand_wash_before_eating', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BasicPoshanModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=50)),
                ('self_made', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('external_support', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('community_level', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('govt_support', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('school_level', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('anganwadi', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('others_nutri', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('local_ngo', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('self_consumption', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('selling_surplus', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('surplus_addition', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('others_level', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('vegetable', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('backyard_poultry', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('backyard_fishery', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('others_scale', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('surplus', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('income', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('one_to_fourthousand_sq', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('seed_ngo', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('seasonal_vegetable', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('perennial_vegetable', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('fruitsgrown', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('dailyfruit', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('indigeous', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('open_cultivation', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('open_cultivation_multilayer', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('protectcultivation_shed_net', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('protectcultivation_shed_polyhouse', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('cultivation_others', models.CharField(blank=True, default='no', max_length=50, null=True)),
                ('month', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('well', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('pond', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('canel', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('bore_well', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('river', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('source_water', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('irrigation', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('school_name', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('any_weekly_class', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('weekly', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('any_innovative', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('mid_day_meal', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('surplus_selling', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('openfield_science_lab', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('hot_cooked_meal', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('school_child', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('school_scale', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('lat', models.CharField(default='', max_length=15)),
                ('lng', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='KoboPoshan',
            fields=[
                ('organization', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=100, null=True)),
                ('lat_lng', models.CharField(blank=True, max_length=100, null=True)),
                ('type_nutri', models.CharField(blank=True, max_length=100, null=True)),
                ('local_ngo', models.CharField(blank=True, max_length=100, null=True)),
                ('level_nutri', models.CharField(blank=True, max_length=100, null=True)),
                ('nutri_scale', models.CharField(blank=True, max_length=100, null=True)),
                ('selling_surplus', models.CharField(blank=True, max_length=255, null=True)),
                ('surplus_in_month', models.CharField(blank=True, max_length=100, null=True)),
                ('nutri_area', models.CharField(blank=True, max_length=100, null=True)),
                ('nutri_area_other', models.CharField(blank=True, max_length=100, null=True)),
                ('seeds', models.CharField(blank=True, max_length=100, null=True)),
                ('seasonal_veg', models.CharField(blank=True, max_length=100, null=True)),
                ('perennial_veg', models.CharField(blank=True, max_length=100, null=True)),
                ('fruits', models.CharField(blank=True, max_length=100, null=True)),
                ('avg_daily_fruits', models.CharField(blank=True, max_length=100, null=True)),
                ('seed_type', models.CharField(blank=True, max_length=100, null=True)),
                ('other_seed_type', models.CharField(blank=True, max_length=100, null=True)),
                ('earning_per_month', models.CharField(blank=True, max_length=100, null=True)),
                ('cultivation_type', models.CharField(blank=True, max_length=100, null=True)),
                ('other_cultivation_type', models.CharField(blank=True, max_length=100, null=True)),
                ('monthly_expenses', models.CharField(blank=True, max_length=100, null=True)),
                ('water_source', models.CharField(blank=True, max_length=100, null=True)),
                ('other_water_source', models.CharField(blank=True, max_length=100, null=True)),
                ('irrigation_water', models.CharField(blank=True, max_length=100, null=True)),
                ('org_name_school', models.CharField(blank=True, max_length=100, null=True)),
                ('weekly_classes', models.CharField(blank=True, max_length=100, null=True)),
                ('weekly_time', models.CharField(blank=True, max_length=100, null=True)),
                ('nutri_scale_school', models.CharField(blank=True, max_length=100, null=True)),
                ('other_nutri_scale_school', models.CharField(blank=True, max_length=100, null=True)),
                ('innovative_practices', models.CharField(blank=True, max_length=100, null=True)),
                ('endtime', models.DateTimeField(blank=True, null=True)),
                ('endtime1', models.DateTimeField(primary_key=True, serialize=False)),
                ('picture', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'kobo_poshan',
                'managed': b'I01\n',
            },
        ),
        migrations.CreateModel(
            name='PoshanFormInformation',
            fields=[
                ('organization_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('district_village_taluka_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('pin_code', models.IntegerField(blank=True, default='', null=True)),
                ('lat', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('lng', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('type_of_nutri', models.CharField(blank=True, default='', max_length=355, null=True)),
                ('name_of_ngo', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('level_nutri_garden', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('nutri_garden_scale', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('area_nutri_garden', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('ngo_year', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('type_seeds', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('seasonal_veg_name', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('perennial_veg_name', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('fruits_name', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('average', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('jan', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('feb', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('march', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('april', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('may', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('june', models.CharField(blank=True, default='no', max_length=50, null=True)),
                ('july', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('august', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('septmber', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('october', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('november', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('december', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('adult', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('children', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('month_earnings', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('month_expense', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('cultivation_type', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('rainy_season', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('raniy_winter_transition', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('summer', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('summer_rainy_transition', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('winter', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('winter_summer_transition', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('surplus_nutri_garden', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('water_source', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('cultivation', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('school_name', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('weekly_class', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('weekly_time', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('school_scale', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('school_practice', models.CharField(blank=True, default='no', max_length=250, null=True)),
                ('id', models.CharField(blank=True, default='no', max_length=250, primary_key=True, serialize=False)),
                ('add_photo', models.CharField(blank=True, default='no', max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PoshanInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=100)),
                ('district_village_taluka_name', models.CharField(max_length=100)),
                ('pin_code', models.IntegerField(blank=True, null=True)),
                ('lat', models.CharField(max_length=15)),
                ('lng', models.CharField(max_length=15)),
                ('type_of_nutri', models.CharField(max_length=50)),
                ('name_of_ngo', models.CharField(max_length=100)),
                ('area_nutri_garden', models.CharField(max_length=100)),
                ('seasonal_veg_name', models.CharField(max_length=100)),
                ('perennial_veg_name', models.CharField(max_length=100)),
                ('fruits_name', models.CharField(max_length=100)),
                ('month_earnings', models.IntegerField(blank=True, null=True)),
                ('level_nutri_garden', models.CharField(max_length=100)),
                ('nutri_garden_scale', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UploadSeedModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('picture', models.ImageField(blank=True, default='SeedPics/noImage.jpg', null=True, upload_to='SeedPics/')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('village', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=8, null=True)),
                ('lat', models.CharField(max_length=15)),
                ('lng', models.CharField(max_length=15)),
                ('seed_nm', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'home_uploadseedmodel',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='uploadpicturemodel',
            options={'managed': True},
        ),
        migrations.RemoveField(
            model_name='uploadpicturemodel',
            name='area',
        ),
        migrations.RemoveField(
            model_name='uploadpicturemodel',
            name='nutri_nm',
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='anganwadi',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='any_innovative',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='any_weekly_class',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='backyard_fishery',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='backyard_poultry',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='bore_well',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='canel',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='community_level',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='cultivation_others',
            field=models.CharField(blank=True, default='no', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='dailyfruit',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='external_support',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='fruitsgrown',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='govt_support',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='hot_cooked_meal',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='income',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='indigeous',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='irrigation',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='local_ngo',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='mid_day_meal',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='month',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='nal',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='one_to_fourthousand_sq',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='open_cultivation',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='open_cultivation_multilayer',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='openfield_science_lab',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='organization',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='others_level',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='others_nutri',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='others_scale',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='perennial_vegetable',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='pond',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='protectcultivation_shed_net',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='protectcultivation_shed_polyhouse',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='river',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='school_child',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='school_level',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='school_name',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='school_scale',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='seasonal_vegetable',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='seed_ngo',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='self_consumption',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='self_made',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='selling_surplus',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='source_water',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='submission_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='surplus',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='surplus_addition',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='surplus_selling',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='type',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='vegetable',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='weekly',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadpicturemodel',
            name='well',
            field=models.CharField(blank=True, default='no', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='uploadwellpicturemodel',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='uploadwellpicturemodel',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='uploadwellpicturemodel',
            name='water_quality',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='uploadpicturemodel',
            name='district',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='uploadpicturemodel',
            name='lat',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='uploadpicturemodel',
            name='lng',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='uploadpicturemodel',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='uploadpicturemodel',
            name='picture',
            field=models.ImageField(blank=True, default='PoshanVatikaPics/noImage.jpg', null=True, upload_to='PoshanVatikaPics/'),
        ),
        migrations.AlterField(
            model_name='uploadpicturemodel',
            name='pincode',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='uploadwellpicturemodel',
            name='picture',
            field=models.ImageField(blank=True, default='WellPics/noImage.jpg', null=True, upload_to='WellPics/'),
        ),
    ]