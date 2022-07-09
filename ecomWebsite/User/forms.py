from django.contrib.auth.forms import UserCreationForm
from User.models import regUser, userProfile
from django.forms import ModelForm

# Create your forms here

class createregUser(UserCreationForm):
    class Meta:
        model = regUser
        fields = ('email',)


class userProfileForm(ModelForm):
    class Meta:
        model = userProfile
        fields = '__all__'
        exclude = ('user',)