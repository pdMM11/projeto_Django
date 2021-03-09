"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
#from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    path('Taxonomy/', views.TaxonomyView.as_view(), name='Taxonomy'),
    path('Host/', views.HostView.as_view(), name='Host'),
    path('Protein/', views.ProteinView.as_view(), name='Protein'),
    path('Peptide/', views.PeptideView.as_view(), name='Peptide'),
    path('Structure/', views.StructureView.as_view(), name='Structure'),
    path('PeptideStructure/', views.PeptideStructureView.as_view(), name='PeptideStructure'),
    path('References/', views.ReferencesView.as_view(), name='References'),
    

    #path('HostTable/', views.HostTable, name='HostTable'),


    path('HostSearch/', views.HostSearchView, name='HostSearch'),
    path('TaxonomySearch/', views.TaxonomySearchView, name='TaxonomySearch'),
    path('ProteinSearch/', views.ProteinSearchView, name='ProteinSearch'),
    path('PeptideSearch/', views.PeptideSearchView, name='PeptideSearch'),
    path('StructureSearch/', views.StructureSearchView, name='StructureSearch'),
    #path('PeptideStructure/', views.PeptideStructureView.as_view(), name='PeptideStructure'),
    path('ReferencesSearch/', views.ReferencesSearchView, name='ReferencesSearch'),


    path('HostAdd/', views.addHost, name='HostAdd'),
    path('TaxonomyAdd/', views.addTaxonomy, name='TaxonomyAdd'),


    #path('', Host.IndexView.as_view(), name='index'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
    #path('', views.Host.as_view(), name='Host'),
]

