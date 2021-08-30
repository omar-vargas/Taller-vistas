from ..models import Measurement

def get_all_measurements( ):
    measurements = Measurement.objects.all()
    return measurements


def get_measurements( pid  ):
    measurement = Measurement.objects.filter(id = pid)
