import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from harold.base.forms import FeedbackForm
from harold.base.models import Feedback


def index(request):
    feedback_list = Feedback.objects.all()
    pager = Paginator(feedback_list, 50)
    page = request.GET.get('page')

    try:
        feedback = pager.page(page)
    except PageNotAnInteger:
        feedback = pager.page(1)
    except EmptyPage:
        feedback = pager.page(pager.num_pages)

    return render(request, 'index.html', {'feedback': feedback, 'nav': 'dashboard'})


def submit_feedback(request):
    form = FeedbackForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data

        fb = Feedback(
            sentiment=data['sentiment'],
            text=data['text'],
            email=data['email']
        )
        
        fb.save()
        return HttpResponseRedirect(reverse('base.thanks'))

    return render(request, 'feedback.html', {'form': form, 'nav': 'feedback'})


def thanks(request):
    return render(request, 'thanks.html')


# FIXME - needs permission
def modify_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)
    action = request.GET.get('action')

    if action == 'note' and request.method == 'POST':
        note = request.POST.get('note', '')
        if note:
            metadata = u'{0} wrote on {1}:'.format(
                request.user.email, datetime.datetime.now().ctime())
            feedback.notes = '{0}\n\n{1}\n{2}'.format(
                feedback.notes,
                metadata,
                note)
            feedback.save()

    elif action == 'assign':
        user_id = request.GET.get('user_id')

        if user_id is None:
            return HttpResponseBadRequest()

        feedback.assigned_to_id = user_id
        feedback.save()

    elif action == 'open':
        feedback.closed = False
        feedback.save()

    elif action == 'close':
        feedback.closed = True
        feedback.save()

    else:
        return HttpResponseBadRequest()

    return HttpResponseRedirect(reverse('base.view_feedback', args=(feedback_id,)))

    
# FIXME -- needs permission
def view_feedback(request, feedback_id):
    feedback = Feedback.objects.get(id=feedback_id)
    return render(request, 'view_feedback.html', {'feedback': feedback})
