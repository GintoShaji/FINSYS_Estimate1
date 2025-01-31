# Generated by Django 3.2.25 on 2024-06-20 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0005_auto_20240615_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fin_Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=10, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('place_of_supply', models.CharField(blank=True, max_length=100, null=True)),
                ('gst_type', models.CharField(max_length=100, null=True)),
                ('gstin', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pan_no', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('billing_street', models.CharField(blank=True, max_length=100, null=True)),
                ('billing_city', models.CharField(blank=True, max_length=100, null=True)),
                ('billing_state', models.CharField(blank=True, max_length=100, null=True)),
                ('billing_pincode', models.CharField(blank=True, max_length=100, null=True)),
                ('billing_country', models.CharField(blank=True, max_length=100, null=True)),
                ('ship_street', models.CharField(blank=True, max_length=100, null=True)),
                ('ship_city', models.CharField(blank=True, max_length=100, null=True)),
                ('ship_state', models.CharField(blank=True, max_length=100, null=True)),
                ('ship_pincode', models.CharField(blank=True, max_length=100, null=True)),
                ('ship_country', models.CharField(blank=True, max_length=100, null=True)),
                ('opening_balance', models.FloatField(blank=True, default=0.0, null=True)),
                ('opening_balance_due', models.FloatField(blank=True, default=0.0, null=True)),
                ('open_balance_type', models.CharField(blank=True, max_length=100, null=True)),
                ('current_balance', models.FloatField(blank=True, default=0.0, null=True)),
                ('credit_limit', models.FloatField(blank=True, default=0.0, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=150, null=True)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('LoginDetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('payment_terms', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finsys_App.fin_company_payment_terms')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Price_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, choices=[('Sales', 'Sales'), ('Purchase', 'Purchase')], default='Sales', max_length=15, null=True)),
                ('item_rate', models.CharField(blank=True, choices=[('percentage', 'Markup or Markdown the item rates by a percentage'), ('individual_rate', 'Enter the rate individually for each item')], default='percentage', max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, default='Indian Rupee', max_length=255, null=True)),
                ('up_or_down', models.CharField(default='None', max_length=100)),
                ('percentage', models.CharField(blank=True, max_length=100, null=True)),
                ('round_off', models.CharField(blank=True, default='None', max_length=100, null=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('status', models.CharField(blank=True, default='Active', max_length=15, null=True)),
                ('Company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('LoginDetails', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Customers_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('action', models.CharField(blank=True, choices=[('Created', 'Created'), ('Edited', 'Edited')], max_length=20, null=True)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('LoginDetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_customers')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Customers_Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, max_length=500, null=True)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_customers')),
            ],
        ),
        migrations.AddField(
            model_name='fin_customers',
            name='price_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finsys_App.fin_price_list'),
        ),
        migrations.AddField(
            model_name='fin_cnotification',
            name='Customers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_customers'),
        ),
    ]
