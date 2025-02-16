from django.contrib import admin
from .models import YogaClass, Instructor

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display instructor name in admin panel

@admin.register(YogaClass)
class YogaClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'date', 'capacity')  # Display key fields
    list_filter = ('instructor', 'date')  # Add filters for instructor and date

def yoga(request):
    yoga_classes = YogaClass.objects.all()  # Fetch all classes from the database
    return render(request, 'yoga.html', {'yoga_classes': yoga_classes})
