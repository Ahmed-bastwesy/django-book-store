# Generated by Django 4.0.4 on 2022-04-20 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('publish_date', models.DateField(null=True)),
                ('add_to_site', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField()),
                ('appropriate', models.CharField(choices=[('child', 'under 8'), ('between', '8-15'), ('adult', 'adults')], default='adult', max_length=100)),
                ('image', models.URLField()),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
            ],
        ),
    ]
