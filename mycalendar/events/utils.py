from .models import Event


def form_validation(form):
    if Event.objects.filter(day=form.instance.day, is_marked_10=True).exists():
        if form.cleaned_data['is_marked_10']:
            form.add_error('is_marked_11', "Запись на консультацию уже существует")
            return False
    if Event.objects.filter(day=form.instance.day, is_marked_11=True).exists():
        if form.cleaned_data['is_marked_11']:
            form.add_error('is_marked_11', "Запись на консультацию уже существует")
            return False
    if Event.objects.filter(day=form.instance.day, is_marked_12=True).exists():
        if form.cleaned_data['is_marked_12']:
            form.add_error('is_marked_11', "Запись на консультацию уже существует")
            return False
    if Event.objects.filter(day=form.instance.day, is_marked_13=True).exists():
        if form.cleaned_data['is_marked_13']:
            form.add_error('is_marked_11', "Запись на консультацию уже существует")
            return False
    if Event.objects.filter(day=form.instance.day, is_marked_14=True).exists():
        if form.cleaned_data['is_marked_14']:
            form.add_error('is_marked_11', "Запись на консультацию уже существует")
            return False
    if Event.objects.filter(day=form.instance.day, is_marked_16=True).exists():
        if form.cleaned_data['is_marked_16']:
            form.add_error('is_marked_11', "Запись на консультацию уже существует")
    return True
