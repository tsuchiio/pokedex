from django.forms import ModelForm, Select,Form
from .models import Pokepost
from django import forms
class PokepostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['age'].widget = Select(choices=[
        ('赤・緑', '赤・緑'),
        ('金・銀', '金・銀'),
        ('ルビー・サファイア・エメラルド', 'ルビー・サファイア・エメラルド'),
        ('ダイヤモンド・パール・プラチナ', 'ダイヤモンド・パール・プラチナ'),
        ('ブラック・ホワイト', 'ブラック・ホワイト'),
        ('X・Y', 'X・Y'),
        ('サン・ムーン','サン・ムーン'),
        ('ソード・シールド・Legendsアルセウス','ソード・シールド・Legendsアルセウス'),
        ('スカーレット・バイオレット','スカーレット・バイオレット'),
    ])
        self.fields['type1'].wedget=Select(choices=[
            ('選択して下さい','選択してください'),
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
        ])
        self.fields['type2'].wedget=Select(choices=[
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
        ])
    class Meta:
        model = Pokepost
        fields = ['num','name','age','image','image2','image2detail','type1','type2','detail']

class PokedexFilter(Form):
    GENERATION_CHICES=[
        ('すべて','すべて'),
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
    SORT_CHOICES = [
        ('num','num'),
        ('-posted_at','-posted_at'),
    ]
    
    age = forms.ChoiceField(choices=[GENERATION_CHICES], required=False)
    type_filter = forms.CharField(max_length=10,required=False)
    name_filter = forms.CharField(max_length=20,required=False)
    sort_by = forms.ChoiceField(choices=SORT_CHOICES,required=False)
    
class ContactForm(forms.Form):
    name = forms.CharField(label='Full Name')
    email = forms.EmailField(label='Mail Adress')
    title = forms.CharField(label='Title')
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = ''
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = ''
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = ''
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = ''
        self.fields['message'].widget.attrs['class'] = 'form-control'