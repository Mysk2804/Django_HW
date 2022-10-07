# Generated by Django 4.1.2 on 2022-10-07 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название раздела')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
            },
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основной')),
                ('article_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='art_name', to='articles.article', verbose_name='Тематика')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='articles.tags', verbose_name='Название')),
            ],
            options={
                'ordering': ('-is_main',),
            },
        ),
        migrations.AddField(
            model_name='article',
            name='name_scope',
            field=models.ManyToManyField(related_name='scopes', through='articles.Scope', to='articles.tags', verbose_name='Тематика раздела'),
        ),
    ]
