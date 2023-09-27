from django.contrib import admin

from django.contrib import admin
from.models import Course,Trainer,Payment,Order
class AdminCourse(admin.ModelAdmin):
    list_display=['Course_name','id','duration','Hours','Fee']
    list_filter=['Fee']

class AdminTrainer(admin.ModelAdmin):
    list_display=['name','languages','Experience']

class AdminPayment(admin.ModelAdmin):
    list_display=['payment_id','user','amount','status','created_at']

class AdminOrder(admin.ModelAdmin):
    list_display=['orderId']
    
admin.site.register(Course,AdminCourse)

admin.site.register(Trainer,AdminTrainer)
#admin.site.register(Payment,AdminPayment)
admin.site.register(Order,AdminOrder)
#admin.site.register(Cart,cartItem)

admin.site.site_header="Course_Enrollment Project"
admin.site.site_title="course_enroll project"
admin.site.index_title="Enrollment Project"
