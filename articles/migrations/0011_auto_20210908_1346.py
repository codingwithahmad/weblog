# Generated by Django 3.2.5 on 2021-09-08 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20210824_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='آدرس آی پی')),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', to='articles.IPAddress', verbose_name='بازدید ها'),
        ),
    ]
