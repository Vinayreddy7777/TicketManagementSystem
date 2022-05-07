from django.db import models

#User Details Model Start
class UserModel(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,help_text="Enter UserName")
    mobile=models.BigIntegerField(help_text="Enter Mobile Number")
    email=models.EmailField(max_length=100,help_text="Enter Email")
    password=models.CharField(max_length=100,help_text="Enter Password")
    class Meta:
        db_table= "User_details"
    
    def __str__(self):
        return self.username
#User Details Model End.

    
    
    
#Ticket Raising Model Start.
class TicketModel(models.Model):
    ticket_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(UserModel,db_column="User_id", on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=100,help_text="Enter Name")
    email=models.EmailField(max_length=100,help_text="Select Email",)
    subject=models.CharField(max_length=150,help_text="Enter Subject")
    message=models.CharField(max_length=300,help_text="Enter Message")
    status=models.CharField(default='Pending',max_length=100,null=True)
    
    class Meta:
        db_table= "Ticket_details"
    
    def __str__(self):
        return self.ticket_id+' '+self.name
#Ticket Raising Model End.