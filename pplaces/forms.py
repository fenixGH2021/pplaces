from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import Project, ProjectLocation


class ProjectForm(ModelForm):
     class Meta:
         model = Project
         fields = [
             'ECCCAssignedProjectIdentfer',
             'ProjectTitleEnglish',
             'ProjectPurposeDescriptonEnglish',
#             'ProjectPurposeDescriptonFrench',
             'GeneralLocationDescriptonEnglish',
#             'GeneralLocationDescriptonFrench',
             'PriorityPlaceUID',
             'ProjectLocation',
             ]
     def __init__(self, *args, **kwargs):
         super(ProjectForm, self).__init__(*args, **kwargs)

         for name, field in self.fields.items():
             field.widget.attrs.update({'class': 'input'})

class ProjectForm_fr(ModelForm):
     class Meta:
         model = Project
         fields = [
#             'ProjectTitleEnglish',
             'ECCCAssignedProjectIdentfer',
             'ProjectTitleFrench',
#             'ProjectPurposeDescriptonEnglish',
             'ProjectPurposeDescriptonFrench',
#             'GeneralLocationDescriptonEnglish',
             'GeneralLocationDescriptonFrench',
             'PriorityPlaceUID',
             'ProjectLocation',
             ]
     def __init__(self, *args, **kwargs):
         super(ProjectForm, self).__init__(*args, **kwargs)

         for name, field in self.fields.items():
             field.widget.attrs.update({'class': 'input'})




class ProjectLocationForm(ModelForm):
    class Meta:
        model = ProjectLocation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProjectLocationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
    