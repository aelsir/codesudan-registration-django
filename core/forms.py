from cProfile import label
from django.db.models.base import Model
from django.forms import ModelForm, fields, inlineformset_factory, modelformset_factory, widgets
from .models import Batch, Registration, Student
from django import forms


# core and login form
class register_login_form(ModelForm):
    class Meta:
        model=Student
        fields=["username", "password"]
        labels={
            "username": "رقم التلفون",
            "password": "رقم الأمان",
        }
        help_texts={
            "username": "الرجاء إدخال رقم تلفونك المكون من 10 أرقام",
            "password": "إختار رقم واحد بين 0-9 لتسجيل الدخول بأمان في المستقبل"
        }
        widgets={
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control w-25 d-flex", "type": "number", "min": "0", "max": "9", "size": "20",})
        }
        required={
            "username",
            "password"
        }


class student_details_from(ModelForm):
    class Meta:
        model=Student

        SUDAN_STATES = [
            ("Outside Sudan", "خارج السودان"),
            ("Khartoum", "الخرطوم"),
            ("North Kordofan", "شمال كردفان"),
            ("Northern", "الشمالية"),
            ("Kassala", "كسّلا"),
            ("Blue Nile", "النيل الأزرق"),
            ("North Darfur", "شمال دارفور"),
            ("South Darfur", "جنوب دارفور"),
            ("South Kordofan", "جنوب كردفان"),
            ("Al Jazirah", "الجزيرة"),
            ("White Nile", "النيل الأبيض"),
            ("River Nile", "نهر النيل"),
            ("Red Sea", "البحر الأحمر"),
            ("Al Qadarif", "القضارف"),
            ("Sennar", "سنّار"),
            ("West Darfur", "غرب دارفور"),
            ("Central Darfur", "وسط دارفور"),
            ("East Darfur", "شرق دارفور"),
            ("East Darfur", "غرب كردفان"),
            ]

        OCCUPATIONS = [
            ("Student", "طالب"),
            ("Graduated", "خريج"),
            ("Employee", "عامل"),
            ("Other", "أخرى"),
            ]

        GENDER_CHOICE = [("M", 'ذكر'), ("F", "أنثى")]
        UNIVERSITY = [
            ("University of Khartoum", "جامعة الخرطوم"),
            ("Sudan University of Science and Technology", "جامعة السودان للعلوم و التكنلوجيا"),
            ("Omdurman Islamic University", "جامعة أمدرمان الإسلامية"),
            ("Al Neelain University", "جامعة النيلين"),
            ("National Ribat University", "جامعة الرباط الوطني"),
            ("Aljazeera University", "جامعة الجزيرة"),
            ("Ahfad University for Women", "جامعة الأحفاد للبنات"),
            ("Alzaiem Alazhari University", "جامعة الزعيم الأزهري"),
            ("Karary University", "جامعة كرري"),
            ("University of Science and Technology", "جامعة العلوم و التقانة"),
            ("The Future university", "جامعة المستقبل"),
            ("University of Medical Sciences and Technology", "جامعة العلوم الطبية والتكنولوجيا"),
            ("Sudan international University", "جامعة السودان المفتوحة"),
            ("Other", "أخرى")
            ]

        fields=["first_name", "father_name", "email", "gender", "birthday", "occupation", "university", "specialization", "state", "address"]
        labels = {
            "first_name": "إسمك",
            "father_name":"إسم الوالد",
            "email":"بريدك الإلكتروني",
            "gender": "النوع",
            "birthday":"تاريخ ميلادك",
            "occupation":"العمل",
            "university":"الجامعة",
            "specialization":"التخصص",
            "state":"الولاية",
            "address":"العنوان",
        }
        required = (
            "first_name",
            "father_name",
            "email",
            "gender",
            "birthday",
            "occupation",
            "university",
            "specialization",
            "state",
        )
        widgets = {
            
            "first_name": forms.TextInput(attrs={"class": "form-control mb-2", "required": True}),
            "father_name": forms.TextInput(attrs={"class": "form-control", "required": True}),
            "email": forms.EmailInput(attrs={"class": "form-control", "required": True}),
            "gender": forms.Select(choices=GENDER_CHOICE, attrs={"class": "form-select", "required": True}),
            "birthday": forms.DateInput(attrs={"type": "date", "required": True}),
            "occupation": forms.Select(choices=OCCUPATIONS, attrs={"class": "form-select", "required": True}),
            "university": forms.Select(choices=UNIVERSITY, attrs={"class": "form-select", "required": True}), 
            "specialization": forms.TextInput(attrs={"class": "form-control", "required": True}), 
            "state": forms.Select(choices=SUDAN_STATES, attrs={"class": "form-select"}), 
            "address": forms.TextInput(attrs={"class": "form-control"}),

            

        }


class new_enrollment_form_1(ModelForm):
    class Meta:
        model=Batch
        fields = ['program', 'number', 'starting_at']

        
class new_registration_batch(ModelForm):
    class Meta:
        model= Batch
        fields = ["id", "program", "starting_at", "number", "ending_at"]

        labels = {
            "number": "ما هو البرنامج الذي تريد التسجيل فيه",
        }

        widgets = {
            "starting_at": forms.TextInput(attrs={"class": "form-control", "required": True})
        }


class new_program_form(ModelForm):
    class Meta:
        model=Batch
        fields = "__all__"


class new_enrollment_from(ModelForm):
    confirm_transaction = forms.IntegerField(label="تأكيد رقم العملية", widget=forms.TextInput(attrs={"class": "form-control"}))
    class Meta:
        model=Registration
        CHANNELS = [
            ("Our Facebook Page", "صفحتنا على الفيسبوك"),
            ("Our Instagram Page", "صفحتنا على إنستغرام"),
            ("WhatsApp Group", "قروب وآتس-أب"),
            ("Other Social Media", "شبكات تواصل إجتماعي أخرى"),
            ("Email", "البريد الإلكتروني"),
            ("Friend", "توصية صديق/ة"),
            ("Other", "أخرى"),
            ]

        fields = ["transaction_id", "reach_channels"]
        labels = {
            "transaction_id": "الرجاء إدخال رقم العملية:",
            "reach_channels": "أين سمعت عن كودـ سودان و هذا البرنامج؟",
        }

        widgets = {
            "transaction_id": forms.TextInput(attrs={"class": "form-control", "type": "number"}),
            "reach_channels": forms.Select(choices=CHANNELS, attrs={"class": "form-select", "required": True}),
        }
        
        required = (
            "transaction_id",
            "reach_channels"
        )


class first_lec_free_form(ModelForm):
    confirm_transaction = forms.IntegerField(label="تأكيد رقم العملية", widget=forms.TextInput(attrs={"class": "form-control"}))
    class Meta:
        model=Registration
        fields = ["package", "transaction_id"]
        labels = {
            "transaction_id": "الرجاء إدخال رقم العملية:",
            "package": "ما هي النسخة التي تريد التسجيل فيها؟",
        }

        PACKAGES = [
            ("basic", "الأساسية"),
            ("golden", "الذهبية"),
        ]

        widgets = {
            "transaction_id": forms.TextInput(attrs={"class": "form-control", "type": "number"}),
            "package": forms.Select(choices=PACKAGES, attrs={"class": "form-select"}),
            
        }
        
        required = (
            "package",
            "transaction_id"
        )


