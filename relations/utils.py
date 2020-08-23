from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date


def get_age(date_object):
    today = date.today()
    age = today.year - date_object.year - ((today.month, today.day) < (date_object.month, date_object.day))
    return age


def get_bmi(height_cm, weight_kg):
    return "{:.2f}".format((weight_kg / (height_cm)**2) * 10000)


def paginate(request_obj, model_obj, pages):
    page = request_obj.GET.get('page', 1)
    paginator = Paginator(model_obj, pages)
    try:
        model_object = paginator.page(page)
    except PageNotAnInteger:
        model_object = paginator.page(1)
    except EmptyPage:
        model_object = paginator.page(paginator.num_pages)
    return model_object


blood_relationships = {
    "A+": {
        "gives": ("A+", "AB+", ),
        "receives": ("A+", "O+", "A-", "O-", ),
    },
    "B+": {
        "gives": ("B+", "AB+", ),
        "receives": ("B+", "O+", "B-", "O-", ),
    },
    "AB+": {
        "gives": ("AB+", ),
        "receives": ("A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-", ),
    },
    "O+": {
        "gives": ("A+", "B+", "AB+", "O+", ),
        "receives": ("O+", "O-", ),
    },
    "A-": {
        "gives": ("A+", "AB+", "A-", "AB-", ),
        "receives": ("A-", "O-", ),
    },
    "B-": {
        "gives": ("B+", "AB+", "B-", "AB-", ),
        "receives": ("B-", "O-", ),
    },
    "AB-": {
        "gives": ("AB+", "AB-", ),
        "receives": ("A-", "B-", "AB-", "O-", ),
    },
    "O-": {
        "gives": ("A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-", ),
        "receives": ("O-", ),
    },
}

gender = [
    ("M", "Male"),
    ("F", "Female")
]

blood_types = [
    ('A+', 'A+', ),
    ('B+', 'B+', ),
    ('AB+', 'AB+', ),
    ('O+', 'O+', ),
    ('A-', 'A-', ),
    ('B-', 'B-', ),
    ('AB-', 'AB-', ),
    ('O-', 'O-',),
]