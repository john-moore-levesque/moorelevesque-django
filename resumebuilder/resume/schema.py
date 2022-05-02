from graphene_django import DjangoObjectType
import graphene
from resume import models

class JobType(DjangoObjectType):
    class Meta:
        model = models.Job

class DutyType(DjangoObjectType):
    class Meta:
        model = models.Duty

class SubDutyType(DjangoObjectType):
    class Meta:
        model = models.SubDuty

# class Query(graphene.ObjectType):
#     all_jobs = graphene.List(JobType)
    
#     def resolve_job_by_slug(root, info, slug):
#         return (
#             models.Job.objects.prefetch_related("duties")
#             .select_related("subduty")
#         )