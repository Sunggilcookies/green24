from django import forms
from custom.models import Help, Answer


# 포스트 폼 생성
class HelpForm(forms.ModelForm):
    class Meta:
        model = Help  # Help 객체 생성
        fields = ['title', 'email', 'content', ]
        labels = {
            'title': '제목',
            'email': '이메일',
            'content': '내용',


        }

