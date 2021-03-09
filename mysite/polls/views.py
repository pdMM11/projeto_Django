import operator

from django.utils import timezone

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.models import Q



from .models import *


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        #Return the last five published questions.
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class HostView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        
        return Host.objects.all()

"""
def searchHost(request):
    query = request.GET.get('q')
    try:
        query = int(query)
    except ValueError:
        query = None
        results = None
    if query:
        results = Host.objects.get(idhost=query)
    context = RequestContext(request)
    return render_to_response('results.html', {"results": results,}, context_instance=context)
    """

class TaxonomyView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        
        return TaxanomyVirus.objects.all()


class ProteinView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        
        return Protein.objects.all()


class PeptideView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        
        return FusionPeptides.objects.all()


class StructureView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        
        return Structure.objects.all()

class PeptideStructureView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        
        return PeptideStructure.objects.all()


class ReferencesView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        
        return References.objects.all()


"""
###############

def HostTable(request):
    return render(request, 'polls/tableHost.html', {'Host': Host.objects.all()})


########################
"""

def HostSearchView(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(idhost__icontains=query) | Q(host__icontains=query)

            results= Host.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'polls/search_host.html', context)

        else:
            return render(request, 'polls/search_host.html')

    else:
        return render(request, 'polls/search_host.html')


def TaxonomySearchView(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(idtaxanomy__icontains=query) | Q(commonname__icontains=query) | Q(family__icontains=query) |  Q(genre__icontains=query) |  Q(species__icontains=query) | Q(subspecies__icontains=query) | Q(ncbitax__icontains=query)

            results= TaxanomyVirus.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'polls/search_tax.html', context)

        else:
            return render(request, 'polls/search_tax.html')

    else:
        return render(request, 'polls/search_tax.html')


def ProteinSearchView(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(idprotein__icontains=query) | Q(name__icontains=query) | Q(class_field__icontains=query) |  Q(activation__icontains=query) |  Q(name_fusogenic_unit__icontains=query) | Q(location_fusogenic__icontains=query) | Q(sequence_fusogenic__icontains=query) | Q(uniprotid__icontains=query) | Q(ncbiid__icontains=query) | Q(ncbiid__icontains=query)

            results= Protein.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'polls/search_protein.html', context)

        else:
            return render(request, 'polls/search_protein.html')

    else:
        return render(request, 'polls/search_protein.html')


def PeptideSearchView(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(idfusion_peptides__icontains=query) | Q(residues__icontains=query) | Q(sequence__icontains=query) |  Q(annotation_method__icontains=query) |  Q(exp_evidence__icontains=query) 

            results= FusionPeptides.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'polls/search_peptide.html', context)

        else:
            return render(request, 'polls/search_peptide.html')

    else:
        return render(request, 'polls/search_peptide.html')


def StructureSearchView(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(idstructure__icontains=query) | Q(exp_method__icontains=query) | Q(repository__icontains=query) 

            results= Structure.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'polls/search_structure.html', context)

        else:
            return render(request, 'polls/search_structure.html')

    else:
        return render(request, 'polls/search_structure.html')


#falta PeptideStructureView

def ReferencesSearchView(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(idreferences__icontains=query) | Q(type_reference__icontains=query) | Q(doi__icontains=query) 

            results= References.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'polls/search_ref.html', context)

        else:
            return render(request, 'polls/search_ref.html')

    else:
        return render(request, 'polls/search_ref.html')




############################################


def addHost(request):
    if request.method == 'POST':
        if request.POST.get('host'):
            
            new_host=Host()

            max_id = Host.objects.all().order_by("-idhost")[0]
        

            #new_host.idhost= request.POST.get('idHost')
            new_host.idhost = int(max_id.idhost) + 1
            
            new_host.host= request.POST.get('host')
            new_host.save()
                
            return render(request, 'polls/add_host.html')  

    else:
        return render(request,'polls/add_host.html')


def addTaxonomy(request):
    if request.method == 'POST':
        if request.POST.get('commonname'):
            
            new_tax=TaxanomyVirus()

            max_id = TaxanomyVirus.objects.all().order_by("-idtaxanomy")[0]
        
            new_tax.idtaxanomy = int(max_id.idtaxanomy) + 1
            
            new_tax.commonname= request.POST.get('commonname')
            
            if request.POST.get('family'): new_tax.family= request.POST.get('family')
            else: new_tax.family= None

            if request.POST.get('genre'): new_tax.genre= request.POST.get('genre')
            else: new_tax.genre= None

            if request.POST.get('species'): new_tax.species= request.POST.get('species')
            else: new_tax.species= None

            if request.POST.get('subspecies'): new_tax.subspecies= request.POST.get('subspecies')
            else: new_tax.subspecies= None

            if request.POST.get('ncbitax'): new_tax.ncbitax= request.POST.get('ncbitax')
            else: new_tax.ncbitax= None

            new_tax.save()
                
            return render(request, 'polls/add_tax.html')  

    else:
        return render(request,'polls/add_tax.html')