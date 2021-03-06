from django.views import generic
from .models import NewsStory
from django.urls import reverse_lazy
from .forms import StoryForm


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4]
        context['all_stories'] = NewsStory.objects.all()
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'


class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ViewAuthorStories(generic.ListView):
    template_name = 'news/viewAuthorStory.html'

    def get_queryset(self):
        return NewsStory.objects.all()

    def get_contect_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_stories'] = NewsStory.objects.filter(author=self.kwargs.get("author")).order_by('-pub_date')
        return context
        

