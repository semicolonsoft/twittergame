from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='account/avatar/',null=True,default='account/avatar/defult.jpg')
    bio = models.CharField(max_length=255, default=None, null=True)
    following=models.ManyToManyField('accounts.User',related_name='followers')
    verified_email = models.BooleanField(default=False)
    verification_code = models.IntegerField(null=True, blank=True)
    verification_code_time = models.DateTimeField(null=True, blank=True)
    GoogleAcc = models.BooleanField(default=False)
    
    def suggested(self):
        a=self.following.all()
        


        suggested=list(a[:5] if a.count()>=5 else a)
        
        for user in a:
            if user in suggested:
                continue
            for user1 in suggested:

                if user.followers.count()>user1.followers.count():
                    suggested.remove(user1)
                    suggested.append(user)
                    break

        return suggested
                
                