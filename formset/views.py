from django.forms import inlineformset_factory
from django.shortcuts import render
from formset.models import Setup, Specification
from formset.forms import SetupForm, SpecificationForm


def home(request):
    setup = Setup()
    setup_form = SetupForm(instance=setup)

    SpecInitFormset = inlineformset_factory(Setup, Specification, can_delete=False, extra=2, fields='__all__')
    spec_formset = SpecInitFormset()

    if request.method == 'POST':
        setup_form = SetupForm(request.POST)

        spec_formset = SpecInitFormset(request.POST, request.FILES)
        if setup_form.is_valid():
            created_setup = setup_form.save(commit=False)
            spec_formset = SpecInitFormset(request.POST, request.FILES, instance=created_setup)

            if spec_formset.is_valid():
                created_setup.save()
                spec_formset.save()

    return render(request, 'home.html',
                  {'title': 'Testing formset', 'setup_form': setup_form, 'formset': spec_formset})
