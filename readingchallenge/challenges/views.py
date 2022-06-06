from django.views import generic
from .models import Challenge, ChallengeForm
from django.urls import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'challenges/index.html'

    def get_queryset(self):
        '''Return all challenges.'''
        return Challenge.objects.order_by("date_created")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_challenge'] = Challenge.objects.all()[:1]
        context['all_challenges'] = Challenge.objects.all()
        return context

class ChallengeView(generic.DetailView):
    model = Challenge
    template_name = 'challenges/challenge.html'
    context_object_name = 'challenge'

class AddChallengeView(generic.CreateView):
    form_class = ChallengeForm
    context_object_name = 'challengeForm'
    template_name = 'challenges/createChallenge.html'
    success_url = reverse_lazy('challenges:index')

    def form_valid(self, form): 
        #set author to user logged in
        form.instance.author = self.request.user
        return super().form_valid(form)


# research how to update Challenges
# class UpdateChallengeView(generic.UpdateView):
#     form_class = UpdateChallengeForm
#     model = Challenge
#     template_name = 'challenges/updateChallenge.html'

