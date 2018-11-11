# Generated by Django 2.0.5 on 2018-10-03 04:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0007_auto_20181003_0410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer_text1',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answer_text2',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answer_text3',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answer_text4',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_text',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_app.Question'),
        ),
    ]
