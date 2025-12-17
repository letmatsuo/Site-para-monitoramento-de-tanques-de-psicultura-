from django.db import models

class LeituraAmonia(models.Model):
    valor = models.FloatField()
    data_hora = models.DateTimeField(auto_now_add=True)

class LeituraTemperatura(models.Model):
    valor = models.FloatField()
    data_hora = models.DateTimeField(auto_now_add=True)

class LeituraPh(models.Model):
    valor = models.FloatField()
    data_hora = models.DateTimeField(auto_now_add=True)

class LeituraTurbidez(models.Model):
    valor = models.FloatField()
    data_hora = models.DateTimeField(auto_now_add=True)

class LeituraO2(models.Model):
    valor = models.FloatField()
    data_hora = models.DateTimeField(auto_now_add=True)


    def _str_(self):
        return f"{self.valor:.2f} ppm em {self.data_hora}"
    


#class Person(models.Model):
 #   first_name = models.CharField(max_length=70)
  #  last_name = models.CharField(max_length=70)



