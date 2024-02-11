# Generated by Django 4.2.4 on 2023-09-20 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_hotelbooking_hotel_alter_hotelbooking_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amenities',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='hotelbooking',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='hotelimages',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='booking_type',
            field=models.CharField(choices=[('Pre Paid', 'Pre Paid'), ('Post Paid', 'Post Paid')], max_length=100),
        ),
    ]
