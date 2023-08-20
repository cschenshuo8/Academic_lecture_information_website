from django import forms
from hello.models import Publisher
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
class PublisherForm(forms.ModelForm):
    # name = forms.CharField(label="名称", error_messages={"required": "这个项必须填写"})
    # address = forms.CharField(label="地址", error_messages={"required": "这个项必须填写"})
    # city = forms.CharField(label="城市", error_messages={"required": "这个项必须填写"})
    # state_province = forms.CharField(label="省份", error_messages={"required": "这个项必须填写"})
    # country = forms.CharField(label="国家", error_messages={"required": "这个项必须填写"})
    # website = forms.URLField(label="网址", error_messages={"required": "这个项必须填写"})

    class Meta:
        model = Publisher
        exclude = ("id",)


