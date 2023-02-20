# Generated by Django 4.1.5 on 2023-01-26 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('age', models.IntegerField()),
                ('preferred_language', models.CharField(choices=[('English', 'English'), ('Kiswahili', 'Kiswahili')], max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Female', 'female'), ('Transgender', 'Transgender'), ('Prefer Not to identify', 'Prefer Not to identify'), ('Male', 'Male')], max_length=100, null=True)),
                ('pronoun', models.CharField(choices=[('She/her', 'She/her'), ('He', 'Him'), ('Prefer Not to say', 'Prefer Not to say')], max_length=100, null=True)),
                ('person_with_disability', models.BooleanField(default=False)),
            ],
        ),
    ]
