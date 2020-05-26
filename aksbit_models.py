from django.db import models


class tbl_Incident_Master(models.Model):
    CameraId = models.CharField('Camera ID', max_length=40)
    Date_Time_frm = models.DateTimeField('Date Time From')
    Date_Time_to=models.DateTimeField('Date Time To')
    SDVideoPath=models.CharField('Video Path',max_length=100)
    FMVideoPath = models.CharField('Video Path', max_length=100)
    SocialDistance=models.CharField('Social Distance',max_length=40)
    FaceMask = models.CharField('Face Mask', max_length=40)

#IncidentType=models.CharField('Incident Type',max_length=2)

# class tbl_incident_Trans_Mask(models.Model):
#     IncidentId_PK=models.CharField('Integer ID',  max_length=40, primary_key=True)
#     incidentId=models.ForeignKey(tbl_Incident_Master,on_delete=models.CASCADE)
#     ObjectId=models.CharField('Object ID',max_length=40)
#
# class tbl_incident_Trans_SD(models.Model):
#     IncidentId_PK=models.CharField('Integer ID',  max_length=40, primary_key=True)
#     incidentId=models.ForeignKey(tbl_Incident_Master,on_delete=models.CASCADE)
#     ObjectId=models.CharField('Object ID',max_length=40)
