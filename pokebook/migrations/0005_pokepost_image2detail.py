# Generated by Django 4.0 on 2023-11-28 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokebook', '0004_pokepost_image2_alter_pokepost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokepost',
            name='image2detail',
            field=models.CharField(blank=True, choices=[('', 'もう一つのポケモンの画像を選んでください'), ('もう一つの姿', 'もう一つの姿'), ('リージョンフォーム', 'リージョンフォーム'), ('メガシンカ', 'メガシンカ'), ('キョダイマックス', 'キョダイマックス'), ('色違い', '色違い'), ('テラスタルした姿', 'テラスタルした姿'), ('レアなフォルム', 'レアなフォルム')], max_length=20, null=True, verbose_name='pokeimagedetail'),
        ),
    ]
