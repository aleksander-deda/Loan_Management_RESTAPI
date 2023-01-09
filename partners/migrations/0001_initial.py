# Generated by Django 4.1.3 on 2022-11-22 14:13

from django.db import migrations, models
import django.db.models.deletion
import partners.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backoffice', '0001_initial'),
        ('superpartners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('personalId', models.CharField(max_length=10, unique=True)),
                ('mobile', models.CharField(max_length=16)),
                ('nipt', models.CharField(max_length=13, unique=True)),
                ('isReferral', models.BooleanField(default=False)),
                ('rating', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, null=True)),
                ('activity', models.CharField(max_length=500)),
                ('accountNumber', models.CharField(max_length=30)),
                ('jsonDatas', models.JSONField(blank=True, null=True)),
                ('isUpdated', models.CharField(blank=True, default='No', max_length=20, null=True)),
                ('isConfirmed', models.BooleanField(default=False)),
                ('isActive', models.BooleanField(default=False)),
                ('isDeleted', models.BooleanField(default=False)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.bank')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.city')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.member')),
                ('superPartner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='superpartners.superpartner')),
            ],
            options={
                'db_table': 'partners',
            },
        ),
        migrations.CreateModel(
            name='PartnerProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('endDate', models.DateField(blank=True, null=True)),
                ('jsonDatas', models.JSONField(blank=True, null=True)),
                ('isUpdated', models.CharField(blank=True, default='No', max_length=20, null=True)),
                ('isConfirmed', models.BooleanField(default=False)),
                ('isActive', models.BooleanField(default=False)),
                ('isDeleted', models.BooleanField(blank=True, default=False, null=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('updatedDate', models.DateTimeField(auto_now=True, null=True)),
                ('isAssigned', models.BooleanField(default=False)),
                ('isExpired', models.BooleanField(default=False)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.partner')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.product')),
            ],
            options={
                'db_table': 'partner_products',
            },
        ),
        migrations.CreateModel(
            name='LoanConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minLoanTerm', models.IntegerField()),
                ('maxLoanTerm', models.IntegerField()),
                ('customerInterest', models.FloatField(blank=True, null=True)),
                ('applicationCommission', models.FloatField(blank=True, null=True)),
                ('bonus', models.FloatField(blank=True, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.product')),
            ],
            options={
                'db_table': 'loan_configs',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=128)),
                ('lastName', models.CharField(max_length=128)),
                ('personalId', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=250)),
                ('idCardDoc', models.FileField(upload_to='file/id_cards/%Y/%m/%d/', validators=[partners.validators.validate_file_extension])),
                ('clausoleDoc', models.FileField(upload_to='file/clausoles/%Y/%m/%d/', validators=[partners.validators.validate_file_extension])),
                ('birthdate', models.DateField()),
                ('gender', models.IntegerField(choices=[('M', 'M'), ('F', 'F')])),
                ('mobile', models.CharField(max_length=16)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('consent_boa', models.CharField(blank=True, max_length=10, null=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.city')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.partner')),
            ],
            options={
                'db_table': 'customers',
            },
        ),
    ]