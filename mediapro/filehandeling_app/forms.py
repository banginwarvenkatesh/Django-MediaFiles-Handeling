from django.forms import ModelForm
from .models import VenueListing

class VenueForm(ModelForm):
    class Meta:
        model = VenueListing
        fields = "__all__"
        lables = {
            "name":"NAME",
            "address":"ADDRESS",
            "contact":"CONTACT",
            "media":"MEDIA"
        }