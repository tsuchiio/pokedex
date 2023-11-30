from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

class Pokename(models.Model):
    AGE_CHOICES = [
        ('赤・緑', '赤・緑'),
        ('金・銀', '金・銀'),
        ('ルビー・サファイア・エメラルド', 'ルビー・サファイア・エメラルド'),
        ('ダイヤモンド・パール・プラチナ', 'ダイヤモンド・パール・プラチナ'),
        ('ブラック・ホワイト', 'ブラック・ホワイト'),
        ('X・Y', 'X・Y'),
        ('サン・ムーン','サン・ムーン'),
        ('ソード・シールド・Legendsアルセウス','ソード・シールド・Legendsアルセウス'),
        ('スカーレット・バイオレット','スカーレット・バイオレッ'),
    ]
    name = models.CharField(verbose_name='ポケモンの名前',max_length=20)
    category = models.CharField(verbose_name='ポケモンの世代', max_length=50,choices=AGE_CHOICES)
    def __str__(self):
        return f"{self.name} ({self.category})"

class Pokepost(models.Model):
    user = models.ForeignKey(
        CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    num = models.PositiveIntegerField(verbose_name='図鑑ナンバー', unique=True,default=0)
    name = models.CharField(verbose_name='ポケモンの名前',max_length=20)
    age = models.CharField(
        verbose_name='pokeage',
        max_length=50,
        choices=[
        ('赤・緑', '赤・緑'),
        ('金・銀', '金・銀'),
        ('ルビー・サファイア・エメラルド', 'ルビー・サファイア・エメラルド'),
        ('ダイヤモンド・パール・プラチナ', 'ダイヤモンド・パール・プラチナ'),
        ('ブラック・ホワイト', 'ブラック・ホワイト'),
        ('X・Y', 'X・Y'),
        ('サン・ムーン','サン・ムーン'),
        ('ソード・シールド・Legendsアルセウス','ソード・シールド・Legendsアルセウス'),
        ('スカーレット・バイオレット','スカーレット・バイオレット'),
        ]
    )
    image = models.ImageField(
        verbose_name='pokeimage',
        upload_to='pokeimages'
    )
    image2 = models.ImageField(
        verbose_name='pokeimage2',
        upload_to='pokeimages',
        blank=True,
        null=True
    )
    image2detail = models.CharField(
        verbose_name='pokeimagedetail',
        max_length=20,
        blank=True,
        null=True,
        choices=[
            ("","もう一つのポケモンの画像について選んでください"),
            ("もう一つの姿","もう一つの姿"),
            ("リージョンフォーム","リージョンフォーム"),
            ("メガシンカ","メガシンカ"),
            ("キョダイマックス","キョダイマックス"),
            ("色違い","色違い"),
            ("テラスタルした姿","テラスタルした姿"),
            ("レアなフォルム","レアなフォルム"),
        ]
    )
    type1 = models.CharField(
        verbose_name='poketype1',
        max_length=20,
        choices=[
            ('','選択してください'),
            ('ノーマル','ノーマル'),
            ('ほのお','ほのお'),
            ('みず','みず'),
            ('くさ','くさ'),
            ('でんき','でんき'),
            ('こおり','こおり'),
            ('かくとう','かくとう'),
            ('どく','どく'),
            ('じめん','じめん'),
            ('ひこう','ひこう'),
            ('エスパー','エスパー'),
            ('むし','むし'),
            ('いわ','いわ'),
            ('ゴースト','ゴースト'),
            ('ドラゴン','ドラゴン'),
            ('あく','あく'),
            ('はがね','はがね'),
            ('フェアリー','フェアリー')
        ],
        default=''
    )
    type2 = models.CharField(
        verbose_name='poketype2',
        max_length=20, blank=True,null=True,
        choices=[
                ('','なし'),
                ('ノーマル','ノーマル'),
                ('ほのお','ほのお'),
                ('みず','みず'),
                ('くさ','くさ'),
                ('でんき','でんき'),
                ('こおり','こおり'),
                ('かくとう','かくとう'),
                ('どく','どく'),
                ('じめん','じめん'),
                ('ひこう','ひこう'),
                ('エスパー','エスパー'),
                ('むし','むし'),
                ('いわ','いわ'),
                ('ゴースト','ゴースト'),
                ('ドラゴン','ドラゴン'),
                ('あく','あく'),
                ('はがね','はがね'),
                ('フェアリー','フェアリー')
            ],
        default=''
    )
    detail = models.TextField(
        verbose_name='pokedetail',
    )

    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )
    def get_absolute_url(self):
        return reverse("pokebook:pokedetail", args=[str(self.id)])
    
    def __str__(self):
        return f"{self.num} - {self.name} - {self.type1}"