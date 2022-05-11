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

class TechnologyType(DjangoObjectType):
    class Meta:
        model = models.Technology

class TechBulletType(DjangoObjectType):
    class Meta:
        model = models.TechBullet

class Query(graphene.ObjectType):
    all_jobs = graphene.List(JobType, job=graphene.String())
    all_tech = graphene.List(TechnologyType, tech=graphene.String())
    all_duties = graphene.List(DutyType, duty=graphene.String())
    all_subduties = graphene.List(SubDutyType, subduty=graphene.String())
    all_tech_bullet = graphene.List(TechBulletType, bullet=graphene.String())
    
    def resolve_all_jobs(root, info):
        return (
            models.Job.objects.all()
        )
    
    def resolve_all_duties(root, info):
        return (
            models.Duty.objects.all().prefetch_related("job")
        )
    
    def resolve_all_tech(root, info):
        return (
            models.Technology.objects.all()
        )
    
    def resolve_all_tech_bullet(root, info):
        return (
            models.TechBullet.objects.all().prefetch_related("tech")
        )
    
    def resolve_all_subduties(root, info):
        return (
            models.SubDuty.objects.all().prefetch_related("duty")
        )
    
    def resolve_jobs_by_subduty()

schema = graphene.Schema(query=Query)