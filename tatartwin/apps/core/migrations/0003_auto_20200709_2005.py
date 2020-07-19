# Generated by Django 3.0.7 on 2020-07-09 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20200608_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examples',
            name='trans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='examples', to='core.Translations', verbose_name='Пример'),
        ),
        migrations.AlterField(
            model_name='translations',
            name='tatar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='core.Tatar', verbose_name='Татарское слово'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('sent_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Оставлено')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Юзер')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.Tatar', verbose_name='Слово')),
            ],
            options={
                'verbose_name': 'История',
                'verbose_name_plural': 'История',
                'ordering': ['-sent_timestamp'],
            },
        ),
    ]