from django import forms
from .models import Godtk

class GodtkForm(forms.ModelForm):
    #메타데이터 :  데이터의 데이터
    #ex) 사진 한장 (촬영장비이름, 촬영환경 등)
    company_name = forms.CharField(
        label='업체이름',
        widget=forms.TextInput(
            attrs={
                'class':'company_name',
                'placeholder':'업체이름'
            }
        )
    )
    event_title = forms.CharField(
        label='이벤트이름',
        widget=forms.TextInput(
            attrs={
                'class':'event_title',
                'placeholder':'이벤트이름'
            }
        )
    )
    start_date = forms.CharField(
        label='이벤트시작날짜',
        widget=forms.TextInput(
            attrs={
                'class':'start_date',
                'placeholder':'이벤트시작날짜'
            }
        )
    )
    end_date = forms.CharField(
        label='이벤트끝나는날짜',
        widget=forms.TextInput(
            attrs={
                'class':'end_date',
                'placeholder':'이벤트끝나는날짜'
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class':'content',
                'placeholder':'내용입력',
                'rows':5,
                'cols':30
            }
        )
    )
    tag = forms.CharField(
        label='해시태그',
        widget=forms.TextInput(
            attrs={
                'class':'hashtag',
                'placeholder':'해시태그',
                'rows':5,
                'cols':30
            }
        )
    )
    event_url = forms.CharField(
        label='event_url',
        widget=forms.TextInput(
            attrs={
                'class':'event_url',
                'placeholder':'event_url'
            }
        )
    )
    img_path = forms.ImageField(label='img_path', required=False)

    class Meta:
        model = Godtk
        #fields = '__all__' #전체가져오기
        fields = ('event_title','company_name','start_date','end_date','tag','content','event_url','img_path') #선택해서 데이터 가져오기