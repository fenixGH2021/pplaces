from django.db import models

# Create your models here.
class PriorityPlacesREF(models.Model):
    PriorityPlaceNameEnglish = models.CharField(max_length=100, verbose_name='Priority Place (En)')
    PriorityPlaceNameFrench = models.CharField(max_length=100, verbose_name='Priority Place (Fr)', null=True, blank=True)
    #PriorityPlaceActveIND = 1

    class Meta:
        ordering = ['PriorityPlaceNameEnglish']

    def __str__(self):
        return self.PriorityPlaceNameEnglish

#  many to many relation with Project; locations called site
class ProjectLocation(models.Model):  # ProjectLocations = Sites
    ProjectLocationNameEnglish = models.CharField(max_length=100, verbose_name='Name (En)')
    ProjectLocationNameFrench = models.CharField(max_length=100, verbose_name='Name (Fr)', null=True, blank=True)
    ProjectLocationGeneralDescriptonEnglish =  models.TextField(verbose_name='Description (En)', null=True, blank=True)
    ProjectLocationGeneralDescriptonFrench  =  models.TextField(verbose_name='Description (Fr)', null=True, blank=True)
    ProjectLocationShapeFileSource = models.CharField(max_length=100, verbose_name='Source', null=True, blank=True)

    class Meta:
        ordering = ['ProjectLocationNameEnglish']

# LocationUID
    def __str__(self):
        return self.ProjectLocationNameEnglish


class Project(models.Model):
    ProjectTitleEnglish = models.CharField(max_length=250, verbose_name='Title (En)')
    ProjectTitleFrench = models.CharField(max_length=250, verbose_name='Title (Fr)', null=True, blank=True)
    ECCCAssignedProjectIdentfer = models.CharField(max_length=50, unique=True, verbose_name='Proj. Number')
    ProjectPurposeDescriptonEnglish = models.TextField(verbose_name='Description (En)', null=True, blank=True)
    ProjectPurposeDescriptonFrench = models.TextField(verbose_name='Description (Fr)', null=True, blank=True)
    GeneralLocationDescriptonEnglish = models.TextField(verbose_name='General Location (En)', null=True, blank=True)
    GeneralLocationDescriptonFrench = models.TextField(verbose_name='General Location (Fr)', null=True, blank=True)
    ProjectLocation = models.ManyToManyField(ProjectLocation)
    created = models.DateField(auto_now_add=True)
    PriorityPlaceUID = models.ForeignKey(PriorityPlacesREF, null=True, blank=True, on_delete=models.SET_NULL)
#    ProgramUID = models.ForeignKey(Program, null=True, blank=True, on_delete=models.SET_NULL)
#    FiscalYear = models.CharField(max_length=10, verbose_name='Fiscal Year')
    
    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.ProjectTitleEnglish
