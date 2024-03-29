from django.contrib import admin

# Register your models here.
from resume.models import Job, Duty, SubDuty, Technology, TechBullet, Link, Certifications

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = (
        "slug",
        "title",
        "company",
        "start",
        "end",
        "current"
    )
    list_editable = (
        "title",
        "company",
        "start",
        "end",
        "current"
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "company",
            "start"
        )
    }

@admin.register(Duty)
class DutyAdmin(admin.ModelAdmin):
    model = Duty
    list_display = (
        "slug",
        "duty",
        "job"
    )
    
    prepopulated_fields = {
        "slug": (
            "duty",
            "job"
        )
    }
    
@admin.register(SubDuty)
class SubDutyAdmin(admin.ModelAdmin):
    model = SubDuty
    list_display = (
        "slug",
        "subduty",
        "duty"
    )
    
    prepopulated_fields = {
        "slug": (
            "duty",
            "subduty"
        )
    }

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    model = Technology
    list_display = (
        "slug",
        "tech"
    )
    
    prepopulated_fields = {
        "slug": (
            "tech",
        )
    }

@admin.register(TechBullet)
class TechBulletAdmin(admin.ModelAdmin):
    model = TechBullet
    list_display = (
        "slug",
        "tech",
        "bullet"
    )
    
    prepopulated_fields = {
        "slug": (
            "tech",
            "bullet"
        )
    }

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    model = Link
    list_display = (
        "slug",
        "link",
        "name"
    )
    
    prepopulated_fields = {
        "slug": (
            "name",
            "link"
        )
    }

@admin.register(Certifications)
class CertificationsAdmin(admin.ModelAdmin):
    model = Certifications
    list_display = (
        "slug",
        "cert",
        "badge",
        "link",
    )
    
    prepopulated_fields = {
        "slug": (
            "cert",
            "link"
        )
    }