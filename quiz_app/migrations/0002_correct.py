# Generated by Django 2.0.5 on 2018-09-16 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Correct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_text', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_app.Question')),
            ],
        ),
    ]