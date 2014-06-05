from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from jitterbunk_app.models import Bunk, UserProfile
from django.db.models import Q
from django import forms
from django.forms import ModelForm
from django.utils import timezone


class BunkForm(ModelForm):
    class Meta:
        model = Bunk
        address = forms.CharField(max_length=15)


def profile(request, pk):

    user = get_object_or_404(UserProfile, pk=pk)

    # just bunked somebody
    if request.method == 'POST':
        form = BunkForm(request.POST)
        # raise NameError(form.data['username'])

        to_user = get_object_or_404(UserProfile, name=form.data['username'])
        b = Bunk(from_user=user, to_user=to_user, time=timezone.now())
        b.save()

    # try:
    user_bunk_list = Bunk.objects.filter(Q(from_user=user)
                                         | Q(to_user=user))
    return render_to_response('profile.html', {
        'user_bunk_list': user_bunk_list,
        'user': user,
        }, context_instance=RequestContext(request))
