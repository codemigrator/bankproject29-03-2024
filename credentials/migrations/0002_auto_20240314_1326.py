# Generated by Django 3.2.22 on 2024-03-14 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fromtable',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='fromtable',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='fromtable',
            name='branch',
            field=models.CharField(default='chalakudy', max_length=250),
        ),
        migrations.AlterField(
            model_name='fromtable',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='fromtable',
            name='district',
            field=models.CharField(default='thrissur', max_length=250),
        ),
        migrations.AlterField(
            model_name='fromtable',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]