from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic.edit import CreateView
from .models import Documento

class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *arqs, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

